import sys

from PIL import Image


def get_image() -> Image:
    if len(sys.argv) < 2:
        print('Please enter image path!')

    path = sys.argv[1]

    return Image.open(path)


def get_ascii(image: Image) -> str:
    width, height = image.size
    string = ''

    for i in range(width):
        for j in range(height):
            position = (i, j)
            pixel = image.getpixel(position)

            if pixel[0] > 150 and pixel[1] > 150 and pixel[2] > 150:
                string += '.'
            else:
                string += ' '

        string += '\n'

    return string


def main():
    image = get_image()
    string = get_ascii(image)

    with open('output.txt', 'w') as file:
        file.write(string)


if __name__ == '__main__':
    main()
