from django.urls import path
from . import views

urlpatterns = [
    path('users', views.user_list, name='user_list'),
    path('new_user', views.new_user, name='new_user' ),
    path('users/<int:user_id>', views.user_detial, name='user_detial'),
    path('users/<int:user_id>/edit', views.edit_user, name='edit_user'),
    path('users/<int:user_id>/delete', views.delete_user, name="delete_user"),
    path('quotes', views.quote_list, name='quote_list'),
    path('new_quote', views.new_quote, name='new_quote' ),
    path('quotes/<int:quote_id>', views.quote_detial, name='quote_detial'),
    path('quotes/<int:quote_id>/edit', views.edit_quote, name='edit_quote'),
    path('quotes/<int:quote_id>/delete', views.delete_quote, name='delete_quote'),
    path('quotes/<int:user_id>', views.users_quotes, name='users_quotes'),
]