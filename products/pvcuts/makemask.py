# from https://pyregion.readthedocs.io/en/latest/getting_started.html

import pyregion
from astropy.io import fits
import numpy as np

region_name = "stickbody.reg"
r = pyregion.open(region_name)

hdu1 = fits.open('../novel_mom0_stick_mask_imfit_c18o_pix_2_Tmb.fits')[0]
mymask = r.get_mask(hdu=hdu1)
hdu1.data[mymask] = 1
hdu1.data[~mymask] = 0
fits.writeto('bool_stickbody.fits', hdu1.data, hdu1.header, clobber=True)

