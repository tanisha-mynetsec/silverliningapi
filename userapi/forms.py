from django import forms

class OtpForm(forms.Form):
    otp = forms.CharField(required=True, widget=forms.PasswordInput)