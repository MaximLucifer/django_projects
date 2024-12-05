import requests
from django.http import JsonResponse

class ExternalAPIClient:
    API_BASE_URL = 'http://127.0.0.1:8000/api/'  # URL приложения 3
    TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMzNDIyMzU3LCJpYXQiOjE3MzM0MjIwNTcsImp0aSI6IjkwMDM3ODJjZmVjOTRmZmRiYmZmNjAzYzAwN2NlN2IwIiwidXNlcl9pZCI6MX0.ospNU4M_84jqN_Nylv3KD34JUvqkvFP765CVW9kU99E'  # Добавьте сюда токен для приложения 1

    @staticmethod
    def get_items():
        headers = {'Authorization': f'Bearer {ExternalAPIClient.TOKEN}'}
        response = requests.get(f'{ExternalAPIClient.API_BASE_URL}items/', headers=headers)
        return response.json()

def fetch_items(request):
    data = ExternalAPIClient.get_items()
    return JsonResponse(data, safe=False)