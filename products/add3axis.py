import pyfits
import numpy as np

mom018hdulist = pyfits.open('mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits')
templatehdulist = pyfits.open('../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')
templatedata = templatehdulist[0].data[np.newaxis,:,:]
templatehdulist[0].header['NAXIS'] = 3
templatehdulist[0].header['CRPIX3'] = mom018hdulist[0].header['CRPIX3']
templatehdulist[0].header['CDELT3'] = mom018hdulist[0].header['CDELT3']
templatehdulist[0].header['CRVAL3'] = mom018hdulist[0].header['CRVAL3']
templatehdulist[0].header['CTYPE3'] = mom018hdulist[0].header['CTYPE3']
templatehdulist[0].header['NAXIS3'] = mom018hdulist[0].header['NAXIS3']
pyfits.writeto('threeaxes_carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits',templatedata,templatehdulist[0].header,output_verify='exception',clobber=True,checksum=False)
