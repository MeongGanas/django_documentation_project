from django.db import models

# Create your models here.


#  CharField untuk bidang karakter dan DateTimeField untuk tanggal waktu.

#  Setiap field memiliki argumen wajib. CharField, sebagai contoh, membutuhkan sebuah argumen max_length.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
