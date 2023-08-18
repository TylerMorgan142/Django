from django.shortcuts import render, redirect, get_object_or_404
from .models import Item


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

