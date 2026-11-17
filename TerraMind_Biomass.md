---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
official: false

---

# Synthetic Biomass Data using TerraMind <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
## Authors: Name Surname¹, Name Surname² and Name Surname³  <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
> ¹ Affiliation ² Affiliation  ³ Affiliation

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in **DATE**. It was developed by a team from the **AFFILIATIONS**.*

##  <!--{ nav="false"}-->
<p align="center">
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="Ca' Foscari" height="80" style="margin: 0 15px;"/>
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="NOC" height="80" style="margin: 0 15px;"/>
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="BAS" height="80" style="margin: 0 15px;"/>
</p>


## Challenge
ESA's BIOMASS mission (Earth Explorer 7) is the first satellite to carry a spaceborne P-band (~70 cm wavelength) Synthetic Aperture Radar (SAR), enabling radar signals to penetrate dense forest canopies down to the ground and retrieve three-dimensional vertical forest structure, such as Forest Canopy Height (FH) and Ground Notch (GN) backscatter. However, due to International Telecommunication Union (ITU) frequency-allocation restrictions protecting Space Object Tracking Radars (SOTRs), P-band acquisitions are prohibited over major regions of the globe—including Europe and North America—and orbital swaths within active zones provide strip-based rather than continuous wall-to-wall coverage. Conversely, globally available missions such as Sentinel-2 (optical) and Sentinel-1 (C-band SAR) offer continuous spatial coverage, but optical reflectance saturates in dense multi-layered forests and C-band radar primarily interacts with upper-canopy foliage rather than penetrating to the forest floor.


## Objective
The objective of this study was to mimic ESA BIOMASS Level-2A products—specifically Forest Canopy Height (FH) and P-band Ground Notch (GN) backscatter—by fine-tuning the multimodal **TerraMind** foundation model on globally available, wall-to-wall Earth observation datasets (Sentinel-2 L2A, Sentinel-1 GRD, and Copernicus DEM). By learning the physical cross-sensor mapping between optical reflectance, C-band radar backscatter, terrain morphology, and P-band vertical forest structure across diverse global biomes, the model reconstructs synthetic BIOMASS-like canopy height and ground-notch layers in regions and gaps lacking direct P-band acquisitions.


## Earth observations <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="" animationOptions={duration:500}}-->
#### Title
Text



## Data and Methods
#### Dataset
- **Multimodal Dataset & Spatial Coverage**: The training corpus consists of 27,799 co-registered multimodal chips (256 × 256 pixels; 1.82 billion valid pixels; 99.84% mean orbital swath coverage) stored across 29 WebDataset shards. Each sample pairs reference P-band targets with wall-to-wall multi-sensor inputs and derived physical features:
  - **Reference Targets (ESA BIOMASS Level-2A)**: Forest Canopy Height (FH) and tri-polarization Ground Notch backscatter (GN: HH, HV, VV).
  - **Optical Inputs**: Sentinel-2 L2A (B02, B03, B04, B08).
  - **C-Band SAR Inputs**: Sentinel-1 GRD backscatter (VV, VH).
  - **Topographic Inputs**: Copernicus DEM (30 m).
  - **Derived Physical Indices**: NDVI, NDWI, SAR cross-polarization ratio, local terrain relief, and slope gradients.

  The dataset spans **11 global Regions of Interest (ROIs)** across four major biome and land-cover regimes:
  - **Tropical Rainforests**: Amazon, Congo Basin, Indonesia.
  - **Savannas & Woodlands**: Cerrado, Miombo, East Australian Eucalyptus.
  - **Boreal & Temperate Forests**: Siberian Taiga, West Russia.
  - **Fragmented Agricultural & Urban Landscapes**: Shandong, Pearl River Delta, Urban Brazil.

  To ensure leak-free evaluation, scenes are partitioned at the acquisition level, holding out 15% of complete satellite scenes per ROI (~22,048 training and ~5,751 validation patches).

- **Temporal Coverage**: 2026 ESA BIOMASS Level-2A acquisitions (from January 2026 onward) paired with quarter-matched (Q1–Q4) Sentinel-1 and Sentinel-2 global mosaics, prioritizing leaf-on summer quarters (Q2/Q3 in the Northern Hemisphere) at latitudes above 45°.

- **Data Sources & Cloud Ingestion**: All datasets are streamed as Cloud-Optimized GeoTIFFs (COGs) and spatially aligned to the native BIOMASS Level-2A grid. Reference FH and GN layers are queried from the **ESA MAAP STAC Catalogue** (`BiomassLevel2a`), Sentinel-1 and Sentinel-2 global mosaics are retrieved via the **Copernicus Data Space Ecosystem (CDSE) STAC API & S3**, and 30 m Copernicus DEM GLO-30 tiles are fetched from **AWS Open Data S3**.

| Modality / Role | Product & Variables | Source & API | Alignment & Quality Control | Normalization Metrics |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Target (FH)** | ESA BIOMASS L2A Forest Height (meters) | ESA MAAP STAC (`BiomassLevel2a`) | Defines reference native CRS and pixel grid; PolInSAR spikes > 75.0 m masked; loss clamped to [0, 65] m | Global μ = 18.41 m, σ = 11.80 m, p95 = 38.24 m; scaled by 38.0 m |
| **Auxiliary Target (GN)** | ESA BIOMASS L2A Ground Notch (HH, HV, VV) | ESA MAAP STAC (`BiomassLevel2a`) | Reprojected to FH grid; linear intensity converted to dB and clamped to [-45, 10] dB | Z-score standardized: μ = [-10.11, -17.82, -10.70] dB, σ = [4.85, 6.26, 4.60] dB |
| **Optical Input (S2)** | Sentinel-2 L2A Global Mosaics (B02, B03, B04, B08) + NDVI, NDWI | CDSE STAC & S3 | Bilinearly resampled to FH grid; scaled to 0–10,000 DN and clamped to [-500, 12,000] DN | **Backbone:** μ = [1503.3, 1718.2, 1853.9, 3083.2], σ = [2141.1, 2039.0, 2134.1, 1871.9] DN<br>**Refiner:** μ = [391.7, 582.6, 545.1, 2360.2], σ = [242.9, 271.5, 418.4, 808.2] DN |
| **Radar Input (S1)** | Sentinel-1 GRD Global Mosaics (VV, VH) + Cross-Pol Ratio (VH − VV) | CDSE STAC & S3 | Bilinearly resampled to FH grid; linear intensity converted to dB and clamped to [-40, 5] dB | **Backbone:** μ = [-12.60, -20.29], σ = [5.20, 5.89] dB<br>**Refiner:** μ = [-9.33, -16.21], σ = [3.55, 5.05] dB |
| **Terrain Input (DEM)** | Copernicus DEM GLO-30 (30 m elevation, 33-px relief, Sobel slopes) | AWS Open Data S3 | 1° × 1° COG tiles resampled to FH grid; masked normalized relief & border-eroded slope masks | **Backbone:** μ = 670.67 m, σ = 951.27 m<br>**Refiner:** Elev 436.93 / 394.27 m; Relief σ = 29.05 m; Slope σ = 0.90 |


#### Methodology workflow
Description



## Results


## Conclusions



## <!--{ as="div" }--> Open Science
| **Name**                                                                                                                                                 | **Type**            | **Agency / Provider**                     | **Description / Usage**                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[DATASET NAME](LINK)** | Dataset             | DeepESDL / ESDC                           | Description how this dataset was used in this story |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)**                                     | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Provides base layers and visualization tools for interactive exploration of NDVI and other Earth observation indicators.                                                                                                                |

#### Notebook
Access the notebook to reproduce the study workflow.
<iframe width="100%" height="600" src="LINK TO NOTEBOOK" frameborder="0"></iframe>


#### References
- Reference 1


- Reference 2




## Contributors
Authors, contibutors, reviewers