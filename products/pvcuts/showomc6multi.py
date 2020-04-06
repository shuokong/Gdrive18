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
                     'color':{'fname':r'carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','hdulistnum':0,'title':r'$\rm Column~Density$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':1.e23,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':84,'ycenter':-6,'wid':1.5,'hei':2.4}},
           'panel2':{
                     'color':{'fname':r'Fil1641NE_hpacs_70.fits','hdulistnum':0,'title':r'$\rm 70~\mu m$','colorscale':'gist_heat','mincolor':0.0008,'maxcolor':0.05,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel3':{
                     'color':{'fname':r'Fil1641NE_hpacs_100.fits','hdulistnum':0,'title':r'$\rm 100~\mu m$','colorscale':'gist_heat','mincolor':0.0008,'maxcolor':0.035,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel4':{
                     'color':{'fname':r'Fil1641NE_feathered_160.fits','hdulistnum':0,'title':r'$\rm 160~\mu m$','colorscale':'gist_heat','mincolor':0.0007,'maxcolor':0.028,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel5':{
                     'color':{'fname':r'Fil1641NE_feathered_250.fits','hdulistnum':0,'title':r'$\rm 250~\mu m$','colorscale':'gist_heat','mincolor':0.0014,'maxcolor':0.030,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel6':{
                     'color':{'fname':r'Fil1641NE_feathered_350.fits','hdulistnum':0,'title':r'$\rm 350~\mu m$','colorscale':'gist_heat','mincolor':0.0007,'maxcolor':0.018,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel7':{
                     'color':{'fname':r'Fil1641NE_jcmt_450.fits','hdulistnum':0,'title':r'$\rm 450~\mu m$','colorscale':'gist_heat','mincolor':0,'maxcolor':0.02,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel8':{
                     'color':{'fname':r'Fil1641NE_feathered_500.fits','hdulistnum':0,'title':r'$\rm 500~\mu m$','colorscale':'gist_heat','mincolor':0.0003,'maxcolor':0.008,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           'panel9':{
                     'color':{'fname':r'Fil1641NE_jcmt_850.fits','hdulistnum':0,'title':r'$\rm 850~\mu m$','colorscale':'gist_heat','mincolor':0,'maxcolor':0.008,'pmincolor':0.5,'pmaxcolor':99.5,'bmaj':None,'bmin':None,'pa':None,'stretch':'linear','xcenter':zoomxcenter,'ycenter':zoomycenter,'wid':zoomwid,'hei':zoomhei}},
           }

lletter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

xpanels = 3
ypanels = 3
fig=plt.figure(figsize=(3*xpanels*1.1*(zoomwid/(zoomwid+zoomhei))*10.,3*ypanels/1.1*(zoomhei/(zoomwid+zoomhei))*10.))
pdfname = 'omc6multi.pdf'
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
        #ff.show_regions('lanecores.reg')
        ff.axis_labels.set_xtext(r'$\rm RA~(J2000)$')
        ff.axis_labels.set_ytext(r'$\rm Dec~(J2000)$')
        ff.tick_labels.set_xformat('dd.d')
        ff.tick_labels.set_yformat('dd.d')
        ff.ticks.set_color('white')
        ff.set_nan_color('black')
        #ff.add_colorbar() 
        #ff.colorbar.set_pad(0.5)
        #ff.colorbar.set_axis_label_text(r'$\rm cm^{-2}$')
        ### colorbar for the last panel
        if panelnum == 4:
            ff.show_regions('stick_two_parts.reg')
        if panelnum == 1:
            ff.show_rectangles(zoomxcenter,zoomycenter,zoomwid,zoomhei,edgecolor='y',linestyle='dashed',linewidth=3) 
            ff.add_scalebar(0.286,corner='bottom right',pad=3) # degree for 2 pc at 400 pc
            ff.scalebar.set_label('2 pc')
            ff.scalebar.set_color('white')
            #ax1 = fig.add_axes([0.9,0.1,0.01,0.3])
            #cmap = mpl.cm.gist_heat
            #norm = mpl.colors.Normalize(vmin=1.e21, vmax=1.e23)
            #colorticks = [0.2e23, 0.4e23, 0.6e23, 0.8e23, 1.0e23]
            #cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,norm=norm,orientation='vertical',ticks=colorticks)
            #cb1.ax.set_yticklabels(['{:<.1f}'.format(colorticks[ii]/1.e23) for ii in range(len(colorticks))]) # 
        else: 
            ff.add_scalebar(0.143,corner='bottom right') # degree for 1 pc at 400 pc
            ff.scalebar.set_label('1 pc')
            ff.scalebar.set_color('white')
        ff.add_label(xcenter + 0.9 * wid / 2.,ycenter - 0.9 * hei / 2.,fitsfiles['panel'+str(panelnum)]['color']['title'],color='white',horizontalalignment='left')
        ff.add_label(xcenter - 0.9 * wid / 2.,ycenter + 0.9 * hei / 2.,'('+lletter[panelnum-1]+')',color='white',horizontalalignment='center')
        if fitsfiles['panel'+str(panelnum)]['color']['bmaj'] is not None:
            print 'plotting beam'
            colorbeamx = xcenter - 0.8 * wid / 2.
            colorbeamy = ycenter - 0.8 * hei / 2.
            colorbmaj = fitsfiles['panel'+str(panelnum)]['color']['bmaj']
            colorbmin = fitsfiles['panel'+str(panelnum)]['color']['bmin']
            colorbeamangle = fitsfiles['panel'+str(panelnum)]['color']['pa']
            ff.show_ellipses(colorbeamx,colorbeamy,colorbmaj,colorbmin,angle=colorbeamangle-90,facecolor='black',edgecolor='black') 
#        for k in range(len(fitsfiles['panel'+str(panelnum)]['contour'].keys())):
#            ff.show_contour(fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['fname'],colors=fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['color'],levels=fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['levels'])
#            colorbeamx = xcenter + 0.8 * radius
#            colorbeamy = ycenter - 0.8 * radius
#            colorbmaj = fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['bmaj']
#            colorbmin = fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['bmin']
#            colorbeamangle = fitsfiles['panel'+str(panelnum)]['contour']['file'+str(k+1)]['pa']
#            ff.show_ellipses(colorbeamx,colorbeamy,colorbmaj,colorbmin,angle=colorbeamangle-90,facecolor='grey',edgecolor='grey') 
        if j != ypanels-1:
            ff.hide_xaxis_label()
            ff.hide_xtick_labels()
        if i != 0:
            ff.hide_yaxis_label()
            ff.hide_ytick_labels()

os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesSFE'))



