from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.
class Chai_Varity(models.Model):
    CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
   ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.name


# One to many

class ChaiReview(models.Model):
    chai = models.ForeignKey(Chai_Varity,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}' 
    

#Many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(Chai_Varity,related_name='stores')
        
    def __str__(self):
        return self.name
    
    
    
# one to one 

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(Chai_Varity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)        
    