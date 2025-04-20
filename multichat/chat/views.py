from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    return render(request, 'chat/room.html', {'room': room})
