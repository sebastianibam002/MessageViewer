from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse

from home.models import StateOfDevice 
# Create your views here.
def index(request):
    states_of_device = StateOfDevice.objects.all().last()
    response = {'message': 'Bom dia', 'led_one': '#ffffff', 'led_two': '#ffffff',
     'led_three': '#ffffff', 'led_four': '#ffffff'}
    if states_of_device is not None:
        response = {'message': states_of_device.message , 'led_one': states_of_device.led_one_hex, 'led_two': states_of_device.led_two_hex,
     'led_three': states_of_device.led_three_hex, 'led_four': states_of_device.led_four_hex}

    return JsonResponse(response)