"""
URL configuration for api_gateway project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
import requests

def forward_request(request, service, endpoint):
    service_urls = {
        'user': 'http://user_service:8001/',
        'product': 'http://product_service:8002/',
        'order': 'http://order_service:8003/',
    }
    url = f"{service_urls[service]}{endpoint}"
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        data=request.body,
        params=request.GET
    )
    return HttpResponse(response.content, status=response.status_code)

urlpatterns = [
    path('<str:service>/<path:endpoint>', forward_request),
]