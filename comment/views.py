from django.shortcuts import render, get_object_or_404
from .models import Comment
from .serializers import CommentSerializer
from movie.models import Movies
from customer.models import Customer

from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_protect
from django.utils import timezone

# Create your views here.
#======================== List Comment by userId=====================
# @api_view(['POST'])
# @csrf_protect
# def list_comment_by_customer(request):

#     try:
#         user_id = request.data['user_id']
#         comment = Comment.objects.filter(user=user_id)
#         data    = CommentSerializer(comment, many=True).data
#         print(len(comment))
#         return Response(data=data,status=status.HTTP_200_OK)
#     except:
#         return Response({'success':False}, status=status.HTTP_200_OK)
# # {
# # "user_id": 20,
# # }

@api_view(['GET'])
@csrf_protect
def list_comment_by_customer_id(request, user_id):

    try:
        comment = Comment.objects.filter(user=user_id)
        data    = CommentSerializer(comment, many=True).data
        print(len(comment))
        return Response(data=data,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_200_OK)
# {
# "user_id": 20,
# }

#==================================== List comment with movieId========================
# @api_view(['POST'])
# @csrf_protect
# def list_comment_by_movie(request):

#     try:
#         movie_id = request.data['movie_id']
#         comment  = Comment.objects.filter(movie=movie_id)
#         data     = CommentSerializer(comment, many=True).data
#         return Response(data=data,status=status.HTTP_200_OK)
#     except:
#         return Response({'success':False}, status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_protect
def list_comment_by_movie_id(request, movie_id):

    try:
        comment  = Comment.objects.filter(movie=movie_id)
        data     = CommentSerializer(comment, many=True).data
        return Response(data=data,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_200_OK)

#============================ Create comment===================


class CreateComment(APIView):
    def post(self, request):

        try:
            data        = request.data
            user_id     = data['user_id']
            movie_id    = data['movie_id']
            content     = data['content']

            movie        = Movies.objects.get(movie_id=movie_id)
            customer     = Customer.objects.get(user_id=user_id)

            createcomment = Comment.objects.create(user=customer, movie=movie, content=content)
            datajson      = CommentSerializer(createcomment).data

            return Response(data=datajson,status=status.HTTP_200_OK)
        except:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

# {
# "user_id": 20,
# "movie_id": 16,
# "content": "This is comment OK"
# }