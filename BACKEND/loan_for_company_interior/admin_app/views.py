from rest_framework import viewsets
from .serializers import UserSerializer,DefaulterSerializer
from .models import User,Defaulter


class UserView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    

class DefaulterView(viewsets.ModelViewSet):
    serializer_class = DefaulterSerializer
    queryset = Defaulter.objects.all()

