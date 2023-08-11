from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.




class Author(models.Model):
    rating = models.SmallIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        posts_rating = Post.objects.filter(author=self).aggregate(result=Sum('rating_news')).get('result')
        comments_rating = Comment.objects.filter(user_comm=self.user).aggregate(result=Sum('rating_comm')).get('result')
        comment_post = Comment.objects.filter(post_comm__author=self).aggregate(result=Sum('rating_comm')).get('result')

        self.rating = 3 * posts_rating + comments_rating + comment_post
        self.save()




class Category(models.Model):
    category = models.CharField(max_length=40, unique=True)

news = 'NE'
article = 'AR'

POST_TYPES = [
    (news, 'новость'),
    (article, 'статья')
]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice = models.CharField(max_length=10, choices=[(news, "новость"),(article, "статья")])
    article_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    head = models.CharField(max_length=70)
    text = models.TextField(max_length=2000)
    rating_news = models.SmallIntegerField(default=0)

    def like_post(self):
        self.rating_news += 1
        self.save()

    def dislike_post(self):
        self.rating_news -= 1
        self.save()

    def preview(self, length=124):
        return f"{self.text[:length]}..." if len(self.text) > length else self.text



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comm = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comm = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comm = models.CharField(max_length=255)
    date_comm = models.DateTimeField(auto_now_add=True)
    rating_comm = models.SmallIntegerField(default=0)

    def like_comm(self):
        self.rating_comm += 1
        self.save()

    def dislike_comm(self):
        self.rating_comm -= 1
        self.save()


