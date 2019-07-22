from django.db import models

# Create your models here
class Photo(models.Model):
    
    def __str__(self):
        return self.photo_name
    
    def save_photo(self):
        self.save()
    
    @classmethod
    def get_all_photos(cls):
        photos = cls.objects.all()
        return photos
    
    @classmethod
    def get_photo_by_id(cls,id):
        photo = cls.objects.filter(id=id)
        return photo
    
    @classmethod
    def delete_photo_by_id(cls,id):
        photo = cls.objects.remove(id=id)
        return photo
    
    @classmethod
    def update_photo_by_id(cls,id):
        photo = cls.objects.update(id=id)
        return photo

    @classmethod
    def search_by_title(cls,search_term):
        photo = cls.objects.filter(title__icontains=search_term)
        return photo
