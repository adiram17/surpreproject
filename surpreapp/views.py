from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@login_required
def home(request):
    return render(request, 'pages/home.html', {})

@login_required
def score(request):
    return render(request, 'pages/score.html', {})

@login_required
def about(request):
    return render(request, 'pages/about.html', {})

@login_required
def scoreattribute(request):
    return render(request, 'pages/scoreattribute.html', {})

@login_required
def scorescale(request):
    return render(request, 'pages/scorescale.html', {})
    
@login_required
def scorelevel(request):
    return render(request, 'pages/scorelevel.html', {})

@login_required
def test(request):
    return render(request, 'pages/test.html', {})

@csrf_protect
def getmessage(request):
    if request.method == 'POST':
        messages.success(request, 'Content Message')
        return redirect('/surpre/test')
    else:
        return redirect('/surpre/test')

@csrf_protect
def scorepost(request):
    if request.method == 'POST':
        if ('calculate' in request.POST):
            messages.success(request, 'Calculated')
        elif('draft' in request.POST):
            messages.success(request, 'Draft')
        elif('save' in request.POST):
            messages.success(request, 'Save')
        return redirect('/surpre/score')
    else:
        return redirect('/surpre/score')