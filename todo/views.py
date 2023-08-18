from django.shortcuts import render, redirect, get_object_or_404
from .models import Item


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "Post":
        name = request.post.get("item_name")
        done = "done" in request.Post
        Item.objects.create(name=name, done=done)

        return redirect("get_todo_list")
    return render(request, 'todo/add_item.html')
