# são responsáveis por processar as requisições HTTP, interagir com o banco de dados, e retornar respostas ao cliente

from rest_framework import viewsets
from .models import Funcionario
from .serializers import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
