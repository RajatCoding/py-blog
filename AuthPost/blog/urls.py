from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='about_us'),
    path('createpost/', views.CreatePost.as_view(), name='createpost'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('updatepost/<int:pk>', views.PostUpdate.as_view(), name='updatepost'),
    path('deletepost/<int:pk>', views.PostDelete.as_view(), name='deletepost'),
    path('detailpost/<int:pk>', views.PostDetail.as_view(), name='detailpost'),


    




]