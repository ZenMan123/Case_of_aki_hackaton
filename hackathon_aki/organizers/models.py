from django.db import models


class Organizer(models.Model):
    e_mail = models.EmailField('Электронная почта', unique=True)
    password = models.CharField('Пароль', max_length=50)
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50, blank=True)
    phone_number = models.CharField('Номер телефона', max_length=50, unique=True)
    position = models.CharField('Должность', max_length=50, blank=True)
    juridical_name = models.CharField('Юридическое лицо', max_length=50, blank=True)
    inn = models.CharField('ИНН', max_length=50, blank=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.middle_name}'

    class Meta:
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'


class Entry(models.Model):
    #client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    #platform = models.ForeignKey('platforms.Platform', on_delete=models.CASCADE)

    date = models.DateTimeField('Дата записи')

    def __str__(self):
        return f'Запись на {self.date}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
