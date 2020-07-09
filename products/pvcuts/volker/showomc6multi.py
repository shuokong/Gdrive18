import aplpy
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from astropy.io import fits
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':50,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

zoomxcenter = 0.1880632
zoomycenter = 0.1880632
zoomwid = 0.377
zoomhei = 0.377

fitsfiles={
            'title':r'$\rm MRCOL,\alpha=-30^\circ,FIR$',
              'pdf':r'simc2s0p5_-30',
#           'panel1':{
#                     'color':{'fname':r'simc2s0p5_-30ccut_i250_noisy.fits','hdulistnum':0,'title':r'$\rm F_{250}$','colorscale':'gist_heat','mincolor':0,'maxcolor':300,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel1':{
                     'color':{'fname':r'simc2s0p5_-30ccut_i850_noisy.fits','hdulistnum':0,'title':r'$\rm F_{850}$','colorscale':'gist_heat','mincolor':0,'maxcolor':20,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel2':{
                     'color':{'fname':r'simc2s0p5_-30ccut_nh.fits','hdulistnum':0,'title':r'$N_H$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':3.e22,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           }

fitsfiles={
            'title':r'$\rm MRCOL_{\rm \rho_0=0.7},\alpha=-50^\circ,FIR$',
              'pdf':r'simc2rho0p7_-50',
#           'panel1':{
#                     'color':{'fname':r'simc2rho0p7_-50ccut_i250_noisy.fits','hdulistnum':0,'title':r'$\rm F_{250}$','colorscale':'gist_heat','mincolor':0,'maxcolor':400,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel1':{
                     'color':{'fname':r'simc2rho0p7_-50ccut_i850_noisy.fits','hdulistnum':0,'title':r'$\rm F_{850}$','colorscale':'gist_heat','mincolor':0,'maxcolor':30,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel2':{
                     'color':{'fname':r'simc2rho0p7_-50ccut_nh.fits','hdulistnum':0,'title':r'$N_H$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':6.e22,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           }


lletter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

xpanels = 2
ypanels = 1
fig=plt.figure(figsize=(3*xpanels*5.*1.13,3*ypanels*5.),frameon=False)
pdfname = fitsfiles['pdf']+'ccut_multi.pdf'
for j in range(0,ypanels):
    for i in range(0,xpanels):
        panelnum = i + 1 + j * xpanels
        subpos=[0.1+0.8/xpanels*i,0.1+0.9/ypanels*(ypanels-1-j),0.8/xpanels/1.01,0.9/ypanels/1.01]
        print 'opening file',fitsfiles['panel'+str(panelnum)]['color']['fname']
        prihdu1 = fits.open(fitsfiles['panel'+str(panelnum)]['color']['fname'])[fitsfiles['panel'+str(panelnum)]['color']['hdulistnum']] 
        datamean = np.nanmean(prihdu1.data)
        ff = aplpy.FITSFigure(prihdu1,figure=fig,subplot=subpos,frameon=False)
        xcenter = fitsfiles['panel'+str(panelnum)]['color']['xcenter']
        ycenter = fitsfiles['panel'+str(panelnum)]['color']['ycenter']
        wid = fitsfiles['panel'+str(panelnum)]['color']['wid']
        hei = fitsfiles['panel'+str(panelnum)]['color']['hei']
        #ff.recenter(xcenter,ycenter,width=wid,height=hei) 
        #ff.set_theme('publication')
        #ff.set_system_latex(True)
        if fitsfiles['panel'+str(panelnum)]['color']['mincolor'] == None:
            print 'setting color range to user input pmin pmax'
            pmincolor = fitsfiles['panel'+str(panelnum)]['color']['pmincolor']
            pmaxcolor = fitsfiles['panel'+str(panelnum)]['color']['pmaxcolor']
            ff.show_colorscale(cmap=fitsfiles['panel'+str(panelnum)]['color']['colorscale'], vmin=pmincolor/100.*datamean, vmax=pmaxcolor/100.*datamean, stretch=fitsfiles['panel'+str(panelnum)]['color']['stretch'])
        else:
            print 'setting color range to user input min max'
            mincolor = fitsfiles['panel'+str(panelnum)]['color']['mincolor']
            maxcolor = fitsfiles['panel'+str(panelnum)]['color']['maxcolor']
            ff.show_colorscale(cmap=fitsfiles['panel'+str(panelnum)]['color']['colorscale'], vmin=mincolor, vmax=maxcolor, stretch=fitsfiles['panel'+str(panelnum)]['color']['stretch'])
        #ff.show_regions('lanecores.reg')
        if panelnum == 4:
            ff.show_regions('stick_two_parts.reg')
        #if panelnum == 1:
        #    ff.add_scalebar(0.143,corner='bottom') # degree for 1 pc at 400 pc
        #    ff.scalebar.set_label('1 pc')
        #    ff.scalebar.set_color('white')
        ff.add_label(0.1,0.9,fitsfiles['panel'+str(panelnum)]['color']['title'],relative=True,color='white')
        ff.set_tick_color('black') 
        ff.hide_xaxis_label()
        ff.hide_xtick_labels()
        ff.hide_yaxis_label()
        ff.hide_ytick_labels()
plt.axis('off')
fig.suptitle(fitsfiles['title'],y=1.05)

os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesSFE'))



