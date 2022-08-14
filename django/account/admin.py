from django.contrib import admin
from .models import Account

# エクセルを読み込むプラグイン
from import_export import resources
from import_export.admin import ImportExportMixin


# Register your models here.
class AccountResource(resources.ModelResource):
    class Meta:
        model = Account


@admin.register(Account)
class WeatherAdmin(ImportExportMixin, admin.ModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = (
        "id",
        "email",
        "username",
        "date_joined",
        "last_login",
        "is_admin",
        "is_active",
        "is_staff",
        "is_superuser",
)

    # django-import-exportsの設定
    resource_class = AccountResource
