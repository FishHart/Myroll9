from email.policy import default
from enum import unique
from django.db import models
from myroll.models import Sbj, Atd
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator

class UserManager(BaseUserManager):
    def create_user(self, username, std_id, std_fac, std_grd, password=None):
        if not username:
            raise ValueError('Users must have an username')
        # elif not std_id:
        #     raise ValueError('Users must have an student ID number')

        user = self.model(
            username = username,
            # email = self.normalize_email(email),
            std_id = std_id,
            std_fac = std_fac,
            std_grd = std_grd
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, std_id, std_fac, std_grd, password):
        user = self.create_user(
            username,
            password=password,
            std_id = std_id,
            std_fac = std_fac,
            std_grd = std_grd,
        )
        # user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(max_length=30, unique=True)
    username = models.CharField(verbose_name="名前", max_length=30, unique=True)
    std_id = models.CharField(verbose_name="学籍番号", max_length=5, primary_key=True)
    std_fac = models.CharField(verbose_name="学科", max_length=2)
    std_grd = models.IntegerField(verbose_name="学年", validators=[MinValueValidator(1), MaxValueValidator(5)])
    # email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    objects = UserManager()

    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['std_id', 'std_fac', 'std_grd']

    # ユーザーごとの出席回数DBの登録
    def create_atdtime(self):
        sbj_list = Sbj.objects.filter(std_fac=(self.std_fac or "ALL"), std_grd=self.std_grd)
        for sbj in sbj_list:
            Atd.objects.create(std_id=self.std_id, sbj_name=sbj.sbj_name)
