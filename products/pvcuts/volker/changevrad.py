from astropy.io import fits

def changevrad(inff,newvl,newvr):
    templatehdulist = fits.open(inff)
    crval3 = templatehdulist[0].header['CRVAL3']
    cdelt3 = templatehdulist[0].header['CDELT3']
    newpl = int((newvl - crval3) / cdelt3)
    newpr = int((newvr - crval3) / cdelt3)
    templatehdulist[0].header['CRVAL3'] = newvl
    templatehdulist[0].header['NAXIS3'] = newpr - newpl +1
    templatehdulist[0].header['CTYPE3'] = 'VELO-LSR'
    templatehdulist[0].header['RESTFREQ'] = 1.09782160000E+11
    templatedata = templatehdulist[0].data[newpl:newpr+1,:,:]
    fits.writeto('vrad_'+inff,templatedata,templatehdulist[0].header,output_verify='exception',clobber=True,checksum=False)

#changevrad('simc2s0p5_-20ccut_C18O.fits',-3.,3.)
#changevrad('simc2s0p5_-20ccut_C18O_noisy.fits',-3.,3.)
#changevrad('simc2s0p2_-30ccut_C18O.fits',-3.,3.)
#changevrad('simc2s0p2_-30ccut_C18O_noisy.fits',-3.,3.)
#changevrad('simc2s0p5_-30ccut_C18O.fits',-3.,3.)
#changevrad('simc2s0p5_-30ccut_C18O_noisy.fits',-3.,3.)
changevrad('simc2rho0p7_-50ccut_C18O.fits',-3.,3.)
changevrad('simc2rho0p7_-50ccut_C18O_noisy.fits',-3.,3.)

