from django.http import HttpResponse, Http404
from django.conf import settings

import os
from PIL import Image, ImageDraw, ImageFont


SCALE = 2


def texter(request, font_face, font_size, color, text):
    font_file = os.path.join(settings.FN_TEXTER_DIR, font_face)
    try:
        font = ImageFont.truetype(font_file, int(font_size) * SCALE)
    except IOError:
        raise Http404
    else:
        size = font.getsize(text)
        image = Image.new('RGBA', size)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=font, fill='#'+color)
        image.thumbnail([coord / SCALE for coord in size], Image.ANTIALIAS)
        response = HttpResponse(mimetype='image/png')
        image.save(response, 'PNG')
        return response
