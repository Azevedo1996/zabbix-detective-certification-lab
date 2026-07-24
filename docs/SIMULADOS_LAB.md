# Simulados Lab

O app `simulados` adiciona níveis de certificação, tópicos, questões, alternativas, simulados, tentativas, respostas e progresso por usuário.

Questões com `requires_lab=True` orientam o aluno a consultar o Zabbix real em `http://localhost:4000`.

O serviço `simulados/services.py` implementa chamadas JSON-RPC para versão, login, hosts, problems, triggers e itens.
