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

fitsfiles={'filename':'chan13co.pdf',
        'template':{'fname':'chan1_stick_mask_han1_imfit_13co_pix_2_Tmb.fits'},
         'channel':{'fname':'stick_mask_han1_imfit_13co_pix_2_Tmb.fits','title':r'13CO(1-0)','mincolor':1,'maxcolor':30,'start':31,'end':50,'xpanels':5,'ypanels':4},
           }

fitsfiles={'filename':'chanc18o.pdf',
        'template':{'fname':'chan1_stick_han1_mask_imfit_c18o_pix_2_Tmb.fits'},
         'channel':{'fname':'../stick_han1_mask_imfit_c18o_pix_2_Tmb.fits','title':r'C18O(1-0)','mincolor':0.5,'maxcolor':8,'start':35,'end':38,'xpanels':2,'ypanels':2},
           }

os.system('cp '+fitsfiles['template']['fname']+' '+'template_'+fitsfiles['template']['fname'])
templatehdulist = fits.open('template_'+fitsfiles['template']['fname'])
templatedata = templatehdulist[0].data
nanpixels = np.isnan(templatedata) # maybe this can be broadcast to the entire channeldata array. tbd
channelhdulist = fits.open(fitsfiles['channel']['fname'])
channeldata = channelhdulist[0].data

def currentvel(hdulistheader,currentchannel):
    vref = hdulistheader['CRVAL3']
    vdelt= hdulistheader['CDELT3']
    return (vref + (currentchannel - 1) * vdelt)/1.e3

xpanels=fitsfiles['channel']['xpanels']
ypanels=fitsfiles['channel']['ypanels']
zoomxcenter = 84.16327978
zoomycenter = -6.301987814
zoomwid = 0.4
zoomhei = 0.4

firstchannelstart=fitsfiles['channel']['start']
lastchannel=fitsfiles['channel']['end']

for startchan in range(firstchannelstart,lastchannel,ypanels*xpanels):

    channelstart=startchan # start from which channel, note the different starting index. tbd
    currentchannel=channelstart
    pdfname=fitsfiles['filename']
    
    fig=plt.figure(figsize=(3*xpanels*1.1*(zoomwid/(zoomwid+zoomhei))*10.,3*ypanels/1.1*(zoomhei/(zoomwid+zoomhei))*10.))
    mincolor = fitsfiles['channel']['mincolor']
    maxcolor = fitsfiles['channel']['maxcolor']
    for j in range(0,ypanels): # this order first follows row
        for i in range(0,xpanels):
            templatedata[0,0,:,:]=channeldata[0,currentchannel-1,:,:]
            templatedata[nanpixels] = np.nan
            templatehdulist.writeto('template_channel.fits',output_verify='exception',clobber=True,checksum=False) # use this as template to output every single channel
            subpos=[0.1+0.8/xpanels*i,0.1+0.9/ypanels*(ypanels-1-j),0.8/xpanels,0.9/ypanels]
            ff = aplpy.FITSFigure('template_channel.fits',figure=fig,subplot=subpos)
            ff.set_theme('publication')
            ff.show_colorscale(vmin=mincolor,vmax=maxcolor,cmap='gray_r',stretch='linear')
            ff.show_regions('stickrings.reg')
            ff.recenter(zoomxcenter,zoomycenter,width=zoomwid,height=zoomhei) 
            ff.tick_labels.set_yformat('dd.d')
            ff.tick_labels.set_xformat('dd.d')
            beamx = zoomxcenter + 0.8 * zoomwid / 2.
            beamy = zoomycenter + 0.8 * zoomhei / 2.
            ff.add_label(beamx,beamy,'{0:.2f}'.format(currentvel(channelhdulist[0].header,currentchannel))+'km/s',color='black',horizontalalignment='center')
            if j != ypanels-1:
                ff.hide_xaxis_label()
                ff.hide_xtick_labels()
            if i != 0:
                ff.hide_yaxis_label()
                ff.hide_ytick_labels()
            currentchannel = currentchannel + 1
            os.system('rm template_channel.fits')
    ax1 = fig.add_axes([0.9,0.1,0.01,0.9])
    cmap = mpl.cm.gray_r
    norm = mpl.colors.Normalize(vmin=mincolor, vmax=maxcolor)
#    norm = mpl.colors.PowerNorm(gamma=0.5,vmin=mincolor, vmax=maxcolor)
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

