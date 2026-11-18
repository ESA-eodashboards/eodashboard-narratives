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
ESA's BIOMASS mission (Earth Explorer 7) is the first satellite to carry a spaceborne P-band (~70 cm wavelength) Synthetic Aperture Radar (SAR). Its long wavelength penetrates dense forest canopies down to the ground, allowing retrieval of vertical forest structure such as Forest Canopy Height (FH) and Ground Notch (GN) backscatter. However, International Telecommunication Union (ITU) frequency restrictions that protect Space Object Tracking Radars prohibit P-band acquisitions over large regions, including Europe and North America, and the active swaths provide strip-based rather than wall-to-wall coverage. Globally available missions such as Sentinel-2 (optical) and Sentinel-1 (C-band SAR) do offer continuous coverage, but optical reflectance saturates in dense multi-layered forests and C-band radar mainly interacts with the upper canopy.


## Objective
The objective of this study was to mimic ESA BIOMASS Level-2A products, specifically Forest Canopy Height and P-band Ground Notch backscatter, by fine-tuning the multimodal **TerraMind v1** Earth Observation foundation model on globally available data (Sentinel-2, Sentinel-1 and Copernicus DEM). By learning the mapping between optical reflectance, C-band backscatter, terrain and P-band forest structure across diverse global biomes, while enforcing geographic generalization, the model can reconstruct BIOMASS-like canopy height in regions without P-band acquisitions. This is demonstrated with a wall-to-wall canopy height map of Germany.


## Methodology

### Dataset
The training corpus consists of 41,019 co-registered multimodal patches (256 × 256 pixels at the ~50 m BIOMASS grid). Each patch pairs BIOMASS reference targets with wall-to-wall inputs:
- **Reference targets (ESA BIOMASS Level-2A)**: Forest Canopy Height (in meters, filtered to 0–75 m) and Ground Notch backscatter in three polarizations (HH, HV, VV, in dB).
- **Optical inputs**: Sentinel-2 L2A Blue, Green, Red and Near-Infrared bands.
- **Radar inputs**: Sentinel-1 GRD VV and VH backscatter.
- **Terrain inputs**: Copernicus DEM GLO-30 elevation.
- **Derived features**: NDVI, NDWI, the C-band cross-polarization ratio, local terrain relief and slope.

The dataset spans **20 global Regions of Interest** across four regimes:
- **Tropical rainforests**: Amazon (Central Brazil), Congo Basin (DRC), Northern Congo Sangha Forest, Tropical Forest Indonesia, Berau–Kelay Dipterocarp Forest (Indonesia).
- **Savannas, dry forests and woodlands**: Cerrado Woodlands (Brazil), Gran Chaco Dry Forest (South America), Miombo Woodlands (Zambia), Bicuar Woodlands (Angola), Central Indian Deciduous Forest (India), East Australian Eucalyptus Forest, Riverina Inland Woodlands (Australia).
- **Boreal and temperate forests**: Siberian Taiga (Russia), Daxinganling Boreal Forest (China), Temperate Mixed Forest (West Russia), Kaingaroa–Whirinaki Forest (New Zealand), Golden Downs Tasman Forest (New Zealand).
- **Fragmented agricultural and urban landscapes**: North China Plain (Shandong), Pearl River Delta (China), Urban Industrial Corridor (Brazil).

To ensure leak-free evaluation, complete satellite acquisitions rather than individual patches were split, holding out 15% of scenes per region (34,444 training and 6,575 validation patches).

### Data Sources & Normalization
All data cover 2026: BIOMASS Level-2A acquisitions from January 2026 onward, paired with quarterly Sentinel-1 and Sentinel-2 global mosaics (leaf-on summer quarters preferred above 45° latitude). All inputs are streamed as Cloud-Optimized GeoTIFFs and resampled onto the native BIOMASS grid.

| Modality | Product | Source | Preprocessing | Normalization |
| :--- | :--- | :--- | :--- | :--- |
| **Canopy Height (target)** | ESA BIOMASS L2A Forest Height | ESA MAAP STAC | Defines the reference grid; values above 75 m masked | Scaled by 38 m; outputs limited to 0–75 m |
| **Ground Notch (auxiliary target)** | ESA BIOMASS L2A Ground Notch (HH, HV, VV) | ESA MAAP STAC | Converted to dB, clipped to −45 to 10 dB | Standardized per polarization |
| **Optical (S2)** | Sentinel-2 L2A global mosaics (B02, B03, B04, B08) | Copernicus Data Space Ecosystem | Resampled to the BIOMASS grid | TerraMind pretraining statistics for the backbone; forest-specific statistics for the refiner |
| **Radar (S1)** | Sentinel-1 GRD global mosaics (VV, VH) | Copernicus Data Space Ecosystem | Resampled to the BIOMASS grid; converted to dB | TerraMind pretraining statistics for the backbone; forest-specific statistics for the refiner |
| **Terrain (DEM)** | Copernicus DEM GLO-30 | AWS Open Data | Resampled to the BIOMASS grid; relief and slope derived | TerraMind pretraining statistics for the backbone; forest-specific statistics for the refiner |

### Model Workflow
The model follows a two-stage, coarse-to-fine design:

1. **Dual-stream normalization**: Each input is standardized twice: once with TerraMind's pretraining statistics for the foundation backbone, and once with forest-specific statistics for the refinement network, which also receives the derived spectral, radar and terrain features.
2. **Stage 1 – TerraMind backbone**: The pretrained TerraMind v1 base model encodes Sentinel-2, Sentinel-1 and DEM inputs, and a UNet decoder turns multi-level features into a coarse canopy height map.
3. **Stage 2 – Terrain-aware refiner**: A lightweight multi-scale convolutional network sharpens stand edges and topographic boundaries that the transformer tends to smooth. It starts as an identity mapping and gradually learns corrections, while an auxiliary head predicts Ground Notch backscatter.
4. **Geographic generalization**: Location inputs are hidden for 88% of training samples, so the model cannot memorize regions and can run without coordinates in unseen areas such as Germany.
5. **Loss function**: The objective combines a height-weighted Huber loss that counters underestimation in tall forests, a log-height term for young regrowth, a term that preserves the spread of predicted heights, a multi-scale gradient term for sharp stand boundaries, and an auxiliary Ground Notch loss.
6. **Training and inference**: The backbone is frozen for the first 3 epochs and then fine-tuned at a lower learning rate for up to 60 epochs, with geometric, radiometric and sensor-dropout augmentations. At inference, scenes are processed in overlapping windows that are blended smoothly and averaged over flipped and rotated copies.


## Earth observations <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Vector","properties":{"id":"trainvalfootprints","title":"Training & Validation Footprints (Train vs. Val)"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/TrainValFootprints-1795009646433.geojson","format":"GeoJSON"},"visible":true,"style":{"stroke-color":["match",["get","split"],"train","#0077ff","val","#ff3300","#ff9900"],"stroke-width":2,"fill-color":["match",["get","split"],"train","rgba(0, 119, 255, 0.25)","val","rgba(255, 51, 0, 0.35)","rgba(255, 153, 0, 0.25)"]}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="2.1" center=[-10.569682342641302,7.8903138332408105] projection="EPSG:3857" animationOptions={duration:500}}-->
#### Training & Validation Footprints
Training (blue) and validation (red) acquisitions span 20 regions across tropical, dry, boreal, temperate and agricultural landscapes. Whole acquisitions are held out for validation to avoid spatial leakage.


## Results
### 1. Validation Across Held-Out Global Biomes
To test transfer across biomes without location information, the best model was evaluated on complete, unseen BIOMASS Level-2A scenes in four contrasting forest regions:

| Validation Region & Biome | Scene ID | All-Pixel RMSE (m) | All-Pixel MAE (m) | All-Pixel Bias (m) | All-Pixel R² | Forest (> 2 m) RMSE (m) | Forest (> 2 m) R² | Tall Canopy (> 20 m) Bias (m) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Amazon Central Brazil** *(Tropical Moist Broadleaf)* | [SCENE_ID] | [XX.XX] | [XX.XX] | [+X.XX] | [0.XXX] | [XX.XX] | [0.XXX] | [+X.XX] |
| **Eucalyptus Forest East Australia** *(Subtropical/Temperate Sclerophyll)* | [SCENE_ID] | [XX.XX] | [XX.XX] | [+X.XX] | [0.XXX] | [XX.XX] | [0.XXX] | [+X.XX] |
| **Taiga Siberia Russia** *(Boreal Needleleaf Taiga)* | [SCENE_ID] | [XX.XX] | [XX.XX] | [+X.XX] | [0.XXX] | [XX.XX] | [0.XXX] | [+X.XX] |
| **Temperate Mixed Forest West Russia** *(European Hemiboreal/Mixed)* | [SCENE_ID] | [XX.XX] | [XX.XX] | [+X.XX] | [0.XXX] | [XX.XX] | [0.XXX] | [+X.XX] |

*(Note: Fill in the metrics from the validation results and add comparison figures showing Sentinel-2 RGB, Sentinel-1 SAR, DEM, BIOMASS ground truth, predicted height and error.)*

### 2. Wall-to-Wall Canopy Height Map of Germany
Without location inputs, the model produced a continuous canopy height map of Germany (5.8°E–15.1°E, 47.2°N–55.1°N) at ~50 m resolution from summer 2026 Sentinel-1/2 mosaics and the Copernicus DEM, along with an optional synthetic P-band Ground Notch layer.

- **Spatial & Ecological Patterns**: [Describe observed regional gradients across Germany, e.g. tall coniferous and mixed montane stands in the Black Forest, Bavarian Forest, Harz and Alpine foothills vs. managed lowland pine forests in Brandenburg/Lower Saxony and treeless agricultural plains.]


## Conclusions
- **Cross-sensor transfer**: Fine-tuning TerraMind v1 with a terrain-aware refiner reconstructs BIOMASS-like canopy height and Ground Notch backscatter from globally available Sentinel-2, Sentinel-1 and Copernicus DEM data.
- **Geographic generalization**: Scene-level splitting, hidden location inputs and terrain features prevent geographic overfitting and enable transfer to regions without P-band coverage due to ITU restrictions, such as Germany and Central Europe.
- **Limitations & future work**: Predictions inherit the ~50 m resolution of BIOMASS Level-2A rather than the 10 m of Sentinel-2, and optical and C-band inputs can still saturate in very tall (> 40 m) tropical forests. Future work will benchmark the Germany map against national airborne laser scanning and NASA GEDI data, and explore super-resolution to 10 m.


## <!--{ as="div" }--> Open Science
| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| :--- | :--- | :--- | :--- |
| **[ESA BIOMASS Level-2A (MAAP STAC)](https://catalog.maap.eo.esa.int/catalogue/)** | Dataset | ESA (Earth Explorer 7 / MAAP) | P-band Forest Canopy Height and Ground Notch reference data used for training and validation. |
| **[Copernicus Sentinel-1 & Sentinel-2 Global Mosaics (CDSE)](https://dataspace.copernicus.eu/)** | Dataset | European Commission / ESA (CDSE) | Quarterly Sentinel-2 optical and Sentinel-1 C-band radar mosaics used for training and the Germany map. |
| **[Copernicus DEM GLO-30](https://registry.opendata.aws/copernicus-dem/)** | Dataset | ESA / Copernicus (AWS Open Data) | 30 m global elevation used to derive terrain relief and slope. |
| **[IBM/ESA TerraMind v1](https://huggingface.co/ibm-esa-geospatial)** | Foundation Model | IBM Research & ESA Φ-lab | Multimodal Earth Observation foundation model fine-tuned with TerraTorch and PyTorch Lightning. |
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