import cv2 as cv
# import numpy as np
 
#  
img = cv.imread(r'wboriginal.png')
b, g, r = cv.split(img)
r_avg = cv.mean(r)[0]
g_avg = cv.mean(g)[0]
b_avg = cv.mean(b)[0]
 
 # Find the gain of each channel
k = (r_avg + g_avg + b_avg) / 3
kr = k / r_avg
kg = k / g_avg
kb = k / b_avg
 
r = cv.addWeighted(src1=r, alpha=kr, src2=0, beta=0, gamma=0)
g = cv.addWeighted(src1=g, alpha=kg, src2=0, beta=0, gamma=0)
b = cv.addWeighted(src1=b, alpha=kb, src2=0, beta=0, gamma=0)
 
balance_img = cv.merge([b, g, r])


print(r_avg ,r_avg, r_avg)
print(k, kr, kg, kb)
print(r,g,b)
cv.imshow('Temple', balance_img)
cv.waitKey(0)
cv.destroyAllWindows()