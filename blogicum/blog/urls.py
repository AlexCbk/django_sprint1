from blog import views

from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detal, name='post_detal'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
]
