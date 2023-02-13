
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from admin_app.views import UserView,DefaulterView
from document_verification.views import DocumentView,BankView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('user',UserView,basename='user')
router.register('defaulter',DefaulterView,basename='defaulter')
router.register('document',DocumentView,basename='document')
router.register('bank',BankView,basename='bank')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
