from django.db import models


class Types(models.Model):
    name = models.CharField(max_length=30)
    privilege_level = models.IntegerField()

    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = 'Types'
