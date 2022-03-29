from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from friendship.models import Friendship
from django.views.decorators.csrf import csrf_protect

# View friends list
@login_required(login_url="/authentification/signin")
def friendsList(request):
    data = Friendship.objects.filter(
        user_applicant_id=str(request.user.id)
    ) | Friendship.objects.filter(user_receiving_id=str(request.user.id))
    friends = data.filter(status=Friendship.statusInvitation.FINISHED)

    return render(
        request, "friendsList.html", {"friends": friends, "myUser": request.user}
    )


# View friend's details
@login_required(login_url="/authentification/signin")
def friendview(request, user_id: str):
    if not isFriend(request, user_id):
        return HttpResponseBadRequest()

    return redirect(str(user_id) + "/bookmark")


# Invite a friend with his pseudo
@login_required(login_url="/authentification/signin")
def inviteFriend(request):
    if request.method == "POST":
        try:
            user_name = request.POST["username"]
            User = get_user_model()
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            return HttpResponseBadRequest()

        if not isExistingInvitation(request, user.id):
            friendship = Friendship(
                user_applicant_id=int(request.user.id), user_receiving_id=int(user.id)
            )

            friendship.save()

    return redirect("friends")


# Accept invitation
@login_required(login_url="/authentification/signin")
@csrf_protect
def accept(request, id_invitation: int):
    try:
        invitation = Friendship.objects.get(id=str(id_invitation))

        if invitation.user_receiving_id != request.user.id:
            return redirect("invites-list")

        invitation.status = Friendship.statusInvitation.FINISHED
        invitation.save()
    except Friendship.DoesNotExist:
        return HttpResponseBadRequest()

    return redirect("friends")


# Delete or refuse invitation
@login_required(login_url="/authentification/signin")
@csrf_protect
def delete(request, id_invitation):
    try:
        invitation = Friendship.objects.get(id=str(id_invitation))

        invitation.delete()
    except Friendship.DoesNotExist:
        return HttpResponseBadRequest()

    return redirect("friends")

# View invitations list
@login_required(login_url="/authentification/signin")
def invitesList(request):
    waitingFriendships = Friendship.objects.filter(
        status=Friendship.statusInvitation.PENDING,
        user_receiving_id=str(request.user.id),
    )

    return render(request, "invitesList.html", {"invites": waitingFriendships})


def isFriend(request, user_id):
    return (
        Friendship.objects.filter(
            user_applicant_id=request.user.id,
            user_receiving_id=user_id,
            status=Friendship.statusInvitation.FINISHED,
        ).exists()
        | Friendship.objects.filter(
            user_applicant_id=user_id,
            user_receiving_id=request.user.id,
            status=Friendship.statusInvitation.FINISHED,
        ).exists()
    )


def isExistingInvitation(request, user_id: str):
    return (
        Friendship.objects.filter(
            user_applicant_id=request.user.id, user_receiving_id=user_id
        ).exists()
        | Friendship.objects.filter(
            user_applicant_id=user_id, user_receiving_id=request.user.id
        ).exists()
    )
