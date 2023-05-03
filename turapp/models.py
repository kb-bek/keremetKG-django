from django.db import models


class Tour(models.Model):

    title = models.CharField(
        max_length=100,
        db_index=True,
        blank=True,
        verbose_name='Название'
    )

    description = models.TextField(
        db_index=True,
        verbose_name='Описание тура'
    )

    price = models.IntegerField(
        db_index=True,
        blank=True,
        verbose_name='Цена'
    )

    image = models.ImageField(
        upload_to='images/tours/% Y/% m/% d/',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.title

class Hotel(models.Model):

    title = models.CharField(
        max_length=100,
        db_index=True,
        blank=True,
        verbose_name='Название'
    )

    address = models.TextField(
        db_index=True,
        verbose_name='Адрес'
    )

    description = models.TextField(
        db_index=True,
        verbose_name='Описание'
    )

    price = models.IntegerField(
        db_index=True,
        blank=True,
        verbose_name='Цена'
    )

    image = models.ImageField(
        upload_to='images/hotels/% Y/% m/% d/',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.title


class Review(models.Model):

    name = models.CharField(
        max_length=40,
        db_index=True,
        blank=True,
        verbose_name='Имя'
    )

    grade = models.IntegerField(
        db_index=True,
        blank=True,
        verbose_name='Оценка'
    )

    review = models.TextField(
            db_index=True,
            verbose_name='Отзыв'
    )

    image = models.ImageField(
        upload_to='images/reviewers/% Y/% m/% d/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.name

