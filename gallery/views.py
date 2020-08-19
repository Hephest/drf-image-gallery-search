from rest_framework import viewsets

from gallery.models import Picture
from gallery.serializers import PictureSerializer


class PictureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only viewset for checking database changes.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
