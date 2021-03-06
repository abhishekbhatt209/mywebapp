
from django.shortcuts import render,redirect
from .models import Document
from django import forms

# Create your views here.

# def home(request):
#     return render(request, 'index.html')

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name','phone' ,'email', 'document', )


def home(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
         form = DocumentForm()
    return render(request, 'index.html',{'form': form})
            
