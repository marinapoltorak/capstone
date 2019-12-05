import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Scientist, Submission
from .serializers import ScientistSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'wisapp/index.html')

@api_view(['GET'])
def get_scientist(request):
    scientist = random.choice(Scientist.objects.all())
    serializer = ScientistSerializer(scientist, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

def add(request):
    if request.method == "POST":
        scientist = Submission()
        scientist.sci_name = request.POST['sci_name']
        scientist.sci_image = request.POST['sci_image']
        scientist.sci_bio = request.POST['sci_bio']
        scientist.sci_big_stuff = request.POST['sci_big_stuff']
        scientist.sci_field = request.POST['sci_field']
        scientist.sci_link = request.POST['sci_link']
        # Fill in the rest of the fields
        scientist.save()

    return render(request, 'wisapp/add.html')
