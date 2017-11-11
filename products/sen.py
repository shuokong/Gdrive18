import sys
from astropy.io import fits
import numpy as np
from scipy import signal

hdu1 = fits.open('mask_imfit_c18o_pix_2_Tmb.fits')[0]
hdu2 = fits.open('combined_scalefactor_c18o.sen.fits')[0]
#hdu1.header['BUNIT'] = 'K'
#print hdu1.header
print hdu1.data.shape
rmsdata = hdu1.data[0:1,:20,:,:]
print hdu2.data.shape
shape2 = hdu2.data.shape
print rmsdata.shape
np.nan_to_num(rmsdata,copy=False)
detrend_rmsdata = signal.detrend(rmsdata,axis=1,type='linear')
noise = np.nanstd(detrend_rmsdata,axis=1,keepdims=True)
repeat_noise = np.repeat(noise,shape2[1],axis=1)
repeat_noise[~(hdu2.data<2)] = np.nan
hdu2.data = repeat_noise
hdu2.writeto('c18o_pix_2_Tmb_sens.fits', output_verify='exception', overwrite=True, checksum=False)

