from django.db import models
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    email = models.EmailField(max_length=50, null=True)
    subscriped_usr = models.BooleanField(null=True)
    LinkedIn_usr_name = models.URLField(max_length=50, null=True)
    Twitter_usr_name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"