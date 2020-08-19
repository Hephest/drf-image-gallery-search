from django.db import models


class Picture(models.Model):
    picture_id = models.CharField(max_length=20, help_text="Picture id from external API")
    author = models.CharField(max_length=100, help_text="Author name")
    camera = models.CharField(max_length=100, help_text="Camera name")
    cropped_picture = models.URLField(help_text="URL for cropped picture")
    full_picture = models.URLField(help_text="URL for full picture")
    tags = models.TextField()

    def __str__(self):
        return 'Picture {}'.format(self.id)
