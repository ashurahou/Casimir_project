import numpy as np
import sys


def im_svd(image, factor):
    """
    Function
    Use SVD to compress the image (presented as a numpy array)
    ---------
    Input
    image: image array
    factor: compression rate
    ---------
    Output
    compress image array
    """
    if factor > 1:
        print('Error, the compression factor cannot be larger than 1')
        sys.exit()
        
    if np.size(image[0,0])==1: #grey scale image
        image_cp = np.zeros(image.shape)
        [u,s,v] = np.linalg.svd(image)
        newlen = int(len(s)*factor)
        s_d = np.diag(s[0:newlen])
        image_cp = u[:,0:newlen].dot(s_d.dot(v[0:newlen,:]))
        image_cp= image_cp.astype('uint8')
    
    elif np.size(image[0,0])==3: #RGB image
#         image_r = image[:,:,0]
#         image_g = image[:,:,1]
#         image_b = image[:,:,2]
#         [u_r,s_r,v_r] = np.linalg.svd(image_r)
#         [u_g,s_g,v_g] = np.linalg.svd(image_g)
#         [u_b,s_b,v_b] = np.linalg.svd(image_b)
        
        image_cp = np.zeros(image.shape)
        for i in range(3):
            image_temp = image[:,:,i]
            [u,s,v] = np.linalg.svd(image_temp)
            newlen = int(len(s)*factor)
            s_d = np.diag(s[0:newlen])
#             print(newlen)            
#             print(image_cp.shape)
#             wait = input("PRESS ENTER TO CONTINUE.")
#             print("something")
            image_cp[:,:,i] = u[:,0:newlen].dot(s_d.dot(v[0:newlen,:]))
            image_cp= image_cp.astype('uint8')
    return image_cp
            
            
        
    