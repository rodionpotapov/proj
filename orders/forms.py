
import re
from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField()
    delivery_adress = forms.CharField(required=False)
    payment_on_get = forms.CharField()

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError('Номер телефона может содержать только цифры')
        
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError('Неверный формат номера')
        
        return data



    # first_name = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {
    #             'class' : 'form-control',
    #             'placeholder' : 'Введите ваше имя',
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {
    #             'class' : 'form-control',
    #             'placeholder':'Введите вашу фамилию',
    #         }
    #     )
    # )

    # phone_number = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {
    #             'class' : 'form-control',
    #             'placeholder' : 'Введите номер телефона',
    #         }
    #     )
    # )

    # requires_delivery = forms.CharField(
    #     widget = forms.RadioSelect(),
    #     choices = [
    #         ('0',False) ,
    #         ('1', True),
    #     ],
    #     initial=0,
    # )
    # delivery_adress = forms.CharField(
    #     widget= forms.Textarea(
    #         attrs={
    #             'class' : 'form-control',
    #             'id' : 'delivery-adress',
    #             'rows': 2,
    #             'placeholder' : 'Введите адрес доставки',
    #         }
    #     )
    # )
    # payment_on_get = forms.ChoiceField(
    #     widget = forms.RadioSelect(),
    #     choices=[
    #         ('0',False),
    #         ('1',True),
    #     ],
    #     initial = 'card',
    # )


    # комментарий тоже верный но он в бэкэнде выполняет работу фронтэнда