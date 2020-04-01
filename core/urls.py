
from django.urls import path
from . import views

urlpatterns = [
     path('', views.logout_view, name = 'log_out'),
#     path('', views.homepage, name = 'homepage'),
     path('users/<username>/', views.userProfileView, name = 'user_profile'),
#    path('', views.HomeView.as_view(), name = 'homepage'),
     path('users/', views.UserList.as_view(), name = 'user_list'),

]
