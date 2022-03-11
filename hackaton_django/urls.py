from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Online Store",
      default_version='v1',
      description="Викторо и Талант Пушки интересно заметят это. Заметили, лол кек чебурек  ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/category/', include('applications.category.urls')),
    path('api/v1/product/', include('applications.product.urls')),
    path('api/v1/review/', include('applications.review.urls')),
    path('api/v1/order/', include('applications.order.urls')),
    path('', include('applications.chat.urls')),
    path('api/v1/swagger(.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)