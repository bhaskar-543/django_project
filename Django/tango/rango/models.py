from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
# Override the __unicode__() method to return out something meaningful!
# Remember if you use Python 2.7.x, define __unicode__ too!
	def __str__(self):
		return self.user.username

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	likes=models.IntegerField(default=0)
	view = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	class Meta:
		verbose_name_plural = 'categories'
	def __str__(self):
		return self.name


class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __str__(self): # For Python 2, use __unicode__ too
		return self.title