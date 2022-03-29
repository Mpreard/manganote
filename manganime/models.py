from django.db import models

from authentification.models import Profile


class MangaLibrairy(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_manga = models.BigIntegerField()
    chapter = models.FloatField()

    class Meta:
        unique_together = (("profile", "id_manga"),)


class AnimeLibrairy(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_anime = models.BigIntegerField()
    episode = models.FloatField()
    season = models.IntegerField()

    class Meta:
        unique_together = (("profile", "id_anime"),)


from django.db import models

from authentification.models import Profile


class MangaLibrairy(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_manga = models.BigIntegerField()
    chapter = models.FloatField()

    class Meta:
        unique_together = (("profile", "id_manga"),)


class AnimeLibrairy(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_anime = models.BigIntegerField()
    episode = models.FloatField()
    season = models.IntegerField()

    class Meta:
        unique_together = (("profile", "id_anime"),)
