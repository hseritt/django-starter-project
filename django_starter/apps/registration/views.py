# views.py
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegisterForm
from .models import Profile
from django_starter.apps.core.logger import get_logger

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print("User %s saved." % user)

            send_mail(
                "Verify your email address",
                "Click on http://localhost:8000/registration/verify/{}".format(
                    user.profile.verification
                ),
                "admin@localhost",
                [user.email],
                fail_silently=False,
            )
            print("Passed the send_mail() ...")

            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


def verify(request, verification):
    logger = get_logger()
    try:
        profile = Profile.objects.get(verification=verification)
        user = profile.user
        profile.is_verified = True
        user.is_active = True

        try:
            profile.save()
            user.save()
        except Exception as err:
            logger.exception(err)

    except (Profile.DoesNotExist, User.DoesNotExist) as err:
        logger.exception(err)
        return render(
            request,
            "registration/error.html",
            {"error": "Invalid verification"},
        )
    return render(request, "registration/success.html", {})
