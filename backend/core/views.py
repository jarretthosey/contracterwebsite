from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Users, Quotes
from .serializers import *
from .forms import UserForm, UserQuote
import json

def user_list(request):
    users = Users.objects.all()
    serialized_users = CoreSerializer(users).users
    return JsonResponse(data=serialized_users, status=200)

@csrf_exempt
def new_user(request):
    if request.method == "POST":
        data = json.load(request)
        form = UserForm(data)
        if form.is_valid():
            user = form.save(commit=True)
            serialized_user = CoreSerializer(user).users
            return JsonResponse(data=serialized_user, status=200)

def user_detial(request, user_id):
    users = Users.objects.filter(id=user_id)
    serialized_users = CoreSerializer(users).users
    return JsonResponse(data=serialized_users, status=200)

@csrf_exempt
def edit_user(request, user_id):
    if request.method == "POST":
        user = Users.objects.filter(id=user_id)
        data = json.load(request)
        form = UserForm(data, instance=user)
        if form.is_valid():
            user = form.save(commit=True)
            serialized_user = CoreSerializer(user).users
            return JsonResponse(data=serialized_user, status=200)

def delete_user(request, user_id):
    pass

def quote_list(request):
    quotes = Quotes.objects.all()
    serialized_quotes = CoreSerializer(quotes).quotes
    return JsonResponse(data=serialized_quotes, status=200)

def new_quote(request):
    pass

def quote_detial(request, quote_id):
    quotes = Quotes.objects.filter(id=quote_id)
    serialized_quotes = CoreSerializer(quotes).quotes
    return JsonResponse(data=serialized_quotes, status=200)

def edit_quote(user, quote_id):
    pass

def delete_quote(request, quote_id):
    pass

def users_quotes(request, user_id):
    quotes = Quotes.objects.filter(user=user_id)
    serialized_quotes = CoreSerializer(quotes).quotes
    return JsonResponse(data=serialized_quotes, status=200)