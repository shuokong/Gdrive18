import aplpy
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':20,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

fitsfiles={'panel1':{
                     'color':{'fname':'../../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','title':r'$\rm Column~Density$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':1.e23,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt',}},
           'panel2':{
                     'color':{'fname':'../../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','title':r'$\rm Column~Density$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':1.e23,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt',}},
           'panel3':{
                     'color':{'fname':'../../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','title':r'$\rm Column~Density$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':1.e23,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt',}},
           'panel4':{
                     'color':{'fname':'../../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','title':r'$\rm Column~Density$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':1.e23,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt',}},
           'panel5':{
                     'color':{'fname':'../../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','title':r'$\rm Column~Density$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':1.e23,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt',}},
           'panel6':{
                     'color':{'fname':'../../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','title':r'$\rm Column~Density$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':1.e23,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt',}},
           'panel7':{
                     'color':{'fname':'../../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','title':r'$\rm Column~Density$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':1.e23,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt',}},
           'panel8':{
                     'color':{'fname':'../../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits','title':r'$\rm Column~Density$','colorscale':'gist_heat','mincolor':1.e21,'maxcolor':1.e23,'bmaj':None,'bmin':None,'pa':None,'stretch':'sqrt',}}
           }

lletter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

xcenter = 84.11926799
ycenter = -6.302519164
wid = 0.5391003
hei = 0.4449478
xpanels = 2
ypanels = 4
fig=plt.figure(figsize=(3*xpanels*1.1*(wid/(wid+hei))*10.,3*ypanels/1.1*(hei/(wid+hei))*10.))
pdfname = 'omc6multi.pdf'
for j in range(0,ypanels):
    for i in range(0,xpanels):
        panelnum = i + 1 + j * xpanels
        subpos=[0.1+0.8/xpanels*i,0.1+0.9/ypanels*(ypanels-1-j),0.8/xpanels/1.01,0.9/ypanels/1.01]
        prihdu1 = fits.open(fitsfiles['panel'+str(panelnum)]['color']['fname'])[0] 
        ff = aplpy.FITSFigure(prihdu1,figure=fig,subplot=subpos)
        ff.recenter(xcenter,ycenter,width=wid,height=hei) 
        ff.set_theme('publication')
        #ff.set_system_latex(True)
        if fitsfiles['panel'+str(panelnum)]['color']['mincolor'] == None:
            print 'setting color range to data min max'
            mincolor = np.nanmin(prihdu1.data)
            maxcolor = np.nanmax(prihdu1.data)
        else:
            print 'setting color range to user input min max'
            mincolor = fitsfiles['panel'+str(panelnum)]['color']['mincolor']
            maxcolor = fitsfiles['panel'+str(panelnum)]['color']['maxcolor']
        ff.show_colorscale(cmap=fitsfiles['panel'+str(panelnum)]['color']['colorscale'], vmin=mincolor, vmax=maxcolor, stretch=fitsfiles['panel'+str(panelnum)]['color']['stretch'])
        ff.show_regions('zoombox.reg')
        #ff.show_regions('lanecores.reg')
        ff.axis_labels.set_xtext(r'$\rm RA~(J2000)$')
        ff.axis_labels.set_ytext(r'$\rm Dec~(J2000)$')
        ff.tick_labels.set_xformat('dd.d')
        ff.tick_labels.set_yformat('dd.d')
        ff.ticks.set_color('white')
        #ff.add_colorbar() 
        #ff.colorbar.set_pad(0.5)
        #ff.colorbar.set_axis_label_text(r'$\rm cm^{-2}$')
        ff.add_scalebar(0.143,corner='top left',pad=1) # degree for 1 pc at 400 pc
        ff.scalebar.set_label('1 pc')
        ff.scalebar.set_color('white')
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
#            if i == xpanels-1:
#                ax1 = fig.add_axes([0.9,0.9*1.1-(j+1)*(0.8*1.1/ypanels),0.01,0.8*1.1/ypanels*0.99])
#                cmap = mpl.cm.rainbow
#                norm = mpl.colors.Normalize(vmin=mincolor, vmax=maxcolor)
#                cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,norm=norm,orientation='vertical',ticks=colorticks)
#                cb1.ax.set_yticklabels(['{:<.3f}'.format(colorticks[ii]*2./427.) for ii in range(len(colorticks))]) # N_H = Av * 2.0e21 cm-2, 1g cm-2 corresponds to N_H = 4.27e23 cm-2
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



