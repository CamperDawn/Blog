from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio= models.CharField(max_length=255, blank=True)
    img= models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.usuario.username
    
# @receiver(post_save, sender=User)
# def crear_perfil_usuario(sender, instance, created, **kwargs):
#     if created:
#         Profile.object.create(usuario=instance)

# @receiver(post_save, sender=User)
# def guardar_perfil_usuario(sender, instance, **kwargs):
#     instance.profile.save()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.IntegerField(default=18, null=False)
    title = models.CharField(max_length=200)
    img= models.ImageField(upload_to="images/", null=True)
    description = models.TextField()
    post_date = models.DateTimeField(default=timezone.now, null=True)
    #likes_number = models.IntegerField(default=0)
    #dislike_number = models.IntegerField(default=0)
    post_type = models.IntegerField(default=2)
    comment_numbers=models.IntegerField(default=0)
    
    def publish(self):
        self.post_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    #likes_number = models.IntegerField(default=0)

    def __str__(self):
        return self.content
    
    def save(self,**args):
        self.post.comment_numbers += 1
        self.post.save()
        return super().save(**args)
    
    def delete(self,**args):
        self.post.comment_numbers -= 1
        self.post.save()
        return super().delete(**args)