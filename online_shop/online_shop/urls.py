"""online_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from core.views import CustomerRegisterView, CustomerLoginView, logout_view

urlpatterns = i18n_patterns(
    path("/", include('home.urls', namespace='home')),
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('product/', include('product.urls', namespace='product')),
    path('customer/', include('customer.urls', namespace='customer')),
    path('register/', CustomerRegisterView.as_view(), name='register-customer'),
    path('login/', CustomerLoginView.as_view(), name='login-customer'),
    path('logout/', logout_view, name='logout-customer'),
    path('order/', include('order.urls', namespace='order')),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
