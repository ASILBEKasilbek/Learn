from django.contrib import admin
from .models import Category, AdminProfile, Profile, Topic, Question, Answer, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname')
    search_fields = ('name', 'surname', 'user__username')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname')
    search_fields = ('name', 'surname', 'user__username')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title',)
    list_filter = ('category',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic')
    search_fields = ('name', 'text')
    list_filter = ('topic',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'user_answer')
    search_fields = ('user__username', 'question__text', 'user_answer')
    list_filter = ('question',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'content', 'user__username')
    list_filter = ('created_at',)
