from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class User(AbstractUser):
    
    image = models.ImageField(upload_to='projects/', null=True, blank=True, verbose_name="Image de profil") 
    
    IMAGE_MAX_SIZE = (200, 200)

    def resize_image(self):
        """
        Surcharge la méthode save pour inclure le redimensionnement de l'image.
        """
        if self.image:
            image = Image.open(self.image.path)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)

