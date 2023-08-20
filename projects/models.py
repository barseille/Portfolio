from django.db import models
from PIL import Image

class Project(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="HTML, CSS, JavaScript, Python etc...")
    github_link = models.URLField(verbose_name="Lien vers la version en ligne", blank=True, null=True)
    technical_skills = models.TextField(help_text="Compétences techniques acquises", null=True)
    soft_skills = models.TextField(help_text="Soft skills acquis", null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    IMAGE_MAX_SIZE = (200, 200)

    def resize_image(self):
        """
        Surcharge la méthode save pour inclure le redimensionnement de l'image.
        """
        if self.image:
            image = Image.open(self.image.path)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)
