from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have an password')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', max_length=50, unique=True)
    password = models.CharField(max_length=128, unique=True, verbose_name='password')
    #AbstractBaseUserにはMyUserManagerが必要
    objects = MyUserManager()
    #一意の識別子として使用されます
    USERNAME_FIELD = 'email'
    #ユーザーを作成するときにプロンプ​​トに表示されるフィールド名のリストです。
    # REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
