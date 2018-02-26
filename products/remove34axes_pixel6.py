import pyfits

templatehdulist = pyfits.open('pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.fits')
print templatehdulist[0].data.shape
templatedata = templatehdulist[0].data[0,:,:]
templatehdulist[0].header['NAXIS'] = 2
del templatehdulist[0].header['CRPIX3']
del templatehdulist[0].header['CUNIT3']
del templatehdulist[0].header['CDELT3']
del templatehdulist[0].header['CRVAL3']
del templatehdulist[0].header['CTYPE3']
del templatehdulist[0].header['NAXIS3']
del templatehdulist[0].header['PC1_1']
del templatehdulist[0].header['PC2_1']
del templatehdulist[0].header['PC3_1']
del templatehdulist[0].header['PC1_2']
del templatehdulist[0].header['PC2_2']
del templatehdulist[0].header['PC3_2']
del templatehdulist[0].header['PC1_3']
del templatehdulist[0].header['PC2_3']
del templatehdulist[0].header['PC3_3']
pyfits.writeto('chan1_pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.fits',templatedata,templatehdulist[0].header,output_verify='exception',clobber=True,checksum=False)

