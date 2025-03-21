from django.shortcuts import render
from app_blog.utility import query

def view(request):
    posts = None
    if request.method == 'GET' :
        posts = query("SELECT * FROM blog_post ORDER BY ID DESC")
        print(posts)

    return render(request, 'app_blog/list.html', {'posts': posts})
