from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have an password')
        
        # self.model は現在のユーザーモデルクラス（CustomUser）を参照
        user = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        # パスワードをハッシュ化 セキュリティの観点でも大切
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Djangoの createsuperuser コマンドを実行したとき使用される
    def create_superuser(self, email, password):
        # まず通常のユーザーを作成
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        # ユーザーに管理者権限を付与
        user.is_admin=True
        # ユーザーにスタッフ権限を付与
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', max_length=50, unique=True)
    password = models.CharField(max_length=128, unique=True, verbose_name='password')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    #AbstractBaseUserにはMyUserManagerが必要
    objects = MyUserManager()
    #一意の識別子として使用されます
    USERNAME_FIELD = 'email'

    # Django管理画面でユーザーリストを表示する際、この方法で返される文字列が各ユーザーの識別子として使用
    def __str__(self):
        return self.email
