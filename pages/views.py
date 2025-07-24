from django.shortcuts import render, redirect
from pages.forms import ContactModelForm
from django.contrib import messages

# Create your views here.
def home_page_view(request):
    return render(request, template_name='index.html')

def contact_page_view(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been send to admins ✅")
        else:
            messages.error(request, "Please, check your data ❌")
            return redirect("pages:contact")
    else:
        return render(request, 'htmls/contact.html')

