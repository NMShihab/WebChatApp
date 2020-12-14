import jwt
from .models import Jwt, CustomUser
from datetime import datetime,timedelta
from django.conf import settings
import random,string
from rest_framework.views import APIView
from .serializers import LoginSerialzier, RegisterSerialzier
from django.contrib.auth import authenticate
from rest_framework.response import Response

# Create your views here.
