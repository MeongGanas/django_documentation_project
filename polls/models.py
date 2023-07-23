import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


#  CharField untuk bidang karakter dan DateTimeField untuk tanggal waktu.

#  Setiap field memiliki argumen wajib. CharField, sebagai contoh, membutuhkan sebuah argumen max_length.


# nanti nama schemanya sesuai dengan nama folder + nama class yang di buat di file models.py. Contoh menggunakan nama kelas Question dan di dalam folder polls, hasilnya nanti jadi polls_question

class Question(models.Model):
    # nama variable = nama field, setelah models. itu adalah tipe data fieldnya nanti
    question_text = models.CharField(max_length=200)
    # CharField -> membuat field tipe data varchar
    pub_date = models.DateTimeField("date published")
    # DateTime -> membuat field tipe datetime dst..


    # Sangat penting menambahkan cara __str__() ke model anda, tidak hanya kenyamanan anda ketika berurusan dengan prompt interaktif
    def __str__(self):
        return str(self.question_text)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
    


# python manage.py makemigrations untuk membuat migrasi untuk membuat schema baru.
# python manage.py migrate untuk mengisi schema baru tersebut sesuai dengan isi file ..._initial.py.