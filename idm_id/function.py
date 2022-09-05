import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
    
def imshow(X, resize=None):
  """
  @interact allow us to work with widgets, as its name states, in an interactive way
  we take an image from a large array and display it. One can go then through the array using 
  a slider. The option of resizing the image is also avilable.
  """
  @interact
  def _imshow(i:(0, len(X)-1), resize=fixed(resize)):
      im = Image.fromarray(X[i])
      if resize:
          im = im.resize(resize)
      return im
