from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """
    用户扩展表
    """
    nickname = models.CharField(max_length=10, null=True, blank=True, verbose_name='昵称' ,help_text='昵称')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'account'
        # permissions=(
        #     ("view_user", "cat view user"),
        # )
