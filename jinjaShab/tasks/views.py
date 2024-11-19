from django.shortcuts import render

# Create your views here.
def user_greeting(request):
    return render(request, 'user_greeting.html')

def class_list(request):
    classes = ['Ведьма', 'Дикарь', 'Охотница', 'Бандит', 'Дворянка', 'Дуэлянт', 'Жрец']
    return render(request, 'class_list.html', {'classes': classes})

def currency_table(request):
    currencies = [
        ['Название', 'Ценность (в Божественных сферах/Сферах хаоса)', 'Редкость'],
        ['Зеркало Каландры', '700 Божественных сфер/210 000 Сфер хаоса', 'Легендарная'],
        ['Божественная сфера', '300 Сфер хаоса', 'Легендарная'],
        ['Сфера возвышения', '15 Сфер хаоса', 'Редкая'],
        ['Сфера хаоса', '1', 'Редкая']
    ]
    return render(request, 'currency_table.html', {'currencies': currencies})