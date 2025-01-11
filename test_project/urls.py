"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.Products, name='Products')
Class-based views
    1. Add an import:  from other_app.views import Products
    2. Add a URL to urlpatterns:  path('', Products.as_view(), name='Products')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('authentications.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('authentications.urls')),
    path('verification/', include('verify_email.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
]
