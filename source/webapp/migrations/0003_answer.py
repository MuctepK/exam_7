# Generated by Django 2.2 on 2019-10-19 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191019_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='webapp.Choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='webapp.Poll')),
            ],
        ),
    ]
