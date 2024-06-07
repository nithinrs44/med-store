from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import records

from django.contrib import messages

from .forms import SearchForm


    # - homepage


def homepg(request):
    
    return render(request,'index.html')


    # - register


def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request,"Account created successfully !")
            
            return redirect('login')
            
    context = {'form':form}
    
    return render(request,'register.html',context=context)


    # - login 

def my_login(request):
    
    form = LoginForm()
    
    if request.method == "POST":
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username,password=password)
            
            if user is not None:
                
                auth.login(request,user)

                messages.success(request,"Logged in successfully !")

                return redirect('dashboard')


    context = {'form': form}
    
    return render(request,'login.html',context=context)


    # - dashboard
    
@login_required(login_url='login')
def dashboard(request):
    
    my_records = records.objects.all()
    
    context = {'records': my_records}
        
    return render(request,'dashboard.html',context=context)


    
@login_required(login_url='login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'create-record.html', context=context)


# - Update a record 

@login_required(login_url='login')
def update_record(request, pk):

    record = records.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect('dashboard')
        
    context = {'form':form}

    return render(request, 'update-record.html', context=context)


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = records.objects.get(id=pk)

    context = {'records':all_records}

    return render(request, 'view-record.html', context=context)


# - Delete a record

@login_required(login_url='login')
def delete_record(request, pk):

    record = records.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect('dashboard')



# - User logout

def logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect('login')



# - search



@login_required(login_url='log')
def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data.get('q')
        results = records.objects.filter(medicine_name__istartswith=query)
    else:
        results = records.objects.all()

    return render(request, 'dashboard.html',{'records':results})

            
            
    



