from PIL import Image

class ImageTable(object):
    def __init__(self, image, c='image'):
        self.image = image
        self.pixels = image.load()
        self.c = c

    @classmethod
    def from_file(cls, file, *args, **kwargs):
        return cls(Image.open(file).convert('RGB'), *args, **kwargs)

    def hexvalue(self, x, y):
        return '#%02x%02x%02x' % self.pixels[x, y]

    def styles(self, fout):
        fout.write('''
table.%s{border-collapse:collapse;border-spacing:0;width:auto;height:auto}
table.%s td{width:1px;height:1px;padding:0}
        ''' % (self.c, self.c))

    def table(self, fout):
        fout.write('<table class="%s">' % self.c)
        for y in range(self.image.size[1]):
            fout.write('<tr>')
            for x in range(self.image.size[0]):
                fout.write('<td style="background:%s"></td>' % self.hexvalue(x, y))
            fout.write('</tr>')
        fout.write('</table>')

    def html(self, fout):
        fout.write('<html><head><style>')
        self.styles(fout)
        fout.write('</style><body>')
        self.table(fout)
        fout.write('</body></html>')


from_file = ImageTable.from_file


if __name__ == '__main__':
    import sys
    it = ImageTable.from_file(sys.argv[1])
    it.html(sys.stdout)
