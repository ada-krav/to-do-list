from django.urls import path

from todo.views import TagListView, TagCreateView

urlpatterns = [
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]


app_name = "todo"
