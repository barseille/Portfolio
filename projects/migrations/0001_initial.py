# Generated by Django 4.2.4 on 2023-08-20 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "technologies",
                    models.CharField(
                        help_text="HTML, CSS, JavaScript, Django, etc.", max_length=500
                    ),
                ),
                ("code_link", models.URLField(verbose_name="Lien vers le code")),
                (
                    "live_link",
                    models.URLField(
                        blank=True,
                        null=True,
                        verbose_name="Lien vers la version en ligne",
                    ),
                ),
                (
                    "highlights",
                    models.TextField(
                        help_text="Points forts du projet, compétences utilisées, etc."
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="projects/"),
                ),
            ],
        ),
    ]
