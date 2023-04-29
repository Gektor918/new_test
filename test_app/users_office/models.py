from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class Office(models.Model):
    name = models.CharField(max_length=25, blank=False, verbose_name='Имя')
    description = models.CharField(max_length=150, blank=False, verbose_name='Краткое описание')
    
    def __str__(self):
        return 'Название: {}'.format(self.name)
    
    class Meta:
        verbose_name = 'Организации'
        verbose_name_plural = 'Организация'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('name'), max_length=30, blank=True)
    last_name = models.CharField(_('surname'), max_length=30, blank=True)
    phone = models.CharField(_('phone'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    office = models.ManyToManyField(Office, through="User_office")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_staff = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def get_full_name(self):
        '''
        Возвращает first_name и last_name с пробелом между ними.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Возвращает сокращенное имя пользователя.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class User_office(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя', related_name='User_office')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, verbose_name='Организации')

    
    def __str__(self):
        return 'Юзер: {}'.format(self.user)
    
    class Meta:
        verbose_name = 'Юзер и Организации'
        verbose_name_plural = 'Юзер и  Организация'