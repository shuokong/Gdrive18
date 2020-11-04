import aplpy
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':30,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

#hdu1 = fits.open('../mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits')[0]
hdu1 = fits.open('../mom0_stick_mask_imfit_c18o_pix_2_Tmb.fits')[0]

zoomxcenter = 84.16327978
zoomycenter = -6.301987814
zoomwid = 0.4
zoomhei = 0.4
xpanels = 1
ypanels = 1
fig=plt.figure(figsize=(3*xpanels*1.1*(zoomwid/(zoomwid+zoomhei))*10.,3*ypanels/1.1*(zoomhei/(zoomwid+zoomhei))*10.))
ff = aplpy.FITSFigure(hdu1, figure=fig)
ff.recenter(zoomxcenter,zoomycenter,width=zoomwid,height=zoomhei) 
ff.set_theme('publication')
#ff.set_system_latex(True)
maxcolor = np.nanmax(hdu1.data)
#maxcolor = 100
ff.show_colorscale(cmap='gray_r', vmin=0.5, vmax=8, stretch='linear')
ff.show_regions('pvcutswcs_overlay.reg')
ff.show_regions('stick_two_parts.reg')
ff.show_regions('lanecores_aroundstick_noname.reg')
ff.add_colorbar() 
ff.axis_labels.set_xtext(r'$\rm RA~(J2000)$')
ff.axis_labels.set_ytext(r'$\rm Dec~(J2000)$')
ff.colorbar.set_pad(0.5)
ff.colorbar.set_axis_label_text(r'$\rm K~km~s^{-1}$')
ff.tick_labels.set_xformat('dd.d')
ff.tick_labels.set_yformat('dd.d')
ff.add_scalebar(0.143,corner='top right',pad=1) # degree for 1 pc at 400 pc
ff.scalebar.set_label('1 pc')
ff.scalebar.set_color('black')
#beamx = 83.41442439
#beamy = -7.022846568
#bmaj = hdu1.header['BMAJ']
#bmin = hdu1.header['BMIN']
#beamangle = hdu1.header['BPA']
#ff.show_ellipses(beamx,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
#ff.add_label(beamx+1.0,beamy+2.0,'0th-moment C$^{18}$O(1-0)',size=12,weight='bold')
pdfname = 'omc6c18omom0.pdf'
os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/2020/StickPaper/'))


