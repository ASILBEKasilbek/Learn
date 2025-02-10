from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Category, Question, Answer, Topic, Profile, News
from .forms import AnswerForm, RegisterForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news': news})

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, "profile.html", {"profile": profile})

@login_required
def profile_edit(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "profile_edit.html", {"form": form})

def home(request):
    categories = Category.objects.all()  # Kategoriyalar
    news = News.objects.order_by('-created_at')[:5]  # Oxirgi 5 yangilik
    return render(request, "home.html", {"categories": categories, "news": news})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = Topic.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'topics': topics})

def question_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    questions = Question.objects.filter(topic=topic)
    return render(request, 'question_detail.html', {'topic': topic, 'questions': questions})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Parolni hash qilish
            user.save()

            # Profil yaratish
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)  # Foydalanuvchini avtomatik login qilish
            return redirect("home")
    else:
        form = RegisterForm()
        profile_form = ProfileForm()

    return render(request, "register.html", {"form": form, "profile_form": profile_form})
def user_login(request):
    # Login funksiyasi
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})

def user_logout(request):
    # Logout funksiyasi
    logout(request)
    return redirect("home")
