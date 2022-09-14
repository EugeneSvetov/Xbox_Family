from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст новости")
    author = models.CharField(max_length=255,verbose_name='Автор')
    cover = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Обложка")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    themes = models.ForeignKey('Themes', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create', 'title']


class Themes(models.Model):
    titles = (
        ('Игры', 'games'),
        ('Xbox', 'Xbox'),
        ('Оффтоп', 'off'),
    )

    title = models.CharField(max_length=6, choices=titles)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэг'