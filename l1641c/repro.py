import numpy as np
from astropy.io import fits

# load hdu
hdu1 = fits.open('re_main_c18o_pix_2_Tmb.fits')[0]
hdu2 = fits.open('re_l1641c_c18o_pix_2_Tmb.fits')[0]

# assign data arrays
maindata = hdu1.data
l1641cdata = hdu2.data

# get data shapes
stokes, channel, dec, ra = maindata.shape
print maindata.shape, l1641cdata.shape, channel

# get rms noise along channel axis and keep the channel dimension
mainstd = np.nanstd(maindata[:,120:145,:,:], axis=1, keepdims=True)
l1641cstd = np.nanstd(l1641cdata[:,120:145,:,:], axis=1, keepdims=True)

# show rms array shapes
print mainstd.shape, l1641cstd.shape
print mainstd[0,0,173,754],l1641cstd[0,0,2586,828]

# repeat the rms array along the channel axis to have same shape as data
mstd = np.repeat(mainstd,channel,axis=1)
lstd = np.repeat(l1641cstd,channel,axis=1)
nanpix = np.isnan(mstd) & np.isnan(lstd)
print mstd.shape,lstd.shape,nanpix.shape

# get weight numbers, change nan to zeros
mainw = np.nan_to_num(1./mstd**2)
l1641cw = np.nan_to_num(1./lstd**2)
maindat = np.nan_to_num(maindata)
l1641cdat = np.nan_to_num(l1641cdata)

# apply weighting, change nanpix back to nan
joindat = (maindat*mainw + l1641cdat*l1641cw) / (mainw + l1641cw)
joindat[nanpix] = np.nan

# write to file
fits.writeto('join_c18o_pix_2_Tmb.fits', joindat, hdu1.header, clobber=True)



