from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="HTML, CSS, JavaScript, Django, etc.")
    code_link = models.URLField(verbose_name="Lien vers le code")
    live_link = models.URLField(verbose_name="Lien vers la version en ligne", blank=True, null=True)
    highlights = models.TextField(help_text="Points forts du projet, compétences utilisées, etc.")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title
