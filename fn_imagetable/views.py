import imagetable
import tempfile
from django import forms, http
from django.shortcuts import render_to_response


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = tempfile.TemporaryFile()
            it = imagetable.from_file(request.FILES['file'])
            it.html(f)
	    f.seek(0)
            return http.HttpResponse(f.read())
    else:
        form = UploadFileForm()

    return render_to_response('fn_imagetable/upload.html', {'form': form})
