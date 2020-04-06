import sys
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename


#hdu1 = fits.open('chan1_pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.fits')[0]
#hdu2 = fits.open('../../OrionAdust/herschelAmelia/OrionA_all_spire250_nh_mask_corr_apex.fits')[0]
#from reproject import reproject_exact
#array, footprint = reproject_exact(hdu2, hdu1.header)
#fits.writeto('stutz_on_c18o_header.fits', array, hdu1.header, clobber=True)

#hdu1 = fits.open('chan1_pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.fits')[0]
#hdu2 = fits.open('../../OrionAdust/lombardi_planck_herschel_plane3_colorT.fits')[0]
#from reproject import reproject_exact
#array, footprint = reproject_exact(hdu2, hdu1.header)
#fits.writeto('lombardi_colorT_on_c18o_header.fits', array, hdu1.header, clobber=True)

#hdu1 = fits.open('chan1_pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.fits')[0]
#hdu2 = fits.open('../../OrionAdust/lombardi_planck_herschel_plane4_colorTerror.fits')[0]
#from reproject import reproject_exact
#array, footprint = reproject_exact(hdu2, hdu1.header)
#fits.writeto('lombardi_colorTerror_on_c18o_header.fits', array, hdu1.header, clobber=True)

#hdu1 = fits.open('mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits')[0]
#hdu2 = fits.open('../../13co/products/tex12.fits')[0]
#from reproject import reproject_interp
#array, footprint = reproject_interp(hdu2, hdu1.header)
#fits.writeto('tex_on_c18o_header.fits', array, hdu1.header, clobber=True)

#hdu1 = fits.open('mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits')[0]
#hdu2 = fits.open('threeaxes_carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')[0]
#from reproject import reproject_interp
#array, footprint = reproject_interp(hdu2, hdu1.header)
#fits.writeto('dustcoldens_on_c18o_header.fits', array, hdu1.header, clobber=True)

hdu1 = fits.open('mom0_stick_mask_imfit_c18o_pix_2_Tmb.fits')[0]
hdu2 = fits.open('../../13co/products/tex12.fits')[0]
from reproject import reproject_interp
array, footprint = reproject_interp(hdu2, hdu1.header)
fits.writeto('tex_on_stick_header.fits', array, hdu1.header, clobber=True)

hdu1 = fits.open('mom0_stick_mask_imfit_c18o_pix_2_Tmb.fits')[0]
hdu2 = fits.open('threeaxes_carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')[0]
from reproject import reproject_interp
array, footprint = reproject_interp(hdu2, hdu1.header)
fits.writeto('dustcoldens_on_stick_header.fits', array, hdu1.header, clobber=True)

hdu1 = fits.open('novel_mom0_stick_mask_imfit_c18o_pix_2_Tmb.fits')[0]
hdu2 = fits.open('../../OrionAdust/herschelAmelia/OrionA-all_conv500_temp.fits')[0]
from reproject import reproject_interp
array, footprint = reproject_interp(hdu2, hdu1.header)
fits.writeto('dustT_on_stick_header.fits', array, hdu1.header, clobber=True)

hdu1 = fits.open('novel_mom0_stick_mask_imfit_c18o_pix_2_Tmb.fits')[0]
hdu2 = fits.open('../../AncillaryData/GBT/OrionA_Tkin_DR1_rebase3_flag.fits')[0]
from reproject import reproject_interp
array, footprint = reproject_interp(hdu2, hdu1.header)
fits.writeto('gasT_on_stick_header.fits', array, hdu1.header, clobber=True)
