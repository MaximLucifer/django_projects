import requests
from django.http import JsonResponse

class ExternalAPIClient:
    API_BASE_URL = 'http://127.0.0.1:8000/api/'  # URL приложения 3
    TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyNjM3OTg1LCJpYXQiOjE3MzI2Mzc2ODUsImp0aSI6ImRmMDQ5ZjQ5OTZiZjRhNmFhMTQ5ZmU1NDAzOTQ0OGFlIiwidXNlcl9pZCI6MX0.ECLbBLztudmztggynY73HhDqfLT0CRQQIQcqN1rt0Y4'  # Добавьте сюда токен для приложения 1

    @staticmethod
    def get_items():
        headers = {'Authorization': f'Bearer {ExternalAPIClient.TOKEN}'}
        response = requests.get(f'{ExternalAPIClient.API_BASE_URL}items/', headers=headers)
        return response.json()

def fetch_items(request):
    data = ExternalAPIClient.get_items()
    return JsonResponse(data, safe=False)