from django.db import models

# Create your models here.
class product_details(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField()
    Cost_per_item=models.BigIntegerField(null=True)
    Stock_quantity=models.BigIntegerField(null=True)
    Volume=models.BigIntegerField(null=True)



    def get_Volume(self):
        Volume=self.Cost_per_item * self.Stock_quantity
        return Volume


    def save(self,*args,**kwargs):
        self.Volume=self.get_Volume()
        super(product_details,self).save(*args,**kwargs)


    def __str__(self):
        return self.Name