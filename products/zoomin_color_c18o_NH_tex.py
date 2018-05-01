import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':22,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)
#from tex import tex
from scipy import stats
import math
import pyfits

rms=0.16
lowrms=3
highrms=5
lowav=0
highav=200*2.*9.4e20
avthres=7.5
lowi=0
highi=20
standardwav=3.3

print 'reading fits files'
hdulist1=pyfits.open('../../12co/products/regrid_Stutz_convol18_tex12.fits') #for Tex
hdulist2=pyfits.open('regrid_Stutz_convol18_mom0_c18o_pix_2_Tmb.fits') #for mom0
hdulist3=pyfits.open('carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits') #for newNICEST38.fits or newNICER38.fits

scidata1=hdulist1[0].data
scidata2=hdulist2[0].data
scidata3=hdulist3[0].data

print 'scidata1.shape', scidata1.shape
print 'scidata2.shape', scidata2.shape
print 'scidata3.shape', scidata3.shape

tex=scidata1[:,:]
mom0=scidata2[0,:,:]
new38=scidata3[:,:]#/9.4e20/2.

xy=np.loadtxt('boxes.txt',dtype='int',delimiter=',') #for boxes.txt
x1=xy[:,0]
y1=xy[:,1]
x2=xy[:,2]
y2=xy[:,3]


count=0
newtex=[]
for i in range(0,len(tex[:,0])):
	for j in range(0,len(tex[0,:])):
		if math.isnan(tex[i,j]) == False and math.isnan(mom0[i,j]) == False and math.isnan(new38[i,j]) == False and mom0[i,j] > 0 and tex[i,j] > 0 and new38[i,j] > 0:
			newtex.append(tex[i,j])
maxte=max(newtex)
minte=min(newtex)
print minte,maxte

merge3av=[]
merge3in=[]
merge3te=[]
count=0
for k in [0]:
	count=count+1
	for i in range(y1[k],y2[k]+1):
		for j in range(x1[k],x2[k]+1):
			if math.isnan(tex[i,j]) == False and math.isnan(mom0[i,j]) == False and math.isnan(new38[i,j]) == False and mom0[i,j] > 0 and tex[i,j] > 0 and new38[i,j] > 0:
				merge3av.append(new38[i,j])
				merge3in.append(mom0[i,j])
				merge3te.append(tex[i,j])
	merge3av.append(lowav-10.)
	merge3in.append(0.)
	merge3te.append(minte)
	merge3av.append(lowav-10.)
	merge3in.append(0.)
	merge3te.append(maxte)

merge3avv=np.array(merge3av)
merge3inn=np.array(merge3in)
merge3tee=np.array(merge3te)
standard38=np.array([lowav,highav])
standardw=standard38*standardwav

p=plt.figure(figsize=(8,6))
plt.subplots_adjust(top=0.87,bottom=0.13,left=0.18,right=0.85)

ax=p.add_subplot(1,1,1)
plt.xscale('linear')
plt.yscale('linear')
plt.scatter(merge3avv,merge3inn,s=5,c=merge3tee,marker="o",edgecolors='none',rasterized=True)
plt.xlim(lowav,highav)
plt.ylim(lowi,highi)
### linear fit
#linarray=(merge3avv[:]<highav) & (merge3avv[:]>lowav+2) & (merge3inn>rms*lowrms)
#linresul=stats.linregress(merge3avv[linarray[:]],merge3inn[linarray[:]])
#plt.plot(merge3avv[linarray[:]],linresul[0]*merge3avv[linarray[:]]+linresul[1],'k-',label='fitted slope: '+str("{0:.1f}".format(linresul[0]))+', r-value: '+str("{0:.2f}".format(linresul[2])),rasterized=True)
##
#plt.plot(standard38,standardw,'r-')
plt.text(0.05, 0.95,'(b)',horizontalalignment='left',verticalalignment='top',transform = ax.transAxes)
#plt.legend(loc=1,frameon=False,prop={'size':16})
#plt.tick_params(axis='both', which='major', labelsize=28)
box = ax.get_position()
ax.set_position([box.x0*1., box.y0, box.width, box.height])
axColor = plt.axes([box.x0*1.005 + box.width * 1.005, box.y0, 0.015, box.height])
cbar=plt.colorbar(cax = axColor, orientation="vertical")
cbar.ax.get_yaxis().labelpad = 20
cbar.set_label(r'$\rm T_{ex}~(K)$', rotation=270)
ax.set_xlabel(r'$\rm N_H~(cm^{-2})$')
ax.set_ylabel(r'$\rm W_{C^{18}O(1-0)}~(K~km~s^{-1})$')
#plt.tick_params(axis='both', which='major', labelsize=28)
ax2=ax.twiny()
axXs = ax.get_xticks()
ax2Xs = []
for X in axXs:
    ax2Xs.append(r"$\rm {0:.1f}$".format(X/2./9.4e20))
ax2.set_xticks(axXs)
ax2.set_xbound(ax.get_xbound())
ax2.set_xticklabels(ax2Xs)
ax2.set_xlabel(r'$\rm A_V~(mag)$')

os.system('rm zoomin_color_c18o_NH_tex.pdf')
plt.savefig('zoomin_color_c18o_NH_tex.pdf',dpi=400)
os.system('open zoomin_color_c18o_NH_tex.pdf')
os.system('cp zoomin_color_c18o_NH_tex.pdf ~/GoogleDrive/imagesSFE/')
#plt.show()


hdulist1.close()
hdulist2.close()
hdulist3.close()
