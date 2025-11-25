from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('news/', views.news_view, name='news'),
    path('team/', views.team_view, name='team'),
    path('history_lines/', views.history_lines_view, name='history_lines'),
    path('partner/', views.partner_view, name='partner'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('new/', views.new_view, name='new'),
]
