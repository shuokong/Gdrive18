import matplotlib.pylab as plt
import pyfits
import pylab
import aplpy
import sys

name_out = 'pv_ratio_13_18.fits'

#pv13 = pyfits.open('../../13co/products/pv_mask_imfit_13co_pix_2_Tmb.fits')
#pv18 = pyfits.open('pv_mask_imfit_c18o_pix_2_Tmb.fits')
#pv13data = pv13[0].data
#pv18data = pv18[0].data
#pv18data = pv13data/pv18data
#pv18.writeto(name_out,output_verify='exception',clobber=True,checksum=False)
#sys.exit()

fig=plt.figure(figsize=(10,6))
gc=aplpy.FITSFigure(name_out,dimensions=[0,1],figure=fig,hdu=0)
gc.show_colorscale(aspect='auto')

gc.ticks.set_xspacing(21.)
gc.ticks.set_minor_frequency(7)
gc.axis_labels.set_ytext('Velocity (km/s)')
gc.ticks.show()
gc.ticks.set_color('black')
gc.ticks.set_length(10)
gc.ticks.set_linewidth(2)
gc.add_colorbar()
gc.set_theme('publication')
gc.colorbar.set_width(0.5)
plt.savefig('pv_ratio_13_18.pdf',bbox_inches='tight')

