from django.db import models

class Database(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlavha')
    description = models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name='Tavsifi')
    url = models.CharField(max_length=50, unique=True, verbose_name='Havolasi')
    image = models.ImageField(upload_to='images/', verbose_name='Surati')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Loyiha '
        verbose_name_plural = 'Loyihalar'
        ordering = ['-id']
