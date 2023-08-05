from django.contrib import admin
from django.db import models
from django.utils.html import format_html


class Advertisement(models.Model):

    # Название товара
    # CharField - короткое текстове поле
    # 'заголовок' - verbose_name - человекочитаемое название
    title = models.CharField('заголовок', max_length=128)

    # Описание товара
    # Длинное текстовое поле
    description = models.TextField('описание')

    # Цена
    # числовое поле с фиксированной точкой
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    # Уместен ли торг
    # Булевое поле (логическое) (окшн)
    auction = models.BooleanField('торг', help_text='Отметьте, если хотите торговаться')

    # Дата публикации
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения/обновления + что изменилось
    updated_at = models.DateTimeField(auto_now=True)
    

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_date = self.created_at.strftime("%H:%M:%S")
            return format_html('<span style="color:green; font-weight:bold;"> Сегодня в {} </span>', created_date)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'


    # Продавец (имя продавца, контакты для связи, отзывы)
    # Фото объявления
    # Рейтинг
    # В продаже/не в продаже - актуальность
