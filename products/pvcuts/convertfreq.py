import sys
import os
import numpy as np
name_in = '/Users/shuokong/GoogleDrive/AncillaryData/GBT/OrionA_NH3_11_DR1_rebase3_trim.fits'
from spectral_cube import SpectralCube
from astropy import units as u

cube = SpectralCube.read(name_in)
vcube = cube.with_spectral_unit(u.m/u.s,velocity_convention='radio')
vcube.write('vel_OrionA_NH3_11_DR1_rebase3_trim.fits',overwrite=True)

