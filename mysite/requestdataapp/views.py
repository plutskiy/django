from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def user_info(request: HttpRequest) -> HttpResponse:
    return render(request, 'requestdataapp/user-info.html')

def params(request: HttpRequest) -> HttpResponse:
    context = {

    }
    return render(request, 'requestdataapp/method-id.html', context=context)


def file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES.get('file'):
        myfile = request.FILES[('file')]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
    return render(request, 'requestdataapp/file-upload.html')