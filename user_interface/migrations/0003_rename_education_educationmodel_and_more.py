# Generated by Django 4.0 on 2021-12-16 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0002_information_cv_information_about_information_address_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Education',
            new_name='EducationModel',
        ),
        migrations.RenameModel(
            old_name='Exprience',
            new_name='ExprienceModel',
        ),
        migrations.RenameModel(
            old_name='information',
            new_name='InformationModel',
        ),
        migrations.RenameModel(
            old_name='Message',
            new_name='MessageModel',
        ),
        migrations.RenameModel(
            old_name='Project',
            new_name='ProjectModel',
        ),
        migrations.RenameModel(
            old_name='SkillSet',
            new_name='SkillSetModel',
        ),
    ]
