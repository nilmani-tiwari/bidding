"""bidding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from bidapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path('registration', register_user, name='register'),
    # path('logout/', logoutUser, name='logoutUser'),
    # path('home/', home, name='home'),
    #  path('add-items/', add_items, name='add_items'),
    #  path('all-items/', all_items, name='all_items'),
    #  path('all-vender/', all_vender, name='all_vender'),
    #  path('loest-bidder/<item_id>/', loest_vender, name='loest_vender'),
    #  path('accounts/login/', login_user, name='login'),
    # path('', login_user, name='login'),
    
    # ################################################## 
    # path('v-home/', vhome, name='vhome'),
    # path('bid-item/<item_id>/', bid_item, name='bid_item'),
    
    # ##################################################
     path('speech/', test_speech, name='test'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)     
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)