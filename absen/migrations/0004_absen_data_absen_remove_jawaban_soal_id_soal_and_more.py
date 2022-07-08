# Generated by Django 4.0.5 on 2022-07-07 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absen', '0003_data_wajah'),
    ]

    operations = [
        migrations.CreateModel(
            name='absen',
            fields=[
                ('id_absen', models.BigAutoField(primary_key=True, serialize=False)),
                ('nama_absen', models.CharField(max_length=100)),
                ('waktu_mulai', models.TextField()),
                ('waktu_selesai', models.TextField()),
                ('waktu_pengerjaan', models.IntegerField()),
                ('id_kelas_guru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absen.kelas_guru')),
            ],
        ),
        migrations.CreateModel(
            name='data_absen',
            fields=[
                ('id_data', models.BigAutoField(primary_key=True, serialize=False)),
                ('file_absen', models.CharField(max_length=1000)),
                ('waktu_absen', models.TextField()),
                ('id_absen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absen.absen')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='jawaban_soal',
            name='id_soal',
        ),
        migrations.RemoveField(
            model_name='kuis',
            name='id_kelas_guru',
        ),
        migrations.RemoveField(
            model_name='nilai',
            name='id_kuis',
        ),
        migrations.RemoveField(
            model_name='nilai',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='soal',
            name='id_kuis',
        ),
        migrations.DeleteModel(
            name='jawaban',
        ),
        migrations.DeleteModel(
            name='jawaban_soal',
        ),
        migrations.DeleteModel(
            name='kuis',
        ),
        migrations.DeleteModel(
            name='nilai',
        ),
        migrations.DeleteModel(
            name='soal',
        ),
    ]
