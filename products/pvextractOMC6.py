import sys
import numpy as np
name_in = 'imsub_mask_imfit_c18o_pix_2_Tmb.fits'
from pvextractor import Path
#from spectral_cube import SpectralCube
from pvextractor import extract_pv_slice

def findpath(pp,cutlen,cutdeg):
    """pp, cutlen in pix, cutdeg in degree from north to east"""
    return ([(pp[0]-cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]+cutlen/2.*np.cos(np.deg2rad(cutdeg))),(pp[0]+cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]-cutlen/2.*np.cos(np.deg2rad(cutdeg)))])

pps = [(321.66161,338.17223),(314.8455,330.80769),(308.02937,323.44315),(301.5254,315.86686),(294.15632,308.97838),(286.94744,301.92969),(280.21915,294.40042),(273.33066,287.19153),(266.76257,279.66226),(260.35467,271.97278),(253.78658,264.44351),(246.7379,257.39482),(239.68921,250.18594),(232.80073,242.97706),(225.91224,235.76818),(218.86356,228.5593),(211.97507,221.35042),(204.76619,214.30173),(197.55731,207.41325),(190.66882,200.20436),(183.94053,192.67509),(176.73165,185.6264),(169.84316,178.25732),(163.11487,170.72805),(156.38658,163.35897),(149.81849,155.82969)]

cutlen = 200./2.
cutdeg = 45
name_outs = []
for nn,pp in enumerate(pps):
    pathi = findpath(pp,cutlen,cutdeg)
    path1 = Path(pathi, width=10) # 10 pixels, 20 arcsec
    slice1 = extract_pv_slice(name_in, path1)
    name_out = 'pvcuts/slice'+str(nn+1)+'_imsub_mask_imfit_c18o_pix_2_Tmb.fits'
    name_outs.append(name_out)
    slice1.writeto(name_out,overwrite=True) 

import matplotlib.pyplot as plt
import pyfits
import os
from matplotlib import gridspec
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':30,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

xpanels = 1
ypanels = 1
xpanelwidth = 7
ypanelwidth = 10
for nn,name_out in enumerate(name_outs):
    pdfname='pvcuts/omc6_pv'+str(nn+1)+'.pdf'
    fig=plt.figure(figsize=(xpanelwidth*xpanels*1.1,ypanelwidth*ypanels))
    gs = gridspec.GridSpec(ypanels,xpanels,height_ratios=[1])
    #plt.subplots_adjust(wspace=0.001,hspace=0.001)
    mmap=pyfits.open(name_out)
    cube=mmap[0].data.T
    cdelt1=mmap[0].header['cdelt2']/1000. # velocity in km/s
    naxis1=mmap[0].header['naxis2']
    crval1=mmap[0].header['crval2']/1000.
    crpix1=mmap[0].header['crpix2']
    cdelt2=mmap[0].header['cdelt1']*3600. # position in arcsec
    naxis2=mmap[0].header['naxis1']
    crval2=mmap[0].header['crval1']*3600.
    crpix2=mmap[0].header['crpix1']
    velticks = np.arange(6.,14.,1.)
    velpix = [(ii-crval1)/cdelt1+crpix1 for ii in velticks]
    veltickslatex = [r"$"+str(int(ii))+r"$" for ii in velticks]
    posticks = np.arange(0.,201.,20.)
    pospix = [(ii-crval2)/cdelt2+crpix2 for ii in posticks]
    postickslatex = [r"$"+str(int(ii))+r"$" for ii in posticks]
    ax1 = plt.subplot(gs[0])
    ax1.imshow(cube,cmap='gray_r',aspect='auto',extent=[-0.5,naxis1-0.5,naxis2+1,1],interpolation='bicubic')
    ax1.set_xticks(velpix)
    ax1.set_xticklabels(veltickslatex)
    ax1.set_yticks(pospix)
    ax1.set_yticklabels(postickslatex)
    ax1.tick_params(axis='both',direction='in',length=5,which='major',top=True,right=True)
    ax1.set_xlabel(r'$\rm Velocity~(km~s^{-1})$')
    ax1.set_ylabel(r'$\rm Offsets~(arcsec)$')
    
    os.system('rm '+pdfname)
    plt.savefig(pdfname,bbox_inches='tight')
    plt.close(fig)
    os.system('open '+pdfname)
    os.system('cp '+pdfname+os.path.expandvars(' ~/GoogleDrive/imagesSFE/pvcuts/'))

