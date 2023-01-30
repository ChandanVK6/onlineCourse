# Generated by Django 4.1.3 on 2023-01-23 14:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('courses_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('intro_Video', embed_video.fields.EmbedVideoField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('passwd', models.CharField(max_length=16)),
                ('sex', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('passwd', models.CharField(max_length=16)),
                ('sex', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_name', models.CharField(max_length=50)),
                ('vid', embed_video.fields.EmbedVideoField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('courses_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=50)),
                ('quiz_url', models.URLField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Pdfs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='pdfs/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Courses_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_date', models.DateTimeField(auto_now_add=True)),
                ('courses_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.courses')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
            options={
                'unique_together': {('user_id', 'courses_id')},
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.instructor'),
        ),
        migrations.AddField(
            model_name='courses',
            name='user',
            field=models.ManyToManyField(related_name='user', through='my_app.Courses_User', to='my_app.user'),
        ),
    ]
