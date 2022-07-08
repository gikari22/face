# Generated by Django 4.0.6 on 2022-07-05 18:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id_user', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_student', models.BooleanField(default=False, verbose_name='Is Student')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Is Teacher')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='kelas_guru',
            fields=[
                ('id_kelas_guru', models.BigAutoField(primary_key=True, serialize=False)),
                ('nama_kelas', models.CharField(max_length=100)),
                ('banner_kelas', models.CharField(max_length=100)),
                ('deskripsi_kelas', models.TextField()),
                ('jumlah_peserta', models.IntegerField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='kuis',
            fields=[
                ('id_kuis', models.BigAutoField(primary_key=True, serialize=False)),
                ('nama_kuis', models.CharField(max_length=100)),
                ('jumlah_kuis', models.IntegerField()),
                ('jumlah_jawaban_perkuis', models.IntegerField()),
                ('waktu_mulai', models.TextField()),
                ('waktu_selesai', models.TextField()),
                ('waktu_pengerjaan', models.IntegerField()),
                ('deskripsi_kuis', models.TextField()),
                ('is_soal_is_added', models.BooleanField(default=False)),
                ('is_jawaban_is_added', models.BooleanField(default=False)),
                ('id_kelas_guru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absen.kelas_guru')),
            ],
        ),
        migrations.CreateModel(
            name='soal',
            fields=[
                ('id_soal', models.BigAutoField(primary_key=True, serialize=False)),
                ('pertanyaan', models.CharField(max_length=1000)),
                ('id_kuis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absen.kuis')),
            ],
        ),
        migrations.CreateModel(
            name='nilai',
            fields=[
                ('id_nilai', models.BigAutoField(primary_key=True, serialize=False)),
                ('nilai', models.IntegerField()),
                ('id_kuis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absen.kuis')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='kelas_murid',
            fields=[
                ('id_kelas_murid', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_kelas_guru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absen.kelas_guru')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jawaban_soal',
            fields=[
                ('id_jawaban', models.BigAutoField(primary_key=True, serialize=False)),
                ('jawaban', models.CharField(max_length=100)),
                ('id_soal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absen.kuis')),
            ],
        ),
        migrations.CreateModel(
            name='jawaban',
            fields=[
                ('id_jawaban', models.BigAutoField(primary_key=True, serialize=False)),
                ('jawaban', models.CharField(max_length=100)),
                ('id_kuis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absen.kuis')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
