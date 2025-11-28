from django.shortcuts import render, redirect
from .models import Light

def dashboard(request):
    lights = Light.objects.all()
    return render(request, "lights/dashboard.html", {"lights": lights})

def toggle_light(request, light_id):
    try:
        light = Light.objects.get(light_id=light_id)
    except Light.DoesNotExist:
        return JsonResponse({"error": "Light not found"}, status=404)

    light.status = not light.status
    light.save()
    return redirect("dashboard")
from django.http import JsonResponse