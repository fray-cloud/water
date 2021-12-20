# Generated by Django 3.2.10 on 2021-12-20 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_camera', '0001_initial'),
        ('app_event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineParamControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_gaussian_ksize', models.IntegerField(choices=[('3', 3), ('5', 5), ('7', 7)], default=('3', 3))),
                ('line_gaussian_sigmaX', models.IntegerField(default=0)),
                ('line_canny_threashold1', models.IntegerField(default=50)),
                ('line_canny_threashold2', models.IntegerField(default=100)),
                ('line_theta', models.IntegerField(default=0)),
                ('line_hough_threshold', models.IntegerField(default=50)),
                ('line_hough_minLineLength', models.IntegerField(default=2)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_camera.camerasetting', verbose_name='카메라 아이디')),
            ],
        ),
    ]