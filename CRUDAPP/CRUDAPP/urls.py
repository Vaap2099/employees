from django.contrib import admin
from django.urls import path, include
from employee.urls import urlpatterns_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns_employee)),
]
