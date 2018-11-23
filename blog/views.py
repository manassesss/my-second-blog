from django.shortcuts import render
from django.utils import timezone
from .models import PostLindo


def post_list(request):
    posts = PostLindo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
