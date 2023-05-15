from django.db import models
from django.contrib.auth.models import User
# Create your models here.
item_status_CHOICES = (
    ("Upcoming", "Upcoming"),
    ("Active", "Active"),
    ("Closed", "Closed"),  
)



# Item(user=user,name=name,image=image,description=description,basePrice=price,exp_date=exp_date)

class Item(models.Model): 
    user =  models.ForeignKey(User, related_name='user_details', on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.CharField(max_length=6383)  
    basePrice=models.PositiveIntegerField(default=0,blank=True,null=True)
    # currentPrice=models.PositiveIntegerField(default=0,blank=True,null=True)  
    status=models.CharField(max_length = 20,choices = item_status_CHOICES,default = 'Active')
    # start_date=models.DateField(blank=True,null=True)
    exp_date=models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)
    
# ItemVenderMapping(vender=vender,item=item,price=price)  ItemVenderMapping.objects.filter(item=item)
class ItemVenderMapping(models.Model):
    vender = models.ForeignKey(User, related_name='vender_details', on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, related_name='user_details', on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)