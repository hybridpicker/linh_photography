from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class PhotoCategory(models.Model):
    title = models.CharField(_(u'Project Name'), max_length=50)

    def __str__(self):
        return str(self.title)

    class Meta:
        '''
        Meta class for PhotoCategory
        '''
        verbose_name = u'Photo Category'
        verbose_name_plural = u'Photo Categories'

class Photo(models.Model):
    title = models.CharField(_(u'Title of the Photo'), max_length=50)
    images = models.ImageField(
        upload_to='portfolio/images/',
        default='portfolio_imageDefault', blank=True)
    description = models.TextField(null=True, blank=True)
    ordering = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        PhotoCategory,
        on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        '''
        Meta class for Photo
        '''
        ordering = ['ordering']
        verbose_name = u'Photo'
        verbose_name_plural = u'Photos'
