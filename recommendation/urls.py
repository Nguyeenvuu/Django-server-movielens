from django.urls import path
from .views import recommendations, recommendations_new_user, recommendations_for_cast

urlpatterns = [

    path('',recommendations,name='recommendations'),
    path('new',recommendations_new_user,name='new'),
    path('cast',recommendations_for_cast,name='cast'),

]