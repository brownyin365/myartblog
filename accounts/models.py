from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import signals



class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(max_length=500, default='')
	city = models.CharField(max_length=100, default='')
	skill = models.CharField(max_length=100, default='')
	
   
	
	

	def __str__(self):
		return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)		


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(default='none@email.com')
    birth_date = models.DateField(default='1900-12-31')
    city = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    hobby = models.CharField(max_length=255, default='')    
    phone = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True, blank=True)
    
	


    def __str__(self):
    	return "Profile of user {}". format(self.user)




def create_profile(sender, **kwargs):
	if kwargs['created']:
	    user_profile = Profile.objects.create(user=kwargs['instance'])
	pass

post_save.connect(create_profile, sender=User)   	



@property
def photo_url(self):
    if self.photo and hasattr(self.photo, 'url'):
        return self.photo.url




