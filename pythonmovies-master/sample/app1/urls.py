from app1 import views
from django.urls import path
app_name='app1'

urlpatterns = [

    path('',views.movie,name='movie'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add',views.add,name='add'),
    path('edit/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]