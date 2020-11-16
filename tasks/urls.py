from django.urls import path, include

from . import views

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    # path('user/<str:pk>', views.dash, name='dash'),       # for using with ID in URL
    path('dash/', views.dash, name='dash'),
    path('view/<str:pk>/', views.view_task, name='view_task'),
    path('edit/<str:pk>/', views.edit_task, name='edit_task'),
    path('delete/<str:pk>/', views.delete_task, name='delete_task'),
]
