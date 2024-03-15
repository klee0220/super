from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Request, CustomUser, FieldAnalyzer
from django.template.loader import get_template
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth import logout


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_all_requests')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def create_request(request):
    # Создаем нового пользователя и анализатора
    user_instance = CustomUser.objects.create(name='John Doe', address='123 Main Street')
    analyzer_instance = FieldAnalyzer.objects.create(user=user_instance, status='Active')

    # Создаем новую заявку
    new_request = Request.objects.create(request_type='Type', urgency='Urgent', user=user_instance, analyzer=analyzer_instance)

    return HttpResponse("Request created successfully!")


def update_request_status(request, request_id):
    # Получаем заявку по идентификатору
    request_instance = get_object_or_404(Request, pk=request_id)

    # Обновляем статус заявки
    request_instance.mark_as_in_progress()  # Метод из модели FieldAnalyzer

    return HttpResponse("Request status updated to 'In Progress'!")


def complete_request(request, request_id):
    # Получаем заявку по идентификатору
    request_instance = get_object_or_404(Request, pk=request_id)

    # Обновляем статус заявки
    request_instance.mark_as_completed()  # Метод из модели FieldAnalyzer

    return HttpResponse("Request status updated to 'Completed'!")


def view_all_requests(request):
    # Получаем все заявки
    all_requests = Request.objects.all()

    # Выводим информацию о заявках
    output = ""
    for request_instance in all_requests:
        output += f"Request ID: {request_instance.id}, Type: {request_instance.request_type}, Urgency: {request_instance.urgency}, Status: {request_instance.status}<br>"

    return HttpResponse(output)


def order_home(request):
    registration_form = RegistrationForm()  # Перенесли сюда
    template = get_template('order_home.html')
    return HttpResponse(template.render({'registration_form': registration_form}, request))
    #return HttpResponse(template.render())
    #return render(request, 'order_home.html', {'registration_form': registration_form})