from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} stars"

class Photo(models.Model):
    image = models.ImageField(upload_to='static/temizliksite/images/galeri/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image.name}"