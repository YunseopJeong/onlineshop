from django import forms

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False,
                                   initial=False,
                                   # 화면에 안 보이게 함.
                                   widget=forms.HiddenInput)