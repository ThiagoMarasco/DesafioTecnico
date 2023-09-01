from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import avaliar_proposta_automaticamente
from .models import Proposta
from django.shortcuts import render,HttpResponse
import json

def paginainicial(request):
    return render(request,'index.html')


@csrf_exempt
def avaliar_proposta(request):

    data = json.loads(request.body.decode('utf-8'))
    document = data.get('document')
    name = data.get('name')
            
    if document is None or name is None:
        return JsonResponse({"error": "Documento e nome são obrigatórios."}, status=400)
    
    dados_proposta = {
        "document": document,
        "name": name
    }
    

    status = avaliar_proposta_automaticamente(dados_proposta)
    if status =='Aprovada':
        status = 'análise humana'

    Proposta.objects.create(
        document=dados_proposta['document'],
        name=dados_proposta['name'],
        status=status
    )
    return JsonResponse({"status": status})


