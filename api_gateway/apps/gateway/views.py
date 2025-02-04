from django.http import JsonResponse
import requests

DOMAINS = {
    "user": "http://localhost",
    "order": "http://localhost",
    "production": "http://localhost",
    "notification": "http://localhost",
}

SERVICES = {
    "user": f"{DOMAINS['user']}:8001",
    "order": f"{DOMAINS['order']}:8002",
    "production": f"{DOMAINS['production']}:8003",
    "notification": f"{DOMAINS['notification']}:8004",
}


def proxy_request(request, service_name, path):
    if service_name not in SERVICES:
        return JsonResponse({"error": "Service not found"}, status=404)

    service_url = f"{SERVICES[service_name]}{path}"
    response = requests.request(
        method=request.method,
        url=service_url,
        headers={
            key: value for (key, value) in request.headers.items() if key != "Host"
        },
        data=request.body,
        allow_redirects=True,
    )
    return JsonResponse(response.json(), status=response.status_code)
