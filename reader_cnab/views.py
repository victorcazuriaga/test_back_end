from django.shortcuts import render
from rest_framework.views import Request, Response, APIView, status
from .services.reader import read_archive
from .services.create_transactions import create_transactions
from .models import DataCnab, TypeTransaction
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .forms import ArchiveForm
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


@login_required(login_url="/api/login_page")
def update_file(request):
    forms = ArchiveForm(request.POST)
    context = {"forms": ArchiveForm}
    if request.method == "GET":
        # update_file = request.FILES["data"]
        return render(request, "upload.html", context=context)
    else:
        data = request.FILES.get("data")
        transactions = read_archive(data)
        create_transactions(transactions)
        return HttpResponse("Registrados com sucesso")


@login_required(login_url="/api/login_page")
def get_all_register(request):
    if request.method == "GET":
        data = ReaderView.get(self=None, request=None).data
        context = {"data": data}
        return render(request, "result.html", context=context)
