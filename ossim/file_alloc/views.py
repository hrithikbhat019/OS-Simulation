from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class home(TemplateView):
	template_name = "home.html"
class contiguous(TemplateView):
	template_name = "index.html"
class linked(TemplateView):
	template_name = "tmp-linked.html"
class indexed(TemplateView):
	template_name = "tmp-indexed.html"


