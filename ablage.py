from skimage.morphology import skeletonize
from skimage import data, img_as_float
import matplotlib.pyplot as plt
from skimage.util import invert
import cv2


image = cv2.imread("Byz_Mon_34.tif", cv2.IMREAD_GRAYSCALE)
image = img_as_float(image)



# Invert the horse image
image = invert(image)

# perform skeletonization
skeleton = skeletonize(image)

# display results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                         sharex=True, sharey=True)

ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('original', fontsize=20)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()