from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Публичные страницы
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('team/', views.team_list, name='team'),
    path('history/', views.history_list, name='history'),
    path('history/<int:pk>/', views.history_detail, name='history_detail'),
    path('partners/', views.partner_list, name='partners'),
    path('contacts/', views.contacts, name='contacts'),
    
    # Авторизация
    path('logout/', views.logout_view, name='logout'),

    # Действия администратора (формы и удаление)
    path('news/add/', views.news_add, name='news_add'),
    path('news/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
    
    path('team/add/', views.team_add, name='team_add'),
    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),
    
    path('history/add/', views.history_add, name='history_add'),
    path('history/<int:pk>/edit/', views.history_edit, name='history_edit'),
    path('history/<int:pk>/delete/', views.history_delete, name='history_delete'),
    
    path('partners/add/', views.partner_add, name='partner_add'),
    path('partners/<int:pk>/edit/', views.partner_edit, name='partner_edit'),
    path('partners/<int:pk>/delete/', views.partner_delete, name='partner_delete'),
]
