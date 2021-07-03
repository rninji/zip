from .forms import CustomUserChangeForm, ProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import Profile 
from item.models import Item


# Create your views here.
def signup_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')

    else:
        form=UserCreationForm()
    return render(request, 'signup.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request=request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else :
     form=AuthenticationForm()
    return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

def mypage_view(request, username):
    person=get_object_or_404(get_user_model(), username=username)
    # items = Item.objects.all()
    # item_list=items.filter(username=request.user.username)
    return render(request,'mypage.html',{'person':person})

def profile(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_change_form.is_valid() and profile_form.is_valid():
            user = user_change_form.save()
            profile_form.save()
            return redirect('mypage', user.username)
        return redirect('profile')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        # 새롭게 추가하는 것이 아니라 수정하는 것이기 때문에
        # 기존의 정보를 가져오기 위해 instance를 지정해야 한다.
        profile, create = Profile.objects.get_or_create(user=request.user)
        # Profile 모델은 User 모델과 1:1 매칭이 되어있지만
        # User 모델에 새로운 인스턴스가 생성된다고 해서 그에 매칭되는 Profile 인스턴스가 생성되는 것은 아니기 때문에
        # 매칭되는 Profile 인스턴스가 있다면 그것을 가져오고, 아니면 새로 생성하도록 한다.
        profile_form = ProfileForm(instance=profile)
        return render(request, 'profile.html', {
            'user_change_form': user_change_form,
            'profile_form': profile_form
        })

