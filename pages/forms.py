from django import forms

from pages.models import ContactModel

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            return phone_number
        
        if len(phone_number) != 13:
            forms.ValidationError("Phone number should be exectly 13 length")
        
        return phone_number 
