import os
import requests
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def uploadFile(request):
    return render(request, 'uploadFile.html')

#helper function
def pinataHelper(file):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    #API key and secret from env
    headers = {
        "pinata_api_key" : settings.PINATA_API_KEY,
        "pinata_secret_api_key" : settings.PINATA_API_SECRET,
    }

    files = {
        'file' : (file.name, file, 'multipart/form-data')
    }

    try:
        response = requests.post(url, files= files, headers=headers)
        response.raise_for_status()

        #extract file hash from response
        result = response.json()
        return result['IpfsHash']
    except requests.exceptions.RequestException as e:
        print("Error uploading to pinata")
        return None


# Django view to handle file upload
def uploadToPinata(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # Upload the file to Pinata
        file_hash = pinataHelper(file)

        if file_hash:
            return JsonResponse({'status': 'success', 'file_hash': file_hash})
        else:
            return JsonResponse({'status': 'error', 'message': 'File upload failed'}, status=400)
    return render(request, 'uploadFile.html')