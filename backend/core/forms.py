from django import forms
from .models import Users, Quotes

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            'first_name',
             'last_name',
             'middle_name',
             'phone_number',
             'address',
             'state',
             'zip_code',
             'city',
             'email',
             'admin',
            ]

class UserQuote(forms.ModelForm):
    class Meta:
        model = Quotes
        fields = [
            'start_date_requested',
            'end_date_requested',
            'quoted_price',
            'final_cost',
            'completed',
            'accepted',
            'user',
        ]