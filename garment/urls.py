"""garment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_aoutpp.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
# -need to import this for upload image in the admin
from django.conf.urls.static import static
# -new
# form django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# -import the store
urlpatterns = [
    #path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securitylogin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('about/', include('about.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),

    # Orders
    path('orders/', include('orders.urls')),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#ADD
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


