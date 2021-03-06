# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_publication', models.DateTimeField(blank=True, null=True)),
                ('text', redactor.fields.RedactorField(verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430')),
                ('state', models.SmallIntegerField(choices=[(0, b'\xd0\x9d\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xbe\xd1\x82\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0'), (1, b'\xd0\x9e\xd0\xb1\xd1\x8b\xd1\x87\xd0\xbd\xd0\xb0\xd1\x8f \xd0\x9d\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'), (2, b'\xd0\x92\xd0\xb0\xd0\xb6\xd0\xbd\xd0\xb0\xd1\x8f \xd0\x9d\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c (\xd0\x9d\xd0\xb0 \xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9)'), (3, b'\xd0\x91\xd0\xb5\xd0\xba\xd0\xb0\xd0\xbf')], default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'BlogImage/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('if_comments', models.BooleanField(default=True, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0435\u0432')),
            ],
            options={
                'ordering': ['-date_creation'],
                'verbose_name': '\u041f\u043e\u0441\u0442',
                'verbose_name_plural': '\u041f\u043e\u0441\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': '\u0422\u0435\u0433',
                'verbose_name_plural': '\u0422\u0435\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='DefaultImageBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', django_resized.forms.ResizedImageField(upload_to=b'DefaultImageBlog/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(related_name='blogposts_category', to='force_blog.Category', verbose_name='\u0422\u0435\u0433\u0438'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='default_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='force_blog.DefaultImageBlog', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.CustomUser', verbose_name='\u0410\u0432\u0442\u043e\u0440'),
        ),
    ]
