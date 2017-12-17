import pyfits

templatehdulist = pyfits.open('han1_mask_imfit_c18o_pix_2_Tmb.fits')
templatedata = templatehdulist[0].data[0,:,:,:]
templatehdulist[0].header['NAXIS'] = 3
del templatehdulist[0].header['CRPIX4']
del templatehdulist[0].header['CDELT4']
del templatehdulist[0].header['CRVAL4']
del templatehdulist[0].header['CTYPE4']
del templatehdulist[0].header['NAXIS4']
pyfits.writeto('nostokes_han1_mask_imfit_c18o_pix_2_Tmb.fits',templatedata,templatehdulist[0].header,output_verify='exception',clobber=True,checksum=False)

