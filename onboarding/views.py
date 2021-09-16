from django.views import View
from django.shortcuts import render
from .models import Target, Manager

class OnboardingView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        targets = request.POST.get('targets')

        manager = Manager(name=name, phone_number=phone_number, email=email)
        manager.save()

        targetEmails = targets.split(",")
        for targetEmail in targetEmails:
            target = Target(email=targetEmail)
            target.save()
            manager.targets.add(target)

        return render(request, 'index.html')
