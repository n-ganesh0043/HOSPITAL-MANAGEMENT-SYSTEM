from django.db import models

# Create your models here.
class Doctors(models.Model):
    d_no=models.AutoField(primary_key=True)
    d_name=models.CharField(max_length=20)
    d_contactno=models.IntegerField(unique=True)
    d_specialization=models.CharField(max_length=50)
    def __str__(self):
        return self.d_name

class Patient(models.Model):
    p_no=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    p_contactno=models.IntegerField(unique=True)
    p_address=models.CharField(max_length=50)
    def __str__(self):
        return self.p_name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    paitent=models.ForeignKey(Patient,on_delete=models.CASCADE)
    dateandtime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.doctor.d_name+"--"+self.paitent.p_name

class Userregistration(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=20)
    user_gender=models.CharField(max_length=30)
    user_contactno=models.IntegerField(unique=True)
    user_address=models.CharField(max_length=40)
    user_mail=models.EmailField()

