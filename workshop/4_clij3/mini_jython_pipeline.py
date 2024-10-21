# This Jython script can be run from within FIJI's script editor

from ij import IJ
from net.clesperanto import CLIJ3

cle = CLIJ3.getInstance()

imp = IJ.openImage("../../data/blobs.tif")
imp.show()

gpu_image = cle.push(imp)

blurred = cle.gaussian_blur(gpu_image, None, 1, 1, 1)
binary = cle.threshold_otsu(blurred, None)
labelled = cle.connected_component_labeling(binary, None, "box")

imp_res = cle.pull(labelled)
imp_res.show()