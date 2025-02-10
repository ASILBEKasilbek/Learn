from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)  # Kategoriya nomi
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Kategoriya rasmi
    admin_name = models.CharField(max_length=100, default="ism")
    admin_surname = models.CharField(max_length=100, default="familya")
    admin_image = models.ImageField(upload_to='admin_images/', blank=True, null=True)
    admin_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):  # <-- `models.Model` dan meros olish shart!
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Foydalanuvchi bilan bog‘lanish
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="profile_images/", blank=True, null=True)

    def __str__(self):
        return self.user.username  # Foydalanuvchi nomini qaytaradi

class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='topics', null=True, blank=True)  # Kategoriya bilan bog‘lanish
    title = models.CharField(max_length=100)  # Mavzu nomi
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Mavzu rasmi

    def __str__(self):
        return self.title

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions', default=1)  # Default qiymat
    name = models.CharField(max_length=100, default='')  # Savol nomi
    text = models.TextField()  # Savol matni

    def __str__(self):
        return self.text[:50]  # Savol matnining birinchi 50 ta belgisi

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')  # Savol bilan bog'lanish
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Foydalanuvchi 1-IDga ega bo'ladi
    user_answer = models.TextField()  # Foydalanuvchi javobi
    github_link = models.URLField(max_length=200, blank=True, null=True)  # GitHub profili uchun link

    def __str__(self):
        return self.user_answer[:50]  # Javobning birinchi 50 ta belgisi

class News(models.Model):
    title = models.CharField(max_length=200)  # Yangilik sarlavhasi
    content = models.TextField()  # Yangilik mazmuni
    created_at = models.DateTimeField(auto_now_add=True)  # Yangilik yaratilgan vaqti
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foydalanuvchi bilan bog‘lanish

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Yangiliklarni yaratish sanasiga ko'ra tartiblash
