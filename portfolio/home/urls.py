from django.urls import path

from home import views

urlpatterns = [

    path('', views.home),
    path('home', views.home),
    path('work', views.work),
    path('resume', views.Resume),
    path('education', views.education),
    path('contact',views.contact),
    path('experience',views.experience),
]
