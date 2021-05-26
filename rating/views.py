from django.shortcuts import render
from .models import Ratings
from .serializers import RatingSerializer
from movie.models import Movies
from customer.models import Customer

from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_protect

from customer.models import Customer
from django.utils import timezone
import collections
##=============================== GET/POST rating BY customer id====================================
# Create your views here.
# @api_view(['POST'])
# @csrf_protect
# def list_view_rating_by_customer(request):

#     try:
#         user_id = request.data['user_id']

#         ratings = Ratings.objects.filter(user=user_id)
        
#         data    = RatingSerializer(ratings, many=True).data
#         print(len(ratings))
#         return Response(data=data,status=status.HTTP_200_OK)
#     except:
#         return Response({'success':False}, status=status.HTTP_200_OK)
@api_view(['GET'])
def list_view_rating_by_customer(request, user_id):

    try:
        ratings = Ratings.objects.filter(user=user_id)
        data    = RatingSerializer(ratings, many=True).data
        print(len(ratings))
        return Response(data=data,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_200_OK)

##=============================== GET/POST rating BY movie id====================================
# @api_view(['POST'])
# @csrf_protect
# def list_view_rating_by_movie(request):

#     try:
#         movie_id = request.data['movie_id']
#         ratings  = Ratings.objects.filter(user=movie_id)
#         data     = RatingSerializer(ratings, many=True).data
#         return Response(data=data,status=status.HTTP_200_OK)
#     except:
#         return Response({'success':False}, status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_protect
def list_view_rating_by_movie(request, movie_id):

    try:
        ratings  = Ratings.objects.filter(movie=movie_id)

        print(len(ratings))
        list_rating = [ele.rating for ele in ratings]
        print("a")
        print(list_rating[0])
        sum_rating = {item : count for item, count in collections.Counter(list_rating).items() if count > 1}
        print(type(sum_rating))
        one_star   = 0
        two_star   = 0
        three_star = 0
        four_star  = 0
        five_star  = 0
        # print(sum_rating["1.0"])
        for k, v in sum_rating.items():
            print(type(v))
            if k >= 0 and k < 2:
                one_star = one_star + v
            if k >= 2 and k < 3:
                two_star = two_star + v
            if k >= 3 and k < 4:
                three_star = three_star + v
            if k >= 4 and k < 5:
                four_star = four_star + v
            if k == 5:
                five_star = five_star + v
        print(five_star)
        print(four_star)
        print(three_star)
        print(two_star)
        print(one_star)
        data_star = {
            '5': five_star,
            '4': four_star,
            '3': three_star,
            '2': two_star,
            '1': one_star,
        }
        return Response(data_star ,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_200_OK)


##=============================== POST create rating====================================
def convert_date(time):
    string_time = str(time).split(" ")[0]
    return int(string_time.replace("-", ""))

class CreateRating(APIView):
    def post(self, request):

        try:
            data        = request.data
            user_id     = data['user_id']
            movie_id    = data['movie_id']
            rating      = data['rating']

            time         = timezone.now()
            time_convert = convert_date(time)
            
            if Ratings.objects.filter(user=user_id) & Ratings.objects.filter(movie=movie_id):
                update = {"HaveRating": True,
                            'user_id':user_id,
                            'movie_id': movie_id,
                            'rating': rating}
                return Response(data=update, status=status.HTTP_200_OK)
            else:
                movie        = Movies.objects.get(movie_id=movie_id)
                customer     = Customer.objects.get(user_id=user_id)
                createRating = Ratings.objects.create(user=customer, movie=movie, rating=rating, time_rating=time_convert)
                create = {"Create": True,
                            'user_id':user_id,
                            'movie_id': movie_id,
                            'rating': rating}

            return Response(data=create,status=status.HTTP_200_OK)
        except:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

    # {
    #     "user_id": 9,
    #     "rating": 4.5,
    #     "time_rating": 1073837168,
    #     "movie_id": 14
    # }
    def put(self, request):

        try:
            data        = request.data
            user_id     = data['user_id']
            movie_id    = data['movie_id']
            rating      = data['rating']
            print(data)
            time         = timezone.now()
            time_convert = convert_date(time)
            print('b')
            if Ratings.objects.filter(user=user_id, movie=movie_id):
                Ratings.objects.filter(user=user_id, movie=movie_id).update(user=user_id, movie=movie_id, rating=rating, time_rating=time_convert)
                update = {"SuccessUpdate": True,
                            'user_id':user_id,
                            'movie_id': movie_id,
                            'rating': rating}
            return Response(data=update,status=status.HTTP_200_OK)
        except:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)