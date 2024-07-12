from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    if request.method == "POST":
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')

        try:
            send_mail(subject, message_body, settings.EMAIL_HOST_USER, [recipient])
            messages.success(request, 'Email sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending email: {str(e)}')

        return redirect('index')

    return render(request, 'app/index.html')
