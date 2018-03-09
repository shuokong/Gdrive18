import sys
from astropy.io import fits
import numpy as np

hdu3 = fits.open('peak_regrid18_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.fits')[0]
hdu4 = fits.open('chan1_pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.fits')[0]

peak12data = hdu3.data

## tex12.fits
tex12data = 5.5 / np.log(1. + 5.5 / (peak12data + 0.82))
tex12data[tex12data<=2.75] = np.nan
hdu4.data = tex12data 
hdu4.writeto('pixel6_convol18_tex12.fits', output_verify='exception', overwrite=True, checksum=False)


