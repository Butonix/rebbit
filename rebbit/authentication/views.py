import requests

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.conf import settings

from rebbit.authentication.forms import SignUpForm
from rebbit.feeds.models import Feed


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                User.objects.create_user(username=username, password=password,
                                         email=email)
                user = authenticate(username=username, password=password)
                login(request, user)
                welcome_post = '{0} has joined the network.'.format(user.username)
                feed = Feed(user=user, post=welcome_post)
                feed.save()
                return redirect('/')
            else:
                recaptcha_error = "Please solve the reCAPTCHA for creating an account."
                return render(request, 'authentication/signup.html',
                              {'form': SignUpForm(),
                               'recaptcha_error': recaptcha_error})

        else:
            return render(request, 'authentication/signup.html',
                          {'form': form})

    else:
        return render(request, 'authentication/signup.html',
                      {'form': SignUpForm()})
