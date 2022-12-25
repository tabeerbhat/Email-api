# Generated by Django 4.1.3 on 2022-12-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eemail', '0003_message_delete_contactemail_delete_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emailhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(blank=True, max_length=254)),
                ('recipient', models.EmailField(blank=True, max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
