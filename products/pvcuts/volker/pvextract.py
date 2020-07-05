import sys
import os
import numpy as np
name_in = 'Simul_30062020ccut_c18o.fits'
name_in = 'Simul_30062020ccut_c18o_noisy.fits'
from pvextractor import Path
#from spectral_cube import SpectralCube
from pvextractor import extract_pv_slice

def findpath(pp,cutlen,cutdeg):
    """pp, cutlen in pix, cutdeg in degree from north to east"""
    return ([(pp[0]-cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]+cutlen/2.*np.cos(np.deg2rad(cutdeg))),(pp[0]+cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]-cutlen/2.*np.cos(np.deg2rad(cutdeg)))])

pps = [(252.1826,254.21843),(245.36649,246.85389),(238.55036,239.48935),(232.04639,231.91306),(224.67731,225.02458),(217.46843,217.97589),(210.74014,210.44662),(203.85165,203.23773),(197.28356,195.70846),(190.87566,188.01898),(184.30757,180.48971),(177.25889,173.44102),(170.2102,166.23214),(163.32172,159.02326),(156.43323,151.81438),(149.38455,144.6055),(142.49606,137.39662),(135.28718,130.34793),(128.0783,123.45945),(121.18981,116.25056),(114.46152,108.72129),(107.25264,101.6726),(100.36415,94.303516),(93.63586,86.774246),(86.90757,79.405166)]

makepvfits = 1

cutlen = 200./4.
cutdeg = 45
name_outs = []
if makepvfits == 1:
    os.system('rm slice*.fits')
for nn,pp in enumerate(pps):
    name_out = 'slice'+str(nn+1)+'_Simul_30062020ccut_c18o.fits'
    name_out = 'slice'+str(nn+1)+'_Simul_30062020ccut_c18o_noisy.fits'
    name_outs.append(name_out)
    if makepvfits == 1:
        pathi = findpath(pp,cutlen,cutdeg)
        path1 = Path(pathi, width=5) # 5 pixels, 20 arcsec
        slice1 = extract_pv_slice(name_in, path1)
        slice1.writeto(name_out,overwrite=True) 

import matplotlib.pyplot as plt
from astropy.io import fits
import os
from matplotlib import gridspec
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':20,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

xpanels = 5
ypanels = 5
xpanelwidth = 3
ypanelwidth = 4
pdfname='sim_c18o_pv.pdf'
pdfname='sim_c18o_noisy_pv.pdf'
fig=plt.figure(figsize=(xpanelwidth*xpanels*1.1,ypanelwidth*ypanels))
plt.subplots_adjust(wspace=0.1,hspace=0.1)
for nn,name_out in enumerate(name_outs):
    mmap=fits.open(name_out)
    cube=mmap[0].data.T
    cdelt1=mmap[0].header['cdelt2'] # velocity in km/s
    naxis1=mmap[0].header['naxis2']
    crval1=mmap[0].header['crval2']
    crpix1=mmap[0].header['crpix2']
    cdelt2=mmap[0].header['cdelt1']*3600. # position in arcsec
    naxis2=mmap[0].header['naxis1']
    crval2=mmap[0].header['crval1']*3600.
    crpix2=mmap[0].header['crpix1']
    velticks = np.arange(-3,4.,1.)
    velpix = [(ii-crval1)/cdelt1+crpix1 for ii in velticks]
    veltickslatex = [r"$"+str(int(ii))+r"$" for ii in velticks]
    posticks = np.arange(0.,201.,20.)
    pospix = [(ii-crval2)/cdelt2+crpix2 for ii in posticks]
    postickslatex = [r"$"+str(int(ii))+r"$" for ii in posticks]
    ax1 = fig.add_subplot(ypanels,xpanels,nn+1)
    ax1.imshow(cube,cmap='gray_r',aspect='auto',extent=[-0.5,naxis1-0.5,naxis2+1,1],interpolation='bicubic')
    ax1.text(0.9, 0.9, str(nn+1),horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)
    ax1.set_xticks(velpix)
    ax1.set_xticklabels(veltickslatex)
    if nn / xpanels == ypanels - 1:
        ax1.set_xlabel(r'$\rm Velocity~(km~s^{-1})$')
    ax1.set_yticks(pospix)
    ax1.set_yticklabels(postickslatex)
    if nn % xpanels == 0:
        ax1.set_ylabel(r'$\rm Offsets~(arcsec)$')
    if nn / xpanels < ypanels - 1:
        plt.setp(ax1.get_xticklabels(),visible=False)
    if nn % xpanels > 0:
        plt.setp(ax1.get_yticklabels(),visible=False)
    ax1.tick_params(axis='both',direction='in',length=5,which='major',top=True,right=True)
    
os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
plt.close(fig)
os.system('open '+pdfname)

