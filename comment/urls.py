from django.urls import path
from .views import list_comment_by_customer_id, list_comment_by_movie_id, CreateComment

urlpatterns = [

    path('customer/<int:user_id>/',list_comment_by_customer_id,name='user'),
    path('movie/<int:movie_id>/',list_comment_by_movie_id,name='movie'),
    path('create/',CreateComment.as_view(),name='create'),
   

]