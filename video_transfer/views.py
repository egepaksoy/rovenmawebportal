from django.shortcuts import redirect, render, HttpResponse
from .models import *


def settings(request):
  general_settings = GeneralSettings.objects.all().first()
  if request.method == "POST":
    general_settings.udp_comm_ip_address = request.POST.get("ip_address")
    general_settings.udp_comm_port = request.POST.get("port")
    general_settings.video_frame_rate = request.POST.get("frame")
    general_settings.video_codec_type = request.POST.get("codec")
    general_settings.video_tune = request.POST.get("tune")

    print(request.POST.get("codec"))

    general_settings.save()

    return redirect("video_transfer_settings")

  else:
    context = {
      "general_settings": general_settings
    }

    return render(request, "video_transfer/settings.html", context=context)
