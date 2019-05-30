from astropy.io import fits
import matplotlib.pyplot as plt

def load_fits(filename):
  img = fits.open(filename)[0].data.squeeze()
  return int(img.argmax()/img.shape[0]), int(img.argmax()%img.shape[1])

if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually.

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
