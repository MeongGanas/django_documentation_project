from django.urls import path

from . import views


app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),

    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),

    # ex: /polls/5/result/
    path("<int:question_id>/results/", views.result, name="result"),

    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote")

    #  <int:question_id>. Menggunakan kurung sudut "menangkap" bagian dari URL dan mengirimnya sebagai argumen kata kunci ke fungsi tampilan. Titik dua (:) memisahkan perubah dan pola nama.
]
