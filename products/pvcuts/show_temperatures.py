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

zoomxcenter = 84.16327978
zoomycenter = -6.301987814
zoomwid = 0.4
zoomhei = 0.4
fitsfiles={
   'panel1':{
      'color':{'fname':r'../tex_on_stick_header.fits','hdulistnum':0,'title':r'${\rm ^{12}CO}~T_{\rm ex}]$','colorscale':'gray','mincolor':10,'maxcolor':60,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei},
    'contour':{
        'file1':{'fname':r'carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','beamcolor':'red','color':'red','levels':1.e22*np.array([1.4,2.8,4.2]),'bmaj':None,'bmin':None,'pa':None},
               },
             },
   'panel2':{
      'color':{'fname':r'../dustT_on_stick_header.fits','hdulistnum':0,'title':r'${\rm Herschel}~T_d]$','colorscale':'gray','mincolor':10,'maxcolor':60,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei},
    'contour':{
        'file1':{'fname':r'carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','beamcolor':'red','color':'red','levels':1.e22*np.array([1.4,2.8,4.2]),'bmaj':None,'bmin':None,'pa':None},
               },
             },
           }

lletter = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

xpanels = 2
ypanels = 1
fig=plt.figure(figsize=(3*xpanels*1.1*(zoomwid/(zoomwid+zoomhei))*10.,3*ypanels/1.1*(zoomhei/(zoomwid+zoomhei))*10.))
pdfname = 'temperatures.pdf'
for j in range(0,ypanels):
    for i in range(0,xpanels):
        panelnum = i + 1 + j * xpanels
        subpos=[0.1+0.8/xpanels*i,0.1+0.9/ypanels*(ypanels-1-j),0.8/xpanels/1.01,0.9/ypanels/1.01]
        print 'opening file',fitsfiles['panel'+str(panelnum)]['color']['fname']
        prihdu1 = fits.open(fitsfiles['panel'+str(panelnum)]['color']['fname'])[fitsfiles['panel'+str(panelnum)]['color']['hdulistnum']] 
        datamean = np.nanmean(prihdu1.data)
        ff = aplpy.FITSFigure(prihdu1,figure=fig,subplot=subpos)
        xcenter = fitsfiles['panel'+str(panelnum)]['color']['xcenter']
        ycenter = fitsfiles['panel'+str(panelnum)]['color']['ycenter']
        wid = fitsfiles['panel'+str(panelnum)]['color']['wid']
        hei = fitsfiles['panel'+str(panelnum)]['color']['hei']
        ff.recenter(xcenter,ycenter,width=wid,height=hei) 
        ff.set_theme('publication')
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
        ff.axis_labels.set_xtext(r'$\rm RA~(J2000)$')
        ff.axis_labels.set_ytext(r'$\rm Dec~(J2000)$')
        ff.tick_labels.set_xformat('dd.d')
        ff.tick_labels.set_yformat('dd.d')
        ff.ticks.set_color('black')
        ff.set_nan_color('white')
        #ff.add_colorbar() 
        #ff.colorbar.set_pad(0.5)
        #ff.colorbar.set_axis_label_text(r'$\rm cm^{-2}$')
        ### colorbar for the last panel
        if panelnum == 1:
            ff.show_regions('stick_two_parts.reg')
        else: 
            ff.show_regions('stick_two_parts.reg')
            ff.show_regions('lanecores_aroundstick_noname.reg')
        if panelnum == xpanels*ypanels:
#            ff.show_rectangles(zoomxcenter,zoomycenter,zoomwid,zoomhei,edgecolor='y',linestyle='dashed',linewidth=3) 
            ff.add_scalebar(0.143,corner='bottom left',pad=0) # degree for 1 pc at 400 pc
            ff.scalebar.set_label('1 pc')
            ff.scalebar.set_color('black')
            ax1 = fig.add_axes([0.9,0.1,0.01,0.89])
            cmap = mpl.cm.gray
            #norm = mpl.colors.Normalize(vmin=10, vmax=60)
            #norm = mpl.colors.LogNorm(vmin=10, vmax=60)
            norm = mpl.colors.PowerNorm(gamma=0.5, vmin=10, vmax=60)
            colorticks = np.array([10,20,30,40,50,60])
            cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,norm=norm,orientation='vertical',ticks=colorticks)
            cb1.ax.set_yticklabels([r'$\rm '+'{:<d}'.format(colorticks[ii])+r'$' for ii in range(len(colorticks))]) # 
            cb1.ax.tick_params(axis='y', direction='out') # 
            #cb1.set_label(r'$\rm K~km~s^{-1}$') 
        else: 
            ff.add_scalebar(0.143,corner='bottom left') # degree for 1 pc at 400 pc
            ff.scalebar.set_label('1 pc')
            ff.scalebar.set_color('black')
#        ff.set_title(fitsfiles['panel'+str(panelnum)]['color']['title'])
        ff.add_label(xcenter + 0.9 * wid / 2.,ycenter + 0.9 * hei / 2.,'('+lletter[panelnum-1]+')',color='black',horizontalalignment='center')
        if fitsfiles['panel'+str(panelnum)]['color']['bmaj'] is not None:
            print 'plotting beam'
            colorbeamx = xcenter + 0.8 * wid / 2.
            colorbeamy = ycenter - 0.8 * hei / 2.
            colorbmaj = fitsfiles['panel'+str(panelnum)]['color']['bmaj'] / 3600.
            colorbmin = fitsfiles['panel'+str(panelnum)]['color']['bmin'] / 3600.
            colorbeamangle = fitsfiles['panel'+str(panelnum)]['color']['pa']
            ff.show_ellipses(colorbeamx,colorbeamy,colorbmaj,colorbmin,angle=colorbeamangle-90,facecolor='black',edgecolor='black') 
        if 'contour' in fitsfiles['panel'+str(panelnum)].keys():
            for k in range(len(fitsfiles['panel'+str(panelnum)]['contour'].keys())):
                ff.show_contour(fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['fname'],colors=fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['color'],levels=fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['levels'])
                if fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['bmaj'] is not None:
                    colorbeamx = xcenter + 0.8 * wid / 2.
                    colorbeamy = ycenter - 0.8 * hei / 2.
                    colorbmaj = fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['bmaj'] / 3600.
                    colorbmin = fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['bmin'] / 3600.
                    colorbeamangle = fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['pa']
                    ff.show_ellipses(colorbeamx,colorbeamy,colorbmaj,colorbmin,angle=colorbeamangle-90,facecolor='grey',edgecolor='grey') 
        if j != ypanels: #-1:
            ff.hide_xaxis_label()
            ff.hide_xtick_labels()
        if i != 0:
            ff.hide_yaxis_label()
            ff.hide_ytick_labels()

os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesSFE'))



