    81 2017/10/31 17:37 cd products/
    82 2017/10/31 18:28 scp -r sk2534@farnam.hpc.yale.edu:/ysm-gpfs/project/sk2534/c18o/c18o_pix_2/combined_scalefactor_c18o.sen .
    83 2017/10/31 18:32 ls
    84 2017/10/31 18:32 ls ..
    85 2017/10/31 18:32 rm ../c18o.*.fits
    86 2017/10/31 18:32 ls
    87 2017/10/31 18:32 mv combined_scalefactor_c18o.sen combined_scalefactor_c18o.sen.mir
    88 2017/10/31 18:32 fitsout combined_scalefactor_c18o.sen
    89 2017/10/31 18:38 lst
    90 2017/10/31 18:39 rm -rf combined_scalefactor_c18o.sen.mir/
    91 2017/10/31 18:39 ds9 combined_scalefactor_c18o.sen.fits
    92 2017/10/31 18:41 scp -r sk2534@farnam.hpc.yale.edu:/ysm-gpfs/project/sk2534/c18o/c18o_pix_2/mask_c18o_pix_2_Tmb.mir .
    93 2017/10/31 18:46 fitsout mask_c18o_pix_2_Tmb
    94 2017/10/31 18:49 ds9 mask_c18o_pix_2_Tmb.fits
    95 2017/10/31 18:54 ls
    96 2017/10/31 18:54 lst
    97 2017/10/31 18:57 ds9 mask_c18o_pix_2_Tmb.fits
    98 2017/10/31 18:58 which miriad
    99 2017/10/31 18:58 puthd in="mask_c18o_pix_2_Tmb.mir/BUNIT" value="K" type=ascii
   100 2017/10/31 18:59 puthd in=mask_c18o_pix_2_Tmb.mir/BUNIT value="K" type=ascii
   101 2017/10/31 18:59 puthd in=mask_c18o_pix_2_Tmb.mir/BUNIT value=K type=ascii
   102 2017/10/31 18:59 prthd in=mask_c18o_pix_2_Tmb.mir
   103 2017/10/31 19:00 ds9 mask_c18o_pix_2_Tmb.fits
   104 2017/10/31 19:01 puthd in="mask_c18o_pix_2_Tmb.mir/BUNIT " value=K type=ascii
   105 2017/10/31 19:02 lst
   106 2017/10/31 19:02 rm -rf mask_c18o_pix_2_Tmb.mir/
   107 2017/10/31 19:04 cp ../../12co/products/bunit.py .
   108 2017/10/31 19:04 vim bunit.py
   109 2017/10/31 19:04 lst
   110 2017/10/31 19:04 rm c18o_pix_2.cm.fits
   111 2017/10/31 19:04 ls
   112 2017/10/31 19:04 vim bunit.py
   113 2017/10/31 19:04 python bunit.py
   114 2017/10/31 19:09 ds9 test.fits
   115 2017/10/31 19:09 mv test.fits mask_c18o_pix_2_Tmb.fits
   116 2017/10/31 19:10 lst
   117 2017/10/31 19:10 fitsin mask_c18o_pix_2_Tmb
   118 2017/10/31 21:03 which convol
   119 2017/10/31 21:05 convol map=mask_c18o_pix_2_Tmb.mir fwhm=10 options=final out=fwhm10_mask_c18o_pix_2_Tmb.mir
   120 2017/11/01 9:19 lst
   121 2017/11/01 9:19 fitsout fwhm10_mask_c18o_pix_2_Tmb
   122 2017/11/01 9:22 ds9 fwhm10_mask_c18o_pix_2_Tmb.fits
   123 2017/11/01 20:40 scp -r sk2534@farnam.hpc.yale.edu:/ysm-gpfs/project/sk2534/c18o/c18o_pix_2/combined_scalefactor_c18o.psf .
   124 2017/11/01 20:40 mv combined_scalefactor_c18o.psf combined_scalefactor_c18o.psf.mir
   125 2017/11/01 20:40 fitsout combined_scalefactor_c18o.psf
   126 2017/11/01 20:44 ds9 combined_scalefactor_c18o.psf.fits
   127 2017/11/01 20:44 ds9 combined_scalefactor_c18o.psf.fits &
   128 2017/11/01 23:42 scp -r sk2534@farnam.hpc.yale.edu:/ysm-gpfs/project/sk2534/c18o/c18o_pix_2/imfit_mask_c18o_pix_2_Tmb.fits .
   128 2017/11/01 23:42 scp -r sk2534@farnam.hpc.yale.edu:/ysm-gpfs/project/sk2534/c18o/c18o_pix_2/imfit_mask_c18o_pix_2_Tmb.fits .
   129 2017/11/02 14:19 ls
   130 2017/11/02 14:19 vim sen.py
   131 2017/11/02 14:19 vim sen.py
   132 2017/11/02 14:19 ds9 mask_c18o_pix_2_Tmb.fits
   133 2017/11/02 14:20 vim sen.py
   134 2017/11/02 14:21 python sen.py
   135 2017/11/02 17:06 vim sen.py
   136 2017/11/02 17:11 python sen.py
   137 2017/11/02 17:17 vim sen.py
   138 2017/11/02 17:17 python sen.py
   139 2017/11/02 17:25 ds9 c18o_pix_2_Tmb_sens.fits
   140 2017/11/02 18:10 prthd in=mask_c18o_pix_2_Tmb.mir
   141 2017/11/02 18:18 ls
   142 2017/11/02 18:19 ds9 mask_c18o_pix_2_Tmb.fits &
   143 2017/11/02 18:19 cp ../../13co/subregions_jrf.reg .
   144 2017/11/02 18:19 mv subregions_jrf.reg ..
   145 2017/11/02 18:20 vim imsub.csh
   146 2017/11/02 18:22 vim imsub.csh
   147 2017/11/02 18:22 vim imsub.csh
   148 2017/11/02 18:23 vim imsub.csh
   149 2017/11/02 18:26 csh -xv imsub.csh
   150 2017/11/02 18:52 ls -d * | grep "sen_gt2"
   151 2017/11/02 18:53 tar cvf volker_c18o.tgz north_mask_c18o_pix_2_Tmb.fits central_mask_c18o_pix_2_Tmb.fits south_mask_c18o_pix_2_Tmb.fits furthersouth_mask_c18o_pix_2_Tmb.fits
   152 2017/11/02 22:23 fitsin c18o_pix_2_Tmb_sens
   153 2017/11/02 23:17 maths exp="<mask_c18o_pix_2_Tmb.mir>" mask="<mask_c18o_pix_2_Tmb.mir>.gt.<c18o_pix_2_Tmb_sens.mir>*3." out=clip3sigma_mask_c18o_pix_2_Tmb.mir
   181 2017/11/03 14:28 cd products/
   182 2017/11/03 14:28 ls
   183 2017/11/03 14:28 git add -f showpeak.py
   184 2017/11/03 14:28 vim showpeak.py
   185 2017/11/03 14:29 git add -f olay.reg
   186 2017/11/03 14:29 python showpeak.py
   190 2017/11/03 14:32 cd products/
   191 2017/11/03 14:32 python showpeak.py
   192 2017/11/03 14:34 python showpeak.py
   196 2017/11/03 14:36 cd -
   197 2017/11/03 14:36 python showpeak.py
   198 2017/11/03 15:48 cp ../../13co/products/showmom0.py .
   199 2017/11/03 15:49 git add -f showmom0.py
   200 2017/11/03 15:49 vim showmom0.py
   201 2017/11/03 15:49 python showmom0.py
   202 2017/11/03 15:52 vim showpeak.py
   203 2017/11/03 15:52 python showpeak.py
   204 2017/11/03 15:53 vim showpeak.py
   205 2017/11/03 15:53 python showpeak.py
   206 2017/11/03 15:53 vim showpeak.py
   207 2017/11/03 15:54 ds9 c18o_pix_2_Tmb_sens.fits
   208 2017/11/03 15:54 vim showpeak.py
   209 2017/11/03 15:54 python showpeak.py
   210 2017/11/03 15:55 vim showpeak.py
   211 2017/11/03 15:55 python showpeak.py
   212 2017/11/03 16:10 vim showmom0.py
   213 2017/11/03 16:10 python showmom0.py
   214 2017/11/03 16:16 ls
   215 2017/11/03 16:17 cp -r ../../13co/products/rgb.bck* .
   216 2017/11/03 16:19 rm rgb.bck.dir/Frame2/mom0_*.fits
   217 2017/11/03 16:20 cp mom0_42_64_c18o_pix_2_Tmb.fits rgb.bck.dir/Frame2/
   218 2017/11/03 16:20 cp mom0_65_86_c18o_pix_2_Tmb.fits rgb.bck.dir/Frame2/
   219 2017/11/03 16:20 cp mom0_87_109_c18o_pix_2_Tmb.fits rgb.bck.dir/Frame2
   220 2017/11/03 16:20 vim rgb.bck
   221 2017/11/03 16:21 ds9 &
   222 2017/11/03 16:23 ds9 mom0_42_64_c18o_pix_2_Tmb.fits
   223 2017/11/03 16:24 vim rgb.bck
   224 2017/11/03 16:25 vim showpeak.py
   224 2017/11/03 16:25 vim showpeak.py
   224 2017/11/03 16:25 vim showpeak.py
   225 2017/11/03 16:33 lst
   226 2017/11/03 16:33 open ds9.ps
   227 2017/11/03 16:49 vim spectra.py
   228 2017/11/03 16:50 vim spectra.py
   229 2017/11/03 16:50 python spectra.py
   230 2017/11/03 16:55 vim spectra.py
   231 2017/11/03 16:56 python spectra.py
   232 2017/11/03 17:39 lst
   233 2017/11/03 17:39 vim showmom1.py
   234 2017/11/03 17:40 python showmom1
   235 2017/11/03 17:40 python showmom1.py
   236 2017/11/03 17:41 vim log.sh
   237 2017/11/03 17:42 maths exp="<mask_c18o_pix_2_Tmb.mir>" mask="<mask_c18o_pix_2_Tmb.mir>.gt.<c18o_pix_2_Tmb_sens.mir>*5." out=clip5sigma_mask_c18o_pix_2_Tmb.mir
   241 2017/11/03 17:59 cd products/
   242 2017/11/03 17:59 lst
   243 2017/11/03 17:59 python showmom1.py
   244 2017/11/03 18:07 cp ../../13co/products/showmom2.py .
   245 2017/11/03 18:14 lst
   246 2017/11/03 18:16 vim showmom2.py
   247 2017/11/03 18:17 python showmom2.py
   248 2017/11/03 18:17 vim showmom2.py
   249 2017/11/03 18:17 python showmom2.py
   250 2017/11/03 18:18 vim showmom2.py
   251 2017/11/03 18:18 python showmom2.py
   252 2017/11/03 19:00 gits
   253 2017/11/03 19:00 lst
   254 2017/11/03 19:01 ls *.py
   255 2017/11/03 19:01 git add -f *.py
   256 2017/11/03 19:01 gits
   257 2017/11/03 19:01 gitc 'all figures'
   258 2017/11/03 19:01 gpthis
   259 2017/11/03 19:01 gitf master
   260 2017/11/04 18:08 vim log.sh
   261 2017/11/04 18:09 scp -r sk2534@farnam.hpc.yale.edu:/ysm-gpfs/project/sk2534/c18o/robust2_c18o_pix_2/mask_c18o_pix_2_Tmb.fits ./mask_robust2_c18o_pix_2_Tmb.fits
   262 2017/11/04 18:24 ds9 mask_robust2_c18o_pix_2_Tmb.fits
   263 2017/11/06 15:19 sshhifi
   268 2017/11/10 14:12 cd products/
   269 2017/11/10 14:12 ls
   270 2017/11/10 14:12 mv imfit_mask_c18o_pix_2_Tmb.fits mask_imfit_c18o_pix_2_Tmb.fits
   271 2017/11/10 14:13 rm -r mask_c18o_pix_2_Tmb.mir
   272 2017/11/10 14:13 fitsin mask_imfit_c18o_pix_2_Tmb
   273 2017/11/10 14:31 vim sen.py
   274 2017/11/10 14:32 python sen.py
   275 2017/11/10 14:44 lst
   276 2017/11/10 14:44 fitsin c18o_pix_2_Tmb_sens
   277 2017/11/10 14:44 rm -rf c18o_pix_2_Tmb_sens.mir
   278 2017/11/10 14:44 fitsin c18o_pix_2_Tmb_sens
   279 2017/11/10 17:30 lst
   280 2017/11/10 17:31 maths exp="<mask_imfit_c18o_pix_2_Tmb.mir>" mask="<mask_imfit_c18o_pix_2_Tmb.mir>.gt.<c18o_pix_2_Tmb_sens.mir>*5." out=clip5sigma_mask_imfit_c18o_pix_2_Tmb.mir
   285 2017/11/10 22:07 cd products/
   286 2017/11/10 22:12 python showmom0.py
   287 2017/11/10 22:14 python showmom1.py
   288 2017/11/10 22:18 python showpeak.py
   289 2017/11/10 23:10 prthd in=mask_imfit_c18o_pix_2_Tmb.mir
   290 2017/11/11 0:00 rm -rf clip3sigma_mask_c18o_pix_2_Tmb.mir/
   291 2017/11/11 0:00 rm -rf clip5sigma_mask_c18o_pix_2_Tmb.mir/
   295 2017/11/11 0:28 cd products/
   296 2017/11/11 0:28 vim imsub.csh
   297 2017/11/11 0:28 csh -xv imsub.csh
   298 2017/11/11 10:53 python spectra.py
   299 2017/11/11 11:04 python showmom2.py
   300 2017/11/11 11:19 open .
   301 2017/11/11 11:21 vim ../datapaperTmb18.csh
   302 2017/11/11 11:21 vim clip5sigma_mask_imfit_c18o_pix_2_Tmb.mir/history
   303 2017/11/11 11:22 ls -thld c18o_pix_2_Tmb_sens.mir/
   304 2017/11/11 11:22 ls -thld c18o_pix_2_Tmb_sens.fits
   305 2017/11/11 11:44 vim mom0_42_64_c18o_pix_2_Tmb.mir/history
   306 2017/11/11 11:44 ls mom0*.fits
   307 2017/11/11 11:45 cp mom0*.fits rgb.bck.dir/Frame2/
   308 2017/11/11 11:45 rm rgb.bck.dir/Frame2/mom0_c18o_pix_2_Tmb.fits
   309 2017/11/11 11:45 ds9 &
   310 2017/11/11 11:47 open ds9.ps
   311 2017/11/11 11:48 lst
   312 2017/11/11 11:48 cp 18mom0range.pdf ~/GoogleDrive/imagesCARMAOrion/
   313 2017/11/11 13:09 gits
   314 2017/11/11 13:09 gitc 'use imfit beam'
   315 2017/11/11 13:09 gpthis
   316 2017/11/12 22:52 vim log.sh
   317 2017/11/12 22:52 rm volker_c18o.tgz
   318 2017/11/12 22:53 tar cf volker_c18o.tgz mask_imfit_c18o_pix_2_Tmb.fits north_mask_c18o_pix_2_Tmb.fits central_mask_c18o_pix_2_Tmb.fits south_mask_c18o_pix_2_Tmb.fits furthersouth_mask_c18o_pix_2_Tmb.fits
   319 2017/11/13 0:12 lst
   320 2017/11/14 14:13 vim showmom0.py
   321 2017/11/14 14:13 python showmom0.py
   322 2017/11/14 14:13 lst
   323 2017/11/14 14:13 open mom0_c18o_pix_2_Tmb.pdf
   324 2017/11/14 14:14 vim showmom0.py
   325 2017/11/14 14:14 python showmom0.py
   326 2017/11/14 14:14 vim showmom0.py
   327 2017/11/14 14:14 python showmom0.py
   328 2017/11/14 16:21 lst
   329 2017/11/15 20:57 vim showpeak.py
   330 2017/11/15 21:02 vim showmom0.py
   331 2017/11/15 21:02 vim showmom0.py
   332 2017/11/15 21:03 python showmom0.py
   333 2017/11/15 21:10 vim showpeak.py
   334 2017/11/15 21:10 python showpeak.py
   339 2017/11/16 18:17 cd products/
   340 2017/11/16 18:19 vim showmom0.py
   341 2017/11/16 18:20 python showmom0.py
   342 2017/11/16 18:21 vim showmom0.py
   343 2017/11/16 18:21 python showmom0.py
   344 2017/11/16 18:24 vim showmom0.py
   345 2017/11/16 18:24 vim showmom0.py
   346 2017/11/16 18:24 python showmom0.py .=
   347 2017/11/16 18:28 vim olay.reg
   348 2017/11/16 18:28 python showmom0.py
   349 2017/11/16 18:30 vim showmom0.py
   350 2017/11/16 18:30 python showmom0.py
   351 2017/11/16 18:31 vim showmom0.py
   352 2017/11/16 18:31 python showmom0.py
   353 2017/11/16 21:48 vim showmom1.py
   354 2017/11/16 21:50 vim showmom1.py
   355 2017/11/16 21:51 python showmom1.py
   356 2017/11/16 21:56 vim showmom1.py
   357 2017/11/16 21:57 python showmom1.py
   358 2017/11/18 11:22 prthd in=mask_imfit_c18o_pix_2_Tmb.mir
   359 2017/11/18 11:38 ds9 c18o_pix_2_Tmb_sens.fits
   360 2017/11/24 22:36 ls -d *.mir
   361 2017/11/24 22:36 casa
   362 2017/11/25 15:10 lst
   363 2017/11/25 15:10 ds9 han1_mask_imfit_c18o_pix_2_Tmb.fits
   364 2017/11/25 15:11 rm han1_mask_imfit_c18o_pix_2_Tmb.fits
   365 2017/11/25 15:11 casa
   366 2017/11/25 15:37 ds9 han1_mask_imfit_c18o_pix_2_Tmb.fits
   367 2017/11/27 20:23 maths exp="<mask_imfit_c18o_pix_2_Tmb.mir>" region="abspix,images(1)" out=chan1_mask_imfit_c18o_pix_2_Tmb.mir
   368 2017/11/27 20:24 fitsout chan1_mask_imfit_c18o_pix_2_Tmb
    15 2017/12/16 15:29 cd products/
    16 2017/12/16 15:29 vim remove4axis.py
    17 2017/12/16 15:29 python remove4axis.py
    18 2017/12/16 15:36 lst
    19 2017/12/16 15:36 ds9 nostokes_han1_mask_imfit_c18o_pix_2_Tmb.fits
    20 2017/12/16 15:42 git add -f remove4axis.py
    21 2017/12/16 16:13 lst
    22 2017/12/16 16:13 vim showmom0.py
    23 2017/12/16 16:14 python showmom0.py
    24 2017/12/16 16:15 vim olay.reg
    25 2017/12/16 16:15 python showmom0.py
    26 2017/12/16 16:24 vim showmom1.py
    27 2017/12/16 16:25 python showmom1.py
    28 2017/12/16 20:15 vim showmom2.py
    29 2017/12/16 20:16 python showmom2.py
    30 2017/12/16 20:17 lst
    31 2017/12/16 20:17 rm mom2_c18o_hist.pdf
    32 2017/12/16 20:17 vim showmom2.py
    33 2017/12/16 20:17 rm ../../imagesCARMAOrion/mom2_c18o_hist.pdf
    34 2017/12/16 23:33 ds9 han1_mask_imfit_c18o_pix_2_Tmb.fits
    35 2017/12/17 11:53 vim showmom0.py
    36 2017/12/17 11:54 vim showmom1.py
    37 2017/12/17 11:56 vim showmom2.py
    38 2017/12/17 11:57 vim olay1.reg
    39 2017/12/17 11:57 vim olay2.reg
    40 2017/12/17 11:58 vim olay3.reg
    41 2017/12/17 11:58 python showmom0.py && python showmom1.py && python showmom2.py
    42 2017/12/17 12:05 gitc 'smaller figures'
    43 2017/12/17 12:05 gits
    44 2017/12/17 12:05 git add -f olay*.reg
    45 2017/12/17 12:05 gits
    46 2017/12/17 12:05 gitc 'smaller figures'
    47 2017/12/17 12:06 gpthis
    48 2017/12/19 11:13 ds9 c18o_pix_2_Tmb_sens.fits
    49 2017/12/19 11:17 ds9 mask_c18o_pix_2_Tmb.fits
    50 2017/12/19 11:17 ls
    51 2017/12/19 11:18 ls -thld mask_*.fits
    52 2017/12/19 15:29 vim showmom2.py
    53 2017/12/19 15:29 python showmom2.py
    54 2017/12/20 18:15 vim spectra.py
    55 2017/12/20 18:16 python spectra.py
    56 2017/12/20 18:17 gits
    57 2017/12/21 22:49 vim spectra.py
    58 2017/12/21 22:49 python spectra.py
    59 2017/12/21 23:43 vim olay1.reg
    60 2017/12/21 23:43 vim olay2.reg
    61 2017/12/21 23:43 vim olay3.reg
    62 2017/12/21 23:47 python showmom0.py && python showmom1.py && python showmom2.py
    63 2017/12/27 17:13 gits
    64 2017/12/28 17:03 vim showmom0.py
    65 2017/12/28 17:05 python showmom0.py
    66 2017/12/28 17:06 vim showmom1.py
    67 2017/12/28 17:07 python showmom1.py
    68 2017/12/28 17:07 vim showmom1.py
    69 2017/12/28 17:08 python showmom1.py
    70 2017/12/28 17:08 vim showmom2.py
    71 2017/12/28 17:11 python showmom2.py
    72 2018/01/11 20:07 gits
    73 2018/01/11 20:07 gitc 'add labels'
    74 2018/01/11 20:07 gpthis
    75 2018/01/14 10:35 vim showmom0.py
    76 2018/01/14 10:36 python showmom0.py
    77 2018/01/14 10:36 vim showmom1.py
    78 2018/01/14 10:39 python showmom1.py
    79 2018/01/14 10:39 vim showmom2.py
    80 2018/01/14 10:40 python showmom2.py
    81 2018/01/14 15:13 open averspec18.pdf
    82 2018/01/14 15:47 vim spectra.py
    83 2018/01/14 15:48 python spectra.py
    84 2018/01/14 15:49 vim spectra.py
    85 2018/01/14 15:50 gits
    86 2018/01/14 15:51 gits
    87 2018/01/14 15:51 gitc 'better figure labels'
    88 2018/01/14 15:51 gpthis
    89 2018/01/18 13:05 vim olay1.reg
    90 2018/01/18 13:05 python showmom0.py
    91 2018/01/18 13:06 vim olay2.reg
    92 2018/01/18 13:06 python showmom1.py
    93 2018/01/18 13:07 python showmom2.py
    94 2018/01/18 13:36 ds9 mom0_c18o_pix_2_Tmb.fits
    95 2018/01/18 13:44 ds9 mom0_c18o_pix_2_Tmb.fits
    96 2018/01/18 14:01 regrid in=../../13co/products/convol_mom0_13co_pix_2_Tmb.mir tin=mom0_c18o_pix_2_Tmb.mir out=regrid18_mom0_13co_pix_2_Tmb.mir
    97 2018/01/18 14:03 maths exp="<regrid18_mom0_13co_pix_2_Tmb.mir>/<mom0_c18o_pix_2_Tmb.mir>" out=ratio_13_18_pix_2_Tmb.mir
    98 2018/01/18 14:03 fitsout ratio_13_18_pix_2_Tmb
    99 2018/01/18 14:03 ds9 ratio_13_18_pix_2_Tmb.fits
   100 2018/01/18 14:05 history
   101 2018/01/18 14:05 vim ratio.csh
   102 2018/01/18 14:06 git add -f ratio.csh
   103 2018/01/18 14:16 cp showmom1.py showratio.py
   104 2018/01/18 14:16 vim showratio.py
   105 2018/01/18 14:20 python showratio.py
   106 2018/01/18 14:20 vim showratio.py
   107 2018/01/18 14:21 python showratio.py
   108 2018/01/18 14:25 gits
   109 2018/01/18 14:25 git add -f showratio.py
   110 2018/01/21 15:34 gits
   111 2018/01/21 15:34 vim showmom0.py
   112 2018/01/21 15:45 ds9 nostokes_han1_mask_imfit_c18o_pix_2_Tmb.fits
   113 2018/01/21 15:48 vim ratio
   114 2018/01/21 15:51 maths exp="<ratio_13_18_pix_2_Tmb.mir>" mask="<mom0_>"
   115 2018/01/21 15:51 ls mom0_c18o_pix_2_Tmb.mir/
   116 2018/01/21 15:51 maths exp="<ratio_13_18_pix_2_Tmb.mir>" mask="<mom0_c18o_pix_2_Tmb.mir>.gt.4." out=mask_ratio_13_18_pix_2_Tmb.mir
   117 2018/01/21 15:52 vim ratio.csh
   118 2018/01/21 15:52 rm ratio_13_18_pix_2_Tmb.fits
   119 2018/01/21 15:52 fitsout mask_ratio_13_18_pix_2_Tmb
   120 2018/01/21 15:52 vim showratio.py
   121 2018/01/21 15:57 python showratio.py
   122 2018/01/21 15:58 vim ratio.csh
   123 2018/01/21 15:58 vim showmom0.py
   124 2018/01/21 15:58 vim showratio.py
   125 2018/01/21 15:58 python showratio.py
   126 2018/01/21 15:59 vim showratio.py
   127 2018/01/21 15:59 python showratio.py
   128 2018/01/21 16:01 vim ratio.csh
   129 2018/01/21 16:05 vim showratio.py
   130 2018/01/21 16:13 gitc 'add L1641C and ratio map'
   131 2018/01/21 16:13 gpthis
   132 2018/01/21 19:37 cp mom0_c18o_pix_2_Tmb.fits ~/GoogleDrive/imagesCARMAOrion/
   133 2018/01/21 19:37 ds9 mom0_c18o_pix_2_Tmb.fits
   134 2018/01/21 19:37 cp mom1_c18o_pix_2_Tmb.fits ~/GoogleDrive/imagesCARMAOrion/
   135 2018/01/21 19:37 cp mom2_c18o_pix_2_Tmb.fits ~/GoogleDrive/imagesCARMAOrion/
   136 2018/01/23 15:44 gitlist
   137 2018/01/23 15:46 grep "add_axes" *.py
   138 2018/01/25 16:55 gits
   139 2018/02/01 17:07 vim pvmap_orion.py
   140 2018/02/01 17:07 ls *.fits
   141 2018/02/01 17:11 lst
   142 2018/02/01 17:11 git add -f pvmap_orion.py
   143 2018/02/01 17:11 git add -f radiomodule_orion.py
   144 2018/02/01 17:11 git add -f posvel_orion.py
   145 2018/02/01 17:11 vim pvmap_orion.py
   146 2018/02/01 17:11 python pvmap_orion.py
   147 2018/02/01 17:13 open test.pdf
   148 2018/02/01 17:34 vim pvmap_orion.py
   149 2018/02/01 17:34 mv test.pdf pv18.pdf
   150 2018/02/01 17:34 cp pv18.pdf ~/GoogleDrive/imagesCARMAOrion/
   151 2018/02/01 17:39 gitc 'pv diagram'
   152 2018/02/01 17:39 gpthis
   153 2018/02/02 9:58 vim pvmap_orion.py
   154 2018/02/02 9:59 python pvmap_orion.py
   155 2018/02/02 10:35 open pv18.pdf
   156 2018/02/02 10:36 cp pv18.pdf ~/GoogleDrive/imagesCARMAOrion/
   157 2018/02/02 16:07 grep beampixel *.py
   158 2018/02/02 23:17 vim channelmap.py
   159 2018/02/02 23:17 ds9 han1_mask_imfit_c18o_pix_2_Tmb.fits
   160 2018/02/02 23:17 cp ../../13co/products/channelmap.py .
   161 2018/02/02 23:17 vim channelmap.py
   162 2018/02/02 23:20 ds9 han1_mask_imfit_c18o_pix_2_Tmb.fits
   163 2018/02/02 23:21 vim channelmap.py
   164 2018/02/02 23:22 python channelmap.py
   165 2018/02/02 23:23 lst
   166 2018/02/02 23:23 vim channelmap.py
   167 2018/02/02 23:24 python channelmap.py
   168 2018/02/02 23:26 lst
   169 2018/02/02 23:26 rm chanc18o0.pdf
   170 2018/02/02 23:26 vim channelmap.py
   171 2018/02/02 23:28 ds9 han1_mask_imfit_c18o_pix_2_Tmb.fits &
   172 2018/02/02 23:30 ds9 chan1_mask_imfit_c18o_pix_2_Tmb.fits &
   173 2018/02/02 23:32 which maths
   174 2018/02/02 23:33 maths exp="<han1_mask_imfit_c18o_pix_2_Tmb.mir>" mask="<chan1_mask_imfit_c18o_pix_2_Tmb.mir>" out=test.mir
   175 2018/02/02 23:34 vim channelmap.py
   176 2018/02/03 9:48 fitsin han1_mask_imfit_c18o_pix_2_Tmb
   177 2018/02/03 9:51 maths exp="<han1_mask_imfit_c18o_pix_2_Tmb.mir>" mask="<chan1_mask_imfit_c18o_pix_2_Tmb.mir>" out=test.mir
   178 2018/02/03 9:51 rm -r han1_mask_imfit_c18o_pix_2_Tmb.mir/
   179 2018/02/03 10:04 vim channelmap.py
   180 2018/02/03 10:05 python channelmap.py
   181 2018/02/03 10:07 vim channelmap.py
   182 2018/02/03 10:07 python channelmap.py
   183 2018/02/03 10:16 lst
   184 2018/02/03 10:16 cp chanc18o*.pdf ~/GoogleDrive/imagesCARMAOrion/channelmaps/c18o/
   185 2018/02/03 10:16 git add -f chan1_mask_imfit_c18o_pix_2_Tmb.fits
   186 2018/02/03 10:16 gitc 'make channel map and pv diagram'
   187 2018/02/03 10:16 gpthis
   188 2018/02/05 18:26 vim pvmap_orion.py
   189 2018/02/05 18:27 vim posvel_orion.py
   190 2018/02/05 18:27 python pvmap_orion.py
   191 2018/02/06 13:09 cp pv18.pdf ~/GoogleDrive/imagesCARMAOrion/
     1 2018/02/07 16:08 cd GoogleDrive/c18o/products/
     2 2018/02/07 16:11 rm han1_mask_imfit_c18o_pix_2_Tmb_channel_*.fits
     3 2018/02/07 16:11 vim channelmap.py
     4 2018/02/07 16:13 lst
     5 2018/02/07 16:13 python channelmap.py
     6 2018/02/07 16:14 lst
     7 2018/02/07 16:14 open chanc18o34.pdf
     8 2018/02/07 16:15 cp chanc18o34.pdf ~/GoogleDrive/imagesCARMAOrion/
     9 2018/02/07 16:42 vim pvmap_orion.py
    10 2018/02/07 16:42 python pvmap_orion.py
    11 2018/02/07 16:43 open pv18.pdf
    12 2018/02/07 16:43 cp pv18.pdf ~/GoogleDrive/imagesCARMAOrion/
    13 2018/02/07 16:43 gits
    14 2018/02/07 16:44 lst
    15 2018/02/07 16:44 git add -f channelmap.py
    16 2018/02/07 16:44 gits
    17 2018/02/07 16:44 gitc 'new representative channel map, better pv diagram ticks'
    18 2018/02/07 16:44 gpthis
    19 2018/02/20 13:56 which sshhifi
    20 2018/02/20 16:47 vim log.sh
     1 2018/02/23 16:36 lst
     2 2018/02/23 16:46 rm convol18_han1_mask_imfit_c18o_pix_2_Tmb.fits
     3 2018/02/23 16:46 casa
     4 2018/02/23 17:20 lst
     5 2018/02/23 17:20 gits
     6 2018/02/23 17:20 git add -f remove34axes_pixel6.py
     7 2018/02/23 17:20 vim remove34axes_pixel6.py
     8 2018/02/25 10:08 lst
     9 2018/02/26 13:50 cp ../../13co/products/usenanmask.py .
    10 2018/02/26 13:50 vim usenanmask.py
    11 2018/02/26 13:51 python usenanmask.py
    12 2018/02/26 13:54 git add -f usenanmask.py
    13 2018/02/26 13:58 lst
    14 2018/02/26 13:58 casa
    15 2018/02/26 14:14 ls -thld *.fits | head
    16 2018/02/26 14:15 rm han1_mask_imfit_c18o_pix_2_Tmb.fits
    17 2018/02/26 16:10 lst
    18 2018/02/26 16:10 vim remove34axes_pixel6.py
    19 2018/02/26 16:11 python remove34axes_pixel6.py
    20 2018/02/26 16:11 git add -f remove34axes_pixel6.py
    21 2018/02/26 16:11 gits
    22 2018/02/26 16:11 vim repro.py
    23 2018/02/26 16:30 gits
    24 2018/02/26 16:30 vim remove34axes_pixel6.py
    25 2018/02/26 16:30 python remove34axes_pixel6.py
    26 2018/02/26 16:30 vim repro.py
    27 2018/02/26 16:30 git add -f repro.py
    28 2018/02/26 16:30 gits
    29 2018/02/26 16:30 vim repro.py
    30 2018/02/26 16:30 python repro.py
    31 2018/02/26 16:31 lst
    32 2018/02/26 16:31 vim repro.py
    33 2018/02/26 16:31 python repro.py
    34 2018/02/26 16:32 lst
    35 2018/02/26 16:32 ds9 stutz_on_c18o_header.fits
    36 2018/02/26 16:39 gits
    37 2018/02/26 16:39 ls -thld *
    38 2018/02/26 16:41 gitc 'apply mask to han1, make 6 arcsec pixel C18O cube and reproject Stutz NH map'
    39 2018/02/26 16:41 gpthis
    40 2018/03/07 16:06 ls *.fits
    41 2018/03/07 16:07 ds9 mask_han1_mask_imfit_c18o_pix_2_Tmb.fits
    42 2018/03/08 10:04 mv ../../GAScores.txt .
    43 2018/03/08 10:04 ls
    44 2018/03/08 10:04 lst
    45 2018/03/08 10:05 vim GAScores.txt
    46 2018/03/08 10:06 cp showmom0.py showKirkcores.py
    47 2018/03/08 10:07 git add -f showKirkcores.py
   227 2018/03/08 10:07 cd ../c18o/products/
   228 2018/03/08 10:07 lst
   229 2018/03/08 10:07 vim GAScores.txt
   230 2018/03/08 10:15 lst
   231 2018/03/08 10:15 python showKirkcores.py
   232 2018/03/08 10:18 python showKirkcores.py
   233 2018/03/08 10:19 lst
   234 2018/03/08 10:19 open GAScores_mom0_c18o_pix_2_Tmb.pdf
   235 2018/03/08 10:24 gits
   236 2018/03/08 10:30 open GAScores_mom0_c18o_pix_2_Tmb.pdf
    48 2018/03/08 10:07 vim showKirkcores.py
    49 2018/03/09 13:31 gits
    50 2018/03/09 13:31 lst
    51 2018/03/09 13:31 mv xcotex.py c18o_vs_N_H.py
   237 2018/03/09 13:31 lst
   238 2018/03/09 13:32 ls -thld * | grep pixel6
   239 2018/03/09 13:34 vim remove34axes_pixel6.py
   240 2018/03/09 13:38 vim usenanmask.py
   241 2018/03/09 13:48 ls -thld * | grep pixel6
   242 2018/03/09 13:49 vim usenanmask.py
   243 2018/03/09 13:53 vim remove34axes_pixel6.py
   244 2018/03/09 13:53 ds9 chan1_pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.fits
   245 2018/03/09 13:54 ds9 pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.fits
   246 2018/03/09 13:55 ls *.fits | grep mom0
   247 2018/03/09 14:01 vim mom0_c18o_pix_2_Tmb.mir/history
   248 2018/03/09 14:03 convol map=mom0_c18o_pix_2_Tmb.mir fwhm=18 pa=0 options=final out=convol18_mom0_c18o_pix_2_Tmb.mir
   249 2018/03/09 14:03 vim log.sh
   250 2018/03/09 14:05 imbin in=convol18_mom0_c18o_pix_2_Tmb.mir bin="3,3,3,3,1,1" out=pixel6_convol18_mom0_c18o_pix_2_Tmb.mir
   251 2018/03/09 14:05 fitsout pixel6_convol18_mom0_c18o_pix_2_Tmb
   252 2018/03/09 14:05 lst
   253 2018/03/09 14:12 lst
   254 2018/03/09 14:12 python c18o_vs_N_H.py
   255 2018/03/09 14:13 python c18o_vs_N_H.py
   256 2018/03/09 14:58 mv ~/GoogleDrive/color_12CO_sample_tex.py .
   257 2018/03/09 14:58 mv color_12CO_sample_tex.py color_c18o_NH_tex.py
   258 2018/03/09 14:58 git add -f color_c18o_NH_tex.py
    52 2018/03/09 13:31 vim c18o_vs_N_H.py
    53 2018/03/09 14:59 vim color_c18o_NH_tex.py
    54 2018/03/09 15:00 cp -r ../../12co/products/pixel6_convol18_mask_imfit_12co_pix_2_Tmb.mir .
    55 2018/03/09 15:01 regrid in="pixel6_convol18_mask_imfit_12co_pix_2_Tmb.mir" tin=chan1_pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.mir axes="1,2" out=regrid18_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.mir
    56 2018/03/09 15:02 smir
    57 2018/03/09 15:02 fitsin chan1_pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb
    58 2018/03/09 15:02 regrid in="pixel6_convol18_mask_imfit_12co_pix_2_Tmb.mir" tin=chan1_pixel6_convol18_han1_mask_imfit_c18o_pix_2_Tmb.mir axes="1,2" out=regrid18_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.mir
    59 2018/03/09 15:02 moment in=regrid18_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.mir mom=-2 out=peak_regrid18_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.mir
    60 2018/03/09 15:03 fitsout peak_regrid18_pixel6_convol18_mask_imfit_12co_pix_2_Tmb
    61 2018/03/09 15:03 cp ../../13co/products/tex_pixel6_convol18.py .
    62 2018/03/09 15:04 git add -f tex_pixel6_convol18.py
    63 2018/03/09 15:04 vim tex_pixel6_convol18.py
    64 2018/03/09 15:05 python tex_pixel6_convol18.py
    65 2018/03/09 15:06 vim tex_pixel6_convol18.py
    66 2018/03/09 15:07 python tex_pixel6_convol18.py
   259 2018/03/09 15:07 lst
   260 2018/03/09 15:08 ls pixel6_convol18_mom0_c18o_pix_2_Tmb.fits
   261 2018/03/09 15:08 ls stutz_on_c18o_header.fits
   262 2018/03/09 15:10 ls -thld * | grep vx
   263 2018/03/09 15:10 ls -thld * | grep vs
   264 2018/03/09 15:19 ds9 stutz_on_c18o_header.fits
   264 2018/03/09 15:19 ds9 stutz_on_c18o_header.fits
   265 2018/03/09 15:21 lst
   266 2018/03/09 15:21 python color_c18o_NH_tex.py
   267 2018/03/09 15:21 gits
   268 2018/03/09 15:21 git add -f boxes.txt
   269 2018/03/09 15:21 vim boxes.txt
   270 2018/03/09 15:22 python color_c18o_NH_tex.py
   271 2018/03/09 15:23 vim boxes.txt
   272 2018/03/09 15:23 python color_c18o_NH_tex.py
   273 2018/03/09 15:23 lst
   274 2018/03/09 15:23 rm color_c18o_NH_tex.pdf
   275 2018/03/09 15:24 python color_c18o_NH_tex.py
   276 2018/03/09 15:26 lst
   277 2018/03/09 15:29 python color_c18o_NH_tex.py
   278 2018/03/09 15:35 python color_c18o_NH_tex.py
   279 2018/03/09 15:36 python color_c18o_NH_tex.py
   280 2018/03/09 15:36 python color_c18o_NH_tex.py
   281 2018/03/09 15:37 python color_c18o_NH_tex.py
   282 2018/03/09 15:40 python color_c18o_NH_tex.py
   283 2018/03/09 15:42 gits
   284 2018/03/09 15:42 cp color_c18o_NH_tex.py color_c18o_NH_tdust.py
   285 2018/03/09 15:43 git add -f color_c18o_NH_tdust.py
    67 2018/03/09 15:07 vim color_c18o_NH_tex.py
   286 2018/03/09 15:43 ls *.fits
   287 2018/03/09 15:44 ls repro.py
   288 2018/03/09 15:44 vim repro.py
   289 2018/03/09 15:44 vim repro.py
   290 2018/03/09 15:45 gits
   291 2018/03/09 15:45 python repro.py
   292 2018/03/09 15:49 lst
   293 2018/03/09 15:50 lst
   294 2018/03/09 15:50 python color_c18o_NH_tdust.py
    68 2018/03/09 15:43 vim color_c18o_NH_tdust.py
   295 2018/03/09 15:51 python color_c18o_NH_tdust.py
    69 2018/03/09 15:50 vim color_c18o_NH_tdust.py
    70 2018/03/09 15:53 gits
   296 2018/03/09 15:53 python color_c18o_NH_tdust.py
    71 2018/03/09 15:55 vim color_c18o_NH_tdust.py
    72 2018/03/09 15:55 vim color_c18o_NH_tex.py
   297 2018/03/09 15:55 python color_c18o_NH_tdust.py
    73 2018/03/09 15:56 python color_c18o_NH_tex.py
    74 2018/03/09 16:00 vim color_c18o_NH_tdust.p
    75 2018/03/09 16:00 vim color_c18o_NH_tdust.pu
    76 2018/03/09 16:00 vim color_c18o_NH_tdust.py
    77 2018/03/09 16:00 python color_c18o_NH_tdust.py
    78 2018/03/09 16:04 vim color_c18o_NH_tdust.py
   298 2018/03/09 17:56 lst
   299 2018/03/09 17:56 open color_c18o_NH_tdust.pdf
   300 2018/03/09 17:58 python color_c18o_NH_tdust.py
   301 2018/03/09 18:04 gits
   302 2018/03/09 18:04 gitc 'W(C18O)-Tdust relation'
   303 2018/03/09 18:04 gpthis
    79 2018/03/09 17:54 vim color_c18o_NH_tdust.py
    80 2018/03/11 12:07 ls
    81 2018/03/11 12:07 lst
    82 2018/03/11 12:08 ls -thld * | head -30
    83 2018/03/11 12:08 vim showKirkcores.py
    84 2018/03/11 12:08 gita
    85 2018/03/11 12:08 gits
    86 2018/03/11 12:08 git add -f GAScores
    87 2018/03/11 12:08 git add -f GAScores.txt
    88 2018/03/11 12:08 gits
    89 2018/03/11 12:08 vim GAScores
    90 2018/03/11 12:08 vim GAScores.txt
    91 2018/03/13 18:10 vim ../../13co/products/channelmap.py
    92 2018/03/13 18:17 vim showmom2.py
    93 2018/03/13 18:17 python showmom2.py
    94 2018/03/13 18:20 vim channelmap.py
    95 2018/03/13 18:20 python channelmap.py
    96 2018/03/13 18:22 vim channelmap.py
    97 2018/03/13 18:22 python channelmap.py
    98 2018/03/13 18:26 vim channelmap.py
    99 2018/03/13 18:26 gits
   100 2018/03/13 18:26 git diff --follow channelmap.py
   101 2018/03/13 18:26 ls
   102 2018/03/13 18:26 ls chan18*
   103 2018/03/13 18:27 ls -thl chanc18o*.pdf
   104 2018/03/13 18:27 vim channelmap.py
   105 2018/03/13 18:27 python channelmap.py
   106 2018/03/13 18:36 gis
   107 2018/03/13 18:36 gits
   108 2018/03/13 18:48 gits
   109 2018/03/13 18:48 gitc 'correct figures'
   110 2018/03/13 18:48 gpthis
   111 2018/03/14 16:23 lst
   112 2018/03/14 16:23 rm showC18Ospectra.py
   113 2018/03/14 16:44 lst
   114 2018/03/14 16:44 gname
   115 2018/03/14 16:45 vim showmom0.py
   116 2018/03/14 16:45 ls *.py | grep mom0 | grep GAS
   117 2018/03/14 16:45 ls *.py | grep mom0
   118 2018/03/14 16:45 vim showKirkcores.py
   119 2018/03/14 21:05 lst
   120 2018/03/14 21:05 gits
   121 2018/03/14 21:05 gits
   122 2018/03/14 21:05 mv show_13CO_spectra_at_Kirk_cores.py show_C18O_spectra_at_Kirk_cores.py
   123 2018/03/14 21:05 git add -f show_C18O_spectra_at_Kirk_cores.py
   124 2018/03/14 21:05 vim show_C18O_spectra_at_Kirk_cores.py
   125 2018/03/14 21:07 gitf master | grep GAS
   126 2018/03/14 21:07 python show_C18O_spectra_at_Kirk_cores.py
   127 2018/03/14 22:29 open .
   128 2018/03/14 22:31 vim show_C18O_spectra_at_Kirk_cores.py
   129 2018/03/14 22:32 python show_C18O_spectra_at_Kirk_cores.py
   130 2018/03/14 22:33 lst
   131 2018/03/14 22:33 open averspec18number0.pdf
   132 2018/03/14 22:33 vim show_C18O_spectra_at_Kirk_cores.py
   133 2018/03/14 22:34 python show_C18O_spectra_at_Kirk_cores.py
   134 2018/03/14 22:35 open averspec18number0.pdf
   135 2018/03/14 22:35 python show_C18O_spectra_at_Kirk_cores.py
   136 2018/03/14 22:35 gits
   137 2018/03/14 22:35 python show_C18O_spectra_at_Kirk_cores.py
   138 2018/03/15 13:55 open .
   139 2018/03/15 13:58 vim show_pv_ratio_13_18.py
   140 2018/03/15 14:04 git add -f show_pv_ratio_13_18.py
   141 2018/03/15 14:04 python show_pv_ratio_13_18.py
   142 2018/03/15 14:04 vim show_pv_ratio_13_18.py
   143 2018/03/15 14:04 python show_pv_ratio_13_18.py
   144 2018/03/15 14:04 vim show_pv_ratio_13_18.py
   145 2018/03/15 14:04 python show_pv_ratio_13_18.py
   146 2018/03/15 14:04 lst
   147 2018/03/15 14:04 ds9 pv_ratio_13_18.fits
   148 2018/03/15 14:06 vim show_pv_ratio_13_18.py
   149 2018/03/15 14:06 python show_pv_ratio_13_18.py
   150 2018/03/15 14:07 lst
   151 2018/03/15 14:07 open pv_ratio_13_18.pdf
   152 2018/03/15 14:08 cp pv_ratio_13_18.pdf ~/GoogleDrive/imagesCARMAOrion/
   153 2018/03/15 14:21 open ~/GoogleDrive/imagesCARMAOrion/mom0_12co_pix_2_Tmb.pdf
   154 2018/03/15 18:33 lst
   155 2018/03/15 18:33 git add -f show_pv_ratio_13_18.py
   156 2018/03/15 18:33 gits
   157 2018/03/15 18:33 vim show_C18O_spectra_at_Kirk_cores.py
   158 2018/03/15 18:37 python show_C18O_spectra_at_Kirk_cores.py
   159 2018/03/15 18:41 lst
   160 2018/03/15 18:41 vim GAScores_C18O_peak_velocities.txt
   161 2018/03/15 18:41 gits
   162 2018/03/15 18:41 git add -f GAScores_C18O_peak_velocities.txt
   163 2018/03/16 12:14 lst
   164 2018/03/16 12:14 vim GAScores_C18O_peak_velocities.txt
   165 2018/03/16 14:16 open .
   166 2018/03/16 14:33 vim show_C18O_spectra_at_Kirk_cores.py
   167 2018/03/16 14:36 rm averspec18number*.pdf
   168 2018/03/16 14:36 lst
   169 2018/03/16 14:36 python show_C18O_spectra_at_Kirk_cores.py
   170 2018/03/16 14:37 lst
   171 2018/03/16 14:37 open averspec18number5.pdf
   172 2018/03/16 14:37 gits
   173 2018/03/16 14:37 python show_C18O_spectra_at_Kirk_cores.py
   174 2018/03/19 15:04 open .
   175 2018/03/19 15:05 gits
   176 2018/03/19 15:17 vim show_C18O_spectra_at_Kirk_cores.py
   177 2018/03/19 15:18 diff ../../13co/products/show_13CO_spectra_at_Kirk_cores.py show_C18O_spectra_at_Kirk_cores.py
   178 2018/03/19 15:19 vim show_C18O_spectra_at_Kirk_cores.py
   179 2018/03/19 15:19 python show_C18O_spectra_at_Kirk_cores.py
   180 2018/03/19 15:28 lst
   181 2018/03/19 15:28 vim GAScores_C18O_peak_velocities.txt
   182 2018/03/19 15:28 gits
   183 2018/03/19 15:29 gitc 'Kirk core beam spectra summary table'
   184 2018/03/19 15:29 gpthis
   185 2018/03/19 15:30 ls *.py
   186 2018/03/19 15:30 vim c18o_vs_N_H.py
   187 2018/03/19 15:30 open c18o_vs_N_H.pdf
   188 2018/03/19 15:30 open color_c18o_NH_t
   189 2018/03/19 15:30 open color_c18o_NH_tdust.pdf
   190 2018/03/19 15:32 open color_c18o_NH_tex.pdf
   191 2018/03/19 15:33 ls *.pdf
   192 2018/03/19 15:33 ls *.pdf | grep -v averspec
   193 2018/03/19 15:33 open c18o_vs_N_H.pdf
   194 2018/03/19 17:08 cp ../../13co/products/velocity_distribution_13CO.py .
   195 2018/03/19 17:08 mv velocity_distribution_13CO.py velocity_distribution_C18O.py
   196 2018/03/19 17:08 git add -f velocity_distribution_C18O.py
   197 2018/03/19 17:08 vim velocity_distribution_C18O.py
   198 2018/03/19 17:09 python velocity_distribution_C18O.py
   199 2018/03/19 17:14 cp velocity_distribution_C18O.py ~/GoogleDrive/
   200 2018/03/19 17:32 gits
   201 2018/03/19 17:32 gitlist
   202 2018/03/19 17:32 gname
   203 2018/03/19 17:34 vim color_c18o_NH_tdust.p
   204 2018/03/19 17:34 vim color_c18o_NH_tdust.py
   205 2018/03/19 17:35 vim color_c18o_NH_tex.py
   206 2018/03/19 17:36 gits
   207 2018/03/19 21:13 ls -thld * | grep mom0
   208 2018/03/19 21:14 vim log.sh
   209 2018/03/19 22:10 vim log.sh
   210 2018/03/20 16:43 grep lombardi *.py
   211 2018/03/20 16:43 vim repro.py
   212 2018/03/20 17:20 vim color_c18o_NH_tdust.py
   213 2018/03/20 17:20 vim channelmap.py
   214 2018/03/20 17:29 vim channelmap.py
   215 2018/03/20 17:31 vim color_c18o_NH_tdust.py
   216 2018/03/20 17:33 vim color_c18o_NH_tex.py
   217 2018/03/20 17:33 python color_c18o_NH_tdust.py && python color_c18o_NH_tex.py
   218 2018/03/20 17:34 cp ../../13co/products/boxes.txt .
   219 2018/03/20 17:34 git add -f boxes.txt
   220 2018/03/20 17:34 vim boxes.txt
   221 2018/03/20 17:34 python color_c18o_NH_tdust.py && python color_c18o_NH_tex.py
   222 2018/03/20 17:46 gits
   223 2018/03/20 17:46 gits
   224 2018/03/21 16:15 vim color_c18o_NH_tdust.py
   225 2018/03/21 16:15 python color_c18o_NH_tdust.py
   226 2018/03/21 16:29 vim color_c18o_NH_tex.py
   227 2018/03/21 16:29 python color_c18o_NH_tex.py
   228 2018/03/21 22:00 mv multicolor_12co_NH_tdust.py multicolor_c18o_NH_tdust.py
   229 2018/03/21 22:00 git add -f multicolor_c18o_NH_tdust.py
   230 2018/03/21 22:00 vim multicolor_c18o_NH_tdust.py
   231 2018/03/21 22:01 python multicolor_c18o_NH_tdust.py
   232 2018/03/21 22:15 vim color_c18o_NH_tdust.py
   233 2018/03/21 22:15 vim multicolor_c18o_NH_tdust.py
   234 2018/03/21 22:16 python multicolor_c18o_NH_tdust.py
   235 2018/03/21 22:35 cp ../../13co/products/subregions_jrf.reg .
   236 2018/03/21 22:35 ds9 stutz_on_c18o_header.fits &
   237 2018/03/21 22:36 vim multicolor_c18o_NH_tdust.py
   238 2018/03/21 22:36 vim multicolor_c18o_NH_tdust.py
   239 2018/03/21 22:36 vim multicolor_c18o_NH_tdust.py
   240 2018/03/21 22:38 python multicolor_c18o_NH_tdust.py
   241 2018/03/21 22:38 vim multicolor_c18o_NH_tdust.py
   242 2018/03/21 22:39 python multicolor_c18o_NH_tdust.py
   243 2018/03/22 15:48 gitc 'regional gas vs dust plots'
   244 2018/03/22 15:48 gpthis
   245 2018/03/22 15:48 gname
   246 2018/03/26 17:58 vim showmom2.py
   247 2018/03/26 17:58 vim olay2.reg
   248 2018/03/26 17:58 python showmom2.py
   249 2018/03/26 17:59 vim olay2.reg
   250 2018/03/26 17:59 python showmom2.py
   251 2018/03/26 18:04 vim pvmap_orion.py
   252 2018/03/26 18:04 python pvmap_orion.py
   253 2018/03/26 18:04 lst
   254 2018/03/26 18:04 open pv18.pdf
   255 2018/03/26 18:05 cp pv18.pdf ~/GoogleDrive/imagesCARMAOrion/
   256 2018/03/27 17:00 ds9 -restore rgb.bck &
   256 2018/03/27 17:00 ds9 -restore rgb.bck &
   257 2018/03/27 17:01 ds9 stutz_on_c18o_header.fits
   258 2018/03/27 17:04 cp rgb18_with_dust.png ../../imagesSFE/
   259 2018/03/27 17:34 ds9 -restore rgb.bck &
   259 2018/03/27 17:34 ds9 -restore rgb.bck &
   260 2018/03/27 17:36 gis
   261 2018/03/27 17:36 gits
   262 2018/03/27 17:37 gits
   263 2018/03/27 17:37 gitc 'thinner color bar pv diagram'
   264 2018/03/27 17:37 gpthis
   265 2018/03/27 19:00 mkdir Lane_cores_spectra
   266 2018/03/27 19:00 cp ../../12co/products/show_12CO_spectra_at_Lane_cores.py .
   267 2018/03/27 19:00 mv show_12CO_spectra_at_Lane_cores.py show_C18O_spectra_at_Lane_cores.py
   268 2018/03/27 19:01 git add -f show_C18O_spectra_at_Lane_cores.py
   269 2018/03/27 19:01 vim show_C18O_spectra_at_Lane_cores.py
   270 2018/03/27 19:01 python show_C18O_spectra_at_Lane_cores.py
   271 2018/03/27 19:08 vim show_C18O_spectra_at_Lane_cores.py
   272 2018/03/28 15:44 cp pv_mask_imfit_c18o_pix_2_Tmb.fits ../../imagesCARMAOrion/
   273 2018/03/28 17:45 vim show_C18O_spectra_at_Lane_cores.py
   274 2018/03/28 18:05 lst
   275 2018/03/28 18:06 python show_C18O_spectra_at_Lane_cores.py
   276 2018/03/28 18:15 vim show_C18O_spectra_at_Lane_cores.py
   277 2018/03/28 18:15 vim show_C18O_spectra_at_Lane_cores.py
   278 2018/03/28 18:16 python show_C18O_spectra_at_Lane_cores.py
   279 2018/03/28 18:23 vim show_C18O_spectra_at_Lane_cores.py
   280 2018/03/28 18:32 gits
   281 2018/03/28 18:32 git diff
   282 2018/03/28 18:32 vim show_C18O_spectra_at_Lane_cores.py
   283 2018/03/28 18:34 python show_C18O_spectra_at_Lane_cores.py
   284 2018/03/29 10:21 vim show_C18O_spectra_at_Lane_cores.py
   285 2018/03/29 10:24 diff ../../12co/products/show_12CO_spectra_at_Lane_cores.py show_C18O_spectra_at_Lane_cores.py
   286 2018/03/29 10:24 python show_C18O_spectra_at_Lane_cores.py
   287 2018/03/29 16:19 gits
   288 2018/03/29 17:56 ls -thd * | grep convol18 | grep pixel6
   289 2018/03/29 17:57 gitf master | grep tex_pixel6
   290 2018/03/29 17:57 ls -thd * | grep convol18 | grep pixel6 | xargs -I % rm -r %
   291 2018/03/29 17:57 gits
   292 2018/03/29 17:57 git checkout -f tex_pixel6_convol18.py
   293 2018/03/29 17:57 gits
   294 2018/03/30 15:11 ls -thld * | grep convol18
   295 2018/03/30 15:11 rm -rf convol18_han1_mask_imfit_c18o_pix_2_Tmb.im/
   296 2018/03/30 15:11 cp -r /Users/shuokong/GoogleDrive/OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.mir .
   297 2018/03/30 15:17 regrid in=convol18_mom0_c18o_pix_2_Tmb.mir out=regrid_Stutz_convol18_mom0_c18o_pix_2_Tmb.mir axes="1,2" tin=carmanro_OrionA_all_spire250_nh_mask_corr_apex.mir
   298 2018/03/30 15:17 lst
   299 2018/03/30 15:17 fitsout regrid_Stutz_convol18_mom0_c18o_pix_2_Tmb
   300 2018/03/30 15:17 ds9 regrid_Stutz_convol18_mom0_c18o_pix_2_Tmb.fits
   301 2018/03/30 16:51 cp ../../12co/products/boxes.txt .
   302 2018/03/30 16:55 fitsout carmanro_OrionA_all_spire250_nh_mask_corr_apex
   303 2018/03/30 16:55 lst
   304 2018/03/30 16:55 vim color_c18o_NH_tdust.py
   305 2018/03/30 16:56 vim color_c18o_NH_tdust.py
   306 2018/03/30 16:58 vim color_c18o_NH_tdust.py
   307 2018/03/30 16:59 rm ../../13co/products/lombardi_colorT*_on_13co_header.fits
   308 2018/03/30 16:59 rm lombardi_colorT*.fits
   309 2018/03/30 17:00 cp ../../13co/products/lombardi_colorT_on_Stutz_header.fits .
   310 2018/03/30 17:00 python color_c18o_NH_tdust.py
   311 2018/03/30 17:02 vim color_c18o_NH_tex.py
   312 2018/03/30 17:03 python color_c18o_NH_tex.py
   313 2018/03/30 17:16 gits
   314 2018/03/30 18:09 gitc 'regrid CO to stutz'
   315 2018/03/30 18:09 gpthis
   316 2018/04/01 16:29 vim color_c18o_NH_tdust.py
   317 2018/04/01 16:30 python color_c18o_NH_tdust.py && python color_c18o_NH_tex.py
   318 2018/04/01 16:31 lst
   319 2018/04/02 18:13 vim color_c18o_NH_tdust.py
   320 2018/04/02 18:17 python color_c18o_NH_tdust.py
   321 2018/04/02 18:18 vim color_c18o_NH_tdust.py
   322 2018/04/02 18:18 python color_c18o_NH_tdust.py
   323 2018/04/02 18:19 vim color_c18o_NH_tdust.py
   324 2018/04/02 18:20 lst
   325 2018/04/02 18:20 python color_c18o_NH_tex.py
   326 2018/04/02 18:20 vim color_c18o_NH_tex.py
   327 2018/04/02 18:21 python color_c18o_NH_tex.py
   328 2018/04/02 18:22 vim color_c18o_NH_tex.py
   329 2018/04/02 18:22 gits
   330 2018/04/02 18:49 cp ../../13co/smooth.py .
   331 2018/04/02 18:49 vim smooth.py
   332 2018/04/02 18:49 vim smooth.py
   333 2018/04/02 18:51 python smooth.py
   334 2018/04/02 23:13 lst
   335 2018/04/02 23:13 vim repro.py
   336 2018/04/02 23:17 vim repro.py
   337 2018/04/02 23:18 python repro.py
   338 2018/04/02 23:18 vim repro.py
   339 2018/04/02 23:19 vim repro.py
   340 2018/04/02 23:19 python repro.py
   341 2018/04/02 23:19 gits
   342 2018/04/02 23:19 git checkout -f repro.py
   343 2018/04/02 23:19 gits
   344 2018/04/02 23:19 lst
   345 2018/04/02 23:20 fitsin specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb
   346 2018/04/02 23:21 regrid in=specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb.mir tin=../../12co/products/mask_imfit_12co_pix_2_Tmb.mir out=test.mir
   347 2018/04/02 23:21 lst
   348 2018/04/02 23:21 rm -r test.mir/
   349 2018/04/02 23:22 regrid in=specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb.mir tin=../../12co/products/mask_imfit_12co_pix_2_Tmb.mir out=regrid_12co_specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb.mir
   350 2018/04/02 23:59 fitsout regrid_12co_specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb
   351 2018/04/03 9:47 ds9 regrid_12co_specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb.fits
   352 2018/04/03 9:50 rm ../../Alyssa/mask_imfit_c18o_pix_2_Tmb.fits
   353 2018/04/03 9:50 rm ../../Alyssa/mask_imfit_13co_pix_2_Tmb.fits
   354 2018/04/03 9:50 cp regrid_12co_specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb.fits ../../Alyssa/
   355 2018/04/03 15:14 vim color_c18o_NH_tex.py
   356 2018/04/03 15:17 python color_c18o_NH_tex.py
   357 2018/04/03 15:18 cp color_c18o_NH_tex.py zoomin_color_c18o_NH_tex.py
   358 2018/04/03 15:18 git add -f zoomin_color_c18o_NH_tex.py
   359 2018/04/03 15:18 vim zoomin_color_c18o_NH_tex.py
   360 2018/04/03 15:19 python zoomin_color_c18o_NH_tex.py
   361 2018/04/05 17:08 ds9 regrid_12co_specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb.fits
   362 2018/04/26 19:14 open .
   363 2018/04/26 19:14 vim color_c18o_NH_tex.py
   364 2018/04/26 19:36 vim color_c18o_NH_tex.py
   365 2018/04/26 19:36 python color_c18o_NH_tex.py
   366 2018/04/26 19:36 vim zoomin_color_c18o_NH_tex.py
   367 2018/04/26 19:37 python zoomin_color_c18o_NH_tex.py
   368 2018/04/28 21:45 exit
     1 2018/04/30 19:20 cd GoogleDrive/c18o/products/
     2 2018/05/01 16:15 cp ../../13co/products/xcotex.py .
     3 2018/05/01 16:15 gits
     4 2018/05/01 16:15 git add -f xcotex.py
     5 2018/05/01 16:15 cp ../../13co/products/showXCO.py .
     6 2018/05/01 16:16 lst
     7 2018/05/01 16:16 gits
     8 2018/05/01 16:16 git add -f showXCO.py
     9 2018/05/01 16:16 vim xcotex.py
    10 2018/05/01 16:17 python xcotex.py
    11 2018/05/01 16:17 cp ../../13co/products/statistics_calculation.py .
    12 2018/05/01 16:17 python xcotex.py
    13 2018/05/01 16:17 ls *.fits
    14 2018/05/01 16:18 vim xcotex.py
    15 2018/05/01 16:18 ls *.fits
    16 2018/05/01 16:18 python xcotex.py
    17 2018/05/01 16:18 vim showXCO.py
    18 2018/05/01 16:19 python showXCO.py
    19 2018/05/01 16:19 cp ../../13co/products/olay4.reg .
    20 2018/05/01 16:19 python showXCO.py
    21 2018/05/01 16:20 vim showXCO.py
    22 2018/05/01 16:20 lst
    23 2018/05/01 16:20 vim showXCO.py
    24 2018/05/01 16:20 python showXCO.py
    25 2018/05/01 16:21 gits
    26 2018/05/01 16:21 gitc 'make C18O X-factor'
    27 2018/05/01 16:21 gpthis
    28 2018/05/01 16:32 gits
    29 2018/05/11 16:46 fitsout convol18_mom0_c18o_pix_2_Tmb
    30 2018/05/17 17:21 ls *.txt
    31 2018/05/17 17:21 vim GAScores.txt
    32 2018/05/17 17:21 vim GAScores_C18O_peak_velocities.txt
    33 2018/05/17 17:25 gits
    34 2018/05/17 17:25 gitlist
    35 2018/05/17 17:25 gname
    36 2018/05/17 17:26 vim show_C18O_spectra_at_Kirk_cores.py
    37 2018/05/17 17:34 ls *.pdf
    38 2018/05/17 17:37 rm averspec18number*.pdf
    39 2018/05/17 17:37 ls *.pdf
    40 2018/05/17 17:37 cp GAScores.txt ../../OrionAdust/Lane2016/
    41 2018/05/17 17:47 ls *.pdf
    42 2018/05/17 17:47 open GAScores_mom0_c18o_pix_2_Tmb.pdf
    43 2018/06/01 17:14 vim log.sh
    44 2018/06/01 17:15 regrid in=mask_imfit_c18o_pix_2_Tmb.mir tin=../../12co/products/mask_imfit_12co_pix_2_Tmb.mir out=regrid_12co_mask_imfit_c18o_pix_2_Tmb.mir axes="1,2"
    45 2018/06/01 17:15 smir
    46 2018/06/01 17:15 regrid in=mask_imfit_c18o_pix_2_Tmb.mir tin=../../12co/products/mask_imfit_12co_pix_2_Tmb.mir out=regrid_12co_mask_imfit_c18o_pix_2_Tmb.mir axes="1,2"
    47 2018/06/01 17:26 fitsout regrid_12co_mask_imfit_c18o_pix_2_Tmb
    48 2018/06/01 18:10 lst
    49 2018/06/01 18:10 vim remove4axis.py
    50 2018/06/01 18:11 lst
    51 2018/06/01 18:11 vim remove4axis.py
    52 2018/06/01 18:11 python remove4axis.py
    53 2018/06/01 18:21 lst
    54 2018/06/02 18:16 lst
    55 2018/06/07 11:59 ls *.reg
    56 2018/06/07 11:59 vim olay4.reg
    57 2018/06/07 12:00 grep Kirk *.py
    58 2018/06/07 12:00 grep kirk *.py
    59 2018/06/07 12:00 grep GAS *.py
    60 2018/06/07 12:00 vim GAScores.txt
    61 2018/06/07 12:01 vim showKirkcores.py
    62 2018/06/07 12:02 cp GAScores.txt ~/GoogleDrive/imagesSFE/
    63 2018/06/08 16:51 gits
    64 2018/06/08 17:02 convol map=mask_imfit_c18o_pix_2_Tmb.mir fwhm=32 options=final out=convol32_mask_imfit_c18o_pix_2_Tmb.mir
    65 2018/06/08 17:17 lst
    66 2018/06/08 17:17 fitsout convol32_mask_imfit_c18o_pix_2_Tmb
    67 2018/06/08 17:22 rm -r convol32_mask_imfit_c18o_pix_2_Tmb.mir/
    68 2018/06/12 16:48 vim showKirkcores.py
    69 2018/06/12 17:02 ls *.pdf
    70 2018/06/12 17:02 open GAScores_mom0_c18o_pix_2_Tmb.pdf
    71 2018/06/13 11:50 grep genfromtxt *.py
    72 2018/06/13 20:51 grep writeto *.py
    73 2018/06/14 14:14 ls convol32_mask_imfit_c18o_pix_2_Tmb.fits
    74 2018/06/14 14:14 ds9 convol32_mask_imfit_c18o_pix_2_Tmb.fits &
    75 2018/06/14 14:16 ds9 mask_imfit_c18o_pix_2_Tmb.fits &
    76 2018/06/22 15:47 ls -thld *.fits | grep G
    77 2018/06/22 15:48 grep specsmooth casa*.log
    78 2018/06/22 15:48 grep smooth casa*.log
    79 2018/06/22 15:48 grep smooth ipython-20171125-*.log
    80 2018/06/22 15:48 grep spec ipython-20171125-*.log
    81 2018/06/22 15:49 vim log.sh
    82 2018/06/22 15:58 ls *.fits | grep han1
    83 2018/06/22 15:58 ds9 mask_han1_mask_imfit_c18o_pix_2_Tmb.fits
    84 2018/06/22 15:59 rm -r han1_mask_imfit_c18o_pix_2_Tmb.im/
    85 2018/06/22 16:01 ls *.fits | grep han1
    86 2018/06/22 16:02 ds9 nostokes_han1_mask_imfit_c18o_pix_2_Tmb.fits
    87 2018/06/22 16:02 rm nostokes_han1_mask_imfit_c18o_pix_2_Tmb.fits
    88 2018/06/22 16:02 ls *.fits | grep han1
    89 2018/06/22 16:02 ds9 mask_han1_mask_imfit_c18o_pix_2_Tmb.fits
    90 2018/06/22 16:02 ls ~/GoogleDrive/Alyssa/
   105 2018/06/26 15:43 cd -
   106 2018/06/27 10:15 convol map=specsmooth_0p25_convol_12co_mask_imfit_c18o_pix_2_Tmb.mir fwhm=32 options=final out=convol32_specsmooth_0p25_convol_12co_mask_imfit_c18o_pix_2_Tmb.mir
   107 2018/06/27 10:16 convol map=specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb.mir fwhm=32 options=final out=convol32_specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb.mir
   108 2018/06/27 10:21 lst
   109 2018/06/27 10:21 fitsout convol32_specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb
   110 2018/07/04 18:24 grep *.tight
   111 2018/07/04 18:24 grep tight *.py
     1 2018/07/15 23:17 cd GoogleDrive/c18o/products/
     2 2018/07/15 23:17 ls *.py
     3 2018/07/15 23:17 vim showKirkcores.py
     4 2018/07/15 23:18 cp showKirkcores.py ../../OrionAdust/herschelAmelia/
   118 2018/08/17 17:24 cd ../../c18o/products/
   119 2018/08/17 17:24 vim showmom0.py
   120 2018/08/17 17:24 python showmom0.py
   121 2018/08/17 17:25 lst
   122 2018/08/20 15:21 vim showmom0.py
   123 2018/08/20 15:21 python showmom0.py
   124 2018/08/20 15:21 lst
   125 2018/08/20 15:22 ds9 18mom0mask.fits
   349 2019/04/06 22:52 cd ../../c18o/products/
   350 2019/04/06 22:52 ls
   351 2019/04/06 22:53 ds9 mask_imfit_c18o_pix_2_Tmb.fits &
   352 2019/04/09 14:45 ls -d *.mir
   353 2019/04/09 14:46 ds9 mask_imfit_c18o_pix_2_Tmb.fits &
   354 2019/04/09 14:47 which imsub
   355 2019/04/09 14:50 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=imsub_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(435,860,910,1346)(65,80)"
   356 2019/04/09 14:50 fitsout imsub_mask_imfit_c18o_pix_2_Tmb
   357 2019/04/09 14:50 lst
   358 2019/04/09 14:51 mv imsub_mask_imfit_c18o_pix_2_Tmb.fits /Users/shuokong/GoogleDrive/ALMA/ALMAproposalC7/OMC6fil
   359 2019/04/09 14:51 mv imsub_mask_imfit_c18o_pix_2_Tmb.mir /Users/shuokong/GoogleDrive/ALMA/ALMAproposalC7/OMC6fil
   360 2019/04/09 15:13 ls *.pdf
   361 2019/04/09 15:13 open mom0_c18o_pix_2_Tmb.pdf
   353 2019/04/17 15:45 cd ~/GoogleDrive/c18o/products/
   354 2019/04/17 15:45 ds9 mask_imfit_c18o_pix_2_Tmb.fits &
   355 2019/04/17 15:45 lst
   359 2019/04/17 15:46 cd -
   362 2019/04/17 15:47 cd -
   363 2019/04/17 15:47 vim log.sh
   364 2019/04/17 15:47 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=imsub_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(435,860,910,1346)"
   365 2019/04/17 15:49 lst
   366 2019/04/17 15:49 fitsout imsub_mask_imfit_c18o_pix_2_Tmb
   367 2019/04/17 15:50 ds9 imsub_mask_imfit_c18o_pix_2_Tmb.fits &
   368 2019/04/17 16:54 gits
   369 2019/04/17 16:57 cd ../c18o/products/
   370 2019/04/17 16:57 ls
   371 2019/04/17 16:58 cp ../../ALMA/ALMAproposalC7/OMC6fil/mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits .
   372 2019/04/17 16:58 ds9 mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits &
   372 2019/04/17 16:58 ds9 mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits &
   373 2019/04/17 17:10 ds9 mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits &
   369 2019/04/17 16:56 vim pvmap_orion.py
   374 2019/04/17 21:59 lst
   375 2019/04/17 22:04 lst
   376 2019/04/17 22:04 python pvextractOMC6.py
   377 2019/04/17 22:05 python pvextractOMC6.py
   378 2019/04/17 22:06 python pvextractOMC6.py
   379 2019/04/17 22:06 lst
   380 2019/04/17 22:06 open omc6_pv.pdf
   381 2019/04/17 22:10 open omc6_pv.pdf
   382 2019/04/17 22:42 lst
   383 2019/04/17 22:42 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   384 2019/04/17 22:47 python pvextractOMC6.py
   385 2019/04/17 22:48 python pvextractOMC6.py
   386 2019/04/17 22:49 python pvextractOMC6.py
   387 2019/04/17 22:49 lst
   388 2019/04/17 22:49 open omc6_pv.pdf
   389 2019/04/17 22:49 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   390 2019/04/17 22:53 python pvextractOMC6.py
   391 2019/04/17 22:53 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   392 2019/04/17 22:56 python pvextractOMC6.py
   393 2019/04/17 22:56 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   394 2019/04/17 22:56 python pvextractOMC6.py
   395 2019/04/17 22:57 lst
   396 2019/04/17 22:57 open omc6_pv.pdf
   370 2019/04/17 21:50 vim pvextractOMC6.py
   371 2019/04/17 22:57 ds9 imsub_mask_imfit_c18o_pix_2_Tmb.fits &
   397 2019/04/17 22:57 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   405 2019/04/18 8:09 cd ../c18o/products/
   406 2019/04/18 8:09 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   407 2019/04/18 8:11 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   407 2019/04/18 8:11 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   408 2019/04/18 8:15 lst
   409 2019/04/18 8:15 python pvextractOMC6.py
   410 2019/04/18 8:15 python pvextractOMC6.py
   411 2019/04/18 8:16 vim ../../OrionAdust/Lane2016/show_vdiff13_Kirk10.py
   412 2019/04/18 8:21 lst
   413 2019/04/18 8:21 lst
   414 2019/04/18 8:21 python pvextractOMC6.py
   415 2019/04/18 8:22 vim ../../OrionAdust/Lane2016/show_vdiff13_Kirk10.py
   416 2019/04/18 8:22 python pvextractOMC6.py
   417 2019/04/18 8:22 vim ../../OrionAdust/Lane2016/show_vdiff13_Kirk10.py
   418 2019/04/18 8:24 python pvextractOMC6.py
   419 2019/04/18 8:25 vim ../../OrionAdust/Lane2016/show_vdiff13_Kirk10.py
   420 2019/04/18 8:26 python pvextractOMC6.py
   421 2019/04/18 8:27 python pvextractOMC6.py
   422 2019/04/18 8:30 lst
   423 2019/04/18 8:30 vim log.sh
   424 2019/04/18 8:31 rm -rf imsub_mask_imfit_c18o_pix_2_Tmb.*
   425 2019/04/18 8:31 vim imsub.csh
   426 2019/04/18 8:32 ds9 mask_imfit_c18o_pix_2_Tmb.fits
   426 2019/04/18 8:32 ds9 mask_imfit_c18o_pix_2_Tmb.fits
   427 2019/04/18 8:32 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=imsub_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(4
   428 2019/04/18 8:33 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=imsub_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(435,860,910,1346)(44,117)"
   429 2019/04/18 8:33 fitsout imsub_mask_imfit_c18o_pix_2_Tmb
   430 2019/04/18 8:33 lst
   431 2019/04/18 8:33 ds9 imsub_mask_imfit_c18o_pix_2_Tmb.fits
   432 2019/04/18 8:34 python pvextractOMC6.py
   433 2019/04/18 8:36 lst
   434 2019/04/18 8:36 ds9 imsub_mask_imfit_c18o_pix_2_Tmb.
   435 2019/04/18 8:36 ds9 imsub_mask_imfit_c18o_pix_2_Tmb.fits
   436 2019/04/18 8:38 lst
   437 2019/04/18 8:38 open omc6_pv.pdf
   438 2019/04/18 8:38 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   439 2019/04/18 8:39 ds9 imsub_mask_imfit_c18o_pix_2_Tmb.fits
   440 2019/04/18 8:41 ds9 mask_imfit_c18o_pix_2_Tmb.fits
   441 2019/04/18 8:44 ds9 slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   442 2019/04/18 8:46 python pvextractOMC6.py
   443 2019/04/18 8:49 python pvextractOMC6.py
   444 2019/04/18 8:50 python pvextractOMC6.py
   445 2019/04/18 8:51 python pvextractOMC6.py
   446 2019/04/18 8:53 python pvextractOMC6.py
   447 2019/04/18 8:53 python pvextractOMC6.py
   448 2019/04/18 8:54 python pvextractOMC6.py
   449 2019/04/18 9:47 lst
   450 2019/04/18 9:47 vim pvcuts.reg
   451 2019/04/18 9:50 python
   452 2019/04/18 9:54 lst
   453 2019/04/18 9:54 python pvextractOMC6.py
   454 2019/04/18 9:54 python pvextractOMC6.py
   455 2019/04/18 9:55 python pvextractOMC6.py
   456 2019/04/18 9:58 python pvextractOMC6.py
   457 2019/04/18 9:58 python pvextractOMC6.py
   458 2019/04/18 9:59 python pvextractOMC6.py
   459 2019/04/18 10:01 vim pvcuts.reg
   460 2019/04/18 10:08 vim ds9.reg
   461 2019/04/18 10:14 lst
   462 2019/04/18 10:14 mkdir pvcuts
   463 2019/04/18 10:14 lst
   464 2019/04/18 10:14 python pvextractOMC6.py
   372 2019/04/17 22:57 vim pvextractOMC6.py
   373 2019/04/18 10:18 gits
   374 2019/04/18 10:18 git add -f pvextractOMC6.py
   375 2019/04/18 10:18 lst
   376 2019/04/18 10:18 rm slice_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   377 2019/04/18 10:18 mv slice*.fits pvcuts/
   378 2019/04/18 10:18 lst
   379 2019/04/18 10:18 mv pvcuts.reg pvcuts
   380 2019/04/18 10:18 rm omc6_pv.pdf
   381 2019/04/18 10:19 vim pvextractOMC6.py
   382 2019/04/18 10:19 lst
   383 2019/04/18 10:19 open ds9.ps
   465 2019/04/18 10:21 mkdir ~/GoogleDrive/imagesSFE/pvcuts
   384 2019/04/18 10:20 vim pvextractOMC6.py
   385 2019/04/18 10:21 cp pvcuts/*.pdf ~/GoogleDrive/imagesSFE/pvcuts/
   386 2019/04/18 10:21 open ds9.ps
   387 2019/04/18 10:22 mv pvcuts.pdf pvcuts/
   388 2019/04/18 10:22 cp pvcuts/pvcuts.pdf ~/GoogleDrive/imagesSFE/pvcuts/
   466 2019/04/18 10:23 ls *.py | grep channel
   467 2019/04/18 10:23 cp channelmap.py ../../nan12co/
   871 2019/05/28 11:07 cd ../c18o/products/
   872 2019/05/28 11:08 lst
   873 2019/05/28 11:08 ls pvcuts/
   874 2019/05/28 11:08 vim pvcuts/pvcuts.reg
   555 2019/05/29 21:49 cd ../c18o/products/
   556 2019/05/29 21:49 gits
   557 2019/05/29 21:49 lst
   883 2019/05/29 21:54 cd ..
   884 2019/05/29 21:54 lst
   885 2019/05/29 21:54 mv ~/Downloads/ORIONA_N2HP_23.4arcsec_vel0.11_sph_v1.0.fits .
   886 2019/05/29 21:54 ds9 ORIONA_N2HP_23.4arcsec_vel0.11_sph_v1.0.fits
   887 2019/05/29 21:56 mv ORIONA_N2HP_23.4arcsec_vel0.11_sph_v1.0.fits pvcuts/
   894 2019/05/30 11:20 cd ../
   895 2019/05/30 11:20 ds9 mask_imfit_c18o_pix_2_Tmb.fits
    73 2019/05/31 10:58 cd ../c18o/products/
   903 2019/06/04 15:19 cd ../../c18o/products/
   904 2019/06/04 15:19 ls *.bck
   908 2019/06/04 15:20 cd -
   909 2019/06/04 15:20 lst
   920 2019/06/09 20:21 cd ..
   921 2019/06/09 20:21 lst
   922 2019/06/09 20:21 gits
   923 2019/06/09 20:21 ds9 imsub_mask_imfit_c18o_pix_2_Tmb.fits &
   924 2019/06/09 20:21 ds9 mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits &
   925 2019/06/09 20:36 ds9 ../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits
   925 2019/06/09 20:36 ds9 ../../OrionAdust/herschelAmelia/carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits
   374 2019/06/12 11:11 cd ..
   375 2019/06/12 11:11 lst
   951 2019/06/12 11:18 cd ..
   952 2019/06/12 11:18 lst
   953 2019/06/12 11:18 python pvextractOMC6.py
   954 2019/06/12 11:27 python pvextractOMC6.py
   955 2019/06/12 11:30 python pvextractOMC6.py
   956 2019/06/12 11:32 python pvextractOMC6.py
   957 2019/06/12 11:54 python pvextractOMC6.py
   958 2019/06/12 11:55 python pvextractOMC6.py
   959 2019/06/12 12:00 python pvextractOMC6.py
   960 2019/06/12 12:02 python pvextractOMC6.py
   961 2019/06/12 12:04 python pvextractOMC6.py
   962 2019/06/12 12:05 gits
   963 2019/06/12 12:05 gitc 'improve pv'
   376 2019/06/12 11:11 vim pvextractOMC6.py
   964 2019/06/12 12:05 gpthis
   965 2019/06/12 12:10 python pvextractOMC6.py
   966 2019/06/12 12:11 python pvextractOMC6.py
   377 2019/06/12 12:09 vim pvextractOMC6.py
   378 2019/06/12 17:15 gits
   382 2019/06/19 20:29 cd ..
   383 2019/06/19 20:30 ls *.py
   384 2019/06/19 20:30 vim pvextractOMC6.py
   385 2019/06/19 20:30 cp pvextractOMC6.py convertfreq.py
   386 2019/06/19 20:31 mv convertfreq.py pvcuts/
   407 2019/06/20 9:17 cd ..
  1107 2019/06/20 9:20 cd ..
  1108 2019/06/20 9:20 ls
  1109 2019/06/20 9:20 ls *.py
  1110 2019/06/20 9:21 grep coldens *.py
  1111 2019/06/20 9:21 vim spectra.py
  1121 2019/06/20 9:28 cd ../../c18o/products/
  1122 2019/06/20 9:28 cp ../../13co/products/coldens.py .
  1123 2019/06/20 9:28 vim coldens.py
   408 2019/06/20 9:17 vim repro.py
  1126 2019/06/20 9:35 cd -
   409 2019/06/20 9:29 vim coldens.py
   410 2019/06/20 9:36 ls mom0_c18o_pix_2_Tmb.fits
  1127 2019/06/20 9:35 vim repro.py
  1128 2019/06/20 9:37 python repro.py
  1129 2019/06/20 9:37 vim repro.py
  1130 2019/06/20 9:37 python repro.py
  1131 2019/06/20 9:37 lst
  1132 2019/06/20 9:38 vim tex_pixel6_convol18.py
  1133 2019/06/20 9:38 ds9 tex_on_c18o_header.fits
  1134 2019/06/20 9:47 ds9 mom0_c18o_pix_2_Tmb.fits
   411 2019/06/20 9:39 vim coldens.py
  1135 2019/06/20 9:53 vim repro.py
  1136 2019/06/20 9:54 python repro.py
  1137 2019/06/20 9:54 lst
  1138 2019/06/20 9:54 ds9 tex_on_c18o_header.fits
   412 2019/06/20 9:55 gits
   413 2019/06/20 9:55 vim imsub_mask_imfit_c18o_pix_2_Tmb.mir/history
   414 2019/06/20 9:57 ds9 mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits
  1139 2019/06/20 9:58 ls
  1140 2019/06/20 9:58 ls mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits
  1141 2019/06/20 9:58 lst
  1142 2019/06/20 10:23 lst
  1143 2019/06/20 10:23 python coldens.py
  1144 2019/06/20 10:23 python coldens.py
  1145 2019/06/20 10:23 python coldens.py
  1146 2019/06/20 10:24 python coldens.py
  1147 2019/06/20 10:25 python coldens.py
  1148 2019/06/20 10:27 python coldens.py
  1149 2019/06/20 10:27 python coldens.py
  1150 2019/06/20 10:27 lst
  1151 2019/06/20 10:27 ds9 coldens18_thin.fits
  1152 2019/06/20 10:28 vim repro.py
  1153 2019/06/20 10:29 python repro.py
  1154 2019/06/20 10:29 vim repro.py
  1155 2019/06/20 10:29 python repro.py
   415 2019/06/20 9:58 vim coldens.py
  1156 2019/06/20 10:33 vim repro.py
  1157 2019/06/20 10:33 python repro.py
  1158 2019/06/20 10:35 vim repro.py
  1159 2019/06/20 10:36 ds9 mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits
  1160 2019/06/20 10:36 vim remove4axis.py
  1161 2019/06/20 10:39 vim repro.py
  1162 2019/06/20 10:42 cp remove4axis.py add3axis.py
  1163 2019/06/20 10:42 git add -f add3axis.py
  1164 2019/06/20 10:42 vim add3axis.py
  1165 2019/06/20 10:47 python add3axis.py
  1166 2019/06/20 10:47 lst
  1167 2019/06/20 10:47 ds9 threeaxes_carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits
  1168 2019/06/20 10:47 vim repro.py
  1169 2019/06/20 10:48 python repro.py
   416 2019/06/20 10:33 vim coldens.py
  1170 2019/06/20 10:48 vim add3axis.py
  1171 2019/06/20 10:51 lst
  1172 2019/06/20 10:51 python add3axis.py
  1173 2019/06/20 10:51 python repro.py
  1174 2019/06/20 10:51 lst
  1175 2019/06/20 10:51 ds9 dustcoldens_on_c18o_header.fits
  1176 2019/06/20 10:51 gits
   417 2019/06/20 10:49 ds9 mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits
   418 2019/06/20 10:51 git add -f coldens
   419 2019/06/20 10:51 git add -f coldens.py
  1177 2019/06/20 10:52 lst
  1178 2019/06/20 10:53 lst
  1179 2019/06/20 10:53 python coldens.py
  1180 2019/06/20 10:53 lst
  1181 2019/06/20 10:54 ds9 abun18.fits
  1182 2019/06/20 10:54 gits
  1183 2019/06/20 10:54 gitc 'get C18O abundance map'
  1184 2019/06/20 10:54 gpthis
   420 2019/06/20 10:51 vim coldens.py
   421 2019/06/20 10:59 lst
   422 2019/06/20 10:59 ls
   423 2019/06/20 10:59 ls pvcuts/
   429 2019/06/20 11:26 cd ..
   430 2019/06/20 11:26 lst
   431 2019/06/20 11:26 ds9 dustcoldens_on_c18o_header.fits
  1185 2019/06/20 10:54 ds9 abun18.fits
  1186 2019/06/20 16:23 lst
  1187 2019/06/20 16:23 python coldens.py
  1188 2019/06/20 16:25 python coldens.py
  1189 2019/06/20 16:25 lst
  1190 2019/06/20 16:25 ds9 coldens18_thin.fits
   432 2019/06/20 16:19 vim coldens.py
   433 2019/06/20 16:28 gits
   434 2019/06/20 16:28 git checkout -f master
   435 2019/06/20 16:28 gits
  1191 2019/06/21 8:43 vim log.sh
  1192 2019/06/21 10:10 ds9 mom0_imsub_mask_imfit_c18o_pix_2_Tmb.fits &
   659 2019/06/25 13:59 cd ../../c18o/products/
   660 2019/06/25 13:59 prthd in=mask_imfit_c18o_pix_2_Tmb.mir
   661 2019/06/25 13:59 ls
   662 2019/06/25 14:00 ls *.fits
   738 2019/07/03 16:14 cd ..
   753 2019/07/04 9:37 cd ..
   754 2019/07/04 9:37 ds9 mom1_c18o_pix_2_Tmb.fits
   911 2019/07/11 22:08 cd ../../c18o/products/
   912 2019/07/11 22:08 ls
   913 2019/07/11 22:08 du -ch * | grep G
   914 2019/07/11 22:08 rm -rf c18o_pix_2_Tmb_sens.*
   915 2019/07/11 22:08 rm -rf clip5sigma_mask_imfit_c18o_pix_2_Tmb.mir/
   916 2019/07/11 22:09 rm -rf convol32_*
   917 2019/07/11 22:09 rm -rf furthersouth_mask_c18o_pix_2_Tmb.*
   918 2019/07/11 22:09 rm -rf nostokes_regrid_12co_mask_imfit_c18o_pix_2_Tmb.fits
   919 2019/07/11 22:09 rm -rf regrid*
   920 2019/07/11 22:09 rm -rf south_mask_c18o_pix_2_Tmb.*
   921 2019/07/11 22:09 rm -rf specsmooth_0p25_mask_imfit_c18o_pix_2_Tmb.*
   922 2019/07/11 22:09 du -ch * | grep G
   949 2019/07/12 14:08 cd products/
   950 2019/07/12 14:08 ls *.pdf
   951 2019/07/12 14:08 grep averspec18.pdf *.py
   952 2019/07/12 14:09 vim ~/.cshrc
   953 2019/07/12 14:10 vim ~/workinglist_tcsh
   954 2019/07/12 14:10 vim ~/.cshrc
   955 2019/07/12 14:14 source ~/.cshrc
   956 2019/07/12 14:14 which cpd
   957 2019/07/12 14:14 cpd spectra.py ../../cn
   958 2019/07/12 14:15 vim ~/.cshrc
   959 2019/07/12 14:15 source ~/.cshrc
    11 2019/10/01 17:11 cd products/
    12 2019/10/01 17:11 lst
    13 2019/10/01 17:11 ls *.reg
     3 2020/02/24 11:49 cd products/
     4 2020/02/24 11:49 ls
     5 2020/02/24 11:49 lst
     6 2020/02/24 11:49 vim log.sh
     7 2020/02/24 11:50 gits
    12 2020/02/24 11:50 cd products/
    13 2020/02/24 11:50 ls
    14 2020/02/24 11:50 lst
    15 2020/02/24 11:53 vim lo
    16 2020/02/24 11:53 vim log.sh
    17 2020/02/24 11:53 grep omc6 *.py
    18 2020/02/24 14:59 gits
    24 2020/02/24 15:00 cd products/
    25 2020/02/24 15:00 lst
    26 2020/02/24 15:00 gits
    27 2020/02/24 15:01 gitlist
    28 2020/02/24 15:01 git diff
    29 2020/02/24 15:04 gitlist
    30 2020/02/24 15:04 gits
     7 2020/02/24 15:29 cd products/
     8 2020/02/24 15:29 gits
     9 2020/02/24 15:30 gits | grep pvcuts
    10 2020/02/24 15:30 git diff --follow pvcuts/lanecores.reg
    11 2020/02/24 15:30 git diff --follow pvcuts/showc18omom0.py
    12 2020/02/24 15:30 git diff --follow pvcuts/showomc6.py
    13 2020/02/24 15:30 git diff --follow pvcuts/showomc6multi.py
    14 2020/02/24 15:31 gits
    57 2020/02/24 15:32 cd ../../c18o/products/
    58 2020/02/24 15:32 git diff
    59 2020/02/24 15:32 gits
    60 2020/02/24 15:32 git diff
    15 2020/02/24 15:33 cp pvcuts/showomc6multi.py ~
    16 2020/02/24 15:33 git checkout -f master
    17 2020/02/24 15:33 gits
    18 2020/02/24 15:33 mv ~/showomc6multi.py pvcuts/
    19 2020/02/24 15:33 gits
    61 2020/02/24 15:40 open pvcuts/omc6multi.pdf
    30 2020/03/09 16:43 cd ~/GoogleDrive/c18o/products/
    31 2020/03/09 16:43 lst
    38 2020/03/09 16:46 cd ..
    39 2020/03/09 16:46 ls *.fits
    40 2020/03/09 16:46 mds9 central_mask_c18o_pix_2_Tmb.fits
    41 2020/03/09 16:47 mds9 imsub_mask_imfit_c18o_pix_2_Tmb.fits
    42 2020/03/09 16:52 ipython
    43 2020/03/09 16:56 convol map=imsub_mask_imfit_c18o_pix_2_Tmb.mir fwhm=28 options=final out=convol28_imsub_mask_imfit_c18o_pix_2_Tmb.mir
    44 2020/03/09 16:56 smir
    45 2020/03/09 16:56 convol map=imsub_mask_imfit_c18o_pix_2_Tmb.mir fwhm=28 options=final out=convol28_imsub_mask_imfit_c18o_pix_2_Tmb.mir
    46 2020/03/09 16:56 lst
    47 2020/03/09 16:56 mv convol28_imsub_mask_imfit_c18o_pix_2_Tmb.mir pvcuts/
    25 2020/03/09 16:58 cd ~/GoogleDrive/c18o/products/
    26 2020/03/09 16:58 ls *.py
    27 2020/03/09 16:58 vim spectra.py
    28 2020/03/09 16:58 vim spectra.py
    29 2020/03/09 16:59 cp spectra.py getspec.py
    30 2020/03/09 16:59 gits
    31 2020/03/09 16:59 vim getspec.py
    32 2020/03/09 17:09 grep beampix *.py
    33 2020/03/09 17:10 cp show_C18O_spectra_at_Lane_cores.py getspec.py
    34 2020/03/09 17:10 mv getspec.py smoothed_C18O_spectra_at_Lane_cores.py
    35 2020/03/09 17:10 gits
    36 2020/03/09 17:11 vim smoothed_C18O_spectra_at_Lane_cores.py
    37 2020/03/09 17:11 lst
    38 2020/03/09 17:11 vim show_C18O_spectra_at_Lane_cores.py
    39 2020/03/09 17:11 open Lane_cores_spectra/
    40 2020/03/09 17:12 mv smoothed_C18O_spectra_at_Lane_cores.py pvcuts/
    46 2020/03/09 22:13 cd ..
    47 2020/03/09 22:13 vim log.sh
    48 2020/03/09 22:13 convol map=mask_imfit_c18o_pix_2_Tmb.mir fwhm=28 options=final out=convol28_mask_imfit_c18o_pix_2_Tmb.mir
    49 2020/03/09 22:13 smir
    50 2020/03/09 22:13 convol map=mask_imfit_c18o_pix_2_Tmb.mir fwhm=28 options=final out=convol28_mask_imfit_c18o_pix_2_Tmb.mir
    51 2020/03/09 22:15 lst
    52 2020/03/09 22:15 mirout convol28_mask_imfit_c18o_pix_2_Tmb.mir
    53 2020/03/09 22:15 lst
    54 2020/03/09 22:16 mv convol28_mask_imfit_c18o_pix_2_Tmb.* pvcuts/
    53 2020/03/10 10:57 cd -
   159 2020/03/10 15:30 cd ..
   160 2020/03/10 15:30 vim log.sh
   161 2020/03/10 15:30 convol map=mask_imfit_c18o_pix_2_Tmb.mir fwhm=70 options=final out=convol70_mask_imfit_c18o_pix_2_Tmb.mir
   162 2020/03/10 15:32 mirout convol70_mask_imfit_c18o_pix_2_Tmb.mir
   189 2020/03/10 15:55 cd ..
   190 2020/03/10 15:55 ls *.bck
   194 2020/03/25 21:23 cd products/
   195 2020/03/25 21:23 vim log.sh
   196 2020/03/25 21:24 mds9 imsub_mask_imfit_c18o_pix_2_Tmb.fits
   197 2020/03/25 21:32 mds9 mask_imfit_c18o_pix_2_Tmb.fits
     1 2020/03/25 22:23 source ~/.cshrc
     2 2020/03/25 22:23 vim log.sh
     3 2020/03/25 22:24 smir
     4 2020/03/25 22:30 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(162,554,910,1346)"
     5 2020/03/25 22:31 mirout stick_mask_imfit_c18o_pix_2_Tmb.mir
     6 2020/03/25 22:31 mv stick_mask_imfit_c18o_pix_2_Tmb.fits ../../omc6datacollection/CARMA_NRO45_combine/
     7 2020/03/25 22:31 rm -rf stick_mask_imfit_c18o_pix_2_Tmb.mir/
     8 2020/03/25 22:32 mds9 ../../omc6datacollection/CARMA_NRO45_combine/stick_mask_imfit_c18o_pix_2_Tmb.fits
   198 2020/03/25 22:20 mds9 mask_imfit_c18o_pix_2_Tmb.fits
   198 2020/03/25 22:20 mds9 mask_imfit_c18o_pix_2_Tmb.fits
    31 2020/03/29 11:38 cd ..
    32 2020/03/29 11:38 vim pvextractOMC6.py
    35 2020/03/29 11:39 cd ..
    36 2020/03/29 11:39 vim pvextractOMC6.py
    37 2020/03/29 11:41 gits
    38 2020/03/29 11:41 vim pvextractOMC6.py
    39 2020/03/29 11:42 gits
    40 2020/03/29 11:42 python pvextractOMC6.py
    41 2020/03/29 11:43 which python
    42 2020/03/29 11:43 ls ~/anaconda/envs/
    43 2020/03/29 11:43 pip install pvextractor
    44 2020/03/29 11:53 ls ~/anaconda/envs/
    45 2020/03/29 11:53 python pvextractOMC6.py
    46 2020/03/29 11:54 vim pvextractOMC6.py
    47 2020/03/29 11:54 python pvextractOMC6.py
    48 2020/03/29 11:54 lst
    49 2020/03/29 11:54 cp test.pdf ~/OneDrive\ -\ University\ of\ Arizona/2020/JCMT2020B/pv.pdf
    50 2020/03/29 11:54 git checkout -f pvextractOMC6.py
    51 2020/03/29 11:54 gits
    24 2020/04/03 22:07 cd ..
    25 2020/04/03 22:07 lst
    26 2020/04/03 22:08 ls *.fits
    27 2020/04/03 22:24 mds9 ~/GoogleDrive/omc6datacollection/CARMA_NRO45_combine/stick_mask_imfit_c18o_pix_2_Tmb.fits &
    28 2020/04/03 22:34 mds9 mask_han1_mask_imfit_c18o_pix_2_Tmb.fits &
    29 2020/04/04 21:20 lst
    37 2020/04/04 21:51 cd ../
    38 2020/04/04 21:51 smir
    39 2020/04/04 21:51 mirin mask_han1_mask_imfit_c18o_pix_2_Tmb.fits
    40 2020/04/04 21:51 lst
    41 2020/04/04 21:51 vim log.sh
    42 2020/04/04 21:52 imsub in=mask_han1_mask_imfit_c18o_pix_2_Tmb.mir out=stick_han1_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(162,554,910,1346)"
    43 2020/04/04 21:52 mirout stick_han1_mask_imfit_c18o_pix_2_Tmb.mir
    44 2020/04/04 21:53 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
    45 2020/04/04 21:53 lst
    46 2020/04/04 21:54 ls -thld mask_han1_mask_imfit_c18o_pix_2_Tmb.fits
    47 2020/04/04 21:54 gits
    48 2020/04/04 21:54 git add -f log.sh
    53 2020/04/04 21:56 cd ..
    54 2020/04/04 21:56 lst
    55 2020/04/04 21:57 moment in=stick_han1_mask_imfit_c18o_pix_2_Tmb.mir out=mom0_stick_han1_mask_imfit_c18o_pix_2_Tmb.mir mom=0
    56 2020/04/04 21:57 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
    57 2020/04/04 21:58 mirout mom0_stick_han1_mask_imfit_c18o_pix_2_Tmb.mir
    58 2020/04/04 21:58 lst
    59 2020/04/04 21:58 mds9 mom0_stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
    60 2020/04/04 21:59 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
    61 2020/04/04 22:01 lst
    62 2020/04/04 22:01 rm -rf mom0_stick_han1_mask_imfit_c18o_pix_2_Tmb.*
    63 2020/04/04 22:01 moment in=stick_han1_mask_imfit_c18o_pix_2_Tmb.mir out=mom0_stick_han1_mask_imfit_c18o_pix_2_Tmb.mir mom=0 region="images(30,42)"
    64 2020/04/04 22:01 mirout mom0_stick_han1_mask_imfit_c18o_pix_2_Tmb.mir
    65 2020/04/04 22:01 mds9 mom0_stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
    66 2020/04/04 22:03 lst
    67 2020/04/04 22:03 rm -rf mom0_stick_han1_mask_imfit_c18o_pix_2_Tmb.*
    68 2020/04/04 22:03 rm -rf stick_han1_mask_imfit_c18o_pix_2_Tmb.mir/
    69 2020/04/04 22:03 lst
    70 2020/04/04 22:03 ls mom0_c18o_pix_2_Tmb.fits
    71 2020/04/04 22:04 mds9 mom0_c18o_pix_2_Tmb.fits
    72 2020/04/04 22:06 ls *.fits
    73 2020/04/04 22:07 ls ../.fits
    74 2020/04/04 22:07 ls ../*.fits
    75 2020/04/04 22:08 cp ../../omc6datacollection/CARMA_NRO45_combine/stick_mask_imfit_c18o_pix_2_Tmb.fits .
    76 2020/04/04 22:08 lst
    77 2020/04/04 22:08 mirin stick_mask_imfit_c18o_pix_2_Tmb.fits
    78 2020/04/04 22:09 moment in=stick_mask_imfit_c18o_pix_2_Tmb.mir out=mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir mom=0 region="kms,images(6.7,9.3)"
    79 2020/04/04 22:09 mds9 stick_mask_imfit_c18o_pix_2_Tmb.fits
    80 2020/04/04 22:10 rm -rf mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir/
    81 2020/04/04 22:10 moment in=stick_mask_imfit_c18o_pix_2_Tmb.mir out=mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir mom=0 region="kms,images(6.7,9.1)"
    82 2020/04/04 22:10 mirout mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir
    83 2020/04/04 22:10 mds9 mom0_stick_mask_imfit_c18o_pix_2_Tmb.fits
    74 2020/04/05 18:01 cd ..
    75 2020/04/05 18:01 lst
    76 2020/04/05 18:01 vim log.sh
    77 2020/04/05 18:02 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(162,554,930,1346)"
    78 2020/04/05 18:02 rm -rf stick_mask_imfit_c18o_pix_2_Tmb.*
    79 2020/04/05 18:02 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(162,554,930,1346)"
    80 2020/04/05 18:02 vim log.sh
    81 2020/04/05 18:03 vim mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir/history
    82 2020/04/05 18:03 vim log.sh
    83 2020/04/05 18:04 rm -rf mom0_stick_mask_imfit_c18o_pix_2_Tmb.*
    84 2020/04/05 18:05 moment in=stick_mask_imfit_c18o_pix_2_Tmb.mir out=mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir mom=0 region="kms,images(6.7,9.1)"
    85 2020/04/05 18:05 mirout mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir
    89 2020/04/05 18:05 cd -
    90 2020/04/05 18:05 lst
    91 2020/04/05 18:06 rm -rf stick_mask_imfit_c18o_pix_2_Tmb.mir/
    92 2020/04/05 18:06 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(162,554,1000,1346)"
    93 2020/04/05 18:06 rm -rf mom0_stick_mask_imfit_c18o_pix_2_Tmb.*
    94 2020/04/05 18:06 moment in=stick_mask_imfit_c18o_pix_2_Tmb.mir out=mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir mom=0 region="kms,images(6.7,9.1)"
    95 2020/04/05 18:06 mirout mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir
    98 2020/04/05 18:06 cd -
    99 2020/04/05 18:07 lst
   100 2020/04/05 18:07 mirout stick_mask_imfit_c18o_pix_2_Tmb.mir
   101 2020/04/05 18:07 cp stick_mask_imfit_c18o_pix_2_Tmb.fits ~/GoogleDrive/omc6datacollection/CARMA_NRO45_combine/
   102 2020/04/05 18:07 rm -rf stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
   103 2020/04/05 18:08 vim log.sh
   104 2020/04/05 18:08 imsub in=mask_han1_mask_imfit_c18o_pix_2_Tmb.mir out=stick_han1_mask_imfit_c18o_pix_2_Tmb.mir region="abspix,boxes(162,554,1000,1346)"
   105 2020/04/05 18:09 mirout stick_han1_mask_imfit_c18o_pix_2_Tmb.mir
    18 2020/04/06 10:42 cd ~/GoogleDrive/c18o/products/
    19 2020/04/06 10:42 vim coldens.py
    20 2020/04/06 10:43 git log -p --follow coldens.py
    21 2020/04/06 10:43 grep coldens *.py
    22 2020/04/06 11:35 rm -rf ~/Downloads/combined_scalefactor_c18o.SNR/
    23 2020/04/06 11:35 rm -rf ~/Downloads/image.download/
    24 2020/04/06 11:36 ls -thld * | grep sen
    25 2020/04/06 11:36 vim sen.py
    26 2020/04/06 11:37 ls *.fits
    27 2020/04/06 11:37 ls *.fits | grep sen
    28 2020/04/06 11:37 vim sen.py
    29 2020/04/06 11:38 gname
    30 2020/04/06 11:39 vim sen.py
    31 2020/04/06 11:40 vim log.sh
    32 2020/04/06 11:43 vim sen.py
    33 2020/04/06 11:46 rm -rf ~/Downloads/c18o.150.sen-20200406T183627Z-001.zip
    34 2020/04/06 11:49 mkdir combined_scalefactor_c18o.sen
    35 2020/04/06 11:49 mv ~/Downloads/header combined_scalefactor_c18o.sen/
    36 2020/04/06 11:49 mv ~/Downloads/history combined_scalefactor_c18o.sen/
    37 2020/04/06 11:49 mv ~/Downloads/mask combined_scalefactor_c18o.sen/
    38 2020/04/06 11:53 mv ~/Downloads/image combined_scalefactor_c18o.sen/
    39 2020/04/06 11:53 lst
    40 2020/04/06 11:55 vim log.sh
    41 2020/04/06 11:56 imsub in=combined_scalefactor_c18o.sen out=stick_sen.mir region="abspix,boxes(162,554,1000,1346)"
    42 2020/04/06 11:56 smir
    43 2020/04/06 11:56 imsub in=combined_scalefactor_c18o.sen out=stick_sen.mir region="abspix,boxes(162,554,1000,1346)"
    44 2020/04/06 11:56 vim log.sh
    45 2020/04/06 11:57 moment in=stick_sen.mir out=mom0_stick_sen.mir mom=0 region="kms,images(6.7,9.1)"
    46 2020/04/06 11:57 mirout mom0_stick_sen.mir
    47 2020/04/06 11:57 lst
    48 2020/04/06 11:57 mds9 mom0_stick_sen.fits
    49 2020/04/06 11:59 vim repro.py
    50 2020/04/06 12:00 gits
    51 2020/04/06 12:00 python repro.py
    52 2020/04/06 12:01 lst
    53 2020/04/06 12:02 prthd in=combined_scalefactor_c18o.sen
    54 2020/04/06 12:02 vim mask_imfit_c18o_pix_2_Tmb.mir/history
    55 2020/04/06 12:03 lst
    56 2020/04/06 12:03 python coldens.py
    57 2020/04/06 12:03 lst
    58 2020/04/06 12:03 mds9 abun18.fits
     1 2020/04/06 12:15 source ~/.cshrc
     2 2020/04/06 12:15 lst
     3 2020/04/06 12:15 python repro.py
     4 2020/04/06 12:16 vim remove4axis.py
     5 2020/04/06 12:16 vim remove4axis.py
     6 2020/04/06 12:17 prthd in=mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir
     7 2020/04/06 12:17 smir
     8 2020/04/06 12:17 prthd in=mom0_stick_mask_imfit_c18o_pix_2_Tmb.mir
     9 2020/04/06 12:17 vim remove34axes_pixel6.py
    10 2020/04/06 12:18 grep novel $DROPATH/python_scripts/*.py
    11 2020/04/06 12:18 grep novel ../../nan13co/*.py
    12 2020/04/06 12:18 grep novel ../../nan12co/*.py
    13 2020/04/06 12:18 grep novel ../../nanc18o/*.py
    14 2020/04/06 12:18 vim remove4axis.py
    15 2020/04/06 12:19 cp remove4axis.py remove3axis.py
    16 2020/04/06 12:19 git add -f remove3axis.py
    17 2020/04/06 12:19 vim remove3axis.py
    18 2020/04/06 12:20 python remove3axis.py
    19 2020/04/06 12:20 lst
    20 2020/04/06 12:20 python repro.py
    21 2020/04/06 12:21 python repro.py
    59 2020/04/06 12:07 vim repro.py
    60 2020/04/06 12:21 gits
    61 2020/04/06 12:22 lst
    22 2020/04/06 12:23 lst
    62 2020/04/06 12:23 vim repro.py
    23 2020/04/06 12:23 python repro.py
    63 2020/04/06 13:46 grep threeaxes *.py
    24 2020/04/06 13:48 lst
    64 2020/04/06 13:47 vim add3axis.py
    65 2020/04/06 13:50 gits
    66 2020/04/06 13:50 python add3axis.py
    67 2020/04/06 13:50 vim add3axis.py
    25 2020/04/06 13:51 python add3axis.py
    26 2020/04/06 13:51 python add3axis.py
    27 2020/04/06 13:52 lst
    28 2020/04/06 13:52 mds9 threeaxes_dustT_on_stick_header.fits
    68 2020/04/06 13:51 vim add3axis.py
    69 2020/04/06 13:54 git diff --follow coldens.py
    70 2020/04/06 13:57 lst
    71 2020/04/06 13:57 python coldens.py
    72 2020/04/06 13:57 lst
    73 2020/04/06 13:57 mds9 abun18tdust.fits
    74 2020/04/06 13:57 mds9 abun18tkin.fits
    75 2020/04/06 13:58 mds9 ../../AncillaryData/GBT/OrionA_Tkin_DR1_rebase3_flag.fits
    76 2020/04/06 13:59 lst
    77 2020/04/06 14:00 rm threeaxes_dustK_on_stick_header.fits
    78 2020/04/06 14:00 rm dustK_on_stick_header.fits
    79 2020/04/06 14:00 lst
    80 2020/04/06 14:01 ls *.fits | grep dustK
    81 2020/04/06 14:01 vim repro.py
    82 2020/04/06 14:01 python repro.py
    83 2020/04/06 14:02 vim add3axis.py
    84 2020/04/06 14:04 python add3axis.py
    85 2020/04/06 14:04 lst
    86 2020/04/06 14:05 python coldens.py
    87 2020/04/06 14:05 lst
    88 2020/04/06 14:05 mds9 abun18tkin.fits
    89 2020/04/06 14:23 lst
    29 2020/04/06 14:42 lst
    30 2020/04/06 14:42 python coldens.py
    90 2020/04/06 14:41 vim coldens.py
    91 2020/04/06 20:32 vim repro.py
    92 2020/04/06 20:42 lst
    93 2020/04/06 20:43 mds9 tex_on_stick_header.fits -region pvcuts/stickbody.reg &
    94 2020/04/07 14:38 lst
     1 2020/04/07 17:02 source ~/.cshrc
    31 2020/04/08 10:08 python coldens.py
    32 2020/04/08 10:08 lst
    33 2020/04/08 10:09 mds9 coldens18_thin_tdust.fits
    34 2020/04/08 10:25 mds9 abun18tdust.fits
    38 2020/04/08 21:12 ls -thld * | grep han1
    39 2020/04/08 21:15 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits &
    40 2020/04/08 21:31 mds9 stick_mask_imfit_c18o_pix_2_Tmb.fits &
     4 2020/05/08 11:30 cd ~/GoogleDrive/c18o/products/
     5 2020/05/08 11:30 ls -thld *.mir
    35 2020/05/08 11:35 cd ../c18o/products/
    36 2020/05/08 11:35 lst
    37 2020/05/08 11:36 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
    38 2020/05/08 11:38 vim log.sh
    39 2020/05/08 11:38 vim pvcuts/log.sh
    40 2020/05/08 11:39 maths exp="<stick_han1_mask_imfit_c18o_pix_2_Tmb.mir>" region="abspix,images(37,38)" out=ringchan_stick_han1_mask_imfit_c18o_pix_2_Tmb.mir
    41 2020/05/08 11:39 smir
    42 2020/05/08 11:39 maths exp="<stick_han1_mask_imfit_c18o_pix_2_Tmb.mir>" region="abspix,images(37,38)" out=ringchan_stick_han1_mask_imfit_c18o_pix_2_Tmb.mir
    43 2020/05/08 11:40 mirout ringchan_stick_han1_mask_imfit_c18o_pix_2_Tmb.mir
    44 2020/05/08 11:40 lst
    45 2020/05/08 11:40 mds9 ringchan_stick_han1_mask_imfit_c18o_pix_2_Tmb.fits &
    46 2020/05/08 11:41 ls ~/GoogleDrive/2020/VLA2020DDT/
    68 2020/05/29 14:58 cd ~/GoogleDrive/c18o/products/
    69 2020/05/29 14:58 mds9 imsub_mask_imfit_c18o_pix_2_Tmb.fits
    70 2020/05/29 14:59 vim imsub.csh
    71 2020/05/29 14:59 vim log.sh
    72 2020/05/29 15:00 which imsub
    73 2020/05/29 15:00 smir
    74 2020/05/29 15:00 which smir
    75 2020/05/29 15:00 vim ~/workinglist_tcsh
    76 2020/05/29 15:00 source ~/workinglist_tcsh
    77 2020/05/29 15:00 smir
    78 2020/05/29 15:03 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick.mir region="abspix,boxes(417,847,928,1359)(81,88)"
    79 2020/05/29 15:03 which fitsout
    80 2020/05/29 15:03 mirout
    81 2020/05/29 15:04 fits in=mask_imfit_c18o_pix_2_Tmb.fits op=xyin out=mask_imfit_c18o_pix_2_Tmb.mir
    82 2020/05/29 15:10 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick.mir region="abspix,boxes(417,847,928,1359)(81,88)"
    83 2020/05/29 15:10 lst
    84 2020/05/29 15:10 fits in=stick.mir op=xyout out=stick.fits
    85 2020/05/29 15:10 lst
    86 2020/05/29 15:10 mds9 stick.fits
    87 2020/05/29 15:11 rm stick.fits
    88 2020/05/29 15:11 rm -rf stick.mir/
    89 2020/05/29 15:11 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick.mir region="abspix,boxes(417,847,928,1358)(81,88)"
    90 2020/05/29 15:11 fits in=stick.mir op=xyout out=stick.fits
    91 2020/05/29 15:12 scp stick.fits sk2534@grace.hpc.yale.edu:/home/sk2534/project/athenapp/athenarun/python/
    92 2020/05/29 15:15 vim remove4axis.py
    93 2020/05/29 15:15 grep fits.open *.py
    94 2020/05/29 15:15 vim usenanmask.py
    95 2020/05/29 15:16 grep fits.writeto *.py
    96 2020/05/29 15:16 vim repro.py
    97 2020/05/29 15:17 mds9 stick.fits
    98 2020/05/29 15:56 rm -r stick.*
    99 2020/05/29 15:57 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick.mir region="abspix,boxes(1,1,128,128)(81,88)"
   100 2020/05/29 15:57 fits in=stick.mir op=xyout out=stick.fits
   101 2020/05/29 15:57 mds9 stick.fits
   102 2020/05/29 15:57 scp stick.fits sk2534@grace.hpc.yale.edu:/home/sk2534/project/athenapp/athenarun/python/
   103 2020/05/29 15:57 lst
   104 2020/05/29 19:00 rm -r stick.*
   105 2020/05/29 19:00 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick.mir region="abspix,boxes(1,1,128,128)(1,20)"
   106 2020/05/29 19:00 fits in=stick.mir op=xyout out=stick.fits
   107 2020/05/29 19:00 scp stick.fits sk2534@grace.hpc.yale.edu:/home/sk2534/project/athenapp/athenarun/python/
   112 2020/05/30 10:21 cd -
   113 2020/05/30 10:22 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=stick512.mir region="abspix,boxes(1,1,512,512)(1,20)"
   114 2020/05/30 10:22 fits in=stick512.mir op=xyout out=stick512.fits
   115 2020/05/30 10:22 scp stick512.fits sk2534@grace.hpc.yale.edu:/home/sk2534/project/athenapp/g512_4pc_isoth_grav_noTurb_rho1_b3_vcol2p0_vshear0p0_T60/python/
     2 2020/06/05 20:48 cd ../../c18o/products/
     3 2020/06/05 20:48 lst
     4 2020/06/05 20:48 rm -rf mask_imfit_c18o_pix_2_Tmb\ \(1\).mir/
     5 2020/06/05 20:48 rm -rf stick.*
     6 2020/06/05 20:49 rm -rf stick512.*
     7 2020/06/05 20:49 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
     4 2020/06/05 21:54 cd ~/GoogleDrive/c18o/products/
     5 2020/06/05 21:55 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits &
    11 2020/06/06 11:50 cd ..
    12 2020/06/06 11:50 lst
    13 2020/06/06 11:51 mds9 ../../omc6datacollection/CARMA/stick_mask_imfit_cs_pix_2_Tmb.fits &
    14 2020/06/06 11:52 mds9 ../../omc6datacollection/CARMA_NRO45_combine/stick_mask_imfit_13co_pix_2_Tmb.fits
    15 2020/06/06 11:57 mds9 ../../omc6datacollection/CARMA_NRO45_combine/stick_mask_imfit_12co_pix_2_Tmb.fits
    16 2020/06/06 12:03 mds9 ../../omc6datacollection/CARMA_NRO45_combine/stick_mask_imfit_13co_pix_2_Tmb.fits
    17 2020/06/06 18:14 ls ../../omc6datacollection/NRO45/
    18 2020/06/06 18:20 mds9 ../../omc6datacollection/NRO45/ORIONA_N2HP_23.4arcsec_vel0.11_sph_v1.0.fits
    19 2020/06/06 18:22 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
    20 2020/06/06 20:24 rm ~/Downloads/athinput.mrcol
    21 2020/06/08 8:20 rm ~/Downloads/omc123_n2hp_int.fits
    22 2020/06/08 8:21 mds9 ~/Downloads/omc123_n2hp_int.fits
    52 2020/06/08 16:02 cd ../../c18o/products/
    53 2020/06/08 16:02 mds9 mask_imfit_c18o_pix_2_Tmb.fits &
    54 2020/06/08 16:05 prthd in=mask_imfit_c18o_pix_2_Tmb.mir
    55 2020/06/08 16:06 imsub in=mask_imfit_c18o_pix_2_Tmb.mir out=omc123_c18o.mir region="boxes(1,2787,1938,3677)"
    56 2020/06/08 16:06 mirout omc123_c18o.mir
    57 2020/06/08 16:06 vim removehistory.py
    58 2020/06/08 16:06 python removehistory.py
    59 2020/06/08 16:06 lst
    60 2020/06/08 16:07 rm -rf omc123_c18o.*
    61 2020/06/08 16:07 mds9 omc123_c18o_Tmb.fits
    23 2020/06/08 14:11 mds9 ~/Downloads/omc123_n2hp_int.fits
    24 2020/06/08 20:54 mds9 omc123_c18o_Tmb.fits
    24 2020/06/08 20:54 mds9 omc123_c18o_Tmb.fits
    25 2020/06/08 21:15 mds9 omc123_c18o_Tmb.fits
    64 2020/06/18 21:24 cd ~/GoogleDrive/c18o/products/
    65 2020/06/18 21:24 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
    66 2020/06/18 21:49 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits
     4 2020/06/30 13:59 cd ~/GoogleDrive/c18o/products/
     5 2020/06/30 13:59 mds9 stick_han1_mask_imfit_c18o_pix_2_Tmb.fits &
    27 2020/07/02 10:22 cd ~/GoogleDrive/c18o/products/
    28 2020/07/02 10:22 vim log.sh
    29 2020/07/02 10:22 grep imsub log.sh | grep han1
    30 2020/07/02 10:22 ls *.reg
    31 2020/07/02 10:22 vim ds9.reg
