from rest_framework import viewsets
from main.api import serializers
from main import models
from main.models import Receitas


class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContaSerializer
    queryset = models.Conta.objects.all()

class ReceitasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReceitasSerializer
    queryset = models.Receitas.objects.all()
    
class DespesasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DespesasSerializer
    queryset = models.Despesas.objects.all()