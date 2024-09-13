from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
from .models import UserProfile
def empDashboard(request):
    userName = None
    userName = request.user.username
    userId=request.user.id
    dept_name = UserProfile.objects.filter(user_id=userId).select_related('department').values_list('department__DeptName', flat=True).first()
    title = request.POST.get('reader_title')
    # TODO : save the updated title to the UserProfile database 
    print('TITLE -->' , title)
    return render(request,'dashboard.html',context={
        'name':userName,
        'loggedIn':True,
        'userId':userId,
        'deptName':dept_name
        })

def empLogout(request):
    if request.method == 'GET':
        logout(request)
        print('logged out')
        return redirect('index')
    return render(request,'index.html',context={})

def index(request):
    return render(request,'index.html',context={})

def empLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print("VALIDDDDDDD----" , user)
            login(request,user)
            return redirect('empDashboard')
    else:
        initial_data = {'username':'','password':''}
        form = AuthenticationForm(initial=initial_data)
        return render(request,'employee.html',{'form':form})
    return render(request,'index.html',{'form':form})