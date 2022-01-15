from dataclasses import fields
from rest_framework import serializers
from main import models

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conta
        fields = '__all__'

class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Receitas
        fields = '__all__'

class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Despesas
        fields = '__all__'