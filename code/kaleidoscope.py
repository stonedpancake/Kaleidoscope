import cv2
import numpy as np
from PIL import Image, ImageFilter
from scipy.interpolate import UnivariateSpline
import pilgram


class PhotoFilters:

    def bright(self, source_name, result_name, brightness=0.5):
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

    def white_black(self, source_name, result_name, brightness=1.2):
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

    def contrast(self, source_name, result_name, coefficient=2):
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

    def emboss(self, source_name, result_name):
        img = Image.open(source_name)
        ing_emboss = img.filter(ImageFilter.EMBOSS)
        ing_emboss.save(result_name)

    def contour(self, source_name, result_name):
        img = Image.open(source_name)
        ing_emboss = img.filter(ImageFilter.CONTOUR)
        ing_emboss.save(result_name)

    def edges(self, source_name, result_name):
        img = Image.open(source_name)
        ing_emboss = img.filter(ImageFilter.FIND_EDGES)
        ing_emboss.save(result_name)

    def spreadLookupTable(self, x, y):  # NOT AN EFFECT (SUPPORT FUNC)
        spline = UnivariateSpline(x, y)
        return spline(range(256))

    def warm_image(self, source_name, result_name):
        increaseLookupTable = self.spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = self.spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        red_channel, green_channel, blue_channel = cv2.split(source_name)
        red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)

        res_img = Image.open(cv2.merge((red_channel, green_channel, blue_channel)))
        res_img.save(result_name)

    def cold_image(self, source_name, result_name):
        increaseLookupTable = self.spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = self.spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        red_channel, green_channel, blue_channel = cv2.split(source_name)
        red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)

        res_img = Image.open(cv2.merge((red_channel, green_channel, blue_channel)))
        res_img.save(result_name)

    def clarendon(self, source_name, result_name):
        res_img = pilgram.clarendon(Image.open(source_name))
        res_img.save(result_name)

    def _1977(self, source_name, result_name):
        res_img = pilgram._1977(Image.open(source_name))
        res_img.save(result_name)

    def reyes(self, source_name, result_name):
        res_img = pilgram.reyes(Image.open(source_name))
        res_img.save(result_name)

    def aden(self, source_name, result_name):
        res_img = pilgram.aden(Image.open(source_name))
        res_img.save(result_name)

    def brannan(self, source_name, result_name):
        res_img = pilgram.brannan(Image.open(source_name))
        res_img.save(result_name)

    def brooklyn(self, source_name, result_name):
        res_img = pilgram.brooklyn(Image.open(source_name))
        res_img.save(result_name)

    def earlybird(self, source_name, result_name):
        res_img = pilgram.earlybird(Image.open(source_name))
        res_img.save(result_name)

    def gingham(self, source_name, result_name):
        res_img = pilgram.gingham(Image.open(source_name))
        res_img.save(result_name)

    def hudson(self, source_name, result_name):
        res_img = pilgram.hudson(Image.open(source_name))
        res_img.save(result_name)

    def inkwell(self, source_name, result_name):
        res_img = pilgram.inkwell(Image.open(source_name))
        res_img.save(result_name)

    def kelvin(self, source_name, result_name):
        res_img = pilgram.kelvin(Image.open(source_name))
        res_img.save(result_name)

    def lark(self, source_name, result_name):
        res_img = pilgram.lark(Image.open(source_name))
        res_img.save(result_name)

    def lofi(self, source_name, result_name):
        res_img = pilgram.lofi(Image.open(source_name))
        res_img.save(result_name)

    def maven(self, source_name, result_name):
        res_img = pilgram.maven(Image.open(source_name))
        res_img.save(result_name)

    def mayfair(self, source_name, result_name):
        res_img = pilgram.mayfair(Image.open(source_name))
        res_img.save(result_name)

    def moon(self, source_name, result_name):
        res_img = pilgram.moon(Image.open(source_name))
        res_img.save(result_name)

    def nashville(self, source_name, result_name):
        res_img = pilgram.nashville(Image.open(source_name))
        res_img.save(result_name)

    def perpetua(self, source_name, result_name):
        res_img = pilgram.perpetua(Image.open(source_name))
        res_img.save(result_name)

    def rise(self, source_name, result_name):
        res_img = pilgram.rise(Image.open(source_name))
        res_img.save(result_name)

    def slumber(self, source_name, result_name):
        res_img = pilgram.slumber(Image.open(source_name))
        res_img.save(result_name)

    def stinson(self, source_name, result_name):
        res_img = pilgram.stinson(Image.open(source_name))
        res_img.save(result_name)

    def toaster(self, source_name, result_name):
        res_img = pilgram.toaster(Image.open(source_name))
        res_img.save(result_name)

    def valencia(self, source_name, result_name):
        res_img = pilgram.valencia(Image.open(source_name))
        res_img.save(result_name)

    def walden(self, source_name, result_name):
        res_img = pilgram.walden(Image.open(source_name))
        res_img.save(result_name)

    def willow(self, source_name, result_name):
        res_img = pilgram.willow(Image.open(source_name))
        res_img.save(result_name)

    def xpro2(self, source_name, result_name):
        res_img = pilgram.xpro2(Image.open(source_name))
        res_img.save(result_name)
