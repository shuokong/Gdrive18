import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import rc
from astropy.io import fits
rc('text', usetex=True)
font = {'weight' : 'normal','size':16,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

lletter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

xpanelwidth = 7
ypanelwidth = 7

hists = {
# 'panel1':{
#    'title':r'$T$','xlabel':r'$F_{250}~\rm (MJy~sr^{-1})$','ylabel':r'','xmin':10.,'xmax':1000.,'ymin':0.001,'ymax':0.5,'xscale':'log','yscale':'log','loc':1,
#    'hist1':{
#       'file':fits.open('../Fil1641NE_feathered_250.fits')[0].data*4.25e4, # convert from Jy/arcsec2 to MJy/sr
#       'mask':fits.open('bool_Fil1641NE_feathered_250.fits')[0].data.astype('bool'),
#     'legend':r'${\rm Herschel}$','linestyle':'r-', 
#             },
#    'hist2':{
#       'file':fits.open('simc2s0p5_-30ccut_i250_noisy.fits')[0].data,
#       'mask':fits.open('bool_simc2s0p5_-30ccut_i250_noisy.fits')[0].data.astype('bool'),
#     'legend':r'$\rm MRCOL$','linestyle':'k-', 
#             },
#    'hist3':{
#       'file':fits.open('simc2rho0p7_-50ccut_i250_noisy.fits')[0].data,
#       'mask':fits.open('bool_simc2rho0p7_-50ccut_i250_noisy.fits')[0].data.astype('bool'),
#     'legend':r'$\rm MRCOL_{\rho_0=0.7}$','linestyle':'b-', 
#             },
#           },
 'panel1':{
    'title':r'$T$','xlabel':r'$F_{850}~\rm (MJy~sr^{-1})$','ylabel':r'','xmin':0.01,'xmax':100.,'ymin':0.001,'ymax':0.5,'xscale':'log','yscale':'log','loc':3,
    'hist1':{
       'file':fits.open('../Fil1641NE_jcmt_850.fits')[0].data*4.25e4/9.,
       'mask':fits.open('bool_Fil1641NE_jcmt_850.fits')[0].data.astype('bool'),
     'legend':r'${\rm JCMT}$','linestyle':'g-', 
             },
    'hist2':{
       'file':fits.open('simc2s0p5_-30ccut_i850_noisy.fits')[0].data,
       'mask':fits.open('bool_simc2s0p5_-30ccut_i850_noisy.fits')[0].data.astype('bool'),
     'legend':r'$\rm MRCOL$','linestyle':'k-', 
             },
    'hist3':{
       'file':fits.open('simc2rho0p7_-50ccut_i850_noisy.fits')[0].data,
       'mask':fits.open('bool_simc2rho0p7_-50ccut_i850_noisy.fits')[0].data.astype('bool'),
     'legend':r'$\rm MRCOL_{\rho_0=0.7}$','linestyle':'b-', 
             },
           },
 'panel2':{
    'title':r'$T$','xlabel':r'$N_H~\rm (\times10^{21}~cm^{-2})$','ylabel':r'','xmin':0.4,'xmax':100.,'ymin':0.001,'ymax':0.5,'xscale':'log','yscale':'log','loc':1,
    'hist1':{
       'file':fits.open('../carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')[0].data/1.e21,
       'mask':fits.open('bool_stickbody_nh.fits')[0].data.astype('bool'),
     'legend':r'${\rm Herschel}$','linestyle':'r-', 
             },
    'hist2':{
       'file':fits.open('simc2s0p5_-30ccut_nh.fits')[0].data/1.e21,
       'mask':fits.open('bool_simc2s0p5_-30ccut_nh.fits')[0].data.astype('bool'),
     'legend':r'$\rm MRCOL$','linestyle':'k-', 
             },
    'hist3':{
       'file':fits.open('simc2rho0p7_-50ccut_nh.fits')[0].data/1.e21,
       'mask':fits.open('bool_simc2s0p5_-30ccut_nh.fits')[0].data.astype('bool'),
     'legend':r'$\rm MRCOL_{\rho_0=0.7}$','linestyle':'b-', 
             },
    'hist4':{
       'file':fits.open('../Fil1641NE_jcmt_850.fits')[0].data*4.25e4/9./8.56256e-1,
       'mask':fits.open('bool_Fil1641NE_jcmt_850.fits')[0].data.astype('bool'),
     'legend':r'$\rm JCMT,850$','linestyle':'g-', 
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
        binl = int(np.log10(xmin)/0.1)*0.1+0.05
        xmax = hists['panel'+str(panel)]['xmax'] 
        binr = int(np.log10(xmax)/0.1)*0.1-0.05
        binn = int((binr-binl)/0.1)+1 
        ymin = hists['panel'+str(panel)]['ymin']
        ymax = hists['panel'+str(panel)]['ymax'] 
        xscale = hists['panel'+str(panel)]['xscale'] 
        yscale = hists['panel'+str(panel)]['yscale']
        datafiles['panel'+str(panel)] = {'title':hists['panel'+str(panel)]['title'],'lines':{},'xlim':[xmin,xmax],'ylim':[ymin,ymax],'xscale':xscale,'yscale':yscale,'xlabel':hists['panel'+str(panel)]['xlabel'],'ylabel':hists['panel'+str(panel)]['ylabel'],'text':'','vertlines':[],'loc':hists['panel'+str(panel)]['loc']}
        linenum = 1 
        for hh in hists['panel'+str(panel)].iterkeys():
            if hh.startswith('hist'): 
                print hh 
                hdu1data = hists['panel'+str(panel)][hh]['file']
                maskdata = hists['panel'+str(panel)][hh]['mask']
                sample = hdu1data[maskdata]
                print 'len(sample)',len(sample)
                print 'min max sample',min(sample),max(sample)
                bins = np.logspace(binl, binr, num=binn) # evenly distributed in log10 space
                binsizes = [np.log10(bins[ind]) - np.log10(bins[ind-1]) for ind in range(1,len(bins))]
                bincenters = [(bins[ind]*bins[ind-1])**0.5 for ind in range(1,len(bins))]
                hist = np.histogram(sample, bins=bins, density=True)
                corecounts = hist[0]
                print bincenters,hist 
                datafiles['panel'+str(panel)]['lines'][str(linenum)] = {'x':bincenters,'y':corecounts,'peaksnr':[],'legends':hists['panel'+str(panel)][hh]['legend'],'linestyles':hists['panel'+str(panel)][hh]['linestyle'],'drawsty':'steps-mid'}
                linenum += 1 

fig=plt.figure(figsize=(xpanelwidth*xpanels*1.1,ypanelwidth*ypanels/1.1))
plt.subplots_adjust(wspace=0.15,hspace=0.01)
pdfname='nhhist.pdf'
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
        lloc = datafiles['panel'+str(panelnum)]['loc']
        ax.legend(frameon=False,labelspacing=0.1,loc=lloc) 
        #if j == 0:
        #    ax.set_title(datafiles['panel'+str(panelnum)]['title'])
        #ax.text(0.05, 0.9,datafiles['panel'+str(panelnum)]['title'],horizontalalignment='left',verticalalignment='center',transform = ax.transAxes)
        #    if i == 1: 
        #        ax.text(0.9, -0.15,r'$\times10^{-8}$',horizontalalignment='left',verticalalignment='center',transform = ax.transAxes)
        #ax.text(0.1, 0.9,'('+lletter[panelnum-1]+')',horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
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
        #if i != 0:
        #    ax.set_yticklabels(ax.get_ylabel(),visible=False) 
        #    ax.set_xticks(ax.get_xticks()[1:]) 
        #else: 
        #    ax.set_ylabel(ylabel)
        #minor_locator = AutoMinorLocator(5)
        #ax.xaxis.set_minor_locator(minor_locator)
        #ax.tick_params(axis='both',direction='in',length=5,which='major',top=True,right=True)
        #ax.tick_params(axis='both',direction='in',length=2,which='minor',top=True,right=True)
        
os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
plt.close(fig)
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' ~/GoogleDrive/imagesSFE/'))

