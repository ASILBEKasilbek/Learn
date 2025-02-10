from django.contrib import admin
from .models import Category, Topic, Question, Answer, News

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  # Qo'shimcha bo'sh qatorlar soni

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Qo'shimcha bo'sh qatorlar soni

class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1  # Qo'shimcha bo'sh qatorlar soni

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Kategoriya nomini ko'rsatish
    search_fields = ('name',)  # Qidiruv maydoni
    inlines = [TopicInline]  # Kategoriya ostida mavzularni ko'rsatish

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')  # Mavzu nomi va kategoriyani ko'rsatish
    list_filter = ('category',)  # Kategoriya bo'yicha filtrlash
    search_fields = ('title',)  # Qidiruv maydoni
    inlines = [QuestionInline]  # Mavzu ostida savollarni ko'rsatish

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic')  # Savol nomi va mavzuni ko'rsatish
    list_filter = ('topic',)  # Mavzu bo'yicha filtrlash
    search_fields = ('name', 'text')  # Qidiruv maydoni
    inlines = [AnswerInline]  # Savol ostida javoblarni ko'rsatish

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user_answer', 'question')  # Foydalanuvchi javobi va savolni ko'rsatish
    search_fields = ('user_answer',)  # Qidiruv maydoni

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'user')  # Yangilik sarlavhasi, yaratish sanasi va foydalanuvchini ko'rsatish
    list_filter = ('created_at',)  # Yaratish sanasi bo'yicha filtrlash
    search_fields = ('title', 'content')  # Qidiruv maydoni
    ordering = ['-created_at']  # Yangiliklarni yaratish sanasiga ko'ra tartiblash
