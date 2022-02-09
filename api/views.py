from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse

from home.models import StateOfDevice 
# Create your views here.
def _hex_to_rgb(hex):
    hex = hex.replace("#", "")
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    return tuple(rgb)

def index(request):
    states_of_device = StateOfDevice.objects.all().last()
    response = {'message': 'Bom dia', 'led_one': '#ffffff', 'led_two': '#ffffff',
     'led_three': '#ffffff', 'led_four': '#ffffff'}
    if states_of_device is not None:
        red, green, blue = _hex_to_rgb(states_of_device.led_one_hex)
        response = {'message': states_of_device.message , 'led_one': red, 'led_two': green,
     'led_three': blue, 'led_four': states_of_device.led_four_hex}

    return JsonResponse(response)