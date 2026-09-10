from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def hi(request):
     return render(request, "experimentation/base.html")

def error_404(request, exception):
    return render(request, "experimentation/404.html", status=404)