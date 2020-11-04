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
    return ([(pp[0]-cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]-cutlen/2.*np.sin(np.deg2rad(cutdeg))),(pp[0]+cutlen/2.*np.cos(np.deg2rad(cutdeg)),pp[1]+cutlen/2.*np.sin(np.deg2rad(cutdeg)))])

name_ins = ['sim_radAB_c2s0p5_-10.fits', 'sim_radAB_c2s0p5_-60.fits', 'sim_radAB_c2s0p5_10.fits', 'sim_radAB_c2s0p5_60.fits', 'sim_radAB_c2s0p5_-20.fits', 'sim_radAB_c2s0p5_-70.fits', 'sim_radAB_c2s0p5_20.fits', 'sim_radAB_c2s0p5_70.fits', 'sim_radAB_c2s0p5_-30.fits', 'sim_radAB_c2s0p5_-80.fits', 'sim_radAB_c2s0p5_30.fits', 'sim_radAB_c2s0p5_80.fits', 'sim_radAB_c2s0p5_-40.fits', 'sim_radAB_c2s0p5_-90.fits', 'sim_radAB_c2s0p5_40.fits', 'sim_radAB_c2s0p5_90.fits', 'sim_radAB_c2s0p5_-50.fits', 'sim_radAB_c2s0p5_0.fits', 'sim_radAB_c2s0p5_50.fits',]

def makepv(name_in):

    pps = [(231.,237.)]
    
    makepvfits = 1
    
    cutlen = 878./4.142
    cutdeg = 47
    name_outs = []
    if makepvfits == 1:
        os.system('rm radABslice.fits')
    for nn,pp in enumerate(pps):
        name_out = 'radABslice.fits'
        name_outs.append(name_out)
        if makepvfits == 1:
            pathi = findpath(pp,cutlen,cutdeg)
            pathi = [(375,355), (159,127)] # directly tell the path
            print 'pathi',pathi
            path1 = Path(pathi, width=30) # 30 pixels, 60 arcsec
            slice1 = extract_pv_slice(name_in, path1)
            slice1.writeto(name_out,overwrite=True) 
    #sys.exit()
    
    xpanels = 1
    ypanels = 1
    xpanelwidth = 6
    ypanelwidth = 7
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
        velticks = np.arange(-3.,3.,1.)
        velpix = [(ii-crval1)/cdelt1+crpix1 for ii in velticks]
        veltickslatex = [r"$"+str(int(ii))+r"$" for ii in velticks]
        posticks = np.arange(0.,651.,50.)
        pospix = [(ii-crval2)/cdelt2+crpix2 for ii in posticks]
        postickslatex = [r"$"+str(int(ii))+r"$" for ii in posticks]
        ax1 = fig.add_subplot(ypanels,xpanels,nn+1)
        ax1.imshow(cube,cmap='gray_r',aspect='auto',extent=[0.5,naxis1+0.5,naxis2+1,1],interpolation='bicubic')
        #ax1.text(0.9, 0.9, str(nn+1),horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)
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
    os.system('cp '+pdfname+os.path.expandvars(' ~/GoogleDrive/2020/StickPaper/'))

for nn in name_ins:
    makepv(nn)
    
