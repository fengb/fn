from django.http import HttpResponse, Http404
from django.conf import settings

import os
from PIL import Image, ImageDraw, ImageFont


SCALE = 2


def texter(request, font_face, font_size, color, text, transforms=''):
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

        image = image.resize([coord / SCALE for coord in size], Image.ANTIALIAS)
        for transform in transforms.split('/'):
            if transform.startswith('r'):
                try:
                    image = image.rotate(int(transform[1:]))
                except ValueError:
                    raise Http404
            else:
                raise Http404

        response = HttpResponse(mimetype='image/png')
        image.save(response, 'PNG')
        return response
