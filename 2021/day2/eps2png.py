import sys
from PIL import Image


def main(argv):
  image_eps = argv[1]
  im = Image.open(image_eps)

  fig = im.convert('RGBA')

  image_png = argv[2]
  fig.save(image_png, lossless=True)


if __name__ == "__main__":
  sys.exit(main(sys.argv))
