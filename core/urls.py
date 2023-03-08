from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title='MakersOverflow',
        description='StackOverflow for makers',
        default_version='v1'
    ), public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('questions.urls')),
    path('api/v1/', include('answers.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('favorites.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
