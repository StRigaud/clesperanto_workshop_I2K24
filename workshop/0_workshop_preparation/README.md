# Workshop preparation

Before attending the workshop, we strongly advise to go through the workshop preparation and install the various requierements on your computer.

## Python requierements

### Mamba / Conda

We will require `Mamba` for installing and managing python environement and packages, we strongly advise the use of [MiniForge](). Please follow their instruction for installing it on your computer. 

> [!TIP] 
> Additionnal explaination for mamba can be found [here](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html)

> [!CAUTION] 
> `Conda` should also work but will be slower for downloading and installing the dependencies

### devbio-napari environment

Using mamba, please install the [devbio-napari](https://github.com/haesleinhuepf/devbio-napari) package into a fresh enviroment, e.g. using this command:

```bash
mamba create --name devbio python=3.11 devbio-napari pyqt -c conda-forge -y
```

Afterwards, please use pip to get the most recent version (which is not available via conda-forge yet):
```bash
pip install devbio-napari==0.11.0
```

When the installation is done, you can activate the environment...
```bash
mamba activate devbio
```
... and start Napari with the Assistant interface:

```bash
naparia
```

Napari should start with the pyclesperanto-assistant:

![napari_assistant](https://github.com/haesleinhuepf/devbio-napari/raw/master/docs/screenshot.png)

### Troubleshouting

If the user interface does not look like shown above, e.g. has much less buttons, you may need to install additional packages or GPU drivers. Read this [troubleshooting section](https://github.com/clesperanto/pyclesperanto?tab=readme-ov-file#troubleshooting-graphics-cards-drivers) for more details.

Any additional issues will be gladly answered during the workshop, do not hesite to comeforth.

## Fiji

clesperanto is also being developed in FIJI. Although no proper release is available yet, you can test running pyclesperanto script with it:

### CLIJ3 update side

Start the update of your FIJI and when it is done, go to the update site list
- `Help menu > Update` then click on `Manage update sites`
- Click on `add unlisted site`
- Add the following site `https://sites.imagej.net/clij3` 
- Validate the changes and restart FIJI

[img]
