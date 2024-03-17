from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('finch/', views.finches_index, name="Index"),
    path('finch/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finch/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finch/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
    path('finch/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finch/<int:finch_id>/assoc_toy/<int:acc_id>/', views.assoc_acc, name='assoc_acc'),
    path('finch/<int:finch_id>/unassoc_acc/<int:acc_id>/', views.unassoc_acc, name='unassoc_acc'),
    path('accessories/', views.AccList.as_view(), name='acc_index'),
    path('accessories/<int:pk>/', views.AccDetail.as_view(), name='acc_detail'),
    path('accessories/create/', views.AccCreate.as_view(), name='acc_create'),
    path('accessories/<int:pk>/update/', views.AccUpdate.as_view(), name='acc_update'),
    path('accessories/<int:pk>/delete/', views.AccDelete.as_view(), name='acc_delete'),
]