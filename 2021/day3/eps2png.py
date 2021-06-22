import sys
from PIL import Image


def eps2png(src, dst):
  image_eps = src
  im = Image.open(image_eps)

  fig = im.convert('RGBA')

  image_png = dst
  fig.save(image_png, lossless=True)


def main(argv):
  eps2png("./images/come.eps", "./images/come.png")


if __name__ == "__main__":
  sys.exit(main(sys.argv))
