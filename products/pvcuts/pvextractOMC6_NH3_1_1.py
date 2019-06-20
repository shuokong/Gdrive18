import sys
import os
import numpy as np
name_in = 'imsub_vel_OrionA_NH3_11_DR1_rebase3_trim.fits'
from pvextractor import Path
#from spectral_cube import SpectralCube
from pvextractor import extract_pv_slice

def findpath(pp,cutlen,cutdeg):
    """pp, cutlen in pix, cutdeg in degree from north to east"""
    return ([(pp[0]-cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]+cutlen/2.*np.cos(np.deg2rad(cutdeg))),(pp[0]+cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]-cutlen/2.*np.cos(np.deg2rad(cutdeg)))])

pps = [(36.063312,45.747523),(34.778631,44.359542),(33.493943,42.971557),(32.26808,41.543657),(30.879183,40.245392),(29.520471,38.916928),(28.252324,37.49788),(26.953986,36.139212),(25.716022,34.720155),(24.508241,33.270897),(23.270275,31.851831),(21.941737,30.523343),(20.613188,29.164658),(19.314832,27.805967),(18.016473,26.447273),(16.687917,25.088576),(15.389552,23.729874),(14.030801,22.401361),(12.672049,21.10304),(11.373668,19.744323),(10.105475,18.325216),(8.7467089,16.996686),(7.4483146,15.607762),(6.1801098,14.188641),(4.9118997,12.799708)]

makepvfits = 0

cutlen = 200./10. # 200 arcsec divided by 10 arcsec pixel scale
cutdeg = 45
name_outs = []
if makepvfits == 1:
    os.system('rm nh3_slice*.fits')
for nn,pp in enumerate(pps):
    name_out = 'nh3_slice'+str(nn+1)+'_imsub_vel_OrionA_NH3_11_DR1_rebase3_trim.fits'
    name_outs.append(name_out)
    if makepvfits == 1:
        pathi = findpath(pp,cutlen,cutdeg)
        path1 = Path(pathi, width=2) # 2 pixels, 20 arcsec
        slice1 = extract_pv_slice(name_in, path1)
        slice1.writeto(name_out,overwrite=True) 

import matplotlib.pyplot as plt
import pyfits
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
os.system('rm omc6_nh3_pv.pdf')
pdfname='omc6_nh3_pv.pdf'
fig=plt.figure(figsize=(xpanelwidth*xpanels*1.1,ypanelwidth*ypanels))
plt.subplots_adjust(wspace=0.1,hspace=0.1)
for nn,name_out in enumerate(name_outs):
    mmap=pyfits.open(name_out)
    incube=mmap[0].data.T
    cube=incube[:,::-1]
    cdelt1=mmap[0].header['cdelt2']/1000. # velocity in km/s
    naxis1=mmap[0].header['naxis2']
    crval1=mmap[0].header['crval2']/1000.
    crpix1=mmap[0].header['crpix2']
    cdelt2=mmap[0].header['cdelt1']*3600. # position in arcsec
    naxis2=mmap[0].header['naxis1']
    crval2=mmap[0].header['crval1']*3600.
    crpix2=mmap[0].header['crpix1']
    velticks = np.arange(6.,14.,1.)
    velpix = [naxis1-((ii-crval1)/cdelt1+crpix1) for ii in velticks]
    veltickslatex = [r"$"+str(int(ii))+r"$" for ii in velticks]
    posticks = np.arange(0.,201.,20.) # set every 20 arcsec
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
os.system('cp '+pdfname+os.path.expandvars(' ~/GoogleDrive/imagesSFE/'))

