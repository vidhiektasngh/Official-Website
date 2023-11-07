from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('idcard', views.idcard, name = 'idcard'),
    path('pending', views.pending, name = 'pending'),
    path('calender', views.calender, name = 'calender'),
    path('spreadsheets', views.spreadsheets, name = 'spreadsheets'),
    path('post/<int:member_id>/', views.generate_id_card, name='post'),
    path('generate_infinite_id_cards/', views.generate_infinite_id_cards, name='generate_infinite_id_cards'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_announcement/', views.create_announcement, name='create_announcement'),
    path('clear_announcements/', views.clear_announcements, name='clear_announcements'),
    path('create_task/', views.create_task, name='create_task'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':    settings.MEDIA_ROOT})
    url(r'^media/(?P<path>.*)$', serve,{'document_root':    settings.MEDIA_ROOT})
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

