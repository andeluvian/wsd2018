from django.db import models

class Product(models.Model):
		title = models.CharField(max_length=255,unique=True,blank = False)
		description = models.TextField(blank=True)
		image_url = models.URLField(null=True, blank=True)
		#image_url = models.ImageField(upload_to='products/<int:product_id>',blank=True)
		quantity = models.PositiveIntegerField(default=0)
	
		def sell(self, save=True):
			self.quantity -= 1
			if save:
				self.save()