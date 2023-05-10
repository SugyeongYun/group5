from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Restaurant, CartItem, Question, Preference
from .forms import QuestionForm, PreferenceForm
from django.utils import timezone
from .ai import*

# Create your views here.

def index(request):
    return render(request, 'index.html')

def discover(request):
    restaurant_list = Restaurant.objects.order_by('id')
    context = {'restaurants': restaurant_list}
    return render(request, 'discover.html', context)

def restaurant_info(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    context = {'restaurant': restaurant}
    return render(request, 'restaurant_info.html', context)

@login_required(login_url='common:login')
def add_item(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    try:
        cart = CartItem.objects.get(restaurant__id=restaurant.pk, user__id=request.user.pk)
        messages.error(request, 'Item already added to cart')

    except CartItem.DoesNotExist:
        user = User.objects.get(pk=request.user.pk)
        cart = CartItem(user=user, restaurant=restaurant)
        cart.save()
        messages.success(request, 'Item added to cart')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='common:login')
def delete_item(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    if request.user == cart_item.user:
        cart_item.delete()
        messages.success(request, 'Item removed from cart')
        return redirect('group5:my_cart')
    else:
        messages.error(request, 'Unauthorized user')
        return redirect('group5:my_cart')

@login_required(login_url='common:login')
def my_cart(request):
    cart_items = CartItem.objects.filter(user__id=request.user.pk)
    if cart_items is not None:
        context = {'cart_items': cart_items}
        return render(request, 'cart_list.html', context)
    return redirect('group5:my_cart')

@login_required(login_url='common:login')
def food_planner(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            preference = form.save(commit=False)
            input_time = get_time(preference.date)
            input_bungi = get_bungi(preference.date)
            input_day = get_day(preference.date)
            restaurants = get_recommendation(preference.category, [input_time, input_bungi, input_day, preference.person_cnt, preference.price])
            restaurant1 = Restaurant.objects.get(name=restaurants[0])
            restaurant2 = Restaurant.objects.get(name=restaurants[1])
            restaurant3 = Restaurant.objects.get(name=restaurants[2])
            context = {
                'restaurant1':restaurant1,
                'restaurant2':restaurant2,
                'restaurant3':restaurant3,
            }
            return render(request, 'result.html', context)
    else:
        form = PreferenceForm()
    context = {'form': form}
    return render(request, 'food_planner.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            messages.success(request, 'Form submitted')
            return redirect('group5:contact_us')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'contact_us.html', context)