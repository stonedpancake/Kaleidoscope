from PIL import Image


class PhotoFilters:

    def bright(self, source_name, result_name, brightness):
        source = Image.open(source_name)
        result = Image.new('RGB', source.size)
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                red = int(r * brightness)
                red = min(255, max(0, red))
                green = int(g * brightness)
                green = min(255, max(0, green))
                blue = int(b * brightness)
                blue = min(255, max(0, blue))
                result.putpixel((x, y), (red, green, blue))
        result.save(result_name, "JPEG")

    def negative(self, source_name, result_name):
        source = Image.open(source_name)
        result = Image.new('RGB', source.size)
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                result.putpixel((x, y), (255 - r, 255 - g, 255 - b))
        result.save(result_name, "JPEG")

    def white_black(self, source_name, result_name, brightness):
        source = Image.open(source_name)
        result = Image.new('RGB', source.size)
        separator = 255 / brightness / 2 * 3
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                total = r + g + b
                if total > separator:
                    result.putpixel((x, y), (255, 255, 255))
                else:
                    result.putpixel((x, y), (0, 0, 0))
        result.save(result_name, "JPEG")

    def gray_scale(self, source_name, result_name):
        source = Image.open(source_name)
        result = Image.new('RGB', source.size)
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
                result.putpixel((x, y), (gray, gray, gray))
        result.save(result_name, "JPEG")

    def sepia(self, source_name, result_name):
        source = Image.open(source_name)
        result = Image.new('RGB', source.size)
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                red = int(r * 0.393 + g * 0.769 + b * 0.189)
                green = int(r * 0.349 + g * 0.686 + b * 0.168)
                blue = int(r * 0.272 + g * 0.534 + b * 0.131)
                result.putpixel((x, y), (red, green, blue))
        result.save(result_name, "JPEG")

    def contrast(self, source_name, result_name, coefficient):
        source = Image.open(source_name)
        result = Image.new('RGB', source.size)

        avg = 0
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                avg += r * 0.299 + g * 0.587 + b * 0.114
        avg /= source.size[0] * source.size[1]

        palette = []
        for i in range(256):
            temp = int(avg + coefficient * (i - avg))
            if temp < 0:
                temp = 0
            elif temp > 255:
                temp = 255
            palette.append(temp)

        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                result.putpixel((x, y), (palette[r], palette[g], palette[b]))

        result.save(result_name, "JPEG")
