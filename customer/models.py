from django.db import models

# Create your models here.

class Customer(models.Model):
    user_id         = models.IntegerField(primary_key=True)
    user_name       = models.TextField()
    password        = models.TextField()
    name            = models.TextField()
    email           = models.TextField()
    adress          = models.TextField()
    birthday        = models.TextField()
    gender          = models.TextField()
    favorite_genres = models.TextField(default="")

    class Meta:
        managed = False
        db_table = 'customer'
       
    
    def __str__(self):
        return self.name + ":" + self.user_name