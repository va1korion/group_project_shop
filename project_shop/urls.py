"""project_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from pages import views
from products.views import product_view
from cart.views import cart_view
from order.views import order_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from users.views import signup, personal_view

urlpatterns = [
    path('admin/', admin.site.urls, name='Admin'),
    path('', views.index, name='Home'),
    path('index.html', views.index, name='Home'),

    path('users/personal/', personal_view, name='Personal'),     # legacy
    path('products/<int:id>', product_view, name='Product'),
    path('order/<int:id>', order_view, name='Order'),
    path('accounts/cart/', cart_view, name='Cart'),
    path('accounts/signup/', signup, name='Sign Up'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='Login'),
    path('accounts/profile/', personal_view, name='Personal')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
