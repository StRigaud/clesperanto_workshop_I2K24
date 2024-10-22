# I2K 2024: clEsperanto: GPU-Accelerated Image Processing Library

Course and material for the clEsperanto workshop presented at I2K 2024 @ Human Technopol (Milan, Italy)

The workshop is an hands-on demo of the `clesperanto` project, focussing on how to use the library for users who want use GPU-acceleration for their Image Processing pipeline.
Although we will follow a plan, the workshop aim to be interactive and hands-on. 

Time limitation may not allow use to oversee all the aspect of the library and its capabilities. We encourage attendes to interact with us with questions, feedbacks, and any specifics aspect they would like to explore during this workshop.

### Summary:
- Introduction of the library and GPU-acceleration
- Napari-assistant:
    - Exercise 1: [processing images using the napari assistant](./workshop/2_napari_assistant/21_naparis_assistant.md) and [export the pipeline in notebook](./workshop/2_napari_assistant/22_export_to_notebook.md)
- pyclesperanto:
    - Exercise 2: [pyclesperanto introduction](./workshop/3_pyclesperanto/31_introduction.ipynb) and [pipeline construction](./workshop/3_pyclesperanto/32_mini_analysis_pipeline.ipynb)
    - Exercise 3: [benchmarking CPU vs GPU](./workshop/3_pyclesperanto/33_benchmarking.ipynb)
- clij3 (Experimental):
    - Running a [jython script](./workshop/4_clij3/mini_jython_pipeline.py) in Fiji

## Requierements

Please follow the workshop preparation [instruction](./workshop/0_workshop_preparation/README.md)

## Acknowledgement

This workshop reuse and adapt several course material:
- [BioImageAnalysisNotebooks](https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/intro.html)
- [PoL-BioImage-Analysis Training School 2023](https://github.com/BiAPoL/PoL-BioImage-Analysis-TS-GPU-Accelerated-Image-Analysis.git)
- [Turku Image Analysis Course 2024](https://github.com/jpylvanainen/Image_analysis_course_24.git)
