from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

from .forms import SignUpForm
from .utils import send_confirmation_email
from .tokens import confirm_email_token_generator


# Create your views here.
User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request, user)
            return render(request, 'registration/signup_success.html')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)

    if confirm_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    
    else:
        return HttpResponseBadRequest('Bad Token')

@login_required
def update_profile(request, uid):
    user = get_object_or_404(User, pk=uid)
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'registration/updated_success.html')
    else:
        form = SignUpForm(instance=request.user)
    
    return render(request, 'registration/update_profile.html', {'form': form})

@login_required
def delete_account(request, uid):
    user = get_object_or_404(User, pk=uid)
    if request.method == 'POST':
        user.delete()
        return render(request, 'registration/deleted_success.html')



