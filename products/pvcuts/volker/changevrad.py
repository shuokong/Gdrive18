from astropy.io import fits

def changevrad(inff):
    templatehdulist = fits.open(inff)
    templatedata = templatehdulist[0].data 
    templatehdulist[0].header['CTYPE3'] = 'VELO-LSR'
    templatehdulist[0].header['RESTFREQ'] = 1.09782160000E+11
    fits.writeto('vrad_'+inff,templatedata,templatehdulist[0].header,output_verify='exception',clobber=True,checksum=False)

changevrad('Simul_30062020ccut_c18o.fits')

