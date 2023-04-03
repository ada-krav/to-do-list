from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag


# Create your views here.
class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
