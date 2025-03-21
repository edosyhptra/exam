from django.shortcuts import render
from app_blog.utility import query

def view(request, id):
    if request.method == 'GET':
        result = query("SELECT * FROM blog_post WHERE id = %s", [id])
        if not result:
            return render(request, "app_blog/read.html", {"error": "Post tidak ditemukan"})
        
        print(result)
    return render(request, "app_blog/read.html", {"post": result[0]})

    