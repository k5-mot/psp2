import sys
from PIL import Image


def eps2png(src, dst):
  image_eps = src
  im = Image.open(image_eps)

  fig = im.convert('RGBA')

  image_png = dst
  fig.save(image_png, lossless=True)


def main(argv):
  eps2png("./images/raster_6.eps", "./images/raster_6.png")
  eps2png("./images/vector_6.eps", "./images/vector_6.png")
  eps2png("./images/raster_9.eps", "./images/raster_9.png")
  eps2png("./images/vector_9.eps", "./images/vector_9.png")
  eps2png("./images/raster_9_2times.eps", "./images/raster_9_2times.png")
  eps2png("./images/vector_9_2times.eps", "./images/vector_9_2times.png")


if __name__ == "__main__":
  sys.exit(main(sys.argv))
