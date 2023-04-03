from django.urls import path

from todo.views import TagListView, TagCreateView, TagUpdateView, TagDeleteView, TaskLiskView, TaskCreateView

urlpatterns = [
    path("", TaskLiskView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),

]


app_name = "todo"
