from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=200, primary_key=True, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Artists(models.Model):
    song = models.CharField(max_length=200, primary_key=True)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, default='single')
    genre = models.CharField(max_length=200, default='none')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.song

class Ratings(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    song = models.ForeignKey(Artists, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.rating

class Price(models.Model):
    song = models.ForeignKey(Artists, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.price
