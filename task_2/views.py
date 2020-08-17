from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import UserProfile
def page1(request):
    if request.method == 'POST':
        f_name = request.POST.get('fname')
        l_name = request.POST['lname']
        ph_no = request.POST['phno']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']

        try:
            user = User.objects.get(username=email)
            return HttpResponse('<h2>User exists</h2>')
        except User.DoesNotExist:
            user = User.objects.create_user(username=email, password=password)
            user.save()
        profile = User(f_name=f_name, l_name=l_name, ph_no=ph_no, email=email, gender=gender, user=user)
        profile.save()

        return redirect('page1')
    else:
        return render(request,'Page1.html')


def page2(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            profile = UserProfile.objects.get(email=email)
            return render(request, 'Page3.html', {'profile': profile, 'message': 'Found user!'})
        except UserProfile.DoesNotExist:
            return render(request, 'Page3.html', {'message': 'Sorry no user with the entered email found'})

    else:
        return render(request, 'Page2.html')