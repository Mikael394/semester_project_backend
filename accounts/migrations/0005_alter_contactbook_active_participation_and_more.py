# Generated by Django 5.0.2 on 2024-05-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_contactbook_hand_writing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactbook',
            name='active_participation',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='hand_writing',
            field=models.CharField(blank=True, choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Fair', 'Fair'), ('Need Improvement', 'Need Improvement')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='happy',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='has_good_time_while_eating',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='material_handling',
            field=models.CharField(blank=True, choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Fair', 'Fair'), ('Need Improvement', 'Need Improvement')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='parent_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='parents_follow_up',
            field=models.CharField(blank=True, choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Fair', 'Fair'), ('Need Improvement', 'Need Improvement')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='reading_skill',
            field=models.CharField(blank=True, choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Fair', 'Fair'), ('Need Improvement', 'Need Improvement')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='teacher_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='wear_uniform',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
    ]
