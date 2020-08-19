from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import filters, generics, viewsets, mixins

from gallery.models import Picture
from gallery.serializers import PictureSerializer


class PictureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only viewset for checking database changes.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(PictureViewSet, self).dispatch(*args, **kwargs)


class PictureSearchAPIView(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    search_fields = (
        'picture_id',
        'author',
        'camera',
        'tags'
    )
    filter_backends = (filters.SearchFilter,)
