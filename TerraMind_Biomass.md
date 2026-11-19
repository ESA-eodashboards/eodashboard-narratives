---
cover-image: https://placehold.co/600x400/png
date: 2026-11-18
theme: esa-biomass-terramind
tags: biomass, terramind, forest-canopy-height, sar, sentinel-1, sentinel-2, foundation-models, germany
official: false

---

# Global-to-Regional Forest Canopy Height Estimation with TerraMind and ESA BIOMASS Level-2A <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
## Authors: [Name Surname]¹, [Name Surname]² and [Name Surname]³  <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
> ¹ [Affiliation 1]  ² [Affiliation 2]  ³ [Affiliation 3]

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in **[Month Year / 2026]**. It was developed by a team from **[Affiliations]**.*

##  <!--{ nav="false"}-->
<p align="center">
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="Affiliation 1" height="80" style="margin: 0 15px;"/>
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="Affiliation 2" height="80" style="margin: 0 15px;"/>
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="Affiliation 3" height="80" style="margin: 0 15px;"/>
</p>


## Challenge
ESA's BIOMASS mission (Earth Explorer 7) is the first satellite to carry a spaceborne P-band (~70 cm wavelength) Synthetic Aperture Radar (SAR). Its long wavelength penetrates dense forest canopies down to the ground, allowing retrieval of vertical forest structure such as Forest Canopy Height (FH). However, International Telecommunication Union (ITU) frequency restrictions that protect Space Object Tracking Radars prohibit P-band acquisitions over large regions, including Europe and North America, and the active swaths provide strip-based rather than wall-to-wall coverage. Globally available missions such as Sentinel-2 (optical) and Sentinel-1 (C-band SAR) do offer continuous coverage, but optical reflectance saturates in dense multi-layered forests and C-band radar mainly interacts with the upper canopy.


## Objective
The objective of this study was to reproduce the ESA BIOMASS Level-2A Forest Canopy Height product from freely available, wall-to-wall data: Sentinel-2, Sentinel-1 and the Copernicus DEM. To do so, we adapted **TerraMind v1**, a deep-learning foundation model for Earth observation developed by IBM and ESA Φ-lab, and trained it on BIOMASS canopy height across globally distributed forest regions. The trained model is then applied over Germany, where BIOMASS does not acquire data, to produce a BIOMASS-like canopy height map.


## Methodology

### Dataset
All inputs are resampled onto the native BIOMASS Level-2A grid (3 arcsec, about 90 × 92 m at the equator) and cut into 41,019 patches of 256 × 256 pixels.

- **Reference labels (ESA BIOMASS Level-2A)**: Forest Canopy Height from P-band PolInSAR (200 m product resolution, delivered on the ~92 m grid). Values above 75 m are treated as PolInSAR outliers and masked. The BIOMASS Ground Notch backscatter (HH, HV, VV) is used only as an auxiliary training signal that helps the model learn ground/canopy structure.
- **Optical inputs**: Sentinel-2 L2A Blue, Green, Red and Near-Infrared bands (B02, B03, B04, B08).
- **Radar inputs**: Sentinel-1 GRD VV and VH backscatter (dB).
- **Terrain inputs**: Copernicus DEM GLO-30 elevation.

A pixel is used only where the BIOMASS label is valid and Sentinel-2, Sentinel-1 and the DEM all have data.

The dataset spans **20 global Regions of Interest** across four regimes:
- **Tropical rainforests**: Amazon (Central Brazil), Congo Basin (DRC), Northern Congo Sangha Forest, Tropical Forest Indonesia, Berau–Kelay Dipterocarp Forest (Indonesia).
- **Savannas, dry forests and woodlands**: Cerrado Woodlands (Brazil), Gran Chaco Dry Forest (South America), Miombo Woodlands (Zambia), Bicuar Woodlands (Angola), Central Indian Deciduous Forest (India), East Australian Eucalyptus Forest, Riverina Inland Woodlands (Australia).
- **Boreal and temperate forests**: Siberian Taiga (Russia), Daxinganling Boreal Forest (China), Temperate Mixed Forest (West Russia), Kaingaroa–Whirinaki Forest (New Zealand), Golden Downs Tasman Forest (New Zealand).
- **Fragmented agricultural and urban landscapes**: North China Plain (Shandong), Pearl River Delta (China), Urban Industrial Corridor (Brazil).


### Data Sources & Normalization
Sentinel-1 and Sentinel-2 come from the quarterly global mosaics of the same quarter as each BIOMASS acquisition (2026). All data are streamed as Cloud-Optimized GeoTIFFs and resampled to the BIOMASS grid.

| Modality | Product | Source | Preprocessing | Normalization |
| :--- | :--- | :--- | :--- | :--- |
| **Canopy Height (label)** | ESA BIOMASS L2A Forest Height | ESA MAAP STAC | Defines the reference grid; values above 75 m masked | Scaled by 38 m; outputs limited to 0–75 m |
| **Ground Notch (auxiliary label)** | ESA BIOMASS L2A Ground Notch (HH, HV, VV) | ESA MAAP STAC | Converted to dB | Standardized per polarization |
| **Optical (S2)** | Sentinel-2 L2A quarterly mosaics (B02, B03, B04, B08) | Copernicus Data Space Ecosystem | Reflectance × 10,000; resampled to the BIOMASS grid | TerraMind pretraining statistics for the foundation model; dataset statistics for the refiner |
| **Radar (S1)** | Sentinel-1 GRD quarterly mosaics (VV, VH) | Copernicus Data Space Ecosystem | Converted to dB; resampled to the BIOMASS grid | TerraMind pretraining statistics for the foundation model; dataset statistics for the refiner |
| **Terrain (DEM)** | Copernicus DEM GLO-30 | AWS Open Data | Bilinear resampling to the BIOMASS grid; relief and slope derived | TerraMind pretraining statistics for the foundation model; dataset statistics for the refiner |

### Training & Validation Split
About 15% of each region is held out for validation, chosen so that validation and training pixels overlap as little as possible. Within each region, BIOMASS scenes with overlapping footprints are grouped, and whole groups go to validation, which gives zero pixel overlap. Where all scenes of a region overlap into one group, the region is instead divided into 0.5° grid cells and whole cells are held out. No patch is discarded.


## Earth observations <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Vector","properties":{"id":"trainvalfootprints","title":"Training & Validation Footprints (Train vs. Val)"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/TrainValFootprints-1795009646433.geojson","format":"GeoJSON"},"visible":true,"style":{"stroke-color":["match",["get","split"],"train","#0077ff","val","#ff3300","#ff9900"],"stroke-width":2,"fill-color":["match",["get","split"],"train","rgba(0, 119, 255, 0.25)","val","rgba(255, 51, 0, 0.35)","rgba(255, 153, 0, 0.25)"]}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="2.1" center=[-10.569682342641302,7.8903138332408105] projection="EPSG:3857" animationOptions={duration:500}}-->
#### Training & Validation Footprints
Training (blue) and validation (red) footprints across the 20 regions. Validation areas are chosen to overlap training areas as little as possible.

## Model & Training

### Model Architecture
The model works in two stages:

1. **Stage 1 – TerraMind foundation model**: TerraMind is a large neural network (~86 million parameters) pretrained by IBM and ESA on millions of co-registered optical, radar and elevation images. It turns the Sentinel-2, Sentinel-1 and DEM inputs into compact descriptions ("features") of the landscape. We keep TerraMind **frozen**, i.e. its pretrained knowledge is used as-is and not changed. Only a small decoder on top is trained to translate these features into a coarse canopy height map.
2. **Stage 2 – Terrain-aware refiner**: A small convolutional network corrects the coarse map at full resolution using physically meaningful inputs: the Sentinel-2 and Sentinel-1 bands, six indices (NDVI, NDWI, VH − VV cross-polarization ratio, radar vegetation index, and NIR and VH texture), and four terrain features (elevation, local relief over ~3 km, and slope in x and y). It starts as a "do nothing" correction and learns adjustments during training. A second small output predicts the Ground Notch as an auxiliary task.


### Training Strategy
Training means repeatedly showing the model patches, measuring how far its prediction is from the BIOMASS label (the "loss"), and adjusting the trainable parts to reduce that error. Several choices address the noisy labels and the tendency of regression models to pull predictions towards the mean height:

- **Height-balanced weighting**: Each pixel is weighted by how rare its height class is, so both low and tall forest count more. This counters a compressed height range, in which low forest is overestimated and tall forest underestimated.
- **Down-weighting implausible scenes**: Scenes whose median height deviates strongly from the other scenes of their region count only 25% in training, which reduces the effect of scene-wide offsets.
- **Region-balanced sampling**: Small regions are sampled more often than their size alone would give, so large regions do not dominate.
- **Simple loss**: The loss deliberately does not enforce sharp edges or fine texture, because the 200 m labels cannot support pixel-scale detail and such terms tend to cause grid-like artefacts.
- **Augmentation**: Patches are randomly flipped and rotated, Sentinel-2 brightness and haze and Sentinel-1 calibration and speckle are slightly perturbed, and in 5% of cases Sentinel-2 or Sentinel-1 is removed entirely. This makes the model robust to sensor differences and missing data.

The model is trained for up to 20 epochs (passes over the training data) and stops early if validation RMSE does not improve for 6 epochs. The checkpoint with the lowest validation RMSE is kept.

### Map Production
Large areas are predicted in overlapping 256 × 256 pixel windows that are blended smoothly to avoid seams. Each window is predicted four times (original, flipped and rotated) and the results are averaged.




## Results
### Validation on Unseen BIOMASS Scenes
The model is evaluated on one complete BIOMASS scene per region that was never part of the training data. Metrics are computed at the ~92 m pixel level and after 2 × 2 averaging (~184 m, close to the 200 m product resolution).

| Validation Region | RMSE (m) | Bias (m) | R² | r | RMSE, 2 × 2 (m) | Bias, 0–10 m labels (m) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Amazon, Central Brazil** *(Tropical moist broadleaf)* | [XX.XX] | [+X.XX] | [0.XXX] | [0.XX] | [XX.XX] | [+X.XX] |
| **Eucalyptus Forest, East Australia** *(Subtropical/temperate sclerophyll)* | [XX.XX] | [+X.XX] | [0.XXX] | [0.XX] | [XX.XX] | [+X.XX] |
| **Taiga, Siberia** *(Boreal needleleaf)* | [XX.XX] | [+X.XX] | [0.XXX] | [0.XX] | [XX.XX] | [+X.XX] |
| **Temperate Mixed Forest, West Russia** *(Hemiboreal mixed)* | [XX.XX] | [+X.XX] | [0.XXX] | [0.XX] | [XX.XX] | [+X.XX] |

*(Note: Fill in once validation is complete.)*

The map below shows one of these scenes step by step: the three inputs, the BIOMASS reference and the model prediction.


## Validation Scene: Amazon, Central Brazil <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Image","properties":{"id":"Amazon_Central_Brazil_s2","title":"Sentinel-2 input"},"source":{"type":"ImageStatic","url":"https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Amazon_S2.png","imageExtent":[-6443542.97,-732757.04,-6350363.04,-580001.53],"projection":"EPSG:3857","crossOrigin":"anonymous","interpolate":false},"visible":true}]' center=[-57.4648,-5.8856] zoom="9.1" projection="EPSG:3857" animationOptions={duration:500}}-->
#### Sentinel-2 input
True-colour composite (red, green, blue) of the quarterly Sentinel-2 mosaic matching the BIOMASS acquisition.

### <!--{ layers='[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Image","properties":{"id":"Amazon_Central_Brazil_s1","title":"Sentinel-1 input"},"source":{"type":"ImageStatic","url":"https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Amazon_S1.png","imageExtent":[-6443542.97,-732757.04,-6350363.04,-580001.53],"projection":"EPSG:3857","crossOrigin":"anonymous","interpolate":false},"visible":true}]' center=[-57.4648,-5.8856] zoom="9.1" projection="EPSG:3857" animationOptions={duration:500}}-->
#### Sentinel-1 input
VV (red), VH (green) and VV/VH ratio (blue). Forests appear green because of strong volume scattering.

### <!--{ layers='[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Image","properties":{"id":"Amazon_Central_Brazil_dem","title":"Copernicus DEM input"},"source":{"type":"ImageStatic","url":"https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Amazon_DEM.png","imageExtent":[-6443542.97,-732757.04,-6350363.04,-580001.53],"projection":"EPSG:3857","crossOrigin":"anonymous","interpolate":false},"visible":true}]' center=[-57.4648,-5.8856] zoom="9.1" projection="EPSG:3857" animationOptions={duration:500}}-->
#### Copernicus DEM input
Elevation from 59 m to 252 m, shown with hillshading.

### <!--{ layers='[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Image","properties":{"id":"Amazon_Central_Brazil_fh_gt","title":"BIOMASS canopy height"},"source":{"type":"ImageStatic","url":"https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Amazon_Height_BIOMASS.png","imageExtent":[-6443542.97,-732757.04,-6350363.04,-580001.53],"projection":"EPSG:3857","crossOrigin":"anonymous","interpolate":false},"visible":true}]' center=[-57.4648,-5.8856] zoom="9.1" projection="EPSG:3857" animationOptions={duration:500}}-->
#### BIOMASS canopy height
The P-band BIOMASS Level-2A canopy height used as reference.

<img src="https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Amazon_Legend_Height.png" width="300"/>

### <!--{ layers='[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Image","properties":{"id":"Amazon_Central_Brazil_fh_pred","title":"Predicted canopy height"},"source":{"type":"ImageStatic","url":"https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Amazon_Height_Predicted.png","imageExtent":[-6443542.97,-732757.04,-6350363.04,-580001.53],"projection":"EPSG:3857","crossOrigin":"anonymous","interpolate":false},"visible":true}]' center=[-57.4648,-5.8856] zoom="9.1" projection="EPSG:3857" animationOptions={duration:500}}-->
#### Predicted canopy height
The model's prediction from Sentinel-2, Sentinel-1 and DEM only, on the same colour scale. Agreement with BIOMASS: RMSE [X.X] m, bias [±X.X] m, r = [0.XX].

<img src="https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Amazon_Legend_Height.png" width="300"/>


## Canopy Height Map of Germany
Using the trained model, a wall-to-wall canopy height map is produced for Germany (5.8°E–15.1°E, 47.2°N–55.1°N) on the BIOMASS grid (~51 × 92 m at 51°N), from leaf-on 2026 Sentinel-1/2 mosaics and the Copernicus DEM. The model predicts a height for every land pixel, so a forest mask is applied before display.

- **Spatial & Ecological Patterns**: [Describe observed regional gradients across Germany, e.g. tall coniferous and mixed montane stands in the Black Forest, Bavarian Forest, Harz and Alpine foothills vs. managed lowland pine forests in Brandenburg/Lower Saxony.]


## Conclusions
- **Feasibility**: A frozen Earth observation foundation model with a small, terrain-aware refiner can learn BIOMASS-like canopy height from globally available Sentinel-2, Sentinel-1 and Copernicus DEM data, and apply it to regions without P-band coverage, such as Germany.
- **Labels set the limit**: Repeat BIOMASS passes agree at only r = 0.18, and whole scenes can be offset by 10–25 m. Model accuracy must be read as agreement with BIOMASS, and improving label quality (e.g. using the BIOMASS quality layer) is as important as improving the model.
- **Limitations**: Only one validation scene per region in four regions; Sentinel-1/2 inputs are quarterly mosaics rather than single acquisitions; the Germany map has no direct BIOMASS reference and is not yet validated.
- **Future work**: Validate the Germany map against independent references such as NASA GEDI, national airborne laser scanning and forest inventories; include the BIOMASS quality layer; and extend validation to more scenes and regions.


## <!--{ as="div" }--> Open Science
| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| :--- | :--- | :--- | :--- |
| **[ESA BIOMASS Level-2A (MAAP STAC)](https://catalog.maap.eo.esa.int/catalogue/)** | Dataset | ESA (Earth Explorer 7 / MAAP) | P-band Forest Canopy Height (labels) and Ground Notch (auxiliary labels) used for training and validation. |
| **[Copernicus Sentinel-1 & Sentinel-2 Global Mosaics (CDSE)](https://dataspace.copernicus.eu/)** | Dataset | European Commission / ESA (CDSE) | Quarterly Sentinel-2 optical and Sentinel-1 C-band radar mosaics used for training and the Germany map. |
| **[Copernicus DEM GLO-30](https://registry.opendata.aws/copernicus-dem/)** | Dataset | ESA / Copernicus (AWS Open Data) | 30 m global elevation used for elevation, relief and slope. |
| **[IBM/ESA TerraMind v1](https://huggingface.co/ibm-esa-geospatial)** | Foundation Model | IBM Research & ESA Φ-lab | Pretrained multimodal Earth observation foundation model, used frozen via TerraTorch. |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)** | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Base layers and tools for interactive exploration of Earth observation indicators. |

#### Notebook
Access the notebook to reproduce the study workflow.
<iframe width="100%" height="600" src="[LINK TO NOTEBOOK]" frameborder="0"></iframe>


#### References
- **ESA BIOMASS Mission**: Quegan, S., et al. (2019). The European Space Agency BIOMASS mission: Measuring forest above-ground biomass from space. *Remote Sensing of Environment*, 227, 44–60. https://doi.org/10.1016/j.rse.2019.03.032
- **TerraMind Foundation Model**: Jakubik, J., et al. (2025). TerraMind: Large-Scale Generative Multimodality for Earth Observation. *IBM Research & ESA Φ-lab*. https://huggingface.co/ibm-esa-geospatial
- **TerraTorch Framework**: Gomes, C., et al. (2025). TerraTorch: The Geospatial Foundation Models Toolkit for PyTorch. https://github.com/IBM/terratorch


## Contributors
- **[Author 1 Name]** ([Affiliation 1]) — Methodology, model architecture, data pipeline, and regional inference.
- **[Author 2 Name]** ([Affiliation 2]) — Validation, geospatial analysis, and scientific review.
- **[Author 3 Name]** ([Affiliation 3]) — Supervision and StoryMap curation.
