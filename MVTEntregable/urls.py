from django.contrib import admin
from django.urls import path
from MVT.views import familiar1 , familiar2 , familiar3 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Familiar1/', familiar1),
    path('Familiar2/', familiar2),
    path('Familiar3/', familiar3),
]
