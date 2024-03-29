import collections
import itertools
import math
import operator
from PIL import Image


def uniquebatches(supported):
    length = len(supported)
    for target in itertools.count():
        ret = ''
        if target >= length:
            for x in reversed(range(1, math.log(target, length) + 1)):
                ret += supported[target / length**x - 1]
                target %= length**x

        yield ret + supported[target]



class ImageTable(object):
    def __init__(self, image, c='image'):
        self.image = image
        self.pixels = image.load()
        self.c = c

    @classmethod
    def from_file(cls, file, *args, **kwargs):
        return cls(Image.open(file).convert('RGB'), *args, **kwargs)

    @property
    def color_classes(self):
        if not hasattr(self, '_color_classes'):
            colors_count = collections.defaultdict(int)
            for x in range(self.image.size[0]):
                for y in range(self.image.size[1]):
                    colors_count[self.pixels[x, y]] += 1

            aliased_colors = sorted((c for (c, count) in colors_count.items() if count > 1), key=operator.itemgetter(1))
            classes = uniquebatches('abcdefghijklmnopqrstuvwxyz')
            self._color_classes = dict((c, next(classes)) for c in aliased_colors)

        return self._color_classes

    def cellattr(self, x, y):
        color = self.pixels[x, y]
        if color in self.color_classes:
            return 'class="%s"' % self.color_classes[color]
        else:
            return 'style="background:#%02x%02x%02x"' % color

    def styles(self, fout):
        fout.write('''
div.%(class)s{width:%(width)s;}
div.%(class)s p{float:left;width:1px;height:1px;padding:0;margin:0}
        ''' % {'class': self.c, 'width': self.image.size[0]})
        for (color, cls) in self.color_classes.items():
            fout.write('div.%s .%s{background:#%02x%02x%02x}' % ((self.c, cls) + color))

    def main(self, fout):
        fout.write('<div class="%s">' % self.c)
        for y in range(self.image.size[1]):
            for x in range(self.image.size[0]):
                fout.write('<p %s></p>' % self.cellattr(x, y))
        fout.write('</div>')

    def html(self, fout):
        fout.write('<html><head><style>')
        self.styles(fout)
        fout.write('</style><body>')
        self.main(fout)
        fout.write('</body></html>')


from_file = ImageTable.from_file


if __name__ == '__main__':
    import sys
    it = ImageTable.from_file(sys.argv[1])
    it.html(sys.stdout)
