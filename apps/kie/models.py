from django.db import models

# Create your models here.


class KeyInfoExtract(models.Model):
    text = models.TextField()
    key_info = models.TextField()
    time = models.TimeField()

    class Meta:
        verbose_name = "关键信息抽取"
        verbose_name_plural = verbose_name
        db_table = "kie"

    def __str__(self):
        return self.text[:10] + "\nresult:" + self.key_info
