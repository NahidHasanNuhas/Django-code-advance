from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GitUserInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	UserSite = models.URLField(blank=True)
	UserPicture = models.ImageField(upload_to='GitPictures', blank=True)

	def __str__(self):
		return self.user.username