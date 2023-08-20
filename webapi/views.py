from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer, RecordSerializer
from .models import User, Record

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('login')
    serializer_class = UserSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('date_record')
    serializer_class = RecordSerializer


class UserView(APIView):
    def get(self, request):
        login = request.query_params.get('login')  # Получение значения параметра 'username' из запроса
        if login:  # Проверка, что параметр 'username' был передан в запросе
            user = User.objects.filter(login=login).first()  # Получение пользователя из базы данных
            if user:
                # Отправка данных пользователя клиенту
                return Response({
                    'username': user.login,
                    'token': user.token,
                })
            else:
                # Отправка сообщения об ошибке, если пользователь с указанным именем не найден
                return Response({'error': 'User not found'}, status=404)
        else:
            # Отправка сообщения об ошибке, если параметр 'username' не указан
            return Response({'error': 'Missing username parameter'}, status=400)