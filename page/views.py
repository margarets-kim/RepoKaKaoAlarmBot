from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse


class KakaoInfo(APIView):
    def post(self, request):

        result = request.data
        print(request)
        return Response('okay', status=200)
        '''repository_url = request.POST.get('repoURL', '')
        user_id = request.POST.get('userRequest.user.id')
        try:
            return Response('정상적으로 값이 담겼습니다', status=200)
        except Exception as e:
            return Response(str(e), status=404)'''
