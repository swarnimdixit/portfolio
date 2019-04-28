from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:300]+'... continue reading.'
