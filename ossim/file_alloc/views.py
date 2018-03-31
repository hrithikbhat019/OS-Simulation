from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class contiguous(TemplateView):
	template_name = "contiguous_file_alloc.html"
class linked(TemplateView):
	template_name = "linked_file_allocation.html"

