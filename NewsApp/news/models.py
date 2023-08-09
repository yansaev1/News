from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)


class Author(models.Model):
    rating = models.IntegerField()
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)


class Category(models.Model):
    category = models.CharField(max_length=40, unique= True)

news = 'Новость'
article = 'Статья'


class Post(models.Model):
    author = models.OneToOneField(Author, on_delete = models.CASCADE, primary_key = True)
    choice = models.CharField(max_length= 5, choices=[(news, "новость"),(article, "статья")])
    article_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    head = models.CharField(max_length= 40)
    text = models.TextField(max_length= 2000)
    rating_news = models.IntegerField()



class PostCategory(models.Model):
    post = models.ManyToManyField(Post, Category)


class Comment(models.Model):
    post_user_comm = models.OneToOneField(Post, User, on_delete= models.CASCADE)
    text_comm = models.CharField(max_length= 255)
    date_comm = models.DateTimeField(auto_now_add=True)
    rating_comm = models.IntegerField()


