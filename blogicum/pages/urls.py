from pages import views

from django.urls import path

app_name = 'pages'

urlpatterns = [
    path('pages/about/', views.about, name='about'),
    path('pages/rules/', views.rules, name='rules'),
]
