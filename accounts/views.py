from .forms import SignUpForm
from django.shortcuts import redirect, render

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})