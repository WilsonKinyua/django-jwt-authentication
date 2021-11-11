from sendgrid.helpers.mail import Mail
from django.conf import settings
from sendgrid import SendGridAPIClient
import os
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# ====================================
# sendgrid
message = Mail(
    from_email='developerwilsonkinyua@gmail.com',
    to_emails='wilsonkinyuam@gmail.com',
    subject='Sending with Twilio sendgrid-python library',
    html_content='<strong>It is easy to send mail with Python and SendGrid</strong>'
)

try:
    sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    response = sg.send(message)
    print(response.status_code)
except Exception as e:
    print(e.message)
