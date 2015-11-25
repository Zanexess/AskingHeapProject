from django.db import models
# Create your models here.

class Tag(models.Model):
    class Meta:
        db_table = "tag"

    tag = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.tag
