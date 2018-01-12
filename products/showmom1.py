import aplpy
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

hdu1 = fits.open('mom1_c18o_pix_2_Tmb.fits')[0]
xcenter=84
ycenter=-6
wid = 1.5
hei = 2.4
xpanels = 1
ypanels = 1
fig=plt.figure(figsize=(3*xpanels*1.1*(wid/(wid+hei))*10.,3*ypanels/1.1*(hei/(wid+hei))*10.))
ff = aplpy.FITSFigure(hdu1, figure=fig)
ff.recenter(xcenter,ycenter,width=wid,height=hei) 
ff.set_theme('publication')
#ff.set_system_latex(True)
maxcolor = np.nanmax(hdu1.data)
ff.show_colorscale(cmap='jet', vmin=5, vmax=13, stretch='linear')
ff.show_regions('olay2.reg')
#ff.show_contour(mask_hdu, levels=1, colors='yellow', linewidths=0.1)
ff.add_colorbar() 
ff.colorbar.set_font(size=12)
ff.colorbar.set_pad(0.5)
ff.colorbar.set_axis_label_text('km s$^{-1}$')
ff.colorbar.set_font(size=12)
ff.set_tick_labels_font(size=12)
ff.set_axis_labels_font(size=12)
ff.add_scalebar(0.286,corner='top left',pad=10) # degree for 2pc at 400 pc
ff.scalebar.set_label('2 pc')
ff.scalebar.set_font_size(12)
beamx = 83.41442439
beamy = -7.022846568
bmaj = hdu1.header['BMAJ']
bmin = hdu1.header['BMIN']
beamangle = hdu1.header['BPA']
ff.show_ellipses(beamx,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
ff.add_label(beamx+0.25,beamy+0.15,'1st-moment C$^{18}$O(1-0)',fontsize=12)
#ff.tick_labels.set_xformat('dd')
#ff.tick_labels.set_yformat('dd')
pdfname = 'mom1_c18o_pix_2_Tmb.pdf'
os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))
sys.exit()

from matplotlib import rc
rc('text', usetex=True)
font = {'weight':'normal','size':12,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

print hdu1.data.shape
#sys.exit()
x = hdu1.data[~np.isnan(hdu1.data)]
p=plt.figure(figsize=(7,6))
fig, ax = plt.subplots(1,1)
# the histogram of the data
n, bins, patches = plt.hist(x, 100, normed=True, histtype='step', color='k')
#print n,bins

plt.xlabel(r'$v_{\rm lsr}~\rm km~s^{-1}$')
plt.ylabel('probability density')
plt.xlim(0,20)
ax.xaxis.set_tick_params(top='on',labeltop='on',direction='in')
ax.yaxis.set_tick_params(direction='in')
#plt.grid(True)
pdfname = 'mom1_c18o_hist.pdf'
os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))

