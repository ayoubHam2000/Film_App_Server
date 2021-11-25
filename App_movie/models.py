from django.db import models
from django.core.files.storage import FileSystemStorage

from Utils.const import *

#region User Account
def get_default_profile_image():
    return "images/movies/default-movie.jpeg"

def get_profile_image_filepath(self, filename):
    return f'images/movies/{self.id}.jpeg'

# keep one image in the server
class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, *args, **kwargs):
        return name

class MovieModel(models.Model):
    movieName = models.CharField(max_length = MAX_CHAR)
    isAnnouced = models.BooleanField(default=False)
    movieCreation_date = models.DateField()
    movieImage = models.ImageField(
        max_length=255, 
        storage=OverwriteStorage(), 
        upload_to = get_profile_image_filepath, 
        null = True, 
        blank = True, 
        default = get_default_profile_image
        )
    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.movieImage
            self.movieImage = None
            super(MovieModel, self).save(*args, **kwargs)
            self.movieImage = saved_image
        super(MovieModel, self).save(*args, **kwargs)

