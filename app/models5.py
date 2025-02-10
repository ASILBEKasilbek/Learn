from django.db import models
from django.contrib.auth.models import User

def category_image_path(instance, filename):
    return f'categories/{instance.name}/{filename}'

def profile_image_path(instance, filename):
    return f'profiles/{instance.user.username}/{filename}'

def admin_image_path(instance, filename):
    return f'admins/{instance.user.username}/{filename}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=category_image_path, blank=True, null=True)

    def __str__(self):
        return self.name

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to=admin_image_path, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=profile_image_path, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category_topics', null=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='topics/', blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, related_name='topic_questions', null=True, blank=True)
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_answers')
    user_answer = models.TextField()
    github_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user_answer[:50]

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_news')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
