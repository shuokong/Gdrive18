import aplpy
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':20,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

hdu1 = fits.open('../../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')[0]

xcenter = 84.11926799
ycenter = -6.302519164
wid = 0.7391003
hei = 0.4449478
xpanels = 1
ypanels = 1
fig=plt.figure(figsize=(3*xpanels*1.1*(wid/(wid+hei))*10.,3*ypanels/1.1*(hei/(wid+hei))*10.))
ff = aplpy.FITSFigure(hdu1, figure=fig)
ff.recenter(xcenter,ycenter,width=wid,height=hei) 
ff.set_theme('publication')
#ff.set_system_latex(True)
maxcolor = np.nanmax(hdu1.data)
#maxcolor = 100
ff.show_colorscale(cmap='gist_heat', vmin=1.e21, vmax=1.e23, stretch='sqrt')
ff.show_regions('zoombox.reg')
ff.add_colorbar() 
ff.axis_labels.set_xtext(r'$\rm RA~(J2000)$')
ff.axis_labels.set_ytext(r'$\rm Dec~(J2000)$')
ff.colorbar.set_pad(0.5)
ff.colorbar.set_axis_label_text(r'$\rm cm^{-2}$')
ff.tick_labels.set_xformat('dd.d')
ff.tick_labels.set_yformat('dd.d')
ff.add_scalebar(0.143,corner='top left',pad=1) # degree for 1 pc at 400 pc
ff.scalebar.set_label('1 pc')
ff.scalebar.set_color('white')
#beamx = 83.41442439
#beamy = -7.022846568
#bmaj = hdu1.header['BMAJ']
#bmin = hdu1.header['BMIN']
#beamangle = hdu1.header['BPA']
#ff.show_ellipses(beamx,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
#ff.add_label(beamx+1.0,beamy+2.0,'0th-moment C$^{18}$O(1-0)',size=12,weight='bold')
pdfname = 'omc6herschel.pdf'
os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesSFE'))


