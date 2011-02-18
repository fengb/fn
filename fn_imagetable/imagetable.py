from PIL import Image

class ImageTable(object):
    def __init__(self, image, c='image'):
        self.image = image
        self.pixels = image.load()
        self.c = c

    @classmethod
    def from_file(cls, file, *args, **kwargs):
        return cls(Image.open(file).convert('RGB'), *args, **kwargs)

    def styles(self):
        return '''
table.%s{border-collapse:collapse;border-spacing:0;width:auto;height:auto}
table.%s td{width:1px;height:1px;padding:0}
        ''' % (self.c, self.c)

    def table(self):
        rows = []
        for y in range(self.image.size[1]):
            rows.append(''.join('<td style="background:%s"></td>' % self.hexvalue(x, y) for x in range(self.image.size[0])))
        return '<table class="%s"><tr>' % self.c + '</tr>\n<tr>'.join(rows) + '</tr></table>'

    def html(self):
        return '<html><head><style>%s</style><body>%s</body></html>' % (self.styles(), self.table())

    def hexvalue(self, x, y):
        return '#%02x%02x%02x' % self.pixels[x, y]


from_file = ImageTable.from_file


if __name__ == '__main__':
    import sys
    it = ImageTable.from_file(sys.argv[1])
    print it.html()
