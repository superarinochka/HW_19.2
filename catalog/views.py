from django.shortcuts import render


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    if request.method == 'POST':
        visiter = dict()
        visiter['name'] = request.POST.get('name', None)
        visiter['phone'] = request.POST.get('phone', None)
        visiter['message'] = request.POST.get('message', None)
        print(visiter)
    return render(request, "catalog/contacts.html")