from django.shortcuts import render

# Create your views here.
def uploadFile(request):
    return render(request, 'uploadFile.html')

