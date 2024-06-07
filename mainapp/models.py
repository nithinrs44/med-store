from django.db import models

class records(models.Model):
    
    # creation_date = models.DateTimeField(auto_now_add=True)
    
    medicine_name = models.CharField(max_length=255)
    
    medicine_des = models.CharField(max_length=500)
    
    # def __str__(self):
    #     return self.medicine_name + " " + self.medicine_des
    
