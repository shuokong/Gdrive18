import sys
import os
import numpy as np
from pvextractor import Path
#from spectral_cube import SpectralCube
from pvextractor import extract_pv_slice

import matplotlib.pyplot as plt
from astropy.io import fits
import os
from matplotlib import gridspec
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':20,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

def findpath(pp,cutlen,cutdeg):
    """pp, cutlen in pix, cutdeg in degree from north to east"""
    return ([(pp[0]-cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]+cutlen/2.*np.cos(np.deg2rad(cutdeg))),(pp[0]+cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]-cutlen/2.*np.cos(np.deg2rad(cutdeg)))])

pps = [(335.62807,342.87924),(328.81196,335.5147),(321.99583,328.15016),(315.49186,320.57387),(308.12278,313.68539),(300.9139,306.6367),(294.18561,299.10743),(287.29712,291.89854),(280.72903,284.36927),(274.32113,276.67979),(267.75304,269.15052),(260.70436,262.10183),(253.65567,254.89295),(246.76719,247.68407),(239.8787,240.47519),(232.83002,233.26631),(225.94153,226.05743),(218.73265,219.00874),(211.52377,212.12026),(204.63528,204.91137),(197.90699,197.3821),(190.69811,190.33341),(183.80962,182.96433),(177.08133,175.43506),(170.35304,168.06598)]


def makepv(name_in,makepvfits=1):
    cutlen = 200./2.
    cutdeg = 47
    name_outs = []
    for nn,pp in enumerate(pps):
        name_out = 'slice'+str(nn+1)+'_'+name_in
        name_outs.append(name_out)
        if makepvfits == 1:
            pathi = findpath(pp,cutlen,cutdeg)
            path1 = Path(pathi, width=10) # 10 pixels, 20 arcsec
            slice1 = extract_pv_slice(name_in, path1)
            slice1.writeto(name_out,overwrite=True) 
    
    xpanels = 5
    ypanels = 5
    xpanelwidth = 3
    ypanelwidth = 4
    pdfname=name_in.split('.')[0]+'.pdf'
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
        velticks = np.arange(-2,2.,1.)
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
    #os.system('open '+pdfname)
    for nn,pp in enumerate(pps):
        name_out = 'slice'+str(nn+1)+'_'+name_in
        os.system('rm '+name_out)

fitsname='simc2s0p5'
fitsname='simc2s0p2'
fitsname='simc2s0p0'
fitsname='simc4s0p5'
fitsname='simc4s0p2'
for rr in [-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90]:
    namin = fitsname+'_'+str(rr)+'.fits'
    rp = makepv(namin)
