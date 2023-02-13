
from rest_framework import viewsets
from .serializers import BankSerializer,DocumentSerializer
from .models import Bank,Document


class BankView(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()


class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()