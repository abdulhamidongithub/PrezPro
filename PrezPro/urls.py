from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from appv1.views import (
    FanlarAPIView,
    DarsliklarAPIView,
    PresentationsAPIView,
    PresentationAPIView
)

schema_view = get_schema_view(
   openapi.Info(
      title="PrezPro API",
      default_version='v1',
      description="web-API's for an educational platform",
      contact=openapi.Contact(email="1997abdulhamid@gmail.com"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('fanlar/', FanlarAPIView.as_view()),
    path('darsliklar/', DarsliklarAPIView.as_view()),
    path('presentations/', PresentationsAPIView.as_view()),
    path('presentation/<int:pk>/', PresentationAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
