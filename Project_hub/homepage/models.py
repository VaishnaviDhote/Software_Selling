from django.db import models

# Create your models here.

class Project(models.Model):
    project_username = models.CharField(max_length=200)
    project_id = models.IntegerField(default=1, primary_key=True)
    project_name = models.CharField(max_length=200)
    project_clientname = models.CharField(max_length=200)
    project_technology = models.CharField(max_length=200)
    project_team = models.CharField(max_length=200)
    project_info = models.CharField(max_length=500)
    project_type = models.CharField(max_length=100)
    project_image = models.ImageField()
    project_link = models.CharField(max_length=200)
    project_startdate = models.CharField(max_length=100)
    project_enddate = models.CharField(max_length=200)
    project_validity = models.CharField(max_length=200)
    project_dcost = models.IntegerField(default=1)
    project_rcost = models.IntegerField(default=1)

class client(models.Model):
    client_id = models.AutoField(default=1, primary_key=True)
    client_name = models.CharField(max_length=200)
    client_gender = models.CharField(max_length=200)
    client_mobile = models.CharField(max_length=200)
    client_email = models.CharField(max_length=200)
    client_about = models.CharField(max_length=200)
    client_projectname = models.CharField(max_length=200)
    client_img = models.ImageField()
    client_link = models.CharField(max_length=200)


class msgbox(models.Model):
    msg_id = models.AutoField(primary_key=True)
    msg_name =  models.CharField(max_length=200)
    msg_email =  models.CharField(max_length=200)
    msg_mobile =  models.CharField(max_length=200)
    msg_service =  models.CharField(max_length=200)
    msg_message =  models.CharField(max_length=200)

# class USER(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=200)
#     user_email = models.CharField(max_length=200)
#     user_gender = models.CharField(max_length=200)
#     user_username = models.CharField(max_length=200)
#     user_password = models.CharField(max_length=200)
#     user_password2 = models.CharField(max_length=200)






