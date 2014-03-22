# -*- coding: utf-8 -*-
"""
8as Jornadas Sig Libre 
26 de Marzo de 2014
Introducción a Python para usos geoespaciales

Creación de un archivo hillshade a partir de un MDE
"""

from osgeo import gdal
from numpy import gradient
from numpy import pi
from numpy import arctan
from numpy import arctan2
from numpy import sin
from numpy import cos
from numpy import sqrt
from numpy import zeros
from numpy import uint8
import matplotlib.pyplot as plt

# <demo> --- stop ---
def hillshade(array, azimuth, angle_altitude):
    azimuth = 360.0 - azimuth 
    
    x, y = gradient(array)
    slope = pi/2. - arctan(sqrt(x*x + y*y))
    aspect = arctan2(-x, y)
    azimuthrad = azimuth*pi / 180.
    altituderad = angle_altitude*pi / 180.
     
 
    shaded = sin(altituderad) * sin(slope)\
     + cos(altituderad) * cos(slope)\
     * cos((azimuthrad - pi/2.) - aspect)
    return 255*(shaded + 1)/2

# <demo> --- stop ---
ds = gdal.Open('data/dem.tiff')  
band = ds.GetRasterBand(1)  
arr = band.ReadAsArray()

hs_array = hillshade(arr,315, 45)
plt.imshow(hs_array,cmap='Greys')
plt.show()
# <demo> --- stop ---