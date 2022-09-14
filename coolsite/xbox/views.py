from django.shortcuts import render
from django.views.generic import ListView, View
from .models import *
from django.template.defaulttags import register

class XboxHome(ListView):
    model = News
    template_name = 'xbox/base.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class XboxNews(View):
    def get(self, request):
        return render(request,'xbox/news.html')

class XboxSales(View):
    def get(self, request):
        return render(request,'xbox/sales.html')

class XboxAboutUs(View):
    def get(self, request):
        return render(request,'xbox/about_us.html')

class XboxContacts(View):
    def get(self, request):
        return render(request,'xbox/contacts.html')