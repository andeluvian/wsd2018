from django.db import models
from django.urls import reverse

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

		def __str__(self):
				return self.title
		def get_absolute_url(self):
        		#return reverse("product:product_view", kwargs={"product_id": self.id})
				return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"
