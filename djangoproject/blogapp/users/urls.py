from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('signup/',views.signup),
    path('login1/',views.login1),
    path('signup1/',views.Signup1.as_view()),
    path('logout/',views.logout),
    path('forgot/',views.forgot),
]
