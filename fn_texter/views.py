from django.http import HttpResponse, Http404
from django.conf import settings

import os
from PIL import Image, ImageDraw, ImageFont


def texter(request, font_face, font_size, text):
    font_file = os.path.join(settings.FN_TEXTER_DIR, font_face)
    try:
        font = ImageFont.truetype(font_file, int(font_size))
    except IOError:
        raise Http404
    else:
        size = font.getsize(text)
        image = Image.new('RGBA', size)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=font, fill='#000')
        response = HttpResponse(mimetype='image/png')
        image.save(response, 'PNG')
        return response
