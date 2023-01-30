from django.contrib import admin
from django.urls import path, include
from .views import Bismillah

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Bismillah, name="Bismillah"),

    path('ajax/', include('AtmAjax.urls')),
]
