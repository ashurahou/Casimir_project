import numpy as np
import matplotlib.image as im
import functions as func

def im_compress(imfname, factor):
    """
    Function
    Compress the input image using SVD method
    ------
    Input
    Image file name
    ------
    Output
    Compressed image
    """
    ## import the image
    image = im.imread(imfname)

    ## compress the image
    cm_image = func.im_svd(image, factor)
    
    ## save the compressed image
    imnewname = imfname[0:-4]+'_compressed_'+str(factor)+imfname[-4:]
    im.imsave(imnewname,cm_image)