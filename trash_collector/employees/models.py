from django.db import models

class Custormer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    confirm_pickup = models.CharField(max_length=9)
    clocked_in = models.CharField(max_length=9)
    
    def __str__(self):
        return self.name




