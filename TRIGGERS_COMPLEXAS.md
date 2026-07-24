# Dicas para Lidar com Triggers Complexas — Zabbix Detective

Triggers complexas são comuns em ambientes reais. O objetivo é reduzir falso positivo, representar impacto real e evitar ruído operacional.

## Regra principal

Antes de escrever uma trigger complexa, descreva a condição em português:

```text
Quero alertar quando ______ acontecer por ______ tempo, exceto quando ______, e recuperar somente quando ______.
```

Se você não consegue escrever a frase, a trigger ainda não está clara.

## Anatomia de uma trigger complexa

Uma trigger complexa geralmente combina:

- mais de uma função;
- mais de um item;
- operadores lógicos `and` / `or`;
- janelas de tempo;
- problem expression;
- recovery expression;
- dependencies;
- tags para roteamento;
- macros para thresholds.

## Estratégia em 8 passos

### 1. Comece simples

Crie primeiro uma expressão mínima:

```text
last(/Host/system.cpu.util)>90
```

Depois evolua para janela de tempo:

```text
avg(/Host/system.cpu.util,5m)>90
```

### 2. Use janela de tempo para reduzir ruído

Evite alertar por pico instantâneo quando o problema real é sustentado.

Exemplo:

```text
min(/Host/vfs.fs.size[/,pfree],10m)<10
```

Interpretação: o espaço livre ficou abaixo de 10% durante toda a janela de 10 minutos.

### 3. Separe abertura e recuperação

Use recovery expression quando a métrica oscila perto do limite.

Exemplo conceitual:

```text
Problem:  avg(cpu,5m)>90
Recovery: avg(cpu,5m)<75
```

Isso cria hysteresis e reduz flapping.

### 4. Use `nodata()` para ausência de coleta

Não tente detectar ausência de dados com `last()` ou `avg()`. Se o problema é silêncio de coleta, use `nodata()`.

Exemplo:

```text
nodata(/Host/agent.ping,5m)=1
```

### 5. Diferencie tempo e quantidade de valores

- `10m` significa janela de tempo.
- `#10` significa quantidade de valores.

Exemplo:

```text
avg(/Host/key,10m)
avg(/Host/key,#10)
```

São conceitos diferentes.

### 6. Use dependencies para causa raiz

Se um host depende de roteador/firewall/link, evite alertas em cascata configurando trigger dependency.

Exemplo conceitual:

```text
Trigger: Host está indisponível
Depends on: Router está indisponível
```

### 7. Use macros para thresholds

Evite fixar limites em templates quando o threshold varia por ambiente.

Exemplo:

```text
avg(/Host/system.cpu.util,5m)>{$CPU.UTIL.MAX}
```

### 8. Documente a intenção

Em triggers críticas, documente:

- por que o limite existe;
- qual impacto representa;
- quando deve abrir;
- quando deve recuperar;
- quais dependências existem;
- qual time deve receber.

## Padrões úteis

### Alta CPU sustentada

```text
avg(/Host/system.cpu.util,5m)>90
```

### Disco crítico com janela

```text
min(/Host/vfs.fs.size[/,pfree],10m)<10
```

### Serviço sem dados

```text
nodata(/Host/service.status,5m)=1
```

### Oscilação com recovery expression

```text
Problem:  avg(/Host/system.cpu.util,5m)>90
Recovery: avg(/Host/system.cpu.util,5m)<75
```

### Comparação com período anterior

Use time shift quando precisar comparar comportamento atual com período passado. Exemplo conceitual:

```text
avg(/Host/key,1h) > avg(/Host/key,1h:now-1d)*1.5
```

## Erros comuns

- Usar `last()` para métrica ruidosa.
- Não criar recovery expression para métrica oscilante.
- Usar `or` quando o correto era `and`.
- Não usar dependency em topologia com router/firewall/link.
- Misturar ausência de coleta com valor ruim.
- Usar threshold fixo em template genérico.
- Criar trigger complexa sem documentação.

## Checklist de revisão para triggers complexas

- [ ] A condição de problema está clara?
- [ ] A janela de tempo faz sentido?
- [ ] Existe risco de flapping?
- [ ] Precisa de recovery expression?
- [ ] Precisa de dependency?
- [ ] Precisa de macro de threshold?
- [ ] A trigger representa sintoma ou causa raiz?
- [ ] A severidade está coerente?
- [ ] As tags roteiam para o time certo?
- [ ] A explicação está documentada?

## Método de troubleshooting

Quando uma trigger complexa não se comportar como esperado:

1. Verifique se os itens estão supported.
2. Consulte Latest data.
3. Teste cada função isoladamente.
4. Verifique janela de tempo e `#N`.
5. Revise operadores lógicos.
6. Verifique recovery expression.
7. Verifique dependencies.
8. Verifique macros usadas no template/host.
9. Verifique tags e actions.
10. Documente a causa.
