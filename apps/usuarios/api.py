from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from django.shortcuts import render, Http404, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .token_generator import account_activation_token

class RegisterUser(APIView):
    @staticmethod
    def post(request, format=None):
        email = request.data['email']
        index = email.find("@")
        data_user = {
            'username': email[0:index],
            'password': request.data['password'],
            'email': request.data['email']
        }
        user_serializer = UserSerializer(data=data_user)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = data_user['email']
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            message = {'message':"Usuario registrado exitosamente!!"}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer