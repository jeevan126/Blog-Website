from django.shortcuts import render, redirect, get_object_or_404

def landing(request):
    return render(request,'base_page.html')
