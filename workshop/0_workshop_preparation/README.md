# Workshop preparation

Before attending the workshop, we strongly advise to go through the workshop preparation and install the various requierements on your computer.

## Mamba / Conda

We will require `Mamba` for installing and managing python environement and packages, we strongly advise the use of [MiniForge](). Please follow their instruction for installing it on your computer. 

> [!TIP] 
> Additionnal explaination for mamba can be found [here](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html)

> [!CAUTION] 
> `Conda` should also work but will be slower for downloading and installing the dependencies

## Napari-assistant installation

Please follow this section to use pyclesperanto with the napari-assistant.
First, install the [devbio-napari](https://github.com/haesleinhuepf/devbio-napari) package into a fresh enviroment, e.g. using this command:

```bash
mamba create --name devbio python=3.11 devbio-napari pyqt -c conda-forge -y
```
and activate the environment
```bash
mamba activate devbio
```
Once the enviroment activated, please use pip to get the most recent version (which is not available via `conda-forge` yet):
```bash
pip install devbio-napari==0.11.0 pyclesperanto==0.14.1 --no-dependencies
```
When the installation is done, you can start Napari with the Assistant interface by running:
```bash
naparia
```
Napari-assistant should pop-up:
![napari_assistant](https://github.com/haesleinhuepf/devbio-napari/raw/master/docs/screenshot.png)

## Python 

Please follow this section to use pyclesperanto as a classic python library:
Install pyclesperanto package into a fresh enviroment, e.g. using this command:
```bash
mamba create --name work python=3.11 pyclesperanto -c conda-forge -y
```
and activate the environment
```bash
mamba activate work
```
You may want to also install other libraries usefull for python BioImage Analysis:
```bash
mamba install scikit-image jupyter pandas dask zarr -c conda-forge -y
```

> [!WARNING]   
> __MAC Users__: Install also : `mamba install ocl_icd_wrapper_apple -c conda-forge -y`  
> __Linux Users__ Install also : `mamba install ocl-icd-system -c conda-forge -y`  

## Fiji

clesperanto is also being developed in FIJI. Although no proper release is available yet, you can test running pyclesperanto script with it:

### CLIJ3 update side

Start the update of your FIJI and when it is done, go to the update site list
- `Help menu > Update` then click on `Manage update sites`
- Click on `add unlisted site`
- Add the following site `https://sites.imagej.net/clij3` 
- Validate the changes and restart FIJI

[img]
