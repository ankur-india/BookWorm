For generating data for testing/training purposes, Sayamindu's suggestion to use Cairo-Pango seems to work the best.
Use the scripts in the following order:

1. generate.py : originally designed by Sayamindu and Debayan, and modified a little by me, use this to generate the	 individual images
2. batch_resize.py :  this gives the flexibility to resize the images, as I found it better to use a mixed sample
3. use ImageMagick to merge the individual images together into one big image. the command for doing so is :
	montage img1.ext img2.ext .... imgN.ext -geometry SizexSize output.ext

NOTE : using ImageMagick is easier, and gives better results than the default output from "generate.py" when 
the sizes are changed. In that case, you can ignore the default merged image generated in step 1. 
Also, I gave up on completing my python script for merging the images (however, the notebook is 
still in repository) because ImageMagick is so easy.