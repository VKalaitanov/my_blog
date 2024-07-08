from django.urls import path, re_path, register_converter
from django.views.decorators.cache import cache_page

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostHome.as_view(), name='home'),  # http://127.0.0.1:8000
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
]
