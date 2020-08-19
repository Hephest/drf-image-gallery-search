from rest_framework.routers import DefaultRouter
from gallery import views

router = DefaultRouter()
router.register(r'pictures', views.PictureViewSet, basename='pictures')

urlpatterns = router.urls
