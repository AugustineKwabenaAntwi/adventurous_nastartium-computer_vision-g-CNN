#libs used
  ##import numpy as np
  #import matplotlib.pyplot as plt
  #import random
def adjust_contrast(image_path):#<--takes image path
 
 #libs used
  ##import numpy as np
  #import matplotlib.pyplot as plt
  #import random

  image = cv2.imread(image_path)
  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)#rgb image

  #converting to gray to calculate for contrast and brightness
  Y = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)[:,:,0] #gray image version

  # computing min and max of Y
  min = np.min(Y)
  max = np.max(Y)

  # compute brightness
  brightness = (max+min)/2
  # compute contrast
  contrast = (max-min)/(max+min)

  ## brightness and contrast adjustment
  brightness = brightness #<--write code to provide random contrast not 0 or same but within [-255,255]
  contrast = random.uniform(0.2, 3) #<-- write code to provide random contrast not 0 or same but within [min,max] 
  image2 = cv2.convertScaleAbs(image_rgb,alpha=contrast, beta=brightness) 
  
  new_image_path = image_path.replace('.jpg', '_adjusted_contrast.jpg')
  output_path = f'/contrast_adjusted/{new_image_path}'
  cv2.imwrite(output_path, image2)