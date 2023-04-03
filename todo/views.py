from django.shortcuts import render
from django.views import generic

from todo.models import Tag


# Create your views here.
class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todo/tags_list.html"
