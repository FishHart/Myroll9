from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# class Std(models.Model):
#     std_id = models.CharField(verbose_name="学籍番号",max_length=5,primary_key=True)
#     std_fac = models.CharField(verbose_name="学科",max_length=2)
#     std_grd = models.IntegerField(verbose_name="学年",validators=[MinValueValidator(1), MaxValueValidator(5)])
#     std_name = models.CharField(verbose_name="名前",max_length=30)
#     std_pwd = models.CharField(verbose_name="パスワード",max_length=30)

class Sbj(models.Model):
    sbj_name = models.CharField(verbose_name="科目",max_length=20,primary_key=True)
    std_fac = models.CharField(verbose_name="学科",max_length=2)
    std_grd = models.IntegerField(verbose_name="学年",validators=[MinValueValidator(1), MaxValueValidator(5)])
    curr_cnt = models.IntegerField(verbose_name="現在の授業回数",validators=[MinValueValidator(0), MaxValueValidator(30)])
    total_cnt = models.IntegerField(verbose_name="授業総数",validators=[MinValueValidator(10), MaxValueValidator(30)])

class Tmt(models.Model):
    id = models.AutoField(primary_key=True)
    day_week = models.IntegerField(verbose_name="曜日",validators=[MinValueValidator(1), MaxValueValidator(7)])
    #TimeField
    sbj_bgn = models.TimeField(verbose_name="開始時刻")
    std_fac = models.CharField(verbose_name="学科",max_length=2)
    std_grd = models.IntegerField(verbose_name="学年",validators=[MinValueValidator(1), MaxValueValidator(5)])
    sbj_name = models.CharField(verbose_name="科目",max_length=20)

class Atd(models.Model):
    id = models.AutoField(primary_key=True)
    std_id = models.CharField(verbose_name="学籍番号",max_length=5)
    sbj_name = models.CharField(verbose_name="科目",max_length=20)
    atd_time = models.DecimalField(
        verbose_name="出席コマ数",
        max_digits=3,
        decimal_places=1,
        default=00.0
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["std_id", "sbj_name"],
                name="std_sbj"
            ),
        ]


# class Attending(models.Model):
#     userpk = models.IntegerField(unique=True, primary_key=True)
#     subject = models.CharField(max_length=10)

#     # def assignment(self):
#     #     self.total_number += 1
#     #     self.save()

#     def __str__(self):
#         return self.subject

# class Subject(models.Model):
#     name = models.CharField(max_length=10, primary_key=True)
#     total = models.IntegerField()
#     count = models.IntegerField()
    
