from django.db import models


class Fase(models.Model):
    ordem = models.PositiveSmallIntegerField(unique=True)
    titulo = models.CharField(max_length=120)
    certificacao = models.CharField(max_length=8)
    nivel = models.CharField(max_length=40)
    descricao = models.TextField()

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return f'{self.certificacao} - {self.titulo}'


class Missao(models.Model):
    class Categoria(models.TextChoices):
        PRINCIPAL = 'principal', 'Eixo principal'
        MONITORING = 'monitoring', 'Monitoring'
        SERVICES = 'services', 'Services'
        INVENTORY = 'inventory', 'Inventory'
        REPORTS = 'reports', 'Reports'
        DATA_COLLECTION = 'data_collection', 'Data collection'
        ALERTS = 'alerts', 'Alerts'
        USERS = 'users', 'Users'
        ADMINISTRATION = 'administration', 'Administration'
        SECURITY = 'security', 'Security'
        ANSIBLE = 'ansible', 'Ansible'
        AUTOMATION_API = 'automation_api', 'Automation API'
        AWS = 'aws', 'AWS'
        DATABASES = 'databases', 'Databases'
        AZURE = 'azure', 'Azure'
        AUTHENTICATION = 'authentication', 'Authentication'

    fase = models.ForeignKey(Fase, null=True, blank=True, on_delete=models.CASCADE, related_name='missoes')
    slug = models.SlugField(unique=True)
    titulo = models.CharField(max_length=140)
    categoria = models.CharField(max_length=32, choices=Categoria.choices)
    descricao = models.TextField()
    ordem = models.PositiveSmallIntegerField(default=1)
    sidebar_label = models.CharField(max_length=60, blank=True)

    class Meta:
        ordering = ['categoria', 'ordem']

    @property
    def is_principal(self):
        return self.categoria == self.Categoria.PRINCIPAL

    def __str__(self):
        return self.titulo


class Desafio(models.Model):
    class Tipo(models.TextChoices):
        TEXTO = 'texto', 'Resposta curta'
        MULTIPLA = 'multipla', 'Múltipla escolha'
        MULTISELECT = 'multiselect', 'Múltipla seleção'
        FORMULARIO = 'formulario', 'Tela simulada com formulário'

    missao = models.ForeignKey(Missao, on_delete=models.CASCADE, related_name='desafios')
    slug = models.SlugField(unique=True)
    titulo = models.CharField(max_length=160)
    tipo = models.CharField(max_length=24, choices=Tipo.choices)
    template_name = models.CharField(max_length=180, default='game/desafios/desafio.html')
    enunciado = models.TextField()
    contexto = models.TextField(blank=True)
    opcoes = models.JSONField(default=list, blank=True)
    campos = models.JSONField(default=list, blank=True)
    resposta = models.JSONField(default=dict)
    explicacao_correta = models.TextField()
    explicacoes_incorretas = models.JSONField(default=dict, blank=True)
    dica = models.TextField(blank=True)
    ordem = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ['missao__ordem', 'ordem']

    def __str__(self):
        return self.titulo
