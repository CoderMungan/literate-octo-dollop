from django.http import JsonResponse
import requests

SERVICES = {
    "user": "http://user-service:8001",
    "order": "http://order-service:8002",
    "production": "http://production-service:8003",
}

def proxy_request(request, service_name, path):
    if service_name not in SERVICES:
        return JsonResponse({"error": "Service not found"}, status=404)

    service_url = f"{SERVICES[service_name]}{path}"
    response = requests.request(
        method=request.method,
        url=service_url,
        headers={key: value for (key, value) in request.headers.items() if key != "Host"},
        data=request.body,
        allow_redirects=True,
    )
    return JsonResponse(response.json(), status=response.status_code)

