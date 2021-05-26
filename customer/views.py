from django.shortcuts import render, get_object_or_404
from .serializers import CustomerSerializer
from .models import Customer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import hashlib
from django.http import JsonResponse
# Create your views here.
#======================== View Detail Customer=========================
class CustomerViewDetail(APIView):
    serializer_class = CustomerSerializer

    def post(self, request):
        try:
            id = request.data["user_id"]

            customer = Customer.objects.get(user_id=id)
            data     = CustomerSerializer(customer).data
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response({"success": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

# {
#     "user_id": 8
# }

#======================== Register Customer=========================
class RegisterCustomer(APIView):
    serializer_class = CustomerSerializer

    def post(self, request):

        user_name       = request.data['user_name']
        password        = request.data['password']
        name            = request.data['name']
        email           = request.data['email']
        adress          = request.data['adress']
        birthday        = request.data['birthday']
        gender          = request.data['gender']
        favorite_genres = request.data['favorite_genres']
        # kiểm tra tên user name đã có trong database hay chưa, Nếu chưa thì thêm, Nếu có rồi thì Response username exist
        if Customer.objects.filter(user_name=user_name):
            return Response({"userName exist": True}, status=status.HTTP_400_BAD_REQUEST)
        elif Customer.objects.filter(email=email):
            return Response({"email exist": True}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Hash password trước khi thêm customer
            passwordEndcode = password.encode('ascii')   
            hash_object = hashlib.md5(passwordEndcode)
            print(hash_object.hexdigest())
            last_id = Customer.objects.all().last().user_id
            print(last_id)
            createCustomer   = Customer.objects.create(user_id=last_id + 1,
                                                    user_name=user_name,
                                                    password=hash_object.hexdigest(),
                                                    name=name,
                                                    email=email,
                                                    adress= adress,
                                                    birthday=birthday,
                                                    gender=gender,
                                                    favorite_genres=favorite_genres
                                                    )
            return Response({"Register success": True}, status=status.HTTP_200_OK)


# {
#     "user_id": 8,
#     "user_name": "user_8",
#     "password": "21541abc",
#     "name": "Susan",
#     "email": "susan@gmail.com",
#     "adress": "Toulon, France",
#     "birthday": "1960-07-07",
#     "gender": "female"
# }


#======================== Login Customer=========================
class LoginCustomer(APIView):
    serializer_class = CustomerSerializer

    def post(self, request):
        try:
            user_name = request.data['user_name']
            password  = request.data['password']

            # Hash password để kiểm tra thông tin customer
            passwordend = password.encode('ascii')   
            hash_object =  hashlib.md5(passwordend)
            print(hash_object.hexdigest())
            print(user_name)
            print(password)

            # Kiểm tra thông tin  user_name có trong bảng customer thì tiến hành kiểm tra thông tin password
            if get_object_or_404(Customer, user_name=user_name):
                customer = Customer.objects.get(user_name=user_name)
                
                if customer.password == hash_object.hexdigest():

            		
                    return Response({"Sign In Success": True,
                    				"user_id": customer.user_id,
                    				"name": customer.name,
                    				"email": customer.email ,
                    				"adress":customer.adress,
                    				"birthday": customer.birthday ,
                    				"gender":customer.gender,
                                    "favorite_genres": customer.favorite_genres}, status=status.HTTP_200_OK)
                else:
                    return Response({"Sign In Success": False }, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"Fail": True}, status=status.HTTP_400_BAD_REQUEST)
# {
#     "user_name": "",
#     "password": ""
# }



