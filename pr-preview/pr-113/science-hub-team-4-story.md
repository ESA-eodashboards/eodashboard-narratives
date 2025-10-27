---
cover-image: https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2022/10/svalbard/24544693-1-eng-GB/Svalbard_pillars.jpg
date: 2025-01-01
theme: theme_name
tags: some,tags

---

# Wet snow mapping with multimodal foundation models  <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2022/10/svalbard/24544693-1-eng-GB/Svalbard_pillars.jpg" }-->
### Authors: Leam Howe, Sean Ó Héir, Miguel Espinosa Minano (Univeristy of Leeds) <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

# 
*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2025. It was developed by a team from University of Leeds.*

## Challenge
Snow varies greatly in its characteristics and effects. Two primary types are dry snow and wet snow, which differ in water content, density, grain size, and formation conditions. Dry snow is powdery and light, occurring in cold temperatures well below freezing, whereas wet snow contains higher water content, is denser, and forms near or above freezing temperatures.

Mapping wet snow is critical because it influences water resource management, flood prediction, climate research, agriculture, and disaster preparedness. Mapping wet snow accurately remains a challenge due to the complex interaction of radar signals with snow characteristics. While dry snow allows deeper penetration of C-band radar signals (up to 10 meters), wet snow’s higher liquid water content absorbs microwave radiation, limiting penetration to just a few centimeters. This leads to a strong contrast in radar backscatter intensity, with wet snow showing significantly lower backscatter compared to dry snow or snow-free ground. Current mapping methods rely heavily on thresholding, filtering, and the availability of dry snow reference areas or optical imagery, which can be computationally expensive, regionally limited, and prone to errors in complex terrain. Moreover, these approaches struggle to distinguish wet snow from other wet surfaces like soil.

<div style="text-align: center;"> <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-4/radarSnowMapping.png?raw=true" width="500"/> <p><b>Figure 1.</b>Schematic representation of microwave interaction with a snow layer. The diagram illustrates the transmission (𝑃𝑡) and reflection (𝑃𝑟) of electromagnetic waves at the air–snow interface.</p> 

</div>
  


The emergence of **Geospatial Foundation Models (GFMs)**, large AI models pre-trained on diverse satellite and airborne data, can fuse multi-modal signals (SAR, optical, thermal, DEM, and reanalysis data) and implicitly learn complex cues for wet snow detection without needing summer reference data, **potentially overcoming existing limitations**.
<div style="text-align: center;"> <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-4/GFM.png?raw=true" width="500"/> <p><b>Figure 2.</b>Unified multimodal Earth foundation model. Large AI models trained on diverse airborne and satellite data integrate multiple sensor types to enable scalable, transferable, and few-/zero-shot learning for tasks such as land cover mapping, flood detection, and forest monitoring.</p> 

</div>
  

## Objective

The objective of this study was to develop a reproducible framework to classify snow types using Sentinel-1 data, focusing on wet snow detection. This involved downloading Sentinel-1 radar data for Svalbard, constructing an Earth System Data Lab (ESDL) data cube, and fine-tuning a Geospatial Foundation Model to perform semantic segmentation of snow types — distinguishing wet snow, dry snow, and no snow.

Predictions from the model were then validated against ground-truth data, enabling assessment of classification accuracy and operational potential for snow mapping applications.

## Use case <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"SSLC1_Seasonal_S1_AMP_hv_interferometric_coherence;:;2d96aa0d-5170-4979-b00e-e9e3eb1d3308;:;SSLC1_Seasonal_S1_AMP_hv_interferometric_coherence;:;EPSG:3857","title":"SSLC1_Seasonal_S1_AMP_hv_interferometric_coherence"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["S1_AMP_HV"],"TILED":true,"TIME":"2020-09-21T00:00:00Z/2020-09-21T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="6.016697172057297" center=[14.510800415896034,77.77939108743098] projection="" animationOptions={duration:500}}-->
#### Svalbard
Svalbard, an Arctic archipelago, is an ideal testbed for wet snow mapping due to its extreme climate and diverse snow conditions. Accurate monitoring of wet snow here supports water resource management, flood risk assessment, and climate studies in this sensitive region. Using Sentinel-1 data, our model identifies and classifies snow types across Svalbard, providing valuable insights for environmental monitoring and decision-making in the Arctic.



<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;">
    <img 
        src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-4/Globe4_svalbard.png?raw=true" 
        style="max-width: 100%; width: 800px; height: auto;"
        alt="Use cases/forests locations"
    />
    <p style="text-align: center; font-size: 1.2em; margin-top: 10px;">
        <b>Figure 3.</b> Use cases: the Svalbard archipelago.
    </p>
</div>

https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-4/results2.png?raw=true
	
## Data and Methods
#### Dataset
- **Source/Input data**: Sentinel-1 satellite imagery (VV and VH polarization patches)
- **Classes/Output data**: Wet snow, dry snow, no data, bare ground, and water.
-  **Coverage**:  A subset of approximately 150 images was used for this project


#### Methodology workflow
The approach builds on a Geospatial Foundational Model (GFM) that has been pre-trained on large-scale geospatial data. The process involves:

- **Model Initialization:** The CROMA model is used as the pretrained backbone (encoder) to extract meaningful geospatial features from Sentinel-1 input data.
- **Decoder Integration:** A UPerNet decoder is added to the pretrained encoder to enable pixel-wise classification, producing a snow segmentation map.
- **Fine-Tuning Process:** The model is fine-tuned using a small labeled dataset (~150 images). The encoder is partially frozen to retain foundational geospatial knowledge, while the decoder is trained for the specific segmentation task.
- **Loss function:** Cross Entropy.
- **Framework:** PANGAEA-BENCH:  a [standardized evaluation protocol](https://arxiv.org/abs/2412.04204) that covers a diverse set of datasets, tasks, resolutions, sensor modalities, and temporalities.

<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;">
    <img 
        src=" https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-4/methods1.png?raw=true" 
        style="max-width: 100%; width: 800px; height: auto;"
        alt=""
    />
    <p style="text-align: center; font-size: 1.2em; margin-top: 10px;">
        <b>Figure 4.</b> Using the Fine-Tuned Geospatial FM.
    </p>
</div>
	

## Results
#### Accuracy metrics
The model learns quickly, **reaching over 90% accuracy** within the first few training rounds and staying stable afterward. Its **ability to distinguish between different surface types**, measured by the IoU metric, improves more gradually and levels off around 55–60%. Some ups and downs in the curve suggest that the model finds it harder to tell apart certain classes — a common issue when dealing with radar data where some surfaces reflect signals in similar ways.

<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;">
    <img 
        src=" https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-4/results.png?raw=truee" 
        style="max-width: 100%; width: 800px; height: auto;"
        alt=""
    />
    <p style="text-align: center; font-size: 1.2em; margin-top: 10px;">
        <b>Figure 5.</b> Validation results.
    </p>
</div>

#### Visual interpreation
From the VV and VH backscatter images, clear textural differences can be observed (brighter and darker streaks) likely corresponding to variations in surface roughness, water, and snow conditions. However, while some areas show strong contrast, others appear smoother, indicating that the model needs to learn subtle backscatter differences.

Looking at the first row of images as an example, the model generalizes well for larger snow zones but struggles with mixed or transitional pixels (e.g., where radar signals change rapidly). This could be due to coarse labeling or spatial smoothing introduced by the decoder.

<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;"> <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-4/results2.png?raw=true" style="max-width: 100%; width: 800px; height: auto;" alt="" /> <p style="text-align: center; font-size: 1.2em; margin-top: 10px;"> <b>Figure 6.</b> Comparison of input Sentinel-1 VV and VH images, predicted segmentation mask, and target mask. </p> </div>

In contrast, the second (bottom) row shows that the model reliably detects large homogeneous features (such as water bodies) but misses smaller-scale heterogeneity, again suggesting limitations related to radar ambiguity or spatial resolution.



## Conclusions
Looking at each class, water and dry snow are identified with very high precision, while wet snow performs fairly well but becomes less consistent after longer training. Bare ground remains the most difficult to detect, likely because its radar signal overlaps with that of wet snow or because there weren’t enough training examples.

Overall, the results show that Sentinel-1 radar data is excellent for spotting water and snow-covered areas but less reliable for distinguishing wet snow from bare ground. The current setup, combining the CROMA encoder with a UPerNet decoder, already performs strongly. Future improvements could come from adding time-series data, integrating extra context such as elevation or temperature, and using better class balancing to help the model learn from underrepresented surfaces.



## <!--{ as="div" }--> Open Science
| **Name**                                                                                                                                       | **Type**            | **Agency / Provider**                     | **Description / Usage**                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Sentinel-1 Snow Classification Dataset](https://sentinel.esa.int/web/sentinel/missions/sentinel-1)**                                        | Dataset             | ESA (European Space Agency)               | A small dataset (~150 images) of Sentinel-1 VV and VH polarization patches used to train a segmentation model for snow classification. Classes include wet snow, dry snow, bare ground, water, and no data.                            |
| **[PANGAEA-BENCH Framework](https://arxiv.org/abs/2412.04204)**                                                                                       | Framework / Toolkit | PANGAEA Consortium                        | Used to fine-tune geospatial foundational models (GFMs) for Earth observation tasks. Enabled the training of the decoder (UPerNet) on the pre-trained CROMA encoder for the snow segmentation task.                                     |
| **[CROMA Geospatial Foundational Model](https://www.esa.int/Applications/Observing_the_Earth/CROMA)**                                          | Model / Encoder     | ESA (European Space Agency)               | Pre-trained encoder providing general geospatial representations. Used as the backbone model, fine-tuned with a UPerNet decoder to produce pixel-wise snow classification outputs.                                                     |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)**                          | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Provides base layers and visualization tools for interactive exploration of NDVI and other Earth observation indicators, potentially useful for validating and visualizing model outputs.                                               |


#### Notebook
Access the notebook to reproduce the study workflow.
<iframe width="100%" height="600" src="LINK TO NOTEBOOK" frameborder="0"></iframe>


#### References
- PANGAEA: A Global and Inclusive Benchmark for Geospatial Foundation Models [Access](https://arxiv.org/abs/2412.04204)

- [CROMA Geospatial Foundational Model](https://www.esa.int/Applications/Observing_the_Earth/CROMA)



## Contributors
Authors, contibutors, reviewers 




