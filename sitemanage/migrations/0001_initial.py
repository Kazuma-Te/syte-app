# Generated by Django 3.1.4 on 2020-12-12 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(max_length=100, verbose_name='meta_title')),
                ('meta_description', models.CharField(max_length=300, verbose_name='meta_description')),
                ('meta_keywords', models.CharField(max_length=300, verbose_name='SEOキーワード')),
                ('author', models.CharField(max_length=30, verbose_name='管理者')),
                ('top_title', models.CharField(max_length=100, verbose_name='TOPページタイトル')),
                ('top_subtitle', models.CharField(max_length=200, verbose_name='TOPページサブタイトル')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sites.site', verbose_name='Site')),
            ],
        ),
    ]
