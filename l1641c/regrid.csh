#!/bin/csh

regrid in=mask_l1641c_c18o_pix_2_Tmb.mir tin=../products/mask_imfit_c18o_pix_2_Tmb.mir options=offset out=regrid_mask_l1641c_c18o_pix_2_Tmb.mir
imcomb in="../products/mask_imfit_c18o_pix_2_Tmb.mir,regrid_mask_l1641c_c18o_pix_2_Tmb.mir" out=join_c18o_pix_2_Tmb.mir rms="1.0,1.0" 
mirout join_c18o_pix_2_Tmb.mir
regrid in="../products/mask_imfit_c18o_pix_2_Tmb.mir" tin=join_c18o_pix_2_Tmb.mir out=re_main_c18o_pix_2_Tmb.mir
regrid in=mask_l1641c_c18o_pix_2_Tmb.mir tin=join_c18o_pix_2_Tmb.mir out=re_l1641c_c18o_pix_2_Tmb.mir
mirout re_main_c18o_pix_2_Tmb.mir
mirout re_l1641c_c18o_pix_2_Tmb.mir

