from django.db import models

class News(models.Model):
    DISPLAY_CHOICES = (
        ('grid', 'Сетка'),
        ('slider', 'Слайдер'),
    )
    title = models.CharField(max_length=200, verbose_name="Название")
    short_description = models.TextField(verbose_name="Краткое описание", blank=True, default='')
    main_content = models.TextField(verbose_name="Основной текст", default='')
    image = models.ImageField(upload_to='news/', verbose_name="Обложка", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    display_style = models.CharField(max_length=10, choices=DISPLAY_CHOICES, default='grid', verbose_name="Стиль отображения галереи")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    
    def __str__(self):
        return self.title

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='news/gallery/', verbose_name="Фото")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Фото новости"
        verbose_name_plural = "Фотографии новостей"
        ordering = ['order']

class TeamMember(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    role = models.CharField(max_length=200, verbose_name="Роль в проекте")
    position = models.CharField(max_length=200, verbose_name="Должность/Место учебы")
    photo = models.ImageField(upload_to='team/', verbose_name="Фото")
    vk_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на ВК")

    class Meta:
        verbose_name = "Участник команды"
        verbose_name_plural = "Команда"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Partner(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    logo = models.ImageField(upload_to='partners/', verbose_name="Логотип")
    url = models.URLField(blank=True, null=True, verbose_name="Ссылка на сайт")

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"

    def __str__(self):
        return self.name

class HistoryLine(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название направления")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='history/', verbose_name="Изображение")
    years = models.CharField(max_length=100, verbose_name="Годы реализации")
    location = models.CharField(max_length=200, verbose_name="География")

    class Meta:
        verbose_name = "Историческая линия"
        verbose_name_plural = "Исторические линии"

    def __str__(self):
        return self.title
