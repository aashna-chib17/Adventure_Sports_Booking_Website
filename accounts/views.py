from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,"That Username is taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"That email is taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password
                    )
                    user.save()
                    messages.success(request,"You are now registered")
                    return redirect('login')


                


        
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
        
        
        
        
        
    else:

    
        return render(request,'accounts/register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password= password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are now logged in")
            return redirect('index')
        else:
            messages.error(request,"User Not Found")
            return redirect('login')
            
    else:
        return render(request,'accounts/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"You have been logged out")
        return redirect('index')


