# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PersonalProfile
from .models import WorkProfile

class PersonalView(APIView):
    def get(self, request):
        pprofiles = PersonalProfile.objects.all()
        return Response({"pprofiles": pprofiles })

class WorkView(APIView):
    def get(self, request):
        wprofiles = WorkProfile.objects.all()
        return Response({"wprofiles": wprofiles })