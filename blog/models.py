from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=250)
	pub_data = models.DateTimeField()
	image = models.ImageField(upload_to='image/')
	body = models.TextField()

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_data.strftime('%b %e, %y')

	def __str__(self):
		return self.title
