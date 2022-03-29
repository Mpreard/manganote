import requests
from django.shortcuts import render
from django.contrib.auth.models import User


# list of manga and animes
from django.views.decorators.csrf import csrf_protect

from authentification.models import Profile
from mangaNote.views import error404
from manganime.models import MangaLibrairy, AnimeLibrairy


def manganimes(request, nbManganime: int = 20, offset: int = 0):
    if "mangas" in request.path:
        response = requests.get(
            "https://kitsu.io/api/edge/manga?page%5Blimit%5D="
            + str(nbManganime)
            + "&page%5Boffset%5D="
            + str(offset)
        )
        data = response.json()

        return render(request, "mangas.html", {"mangas": data["data"]})
    if "animes" in request.path:
        response = requests.get(
            "https://kitsu.io/api/edge/anime?page%5Blimit%5D="
            + str(nbManganime)
            + "&page%5Boffset%5D="
            + str(offset)
        )
        data = response.json()

        return render(request, "animes.html", {"animes": data["data"]})

    return 0


# manga/anime details page
def manganimeDetails(request, manganimeId: int):
    # manganimeId = id du manga/anime pour lequel on va voir les details
    if "mangas" in request.path:
        response = requests.get("https://kitsu.io/api/edge/anime/" + str(manganimeId))
        data = response.json()

        return render(request, "manga.html", {"manga": data["data"]})

    elif "animes" in request.path:
        response = requests.get("https://kitsu.io/api/edge/anime/" + str(manganimeId))
        data = response.json()

        return render(request, "anime.html", {"anime": data["data"]})

    return 0


@csrf_protect
def addBookmark(request, manganimeId: int):
    profile = Profile.objects.get(user=request.user)
    if "mangas" in request.path:
        if MangaLibrairy.objects.filter(profile=profile, id_manga=manganimeId).exists():
            mangaLib = MangaLibrairy.objects.filter(
                profile=profile, id_manga=manganimeId
            )
            mangaLib.update(chapter=request.POST["chapter"])
        else:
            mangaLib = MangaLibrairy(
                profile=profile, id_manga=manganimeId, chapter=request.POST["chapter"]
            )
            mangaLib.save()

        return manganimeDetails(request, manganimeId)

    elif "animes" in request.path:

        if AnimeLibrairy.objects.filter(profile=profile, id_anime=manganimeId).exists():
            animeLib = AnimeLibrairy.objects.filter(
                profile=profile, id_anime=manganimeId
            )
            animeLib.update(
                season=request.POST["season"], episode=request.POST["episode"]
            )
        else:
            animeLib = AnimeLibrairy(
                profile=profile,
                id_anime=manganimeId,
                season=request.POST["season"],
                episode=request.POST["episode"],
            )
            animeLib.save()

        return manganimeDetails(request, manganimeId)

    return 0


@csrf_protect
def deleteBookmark(request, manganimeId: int):
    profile = Profile.objects.get(user=request.user)
    if "mangas" in request.path:
        try:
            mangaLib = MangaLibrairy.objects.filter(
                profile=profile, id_manga=manganimeId
            )
            mangaLib.delete()
        except MangaLibrairy.DoesNotExist:
            print("manga pas en lib")

        return manganimeDetails(request, manganimeId)

    elif "animes" in request.path:

        try:
            animeLib = AnimeLibrairy.objects.filter(
                profile=profile, id_anime=manganimeId
            )
            animeLib.delete()
        except AnimeLibrairy.DoesNotExist:
            print("anime pas en lib")

        return manganimeDetails(request, manganimeId)

    return 0


def getBookmark(request, userId: int):
    # is friend en cours de dev
    if True:
        user = User.objects.get(id=userId)
        profile = Profile.objects.get(user=user)
        arrayData = []
        if "mangas" in request.path:
            try:
                mangaLib = MangaLibrairy.objects.filter(
                    profile=profile
                )
                for manga in mangaLib:
                    response = requests.get("https://kitsu.io/api/edge/anime/" + str(manga.id_manga))
                    data = response.json()
                    tempArr = [data['data'], {"manga": manga}]
                    arrayData.append(tempArr)
                context = {
                    "arrayData": arrayData
                }
                return render(request, "bookmarkManga.html", context)
            except MangaLibrairy.DoesNotExist:
                return "Librairie vide"

        elif "animes" in request.path:

            try:
                animeLib = AnimeLibrairy.objects.filter(
                    profile=profile
                )
                for anime in animeLib:
                    response = requests.get("https://kitsu.io/api/edge/anime/" + str(anime.id_anime))
                    data = response.json()
                    tempArr = [data['data'], {"anime": anime}]
                    arrayData.append(tempArr)
                context = {
                    "arrayData": arrayData
                }
                return render(request, "bookmarkAnime.html", context)
            except AnimeLibrairy.DoesNotExist:
                return "aucun anime dans la librairie"

    return error404(request, "non autorisé")
