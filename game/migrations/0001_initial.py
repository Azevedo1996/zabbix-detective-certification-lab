from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name='Fase', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('ordem', models.PositiveSmallIntegerField(unique=True)),
            ('titulo', models.CharField(max_length=120)),
            ('certificacao', models.CharField(max_length=8)),
            ('nivel', models.CharField(max_length=40)),
            ('descricao', models.TextField()),
        ], options={'ordering': ['ordem']}),
        migrations.CreateModel(name='Missao', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('slug', models.SlugField(unique=True)),
            ('titulo', models.CharField(max_length=140)),
            ('categoria', models.CharField(choices=[('principal', 'Eixo principal'), ('monitoring', 'Monitoring'), ('services', 'Services'), ('inventory', 'Inventory'), ('reports', 'Reports'), ('data_collection', 'Data collection'), ('alerts', 'Alerts'), ('users', 'Users'), ('administration', 'Administration')], max_length=32)),
            ('descricao', models.TextField()),
            ('ordem', models.PositiveSmallIntegerField(default=1)),
            ('sidebar_label', models.CharField(blank=True, max_length=60)),
            ('fase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='missoes', to='game.fase')),
        ], options={'ordering': ['categoria', 'ordem']}),
        migrations.CreateModel(name='Desafio', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('slug', models.SlugField(unique=True)),
            ('titulo', models.CharField(max_length=160)),
            ('tipo', models.CharField(choices=[('texto', 'Resposta curta'), ('multipla', 'Múltipla escolha'), ('multiselect', 'Múltipla seleção'), ('formulario', 'Tela simulada com formulário')], max_length=24)),
            ('template_name', models.CharField(default='game/desafios/desafio.html', max_length=180)),
            ('enunciado', models.TextField()),
            ('contexto', models.TextField(blank=True)),
            ('opcoes', models.JSONField(blank=True, default=list)),
            ('campos', models.JSONField(blank=True, default=list)),
            ('resposta', models.JSONField(default=dict)),
            ('explicacao_correta', models.TextField()),
            ('explicacoes_incorretas', models.JSONField(blank=True, default=dict)),
            ('dica', models.TextField(blank=True)),
            ('ordem', models.PositiveSmallIntegerField(default=1)),
            ('missao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desafios', to='game.missao')),
        ], options={'ordering': ['missao__ordem', 'ordem']}),
    ]
