import sys
from astropy.io import fits
import numpy as np

ppi = 3.14159265359
cc = 2.99792458e10 # cm/s
hh = 6.62607e-27 # erg*s
kb = 1.38065e-16 # erg/K
ttbg = 2.73 # K

def sk_aaa(nu,llj,mu): # calculate Einstein A coefficient, nu is frequency in Hz, llj is the lower J of transition J+1->J, mu is the dipole moment in Debye. 2013-Feb-24
    llambda=cc/nu #cm
    mmu=mu*1.e-18 #esu cm
    mu_ul=np.sqrt((llj+1.)/(2.*llj+3.))*mmu
    return 64.*ppi*ppi*ppi*ppi*mu_ul*mu_ul/(3.*hh*llambda*llambda*llambda)

def sk_jjnu(tt,nu): # tt is the temperature in K, nu is the frequency in Hz. 2013-Feb-19
    return hh*nu/kb/(np.exp(hh*nu/kb/tt)-1.)

def sk_qqrot(B,tt): # B should be in Hz, tt in K, following Caselli et al. 2002. 2013-Feb-18    qrot=0.
    return kb*tt/hh/B+0.333

def sk_nntot(ww,nu,ggl,ggu,ttex,B,llj,mu): # calculate total column density given one transition. ww is integrated intensity in K km/s, nu is the frequency in Hz, ggl & ggu are weight, ttex is excitation temperature in K, B is rotation constant in Hz, llj is the lower J, mu is the dipole moment in Debye. 2013-Feb-18
    #eel=eel/8065.6*1.6022e-12#erg
    llambda=cc/nu#cm
    aa=sk_aaa(nu,llj,mu)#Einstein coefficient in s-1
    return 8.*ppi*ww*1.e5/llambda/llambda/llambda/aa*ggl/ggu/(sk_jjnu(ttex,nu)-sk_jjnu(ttbg,nu))/(1.-np.exp(-hh*nu/kb/ttex))*sk_qqrot(B,ttex)/ggl/np.exp(-llj*(llj+1.)*hh*B/kb/ttex)

hdu1 = fits.open('mom0_stick_mask_imfit_c18o_pix_2_Tmb.fits')[0]
hdu2 = fits.open('tex_on_stick_header.fits')[0]
hdu2td = fits.open('dustT_on_stick_header.fits')[0]
hdu2tk = fits.open('gasT_on_stick_header.fits')[0]
hdu3 = fits.open('dustcoldens_on_stick_header.fits')[0]
hdu4 = fits.open('mom0_stick_mask_imfit_c18o_pix_2_Tmb.fits')[0]
hdu5 = fits.open('mom0_stick_sen.fits')[0]

mom018data = hdu1.data
mom0sens = hdu5.data * 1.24 # K
sensbool = np.copy(mom018data)
sensbool[mom018data < 3.*mom0sens] = np.nan
sensbool[mom018data >= 3.*mom0sens] = 1
tex12data = hdu2.data
tdustdata = hdu2td.data
tkindata = hdu2tk.data
dustcoldensdata = hdu3.data

## coldens18_tauthin.fits
coldens18_thin = sk_nntot(mom018data,109.782182e9,1.,3.,tex12data,54891.420e6,0,0.11079)
hdu4.data = sk_nntot(mom018data,109.782182e9,1.,3.,tex12data,54891.420e6,0,0.11079)
hdu4.data = hdu4.data * sensbool
hdu4.writeto('coldens18_thin_tex.fits', output_verify='exception', overwrite=True, checksum=False)

hdu4.data = coldens18_thin/dustcoldensdata
hdu4.data = hdu4.data * sensbool
hdu4.writeto('abun18tex.fits', output_verify='exception', overwrite=True, checksum=False)

## use Herschel dust temperature
coldens18_thin = sk_nntot(mom018data,109.782182e9,1.,3.,tdustdata,54891.420e6,0,0.11079)
hdu4.data = sk_nntot(mom018data,109.782182e9,1.,3.,tdustdata,54891.420e6,0,0.11079)
hdu4.data = hdu4.data * sensbool
hdu4.writeto('coldens18_thin_tdust.fits', output_verify='exception', overwrite=True, checksum=False)

hdu4.data = coldens18_thin/dustcoldensdata
hdu4.data = hdu4.data * sensbool
hdu4.writeto('abun18tdust.fits', output_verify='exception', overwrite=True, checksum=False)

## use NH3 kinetic temperature
coldens18_thin = sk_nntot(mom018data,109.782182e9,1.,3.,tkindata,54891.420e6,0,0.11079)
hdu4.data = sk_nntot(mom018data,109.782182e9,1.,3.,tkindata,54891.420e6,0,0.11079)
hdu4.data = hdu4.data * sensbool
hdu4.writeto('coldens18_thin_tkin.fits', output_verify='exception', overwrite=True, checksum=False)

hdu4.data = coldens18_thin/dustcoldensdata
hdu4.data = hdu4.data * sensbool
hdu4.writeto('abun18tkin.fits', output_verify='exception', overwrite=True, checksum=False)
