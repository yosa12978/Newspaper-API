from django.db import models

class NP(models.Model):
    Title = models.CharField(max_length = 120)
    Company = models.CharField(max_length = 50, default = "Unknown")
    Newspaper = models.FileField(upload_to = '../media/')
    Year = models.IntegerField(default=None)
    User = models.CharField(max_length = 100)

    def __str__(self):
        return "{} - {} - {}".format(self.Title, self.Company, self.Year)