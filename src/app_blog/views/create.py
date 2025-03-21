from django.shortcuts import render
from app_blog.utility import query

def view(request):
    result = None
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        result = query("INSERT INTO blog_post (title, content) VALUES (%s, %s) returning *", [title, content])  
        print(result)
    return render(request, 'app_blog/create.html')