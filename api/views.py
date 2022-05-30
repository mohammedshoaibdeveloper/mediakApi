from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from django.conf import settings
from api.models import *
# Create your views here.


def index(request):
    return HttpResponse('<h1>Project Mediak</h1>')


class GetData(APIView):

    def get(self,request):

        id = request.GET['id']

        data = audiofiles.objects.filter(user_id__id = id).values('id','audio')
        return Response({'status':True,'data':data},status=200)