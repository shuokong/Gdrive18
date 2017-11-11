rm -rf north_mask_c18o_pix_2_Tmb.mir
rm -rf central_mask_c18o_pix_2_Tmb.mir
rm -rf south_mask_c18o_pix_2_Tmb.mir
rm -rf furthersouth_mask_c18o_pix_2_Tmb.mir
imsub in=mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(1,3347,1938,3677)" out=north_mask_c18o_pix_2_Tmb.mir
imsub in=mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(1,2908,1938,3346)" out=central_mask_c18o_pix_2_Tmb.mir
imsub in=mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(1,1620,1938,2907)" out=south_mask_c18o_pix_2_Tmb.mir
imsub in=mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(1,1,1938,1619)" out=furthersouth_mask_c18o_pix_2_Tmb.mir
fits op=xyout in=north_mask_c18o_pix_2_Tmb.mir out=north_mask_c18o_pix_2_Tmb.fits
fits op=xyout in=central_mask_c18o_pix_2_Tmb.mir out=central_mask_c18o_pix_2_Tmb.fits
fits op=xyout in=south_mask_c18o_pix_2_Tmb.mir out=south_mask_c18o_pix_2_Tmb.fits
fits op=xyout in=furthersouth_mask_c18o_pix_2_Tmb.mir out=furthersouth_mask_c18o_pix_2_Tmb.fits

#rm -rf north_coldens18_tauinte.mir
#rm -rf central_coldens18_tauinte.mir
#rm -rf south_coldens18_tauinte.mir
#rm -rf furthersouth_coldens18_tauinte.mir
#imsub in=coldens18_tauinte.mir region="abspix,boxes(1,3347,2438,4261)" out=north_coldens18_tauinte.mir
#imsub in=coldens18_tauinte.mir region="abspix,boxes(1,2908,2438,3346)" out=central_coldens18_tauinte.mir
#imsub in=coldens18_tauinte.mir region="abspix,boxes(1,1620,2438,2907)" out=south_coldens18_tauinte.mir
#imsub in=coldens18_tauinte.mir region="abspix,boxes(1,1,2438,1619)" out=furthersouth_coldens18_tauinte.mir
#fits op=xyout in=north_coldens18_tauinte.mir out=north_coldens18_tauinte.fits
#fits op=xyout in=central_coldens18_tauinte.mir out=central_coldens18_tauinte.fits
#fits op=xyout in=south_coldens18_tauinte.mir out=south_coldens18_tauinte.fits
#fits op=xyout in=furthersouth_coldens18_tauinte.mir out=furthersouth_coldens18_tauinte.fits

