import numpy as np
import matplotlib as mpl
import matplotlib.cm

def color_image(image, num_classes=20):

    norm = mpl.colors.Normalize(vmin=0., vmax=num_classes)
    mycm = mpl.cm.get_cmap('Set1')
    return mycm(norm(image))
