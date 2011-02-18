import imagetable
from django.shortcuts import render_to_response
from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return render_to_response('fn_imagetable/render.html', {'imagetable': imagetable.from_file(request.FILES['file'])})
    else:
        form = UploadFileForm()

    return render_to_response('fn_imagetable/upload.html', {'form': form})
