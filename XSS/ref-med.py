from django.http import HttpResponse
from django.utils.safestring import mark_safe

def profile(request):
    bio = request.GET.get("bio", "")
    return HttpResponse(mark_safe(f"<div class='bio'>{bio}</div>"))
