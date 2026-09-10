from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def hi(request):
     return render(request, "experimentation/base.html")