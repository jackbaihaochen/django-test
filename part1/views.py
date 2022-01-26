from django.shortcuts import render

# Create your views here.
def test_view (request, *args, **kwargs) :
    return render(request, 'test_template.html', {})

def test_home (request, *args, **kwargs) :
    return render(request, 'base.html', {})