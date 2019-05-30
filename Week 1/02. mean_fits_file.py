import numpy as np
from  astropy.io import fits

def mean_fits(filelist):
  result = []
  for x in filelist:
    result.append(fits.open(x)[0].data.squeeze())
  return np.dstack(tuple(result)).mean(axis=-1)

if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()