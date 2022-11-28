from django.shortcuts import render
from rest_framework.views import Request, Response, APIView, status
from .services.reader import read_archive
from .services.create_transactions import create_transactions
from .models import DataCnab, TypeTransaction
from django.contrib.auth.decorators import login_required
from .forms import ArchiveForm
from django.http import HttpResponse
# Create your views here.


class ReaderView(APIView):
    @classmethod
    def post(self, request: Request) -> Response:
        data = request.FILES["data"]
        transactions = read_archive(data)
        create_transactions(transactions)
        return Response("Registrados com sucesso", status.HTTP_200_OK)

    def get(self, request: Request) -> Response:
        cnab_data = DataCnab.objects.values()
        cnab_list = []
        for data in cnab_data:
            tipo = data.pop("tipo_id")
            data_tipo = TypeTransaction.objects.filter(id=tipo).values()
            cnab_list += [{**data, "tipo": data_tipo}]
        return Response(cnab_list, status.HTTP_200_OK)
