from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('finch/', views.finches_index, name="Index"),
    path('finch/<int:finch_id>/', views.finches_detail, name='Detail'),
]