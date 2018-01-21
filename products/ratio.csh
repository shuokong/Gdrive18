regrid in=../../13co/products/convol_mom0_13co_pix_2_Tmb.mir tin=mom0_c18o_pix_2_Tmb.mir out=regrid18_mom0_13co_pix_2_Tmb.mir
maths exp="<regrid18_mom0_13co_pix_2_Tmb.mir>/<mom0_c18o_pix_2_Tmb.mir>" out=ratio_13_18_pix_2_Tmb.mir
#fitsout ratio_13_18_pix_2_Tmb
maths exp="<ratio_13_18_pix_2_Tmb.mir>" mask="<mom0_c18o_pix_2_Tmb.mir>.gt.4." out=mask_ratio_13_18_pix_2_Tmb.mir
fitsout mask_ratio_13_18_pix_2_Tmb
