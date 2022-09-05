from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Subscription
from .models import Payment
from .forms import SubscriptionForm
# Create your views here.


def home(request):
    return render(request, 'subscription.html')


def createsubscription(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SubscriptionForm()
    return render(request, "subscription.html", {'form': form})


def success(request):
    return render(request, 'success.html')


def displaysubscription(request):
    obj = Subscription.objects.all()
    #context = {'object': obj}
    return render(request, 'package.html', {'object': obj})


def payment(request, subscription_id):
    subscription = Subscription.objects.get(pk=subscription_id)
    return render(request, 'payment.html', {"subscription": subscription})


def confirmation(request):
    if request.method == 'POST':
        if request.POST.get('User_id') and request.POST.get('Subscription_id') and request.POST.get('TotalAmount'):
            payment = Payment()
            payment.User_id = request.POST.get('User_id')
            payment.Subcription_id = request.POST.get('Subscription_id')
            payment.TotalAmount = request.POST.get('TotalAmount')
            payment.save()

            return HttpResponseRedirect('success')
        else:
            return render(request, "payment.html")
