from django.views import View
from django.shortcuts import render
from .models import Target, Manager
from onboarding.services import send_email


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

        target_emails = targets.split(",")
        for target_email in target_emails:
            target = Target(email=target_email)
            target.save()
            manager.targets.add(target)
        send_email(target_emails)
        return render(request, 'sent.html')
