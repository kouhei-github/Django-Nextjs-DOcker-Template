from django.shortcuts import render
from .models import Account
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

import uuid
from pathlib import Path
import environ
import os

from .serializers import UserSerializer
from .service.mail_service import sendmail

# Create your views here.
class UserViewSet(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Account.objects.filter(id=self.request.user.id)


class UserEmailExist(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.env = environ.Env(DEBUG=(bool, False))
        self.env.read_env(os.path.join(BASE_DIR, '.env'))

    def get(self, request):
        to_email = request.query_params.get('email')
        accounts = Account.objects.filter(email=to_email)
        if accounts.exists():
            from_email = "dym.send.only.mail@gmail.com"
            title = "パスワードの再設定を行ってください"
            front_url = self.env('URL')
            random = str(uuid.uuid4())[-6:] + str(accounts[0].id) +str(uuid.uuid4())[:6]
            message = "下記URLからパスワードの再設定を行なってください。\n"
            message += "24時間でこのURLは失効致しますので、\n"
            message += "お早めに再設定をお願い致します。\n\n"
            message += front_url + random + "/reset"
            sendmail(from_email, to_email, title, message)
            return Response(data="メールアドレスが見つかりました", status=status.HTTP_200_OK)
        return Response(data="メールアドレスが存在しません", status=status.HTTP_404_NOT_FOUND)


class UserPassWordSettingView(APIView):
    permission_classes = (AllowAny,)

    def put(self, request):
        payload = request.data
        account_id = payload["id"]
        mail = payload["email"]
        new_password = payload["password"]

        user_queryset = Account.objects.get(id=account_id)
        if not user_queryset.email == mail:
            return Response(data="メールアドレスが違います", status=status.HTTP_404_NOT_FOUND)
        user_queryset.set_password(new_password)
        user_queryset.save()
        return Response(data="更新しました", status=status.HTTP_200_OK)
