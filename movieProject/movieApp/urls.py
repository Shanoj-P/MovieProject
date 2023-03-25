from django.urls import path

from . import views
app_name = 'movieApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movieId>/', views.details, name='details'),
    path('add/', views.addMovie, name = 'addMovie'),
    path('update/<int:id>/',views.update,name = 'update'),
    path('delete/<int:id>/',views.delete,name = 'delete')
   ]