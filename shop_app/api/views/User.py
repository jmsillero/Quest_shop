from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import viewsets, exceptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from shop_app.serializer import UserSerializer
from rest_framework.response import Response
import  re


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def create(request):
#     try:
#         name = request.POST['name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#
#         if name and email and last_name and password:
#             password = make_password(password)
#             re_email = '^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$'
#             if re.math(re_email, email):
#
#
#
#
#     except Exception as e:
#         return Response(
#         data={'message': 'Se produjo un error inesperado al intentar crear un usuario.' + e.__str__(),
#               'data': [], 'code': 500})