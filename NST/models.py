from django.db import models
class NstImages(models.Model):
    content = models.ImageField(upload_to='content/uploads',verbose_name="", default='img1.jpg')
    style = models.ImageField(upload_to='style/uploads',verbose_name="", default='img2.jpg')
    
   
    

    