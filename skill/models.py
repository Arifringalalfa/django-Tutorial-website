from django.db import models


class Myskill(models.Model):
    image = models.ImageField(upload_to ='skillimage/')
    Title = models.CharField(max_length =50, blank=False)
    Description = models.TextField(max_length = 500, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def summary(self):
        return self.Description[0:100]

    def __str__(self):
        return self.Title

class Contactpage(models.Model):
    cname = models.CharField(max_length=50)
    cemail = models.EmailField(max_length =50)
    cquerry = models.TextField(max_length=1000)

    def __str__(self):
        return self.cname