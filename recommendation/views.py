from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import ast
import datetime
import time
import collections
import random


from .models import RecommendedMovies
from movie.models import Movies
# Create your views here.

def convert_movie(movie):
    dict_movie = {}
    dict_movie['movie_id'] = movie.movie_id
    dict_movie['timestamp'] = time.mktime(datetime.datetime.strptime(str(movie.release_date), "%m/%d/%Y").timetuple())
    return dict_movie

def convert_favorite(text):
    list_favorite = text.split('|')
    return list_favorite


@api_view(['POST',])
def recommendations(request):
    data = request.data
    if data:
        userId = data['user_id']
        try:
            recommendations = RecommendedMovies.objects.get(user = userId)

            movies = Movies.objects.all()

            sorted_movies = sorted(movies, key=lambda x: x.popularity, reverse=True)[0:200]
            popularity_movies = [ele.movie_id for ele in sorted_movies]

            print('truoc for')
            movies2 = []
            for movie in movies:
                if (movie.release_date != None):
                    try:
                        temp = int(str(movie.release_date).split('/')[2])
                        if (temp > 2000):
                            dict_movie = convert_movie(movie)
                            movies2.append(dict_movie)
                    except:
                        pass
            print('sau for ok')
            sorted_movies = sorted(movies2, key=lambda x: x['timestamp'], reverse=True)[0:10]
            new_movies = [ele['movie_id'] for ele in sorted_movies]
            print('ok')
            data_json = {
                'success': True,
                'user_id': userId,
                'recommendations': ast.literal_eval(recommendations.recommendations),
                'popularity': popularity_movies,
                'new': new_movies
            }
            print('len recommendations:', len(data_json['recommendations']))
            return Response(data_json, status=status.HTTP_200_OK)
        except:
            return Response({'success1':False}, status=status.HTTP_200_OK)
    else:
        return Response({'success2':False}, status=status.HTTP_200_OK)

@api_view(['POST',])
def recommendations_new_user(request):
    data = request.data
    if data:
        userId          = data['user_id']
        favorite_genres = data['favorite_genres']
        try:
            movies = Movies.objects.all()

            sorted_movies = sorted(movies, key=lambda x: x.popularity, reverse=True)[0:200]
            popularity_movies = [ele.movie_id for ele in sorted_movies]

            print('truoc for')
            movies2 = []
            for movie in movies:
                if (movie.release_date != None):
                    try:
                        temp = int(str(movie.release_date).split('/')[2])
                        if (temp > 2000):
                            dict_movie = convert_movie(movie)
                            movies2.append(dict_movie)
                    except:
                        pass
            print('sau for ok')
            sorted_movies = sorted(movies2, key=lambda x: x['timestamp'], reverse=True)[0:10]
            new_movies = [ele['movie_id'] for ele in sorted_movies]


            # Lấy recommendation dựa vào generes của người dùng và trong bảng xếp hạng 1000 popularity 
            sorted_movies_popularity = sorted(movies, key=lambda x: x.popularity, reverse=True)[201:1200]
            
            #convert Data request về dạng list các generes
            generes = convert_favorite(favorite_genres)
            
            # Chứa các movie search trong top 1000 dựa vào generes
            list_result = []

            for genere in generes:
                for movie in sorted_movies_popularity:
                    if(genere.lower() in movie.genres.lower()):
                        
                        list_result.append(movie.movie_id)

            
            # Chứa các movie_id đã loại bỏ các movie trùng lặp
            list_recommendations = [item for item, count in collections.Counter(list_result).items() if count > 0]
            
            list_recommendations_random = random.choices(list_recommendations, k=len(list_recommendations))
           
            data_json = {
                'success': True,
                'user_id': userId,
                'recommendations': list_recommendations_random,
                'popularity': popularity_movies,
                'new': new_movies
            }
            print('len recommendations:', len(data_json['recommendations']))
            return Response(data_json, status=status.HTTP_200_OK)
        except:
            return Response({'success1':False}, status=status.HTTP_200_OK)
    else:
        return Response({'success2':False}, status=status.HTTP_200_OK)

def convertTuple(tup):
    str =  ''.join(tup)
    return str
# {
# "user_id": 8,
# "favorite_genres": "Science Fiction|Action|Adventure|Thriller"
# }

@api_view(['POST',])
def recommendations_for_cast(request):
    data = request.data
    if data:
        cast_name = data['cast_name']
        try:
            movies = Movies.objects.all()
            movies_list = [ele for ele in movies if ele.actor is not None]
            list_result = []
            count = 0
            print(movies_list[8].actor)
            for movie in movies_list:
                if (cast_name.lower() in movie.actor.lower()):
                    list_result.append(movie.movie_id)
            print(list_result)
            data_json = {
                'success': True,
                'movie': list_result
            }
            return Response(data_json, status=status.HTTP_200_OK)
        except:
            return Response({'success1':False}, status=status.HTTP_200_OK)
    else:
        return Response({'success2':False}, status=status.HTTP_200_OK)