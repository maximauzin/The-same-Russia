from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Partner(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='partner_logos/')

    def __str__(self):
        return self.name
