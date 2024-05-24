# Generated by Django 5.0.2 on 2024-05-22 15:40

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_contactbook_active_participation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='accounts.attendance')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='accounts.student')),
            ],
            options={
                'unique_together': {('attendance', 'student')},
            },
        ),
    ]
