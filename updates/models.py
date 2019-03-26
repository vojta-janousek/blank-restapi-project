import json

from django.db import models
from django.conf import settings
from django.core.serializers import serialize

# Create your models here.
def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):

    def serialize(self):
        qs = self
        return serialize('json', qs, fields=('user', 'content'))


class UpdateManager(models.Manager):

    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        json_data = serialize("json", [self], fields=('user', 'content'))
        structure = json.loads(json_data)
        print(structure)
        data = json.dumps(structure[0]['fields'])
        return data
