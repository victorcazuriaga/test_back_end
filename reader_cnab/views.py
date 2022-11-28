from django.shortcuts import render
from rest_framework.views import Request, Response, APIView, status
import os
import ipdb
import json
from .services.reader import read_archive
# Create your views here.


class ReaderView(APIView):
    def post(self, request: Request) -> Response:
        data = request.FILES["data"]
        transactions = read_archive(data)
        return Response(transactions, status.HTTP_200_OK)
