# Workshop preparation

Before attending the workshop, we strongly advise to go through the workshop preparation and install the various requierements on your computer.

## Python requierements

### Mamba / Conda

We will require `Mamba` for installing and managing python environement and packages, we strongly advise the use of [MiniForge](). Please follow their instruction for installing it on your computer. 

> [!TIP] 
> Additionnal explaination for mamba can be found [here](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html)

> [!CAUTION] 
> `Conda` should also work but will be slower for downloading and installing the dependencies

### DevBio environment

Using mamba, please install the [devbio-napari]() package into a fresh enviroment, e.g. using this command:

```bash
mamba create --name devbio python=3.11 devbio-napari pyqt -c conda-forge -y
```

When the installation is done, you can activate the environment and test that all was correctly install by running the following command:

```bash
mamba activate devbio && naparia
```

Napari should start with the pyclesperanto-assistant:

![napari_assistant](https://github.com/haesleinhuepf/devbio-napari/raw/master/docs/screenshot.png)

### Troubleshouting

Any issues will be gladly answered during the workshop, do not hesite to comeforth.



## Fiji

clesperanto is also being developed in FIJI. Although no proper release is available yet, you can test running pyclesperanto script with it:

### CLIJ3 update side

Start the update of your FIJI and when it is done, go to the update site list
- `Help menu > Update` then click on `Manage update sites`
- Click on `add unlisted site`
- Add the following site `` 
- Validate the changes and restart FIJI

[img]