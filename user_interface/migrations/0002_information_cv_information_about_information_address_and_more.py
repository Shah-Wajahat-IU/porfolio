# Generated by Django 4.0 on 2021-12-16 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='CV',
            field=models.FileField(blank=True, null=True, upload_to='cv/'),
        ),
        migrations.AddField(
            model_name='information',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/'),
        ),
        migrations.AddField(
            model_name='information',
            name='bio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='others',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('imageLink', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('projectRating', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='2', max_length=10, null=True)),
                ('demo', models.URLField(blank=True, null=True)),
                ('githubLink', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.user')),
            ],
            options={
                'ordering': ['-projectRating'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('imageLink', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('skillrank', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.user')),
            ],
            options={
                'ordering': ['-skillrank'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=50, null=True)),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.user')),
            ],
            options={
                'ordering': ['-send_time'],
            },
        ),
        migrations.CreateModel(
            name='Exprience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('the_year', models.CharField(blank=True, max_length=50, null=True)),
                ('institude', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.user')),
            ],
            options={
                'ordering': ['-the_year'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('the_year', models.CharField(blank=True, max_length=50, null=True)),
                ('institude', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.user')),
            ],
            options={
                'ordering': ['-the_year'],
            },
        ),
    ]