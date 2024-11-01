# Napari assistant

# The Napari Assistant

The Napari Assistant is a plugin for napari that allows you setting up an image processing workflow.

Start the `devbio` evironment and then start napari with the assistant:
```bash
mamba activate devbio
napari
```
The napari window will open. Click on the menu `File > Open Samples > napari builtins > Cells(3D+2Ch)` to open an example image.

![](./images/napari-assistant02.jpg)

![](./images/napari-assistant03.jpg)

You can explore this dataset by clicking on the `2D/3D` view button.

![](./images/napari-assistant04.jpg)

Now, let's start some processing. Enter "clesperanto" in the search field to only show functions from the clesperanto library.

![](images/filter_clesperanto.png)

Within the `Assistant` panel, click on the `Remove noise` button.

![](./images/napari-assistant06.jpg)

Click on the `Eye` buttons in the layer list to hide the original image and show the result of the `Remove noise` step only.

![](./images/napari-assistant07.jpg)

Click on the `Binarize` button in the Assistant panel to add a new step to the workflow that generates a binary image from the current layer.

![](./images/napari-assistant08.jpg)

Toggle 2D/3D view and layer visibility to explore the result of the `Binarize` step.

![](./images/napari-assistant09.jpg)

After switching back to 2D view, click the `Label` button in the Assistant and choose the operation `Connected component labeling (clEsperanto)`.

![](./images/napari-assistant11.jpg)

Select the `Result of gaussian_blur` layer in the layer list and modify its `sigma` parameters. You will note that the subsequent steps (Threshold Otsu and Connected Component Labeling) are also updated.

![](./images/napari-assistant12.jpg)

Switch to grid view, show all layers using their `Eye` buttons and continue modifying the parameters.

![](./images/napari-assistant13.jpg)

![](./images/napari-assistant14.jpg)

Close all layers except `nuclei` and `membrane`.

![](./images/napari-assistant15.jpg)

Turn of Gridview and click again on the `Label` button in the Assistant.

![](./images/napari-assistant16.jpg)

This time, do not change the operation but the `spot_sigma` parameter instead.

![](./images/napari-assistant17.jpg)

Toggle again to 3D view and inspect the result of this single step.

![](./images/napari-assistant18.jpg)








