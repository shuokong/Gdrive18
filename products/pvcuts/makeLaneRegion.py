import numpy as np

corenames, xw, yw, peak850, flux850, cmaj, cmin, cpa = np.loadtxt('/Users/shuokong/GoogleDrive/OrionAdust/Lane2016/Getsources_cores_degree.txt',usecols=(0,1,2,3,4,5,6,7),unpack=True,dtype='string')
xcenter = 84.11926799
ycenter = -6.302519164
wid = 0.7391003
hei = 0.4449478
left = xcenter + wid/2.
right = xcenter - wid/2.
top = ycenter + hei/2.
bottom = ycenter - hei/2.

ff = open('lanecores.reg','w')
ff.write('# Region file format: DS9 version 4.1\nglobal color=magenta dashlist=8 3 width=1 font="helvetica 15 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')

for cc,vv in enumerate(corenames):
    if float(xw[cc]) < left and float(xw[cc]) > right and float(yw[cc]) > bottom and float(yw[cc]) < top:
        ff.write('circle('+xw[cc]+','+yw[cc]+',15")\n')

ff.close()

