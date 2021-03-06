# from https://pyregion.readthedocs.io/en/latest/getting_started.html

import pyregion
from astropy.io import fits
import numpy as np

#region_name = "stick_two_parts.reg"
#r = pyregion.open(region_name)
#
#hdu1 = fits.open('../carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')[0]
#mymask = r.get_mask(hdu=hdu1)
#hdu1.data[mymask] = 1
#hdu1.data[~mymask] = 0
#fits.writeto('bool_stickbody_nh.fits', hdu1.data, hdu1.header, clobber=True)

#region_name = "stick_two_parts.reg"
#r = pyregion.open(region_name)
#
#hdu1 = fits.open('../Fil1641NE_feathered_250.fits')[0]
#mymask = r.get_mask(hdu=hdu1)
#hdu1.data[mymask] = 1
#hdu1.data[~mymask] = 0
#fits.writeto('bool_Fil1641NE_feathered_250.fits', hdu1.data, hdu1.header, clobber=True)

#region_name = "stick_two_parts.reg"
#r = pyregion.open(region_name)
#
#hdu1 = fits.open('../Fil1641NE_jcmt_850.fits')[0]
#mymask = r.get_mask(hdu=hdu1)
#hdu1.data[mymask] = 1
#hdu1.data[~mymask] = 0
#fits.writeto('bool_Fil1641NE_jcmt_850.fits', hdu1.data, hdu1.header, clobber=True)

#region_name = "simc2s0p5_-30ccut_nh.reg"
#r = pyregion.open(region_name)
#
#hdu1 = fits.open('simc2s0p5_-30ccut_nh.fits')[0]
#mymask = r.get_mask(hdu=hdu1)
#hdu1.data[mymask] = 1
#hdu1.data[~mymask] = 0
#fits.writeto('bool_simc2s0p5_-30ccut_nh.fits', hdu1.data, hdu1.header, clobber=True)

#region_name = "simc2s0p5_-30ccut_nh.reg"
#r = pyregion.open(region_name)
#
#hdu1 = fits.open('simc2s0p5_-30ccut_i250_noisy.fits')[0]
#mymask = r.get_mask(hdu=hdu1)
#hdu1.data[mymask] = 1
#hdu1.data[~mymask] = 0
#fits.writeto('bool_simc2s0p5_-30ccut_i250_noisy.fits', hdu1.data, hdu1.header, clobber=True)

#region_name = "simc2s0p5_-30ccut_nh.reg"
#r = pyregion.open(region_name)
#
#hdu1 = fits.open('simc2s0p5_-30ccut_i850_noisy.fits')[0]
#mymask = r.get_mask(hdu=hdu1)
#hdu1.data[mymask] = 1
#hdu1.data[~mymask] = 0
#fits.writeto('bool_simc2s0p5_-30ccut_i850_noisy.fits', hdu1.data, hdu1.header, clobber=True)

region_name = "simc2s0p5_-30ccut_nh.reg"
r = pyregion.open(region_name)

hdu1 = fits.open('simc2rho0p7_-50ccut_nh.fits')[0]
mymask = r.get_mask(hdu=hdu1)
hdu1.data[mymask] = 1
hdu1.data[~mymask] = 0
fits.writeto('bool_simc2rho0p7_-50ccut_nh.fits', hdu1.data, hdu1.header, clobber=True)

region_name = "simc2s0p5_-30ccut_nh.reg"
r = pyregion.open(region_name)

hdu1 = fits.open('simc2rho0p7_-50ccut_i250_noisy.fits')[0]
mymask = r.get_mask(hdu=hdu1)
hdu1.data[mymask] = 1
hdu1.data[~mymask] = 0
fits.writeto('bool_simc2rho0p7_-50ccut_i250_noisy.fits', hdu1.data, hdu1.header, clobber=True)

region_name = "simc2s0p5_-30ccut_nh.reg"
r = pyregion.open(region_name)

hdu1 = fits.open('simc2rho0p7_-50ccut_i850_noisy.fits')[0]
mymask = r.get_mask(hdu=hdu1)
hdu1.data[mymask] = 1
hdu1.data[~mymask] = 0
fits.writeto('bool_simc2rho0p7_-50ccut_i850_noisy.fits', hdu1.data, hdu1.header, clobber=True)

