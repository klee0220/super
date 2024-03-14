from django.shortcuts import render
from order_app.models import Request
from order_app.models import CustomUser, FieldAnalyzer

# Создаем нового пользователя и анализатора
user_instance = CustomUser.objects.create(name='John Doe', address='123 Main Street')
analyzer_instance = FieldAnalyzer.objects.create(user=user_instance, status='Active')


# Создание новой заявки
request = Request.objects.create(request_type='Type', urgency='Urgent', user=user_instance, analyzer=analyzer_instance)
request_id = request.id  # Получение заявки по идентификатору (ID)
request = Request.objects.get(id=request_id)
# Изменение статуса на "В работе"
request.mark_as_in_progress()
# Изменение статуса на "Выполнено"
request.mark_as_completed()
# Получение всех заявок
all_requests = Request.objects.all()
# Получение заявок для конкретного пользователя
user_requests = Request.objects.filter(user=user_instance)
# Получение заявок для конкретного анализатора
analyzer_requests = Request.objects.filter(analyzer=analyzer_instance)
# Получение заявки по идентификатору (ID)
request = Request.objects.get(id=request_id)
# Удаление заявки
request.delete()