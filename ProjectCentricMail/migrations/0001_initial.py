# Generated by Django 2.1.1 on 2018-10-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.CharField(max_length=32)),
                ('Sender', models.CharField(max_length=2048)),
                ('Subject', models.CharField(max_length=128)),
                ('Date', models.DateField()),
                ('Snippet', models.CharField(max_length=512)),
                ('Message_body', models.CharField(max_length=8192)),
                ('Username', models.CharField(max_length=128)),
            ],
        ),
    ]
