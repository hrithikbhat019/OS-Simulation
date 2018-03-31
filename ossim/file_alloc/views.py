from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class contiguous(TemplateView):
	template_name = "contiguous_file_allocation.html"
class linked(TemplateView):
	template_name = "linked_file_allocation.html"
class indexed(TemplateView):
	template_name = "indexed_file_allocation.html"


