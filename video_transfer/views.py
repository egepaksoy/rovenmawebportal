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

def input_view(request):
  input_settings = InputSettings.objects.all().first()
  output_settings = OutputSettings.objects.all().first()

  if request.method == "POST":
    input_settings.input_protocol = request.POST.get("input_protocol")
    input_settings.input_url = request.POST.get("input_url")
    output_settings.output_protocol = request.POST.get("output_protocol")
    output_settings.output_url = request.POST.get("output_url")
    output_settings.output_audio_format = request.POST.get("output_audio_format")
    output_settings.output_video_format = request.POST.get("output_video_format")
    
    input_settings.save()
    output_settings.save()

  else:
    context = {
      "input_settings": input_settings,
      "output_settings": output_settings
    }
    return render(request, 'video_transfer/input_settings.html', context=context)

def save_input(request):
  input_settings = InputSettings.objects.all().first()
  if request.method == "POST":
    input_settings.input_protocol = request.POST.get("input_protocol")
    input_settings.input_url = request.POST.get("input_url")
    
    input_settings.save()

  return redirect("video_input")


def save_output(request):
  output_settings = OutputSettings.objects.all().first()

  if request.method == "POST":
    output_settings.output_protocol = request.POST.get("output_protocol")
    output_settings.output_url = request.POST.get("output_url")
    output_settings.output_audio_format = request.POST.get("output_audio_format")
    output_settings.output_video_format = request.POST.get("output_video_format")
    
    output_settings.save()

  return redirect("video_input")