from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)
    photo = models.ImageField(null = True, blank=True)
    # upload_to='photos/'

    # def __str__(self):
    #     return self.name

class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True) # relation plusieur à plusieurs

    def __str__(self):
        return self.title

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)   # relation 1 a plusieurs, on_delete=models.CASCADE signifie que quand on supprime un contact on supp toutes ces résas mai spas l'inverse.
    album = models.OneToOneField(Album, on_delete=models.CASCADE)    # relation 1 à 1

    def __str__(self):
        return self.contact.name


# model po
# photo = models.ImageField(upload_to='photos/')