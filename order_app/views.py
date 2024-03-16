from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Request, FieldAnalyzer
from django.template.loader import get_template
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, RequestForm


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
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_instance = form.save(commit=False)
            # Получаем текущего пользователя
            user = request.user
            # Получаем или создаем анализатор для текущего пользователя
            analyzer_instance, created = FieldAnalyzer.objects.get_or_create(user=user)
            # Проверяем, был ли создан новый анализатор
            if created:
                analyzer_instance.status = 'Active'  # Присваиваем статус "Active"
                analyzer_instance.save()
            # Присваиваем анализатору и сохраняем заявку
            request_instance.analyzer = analyzer_instance
            request_instance.user = user
            request_instance.save()
            return redirect('view_all_requests')
    else:
        form = RequestForm()
    return render(request, 'create_request.html', {'form': form})


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
    return render(request, 'view_all_requests.html', {'all_requests': all_requests})


def order_home(request):
    registration_form = RegistrationForm()  # Перенесли сюда
    template = get_template('order_home.html')
    return HttpResponse(template.render({'registration_form': registration_form}, request))


def request_detail(request, request_id):
    request_instance = get_object_or_404(Request, pk=request_id)
    return render(request, 'request_detail.html', {'request_instance': request_instance})
