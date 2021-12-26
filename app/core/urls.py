# Third party dependencies
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ResuelveTuDeuda Backend",
        default_version='v1',
        description="ResuelveTuDeuda Backend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jorgeabm1992@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
