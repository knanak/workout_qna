from django.urls import path
from. import views 


app_name = "curation"
urlpatterns = [
    # /curation/
    path("", views.main, name="main"),
    path("neck/", views.neck, name="neck"),
    path("shoulder/", views.shoulder, name="shoulder"),
    path("back/", views.back, name="back"),
    path("hip/", views.hip, name="hip"),
    path("knee/", views.knee, name="knee"),
    path("qna/<str:q_name>/<int:q_id>/", views.getQna, name="getQna"),
    path("result/", views.result, name="result"),
    path("manage/", views.manage, name="manage"),
    path("<int:q_id>/list/", views.list, name="list"),
    path("<int:q_id>/edit/", views.edit, name="edit"),

    path("qnaResister/", views.register, name="register"),

]
