from django.shortcuts import render, get_object_or_404
from .models import Category, Question, Answer
from .forms import AnswerForm

# Asosiy sahifa (kategoriyalar)
def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

# Kategoriya bo'yicha savollar
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    questions = category.questions.all()

    if request.method == 'POST':
        for question in questions:
            form = AnswerForm(request.POST)
            if form.is_valid():
                Answer.objects.create(question=question, user_answer=form.cleaned_data['user_answer'])

    else:
        form = AnswerForm()

    return render(request, 'category_detail.html', {'category': category, 'questions': questions, 'form': form})
