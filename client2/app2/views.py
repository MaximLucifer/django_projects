import requests
from django.http import JsonResponse

class ExternalAPIClient:
    API_BASE_URL = 'http://127.0.0.1:8000/api/'  # URL приложения 3

    @staticmethod
    def get_items():
        response = requests.get(f'{ExternalAPIClient.API_BASE_URL}items/')
        return response.json()

def fetch_items(request):
    data = ExternalAPIClient.get_items()
    return JsonResponse(data, safe=False)

