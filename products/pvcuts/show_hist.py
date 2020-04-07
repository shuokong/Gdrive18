import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import rc
from astropy.io import fits
rc('text', usetex=True)
font = {'weight' : 'normal','size':30,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

lletter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

xpanelwidth = 7
ypanelwidth = 7

thist = 1

if thist == 1:
    hists = {
     'panel1':{
        'title':r'$T$','xlabel':r'$T~\rm (K)$','ylabel':r'$\rm density$','xmin':10,'xmax':70,'ymin':0,'ymax':0.5,'xscale':'linear','yscale':'linear',
        'hist1':{
           'file':fits.open('../tex_on_stick_header.fits')[0].data[0,:,:],
           'mask':fits.open('bool_stickbody.fits')[0].data.astype('bool'),
         'legend':r'${\rm ^{12}CO}~T_{\rm ex}$','linestyle':'k-', 
                 },
        'hist2':{
           'file':fits.open('../threeaxes_dustT_on_stick_header.fits')[0].data[0,:,:],
           'mask':fits.open('bool_stickbody.fits')[0].data.astype('bool'),
         'legend':r'$\rm T_{\rm dust}$','linestyle':'r-', 
                 },
        'hist3':{
           'file':fits.open('../threeaxes_gasT_on_stick_header.fits')[0].data[0,:,:],
           'mask':fits.open('bool_stickbody.fits')[0].data.astype('bool'),
         'legend':r'$\rm T_{\rm kin}$','linestyle':'b-', 
                 },
               },
     'panel2':{
        'title':r'$\rm Abundance$','xlabel':r'$\rm [C^{18}O/H]$','ylabel':r'$\rm density$','xmin':1,'xmax':100,'ymin':0,'ymax':0.5,'xscale':'linear','yscale':'linear',
        'hist1':{
           'file':fits.open('../abun18tex.fits')[0].data[0,:,:]*1e8,
           'mask':fits.open('bool_stickbody.fits')[0].data.astype('bool'),
         'legend':r'${\rm ^{12}CO}~T_{\rm ex}$','linestyle':'k-', 
                 },
        'hist2':{
           'file':fits.open('../abun18tdust.fits')[0].data[0,:,:]*1e8,
           'mask':fits.open('bool_stickbody.fits')[0].data.astype('bool'),
         'legend':r'$\rm T_{\rm dust}$','linestyle':'r-', 
                 },
        'hist3':{
           'file':fits.open('../abun18tkin.fits')[0].data[0,:,:]*1e8,
           'mask':fits.open('bool_stickbody.fits')[0].data.astype('bool'),
         'legend':r'$\rm T_{\rm kin}$','linestyle':'b-', 
                 },
               },
             }
    xpanels = 2
    ypanels = 1
    datafiles = {}
    for i in range(0,xpanels):
        for j in range(0,ypanels): # 
            panel = i+j*xpanels+1
            print 'panel',panel 
            print hists['panel'+str(panel)]['title']
            xmin = hists['panel'+str(panel)]['xmin']
            xmax = hists['panel'+str(panel)]['xmax'] 
            ymin = hists['panel'+str(panel)]['ymin']
            ymax = hists['panel'+str(panel)]['ymax'] 
            xscale = hists['panel'+str(panel)]['xscale'] 
            yscale = hists['panel'+str(panel)]['yscale']
            datafiles['panel'+str(panel)] = {'title':hists['panel'+str(panel)]['title'],'lines':{},'xlim':[xmin,xmax],'ylim':[ymin,ymax],'xscale':xscale,'yscale':yscale,'xlabel':hists['panel'+str(panel)]['xlabel'],'ylabel':hists['panel'+str(panel)]['ylabel'],'text':'','vertlines':[]}
            linenum = 1 
            for hh in hists['panel'+str(panel)].iterkeys():
                if hh.startswith('hist'): 
                    print hh 
                    hdu1data = hists['panel'+str(panel)][hh]['file']
                    maskdata = hists['panel'+str(panel)][hh]['mask']
                    sample = hdu1data[maskdata]
                    print 'len(sample)',len(sample)
                    print 'min max sample',min(sample),max(sample)
                    hist, bin_edges = np.histogram(sample,bins=40,range=(xmin,xmax),density=True)
                    bincenter = (bin_edges[:-1] + bin_edges[1:]) / 2.
                    datafiles['panel'+str(panel)]['lines'][str(linenum)] = {'x':bincenter,'y':hist,'peaksnr':[],'legends':hists['panel'+str(panel)][hh]['legend'],'linestyles':hists['panel'+str(panel)][hh]['linestyle'],'drawsty':'steps-mid'}
                    linenum += 1 
    
    fig=plt.figure(figsize=(xpanelwidth*xpanels*1.1,ypanelwidth*ypanels/1.1))
    plt.subplots_adjust(wspace=0.05,hspace=0.01)
    pdfname='thist.pdf'
    for i in range(0,xpanels):
        for j in range(0,ypanels):
            panelnum = i+j*xpanels+1
            ax = fig.add_subplot(ypanels,xpanels,panelnum)
            if 'panel'+str(panelnum) not in datafiles.keys(): continue
            ax.set_xscale(datafiles['panel'+str(panelnum)]['xscale']) 
            ax.set_yscale(datafiles['panel'+str(panelnum)]['yscale']) 
            if datafiles['panel'+str(panelnum)]['ylim']:
                ydown = datafiles['panel'+str(panelnum)]['ylim'][0]
                yup   = datafiles['panel'+str(panelnum)]['ylim'][1]
                ax.set_ylim(ydown,yup)
            if datafiles['panel'+str(panelnum)]['xlim']:
                xmin,xmax = datafiles['panel'+str(panelnum)]['xlim']
                ax.set_xlim(xmin,xmax)
                #ax.hlines(0,xmin,xmax,linestyle='dotted')
            for datafilenum in range(len(datafiles['panel'+str(panelnum)]['lines'].keys())): 
                x = datafiles['panel'+str(panelnum)]['lines'][str(datafilenum+1)]['x']
                y = datafiles['panel'+str(panelnum)]['lines'][str(datafilenum+1)]['y']
                #ax.hist(x,bins='auto',range=(xmin,xmax))
                linestyle = datafiles['panel'+str(panelnum)]['lines'][str(datafilenum+1)]['linestyles']
                legend = datafiles['panel'+str(panelnum)]['lines'][str(datafilenum+1)]['legends']
                drawsty = datafiles['panel'+str(panelnum)]['lines'][str(datafilenum+1)]['drawsty']
                ax.plot(x,y,linestyle,label=legend,drawstyle=drawsty)
                #ax.text(peakvelocity+0.8, yup*0.9, '%.1f' % peakvelocity + ',' + '%.1f' % peaksnr,horizontalalignment='left',verticalalignment='center')
            ax.legend(frameon=False,labelspacing=0.2) 
            if j == 0:
                ax.set_title(datafiles['panel'+str(panelnum)]['title'])
            #ax.text(0.05, 0.9,datafiles['panel'+str(panelnum)]['title'],horizontalalignment='left',verticalalignment='center',transform = ax.transAxes)
                if i == 1: 
                    ax.text(0.9, -0.15,r'$\times10^{-8}$',horizontalalignment='left',verticalalignment='center',transform = ax.transAxes)
            ax.text(0.1, 0.9,'('+lletter[panelnum-1]+')',horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
            xlabel = datafiles['panel'+str(panelnum)]['xlabel']
            ylabel = datafiles['panel'+str(panelnum)]['ylabel']
            vertlinex = datafiles['panel'+str(panelnum)]['vertlines']
            for vl in vertlinex:
                ax.vlines(vl,ydown,yup*0.7,linestyles='dotted',colors='k')
            if j != ypanels-1:
                ax.set_yticks(ax.get_yticks()[1:])
                ax.set_xticklabels(ax.get_xlabel(),visible=False)
            else: 
                ax.set_xlabel(xlabel)
            if i != 0:
                ax.set_yticklabels(ax.get_ylabel(),visible=False) 
                ax.set_xticks(ax.get_xticks()[1:]) 
            else: 
                ax.set_ylabel(ylabel)
            minor_locator = AutoMinorLocator(5)
            ax.xaxis.set_minor_locator(minor_locator)
            ax.tick_params(axis='both',direction='in',length=5,which='major',top=True,right=True)
            ax.tick_params(axis='both',direction='in',length=2,which='minor',top=True,right=True)
            
    os.system('rm '+pdfname)
    plt.savefig(pdfname,bbox_inches='tight')
    plt.close(fig)
    os.system('open '+pdfname)
    os.system('cp '+pdfname+os.path.expandvars(' ~/GoogleDrive/imagesSFE/'))

