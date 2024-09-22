from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from .models import Order


def mark_received(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "ההזמנה התקבלה"
    order.save()
    print(f"Order {order_id} status updated to received.")  # הוספת לוג
    return redirect('admin:orders_order_changelist')

def mark_approved(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "ההזמנה אושרה"
    order.save()
    print(f"Order {order_id} status updated to approved.")  # הוספת לוג
    return redirect('admin:orders_order_changelist')

def mark_arrived(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "ההזמנה הגיעה לחנות"
    order.save()
    print(f"Order {order_id} status updated to arrived.")  # הוספת לוג
    return redirect('admin:orders_order_changelist')

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing_page')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def landing_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'landing_page.html')

@login_required
def new_order(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        details = request.POST.get('details')
        Order.objects.create(user=request.user, details=details)
        return redirect('landing_page')
    return render(request, 'new_order.html')

@login_required
def track_orders(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders = Order.objects.filter(user=request.user)
    return render(request, 'track_orders.html', {'orders': orders})

def logout_view(request):
    auth_logout(request)
    return redirect('home')  # או 'landing_page' אם אתה מעדיף