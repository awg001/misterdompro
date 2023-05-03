from .models import Bruschatka
from rest_framework import viewsets, permissions
from .serializers import BruschatkaSerializer


class BruschatkaViewSet(viewsets.ModelViewSet):
    queryset = Bruschatka.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BruschatkaSerializer
