# Generated by Django 3.1.3 on 2020-12-31 08:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ITsupermanapp', '0018_answermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answermodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='answermodel',
            name='content',
        ),
        migrations.RemoveField(
            model_name='answermodel',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='answermodel',
            name='title',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='answer',
        ),
        migrations.AddField(
            model_name='answermodel',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='ITsupermanapp.questionmodel'),
            preserve_default=False,
        ),
    ]