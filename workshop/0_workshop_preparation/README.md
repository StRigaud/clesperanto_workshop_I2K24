# Workshop preparation

Before attending the workshop, we strongly advise to go through the workshop preparation and install the various requierements on your computer.

## Mamba / Conda

We will require `Mamba` for installing and managing python environement and packages, we strongly advise the use of [MiniForge](). Please follow their instruction for installing it on your computer. 

> [!TIP] 
> Additionnal explaination for mamba can be found [here](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html)

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
pip install devbio-napari==0.11.0
```
When the installation is done, you can start Napari with the Assistant interface by running:
```bash
naparia
```
Napari-assistant should pop-up:
![napari_assistant](https://github.com/haesleinhuepf/devbio-napari/raw/master/docs/screenshot.png)


## Fiji

clesperanto is also being developed in FIJI. Although no proper release is available yet, if time allows, we will test running some clesperanto script on fiji.
Has this is an on-going development, we do not advise users to use it, but live testing during the workshop could greatly help us in this development.

### CLIJ3 update side

Start the update of your FIJI and when it is done, go to the update site list
- `Help menu > Update` then click on `Manage update sites`
- Click on `add unlisted site`
- Add the following site `https://sites.imagej.net/clij3` 
- Validate the changes and restart FIJI

![Screenshot from 2024-10-21 13-41-46](https://github.com/user-attachments/assets/dd0dfa48-8dd5-4d26-b8ed-00bb5c1f32d9)


