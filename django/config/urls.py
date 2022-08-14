from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import static

from rest_framework_jwt.views import obtain_jwt_token  # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', obtain_jwt_token),  # 追加
    re_path('media/(?P<path>.*)', static.serve,
            {'document_root': settings.MEDIA_ROOT}),
] + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
