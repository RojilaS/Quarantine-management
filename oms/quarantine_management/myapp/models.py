from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()


    

class user_details(models.Model):
    
    # fname = models.CharField(max_length=50,null=True)
    # lname = models.CharField(max_length=50,null=True)
    
    contact = models.IntegerField(null=True)
    email = models.CharField(max_length=50)
    username=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.username
    

class owner_details(models.Model):
    user_id = models.IntegerField(default=0,null=True)
    fname = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=50,null=True)
    contact = models.IntegerField(null=True)
    email = models.CharField(max_length=50,null=True)
    document = models.FileField(upload_to='ownerdocs',null=True)
    username=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    is_approved=models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.username



class place(models.Model):
   
    districtname = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.districtname 
    


class building_details(models.Model):
    h_id = models.IntegerField(default=0)
    p_id = models.ForeignKey(place, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(owner_details, on_delete=models.CASCADE)
    house_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    capacity = models.IntegerField()
    picture = models.ImageField(upload_to="Building")
    contact = models.IntegerField()
    rental = models.IntegerField()

    def __str__(self):
        return self.house_name 


class booking(models.Model):
    h_id = models.ForeignKey(building_details, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    owner_id =models.ForeignKey(owner_details, on_delete=models.CASCADE)
    
    requested_date = models.DateField()
    check_in = models.DateField()
    check_out = models.DateField(null=True) 
    members = models.IntegerField()
    status=models.CharField(max_length=100,default="Not Approved")
    doc1 = models.FileField(upload_to='docs')
    doc2 = models.FileField(upload_to='docs')

    def __str__(self):
        return self.id



class payment(models.Model):
    booking_id = models.ForeignKey(booking, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    amount = models.IntegerField()
    card_no = models.IntegerField()
    exp = models.IntegerField()
    cvv = models.IntegerField()


class review_rating(models.Model):
    user_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    h_id = models.ForeignKey(building_details, on_delete=models.CASCADE)
    review = models.CharField(max_length=300)
    rating = models.IntegerField()


