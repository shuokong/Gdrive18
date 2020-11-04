import numpy as np
import os
import sys
import math
import aplpy
import matplotlib as mpl
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':50,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

fitsfiles1={
        'template':{'fname':'chan1_simc2s0p5_-30ccut_c18o.fits'},
         'channel':{'fname':'simc2s0p5_-30ccut_c18o.fits','title':r'$\rm MRCOL,\alpha=-30^\circ,C^{18}O$','mincolor':0.5,'maxcolor':8,'chan1':28,'chan2':33},
           }

fitsfiles2={
        'template':{'fname':'chan1_simc2s0p5_-30ccut_c18o_noisy.fits'},
         'channel':{'fname':'simc2s0p5_-30ccut_c18o_noisy.fits','title':r'$\rm MRCOL,\alpha=-30^\circ,C^{18}O,noise$','mincolor':0.5,'maxcolor':8,'chan1':28,'chan2':33},
           }

fitsfiles3={
        'template':{'fname':'chan1_simc2s0p5_-30ccut_13co_noisy.fits'},
         'channel':{'fname':'simc2s0p5_-30ccut_13co_noisy.fits','title':r'$\rm MRCOL,\alpha=-30^\circ,^{13}CO,noise$','mincolor':1,'maxcolor':30,'chan1':28,'chan2':33},
           }

fitsfiles4={
        'template':{'fname':'chan1_Simul_30062020ccut_c18o.fits'},
         'channel':{'fname':'Simul_30062020ccut_c18o.fits','title':r'$\rm MRCOL,\alpha=-80^\circ,C^{18}O$','mincolor':0.5,'maxcolor':8,'chan1':17,'chan2':22},
           }

fitsfiles5={
        'template':{'fname':'chan1_Simul_30062020ccut_c18o_noisy.fits'},
         'channel':{'fname':'Simul_30062020ccut_c18o_noisy.fits','title':r'$\rm MRCOL,\alpha=-80^\circ,C^{18}O,noise$','mincolor':0.5,'maxcolor':8,'chan1':17,'chan2':22},
           }

fitsfiles6={
        'template':{'fname':'chan1_Simul_30062020ccut_13co_noisy.fits'},
         'channel':{'fname':'Simul_30062020ccut_13co_noisy.fits','title':r'$\rm MRCOL,\alpha=-80^\circ,^{13}CO,noise$','mincolor':1,'maxcolor':30,'chan1':17,'chan2':22},
           }

fitsfiles7={
        'template':{'fname':'chan1_simc2rho0p7_-50ccut_c18o.fits'},
         'channel':{'fname':'simc2rho0p7_-50ccut_c18o.fits','title':r'$\rm MRCOL_{\rho_0=0.7},\alpha=-50^\circ,C^{18}O$','mincolor':0.5,'maxcolor':8,'chan1':22,'chan2':27},
           }

fitsfiles8={
        'template':{'fname':'chan1_simc2rho0p7_-50ccut_c18o_noisy.fits'},
         'channel':{'fname':'simc2rho0p7_-50ccut_c18o_noisy.fits','title':r'$\rm MRCOL_{\rho_0=0.7},\alpha=-50^\circ,C^{18}O,noise$','mincolor':0.5,'maxcolor':8,'chan1':22,'chan2':27},
           }

def currentvel(hdulistheader,currentchannel):
    vref = hdulistheader['CRVAL3']
    vdelt= hdulistheader['CDELT3']
    return (vref + (currentchannel - 1) * vdelt)

ypanels=2
xpanels=3
zoomxcenter = 0.1880632
zoomycenter = 0.1880632
zoomwid = 0.3
zoomhei = 0.3

def chanmap(fitsfiles):

    os.system('cp '+fitsfiles['template']['fname']+' '+'template_'+fitsfiles['template']['fname'])
    templatehdulist = fits.open('template_'+fitsfiles['template']['fname'])
    templatedata = templatehdulist[0].data
    nanpixels = np.isnan(templatedata) # maybe this can be broadcast to the entire channeldata array. tbd
    channelhdulist = fits.open(fitsfiles['channel']['fname'])
    channeldata = channelhdulist[0].data

    firstchannelstart=fitsfiles['channel']['chan1']
    lastchannel=fitsfiles['channel']['chan2']
    
    for startchan in range(firstchannelstart,lastchannel,ypanels*xpanels):
    
        channelstart=startchan # start from which channel, note the different starting index. tbd
        currentchannel=channelstart
        pdfname=fitsfiles['channel']['fname'].split('.')[0]+'_chanmap.pdf'
        
        fig=plt.figure(figsize=(3*xpanels*1.1*(zoomwid/(zoomwid+zoomhei))*10.,3*ypanels/1.1*(zoomhei/(zoomwid+zoomhei))*10.))
        mincolor = fitsfiles['channel']['mincolor']
        maxcolor = fitsfiles['channel']['maxcolor']
        for j in range(0,ypanels): # this order first follows row
            for i in range(0,xpanels):
                templatedata[0,:,:]=channeldata[currentchannel-1,:,:]
                templatedata[nanpixels] = np.nan
                templatehdulist.writeto('template_channel.fits',output_verify='exception',clobber=True,checksum=False) # use this as template to output every single channel
                subpos=[0.1+0.8/xpanels*i,0.1+0.9/ypanels*(ypanels-1-j),0.8/xpanels,0.9/ypanels]
                ff = aplpy.FITSFigure('template_channel.fits',figure=fig,subplot=subpos)
                ff.set_theme('publication')
                if i==1 and j==0: 
                    ff.add_scalebar(0.143,corner='bottom right') # degree for 1 pc at 400 pc
                    ff.scalebar.set_label('1 pc')
                    ff.scalebar.set_color('black')
                    if fitsfiles['channel']['fname'] == 'simc2s0p5_-30ccut_c18o_noisy.fits': 
                        ff.show_regions('pvcutsim3.reg')
                ff.show_colorscale(vmin=mincolor,vmax=maxcolor,cmap='gray_r',stretch='linear')
                ff.recenter(zoomxcenter,zoomycenter,width=zoomwid,height=zoomhei) 
    #            if j == 1: 
    #                ff.show_regions('stickrings.reg')
                ff.tick_labels.set_yformat('dd.d')
                ff.tick_labels.set_xformat('dd.d')
                beamx = zoomxcenter - 0.8 * zoomwid / 2.
                beamy = zoomycenter + 0.8 * zoomhei / 2.
                ff.add_label(beamx,beamy,'{0:.2f}'.format(currentvel(channelhdulist[0].header,currentchannel))+'km/s',color='black',horizontalalignment='center')
    #            if j != ypanels-1:
                ff.hide_xaxis_label()
                ff.hide_xtick_labels()
    #            if i != 0:
                ff.hide_yaxis_label()
                ff.hide_ytick_labels()
                currentchannel = currentchannel + 1
                os.system('rm template_channel.fits')
        fig.suptitle(fitsfiles['channel']['title'],y=1.03)
        ax1 = fig.add_axes([0.9,0.1,0.01,0.9])
        cmap = mpl.cm.gray_r
        norm = mpl.colors.Normalize(vmin=mincolor, vmax=maxcolor)
        #norm = mpl.colors.PowerNorm(gamma=0.5,vmin=mincolor, vmax=maxcolor)
        cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,norm=norm,orientation='vertical')#,ticks=colorticks)
        
        # close and save file
        fig.canvas.draw()
        os.system('rm '+pdfname)
        plt.savefig(pdfname,bbox_inches='tight')
        plt.close(fig)
        os.system('open '+pdfname)
        os.system('cp '+pdfname+' ~/GoogleDrive/2020/StickPaper/')
    
    templatehdulist.close()
    channelhdulist.close()
    os.system('rm template_'+fitsfiles['template']['fname'])

chanmap(fitsfiles1)
chanmap(fitsfiles2)
#chanmap(fitsfiles3)
chanmap(fitsfiles4)
#chanmap(fitsfiles5)
#chanmap(fitsfiles6)
#chanmap(fitsfiles7)
#chanmap(fitsfiles8)
