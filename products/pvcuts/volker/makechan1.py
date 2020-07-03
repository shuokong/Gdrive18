from astropy.io import fits

def makechan1(inff):
    templatehdulist = fits.open(inff)
    templatedata = templatehdulist[0].data[0:1,:,:]
    templatehdulist[0].header['NAXIS3'] = 1
    fits.writeto('chan1_'+inff,templatedata,templatehdulist[0].header,output_verify='exception',clobber=True,checksum=False)

makechan1('Simul_30062020ccut_c18o.fits')
makechan1('Simul_30062020ccut_c18o_noisy.fits')

