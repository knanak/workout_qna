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
    path("qna/", views.getQna, name="getQna"),
    path("qna/<int:q_id>", views.nextQna, name="nextQna"),

]
