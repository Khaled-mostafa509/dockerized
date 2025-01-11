from django.http import request
from rest_framework import generics, permissions, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import CompanyCustomRegistrationSerializer, PersonCustomRegistrationSerializer, UserSerializer, LoginSerializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .models import User
from .permissions import IsCompanyUser, IsPersonUser
from .forms import SignupForm, OTPForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
import math
import random
from .forms import LoginForm
from django.contrib import messages


class CompanySignupView(generics.GenericAPIView):
    serializer_class = CompanyCustomRegistrationSerializer

    # def post(self, request, format=None):
    #     serializer = CompanyCustomRegistrationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED,)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "account created successfully"
        })


class PersonSignupView(generics.GenericAPIView):
    serializer_class = PersonCustomRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = request.POST['email']
            o = generateOTP()
            send_mail(
                'subject',
                o,
                settings.EMAIL_HOST_USER,
                [email],
            )
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "account created successfully"
        })


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            o = generateOTP()
            send_mail(
                'subject',
                o,
                settings.EMAIL_HOST_USER,
                [email],
            )
            print(form)
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/accounts/OTPValidate')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})


def OTPCODE(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            code = request.POST['code']
            form.save()
            code = form.cleaned_data['code']
            authenticate(o=code)
            return redirect('/accounts/profile')
    else:
        form = OTPForm()

        return render(request, 'registration/OTP.html', {'form': form})


class CustomAuthToken(ObtainAuthToken):
    # serializer_class=LoginSerializers
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return render({
            # 'token':token.key,
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class PersonOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsPersonUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CompanyOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsCompanyUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# def sign_in(request):
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request, 'registration/login.html', {'form': form})

def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f'Hi {username.title()}, welcome back!')
                return redirect('posts')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'registration/login.html', {'form': form})
