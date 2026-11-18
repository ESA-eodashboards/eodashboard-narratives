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
ESA's BIOMASS mission (Earth Explorer 7) is the first satellite to carry a spaceborne P-band (~70 cm wavelength) Synthetic Aperture Radar (SAR), enabling radar signals to penetrate dense forest canopies down to the ground and retrieve three-dimensional vertical forest structure, such as Forest Canopy Height (FH) and Ground Notch (GN) backscatter. However, due to International Telecommunication Union (ITU) frequency-allocation restrictions protecting Space Object Tracking Radars (SOTRs), P-band acquisitions are prohibited over major regions of the globe—including Europe and North America—and orbital swaths within active zones provide strip-based rather than continuous wall-to-wall coverage. Conversely, globally available missions such as Sentinel-2 (optical) and Sentinel-1 (C-band SAR) offer continuous spatial coverage, but optical reflectance saturates in dense multi-layered forests and C-band radar primarily interacts with upper-canopy foliage rather than penetrating to the forest floor.


## Objective
The objective of this study was to mimic ESA BIOMASS Level-2A products—specifically Forest Canopy Height (FH) and P-band Ground Notch (GN) backscatter—by fine-tuning the multimodal **TerraMind v1** (`terramind_v1_base`) Earth Observation foundation model on globally available, wall-to-wall datasets (Sentinel-2 L2A, Sentinel-1 GRD, and Copernicus DEM GLO-30)[cite: 6]. By learning the physical cross-sensor mapping between optical reflectance, C-band radar backscatter, terrain morphology, and P-band vertical forest structure across diverse global biomes—while enforcing out-of-distribution (OOD) geographic generalization—the model reconstructs synthetic BIOMASS-like canopy height and ground-notch layers in regions lacking direct P-band acquisitions, demonstrated operationally through a wall-to-wall canopy height map of Germany[cite: 1, 6].


## Data and Methods
#### Dataset
- **Multimodal Dataset & Spatial Coverage**: The training corpus consists of co-registered multimodal chips (256 × 256 pixels, ~50 m native grid spacing; calibrated across 27,799 baseline patches and expanded to 41,019 total patches with ≥ 98% valid joint swath coverage) stored in WebDataset `.tar` shards (`dataset_shards_v2`) alongside a GeoPackage spatial footprint index (`patch_footprints.gpkg`)[cite: 1, 6, 7]. Each sample pairs reference P-band targets with wall-to-wall multi-sensor inputs and derived physical features[cite: 6, 7]:
  - **Reference Targets (ESA BIOMASS Level-2A)**: Forest Canopy Height (FH, in meters, filtered to [0.0, 75.0] m) and tri-polarization Ground Notch backscatter (GN: HH, HV, VV in dB)[cite: 5, 7].
  - **Optical Inputs**: Four Sentinel-2 L2A bands (`B02` Blue, `B03` Green, `B04` Red, `B08` NIR Narrow)[cite: 6, 7].
  - **C-Band SAR Inputs**: Dual-polarization Sentinel-1 GRD backscatter (`VV`, `VH`)[cite: 6, 7].
  - **Topographic Inputs**: Copernicus DEM GLO-30 elevation (30 m)[cite: 6, 7].
  - **Derived Physical Indices**: NDVI, NDWI, standardized C-band cross-polarization ratio (VH − VV in dB), 33-pixel (~1 km) masked local terrain relief, and border-eroded Sobel slope gradients (dz/dx, dz/dy)[cite: 6].

  The dataset spans **20 global Regions of Interest (ROIs)** across four major biome and land-cover regimes[cite: 7]:
  - **Tropical Rainforests**: Amazon (Central Brazil), Congo Basin (DRC), Northern Congo Sangha Forest, Tropical Forest Indonesia, Berau–Kelay Dipterocarp Forest (Indonesia)[cite: 7].
  - **Savannas, Dry Forests & Woodlands**: Cerrado Woodlands (Brazil), Gran Chaco Dry Forest (South America), Miombo Woodlands (Zambia), Bicuar Woodlands (Angola), Central Indian Deciduous Forest (India), East Australian Eucalyptus Forest, Riverina Inland Woodlands (Australia)[cite: 7].
  - **Boreal & Temperate Forests**: Siberian Taiga (Russia), Daxinganling Boreal Forest (China), Temperate Mixed Forest (West Russia), Kaingaroa–Whirinaki Forest (New Zealand), Golden Downs Tasman Forest (New Zealand)[cite: 7].
  - **Fragmented Agricultural & Urban Landscapes**: North China Plain (Shandong), Pearl River Delta (Inland China), Urban Industrial Corridor (Brazil)[cite: 7].

  To ensure leak-free evaluation, scenes are partitioned at the acquisition level (`scene_id`), holding out 15% of complete satellite scenes per ROI (34,444 training and 6,575 validation patches)[cite: 5].


## Earth observations <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Vector","properties":{"id":"trainfootprints","title":"Training & Validation Footprints"},"source":{"type":"Vector","url":"./assets/tdedring/trainfootprints-1795006014892.geojson","format":"GeoJSON"},"visible":true,"style":{"stroke-color":"#ff9900","stroke-width":2,"fill-color":"rgba(255, 153, 0, 0.25)"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="EPSG:3857" animationOptions={duration:500}}-->
#### Global Distribution of Training & Validation Patches
The training and validation corpus spans 20 globally distributed Regions of Interest covering tropical broadleaf rainforests, dry tropical woodlands and savannas, boreal needleleaf taiga, southern-hemisphere temperate plantations, and fragmented agricultural-urban transition zones[cite: 7]. By grouping patches by satellite acquisition (`scene_id`) prior to splitting, spatially adjacent or overlapping chips from the same orbital pass are strictly isolated between training and validation sets, preventing spatial memorization[cite: 5].


## Data Sources & Normalization
- **Temporal Coverage**: 2026 ESA BIOMASS Level-2A acquisitions (from January 2026 onward) paired with quarter-matched (Q1–Q4) Sentinel-1 and Sentinel-2 global mosaics, prioritizing leaf-on summer quarters (`Q3`/`Q2` in the Northern Hemisphere, `Q1`/`Q4` in the Southern Hemisphere) at latitudes above 45°[cite: 2, 7].

- **Data Sources & Cloud Ingestion**: All datasets are streamed as Cloud-Optimized GeoTIFFs (COGs) and spatially aligned to the native BIOMASS Level-2A grid via bilinear resampling (`rioxarray.reproject_match`)[cite: 2, 7]. Reference FH and GN layers are queried from the **ESA MAAP STAC Catalogue** (`BiomassLevel2a`), Sentinel-1 and Sentinel-2 global mosaics are retrieved via the **Copernicus Data Space Ecosystem (CDSE) STAC API & S3**, and 30 m Copernicus DEM GLO-30 tiles are fetched from **AWS Open Data S3**[cite: 2, 7].


| Modality / Role | Product & Variables | Source & API | Alignment & Quality Control | Normalization Metrics |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Target (FH)** | ESA BIOMASS L2A Forest Height (meters) | ESA MAAP STAC (`BiomassLevel2a`, `BIO_FP_FH__L2A_`) | Defines reference native CRS and pixel grid; PolInSAR spikes > 75.0 m masked | Scaled by 38.0 m (`FH_SCALE_M`); evaluation clamped to [0.0, 75.0] m |
| **Auxiliary Target (GN)** | ESA BIOMASS L2A Ground Notch (`HH`, `HV`, `VV`) | ESA MAAP STAC (`BiomassLevel2a`, `BIO_GN__L2A_`) | Reprojected to FH grid; linear intensity converted to dB and clamped to [-45, 10] dB | Z-score standardized: μ = [-10.11, -17.82, -10.70] dB, σ = [4.85, 6.26, 4.60] dB |
| **Optical Input (S2)** | Sentinel-2 L2A Global Mosaics (`B02`, `B03`, `B04`, `B08`) + NDVI, NDWI | CDSE STAC & S3 (`sentinel-2-global-mosaics`) | Bilinearly resampled to FH grid; scaled to 0–10,000 DN and clamped to [-500, 12,000] DN | **Backbone:** μ = [1503.3, 1718.2, 1853.9, 3083.2], σ = [2141.1, 2039.0, 2134.1, 1871.9] DN<br>**Refiner:** μ = [391.7, 582.6, 545.1, 2360.2], σ = [242.9, 271.5, 418.4, 808.2] DN |
| **Radar Input (S1)** | Sentinel-1 GRD Global Mosaics (`VV`, `VH`) + Cross-Pol Ratio (VH − VV) | CDSE STAC & S3 (`sentinel-1-global-mosaics`) | Bilinearly resampled to FH grid; linear intensity converted to dB and clamped to [-40, 5] dB | **Backbone:** μ = [-12.60, -20.29], σ = [5.20, 5.89] dB<br>**Refiner:** μ = [-9.33, -16.21], σ = [3.55, 5.05] dB |
| **Terrain Input (DEM)** | Copernicus DEM GLO-30 (30 m elevation, 33-px relief, Sobel slopes) | AWS Open Data S3 (`copernicus-dem-30m`) | 1° × 1° COG tiles resampled to FH grid; masked normalized relief & border-eroded slope masks | **Backbone:** μ = 670.67 m, σ = 951.27 m<br>**Refiner:** Elev 436.93 / 394.27 m; Relief σ = 29.05 m; Slope σ = 0.90 |


#### Methodology workflow
The modeling framework (`BiomassTerraMindModule`) implements a two-stage coarse-to-fine multimodal fusion pipeline engineered for sharp stand boundary preservation and zero-coordinate out-of-distribution (OOD) geographic generalization[cite: 6]:

1. **Dual-Stream Standardization & Physics Feature Engineering**: Each input batch is standardized into two parallel streams: (a) an official IBM/TerraMind pretraining stream fed to the foundation backbone, and (b) a forest-calibrated 18-channel spatial refiner stream combining standardized S2 (4 ch), S1 (2 ch), physical indices (NDVI, NDWI, and standardized VH − VV cross-pol ratio; 3 ch), masked multi-scale terrain features (elevation, 33 × 33 local topographic relief, and 3 × 3 border-eroded Sobel slopes dz/dx, dz/dy to correct SAR layover and foreshortening; 4 ch), and cyclic geographic coordinates [sin(lat), cos(lat), sin(lon), cos(lon), valid_gate] (5 ch)[cite: 6].
2. **Stage 1 — TerraMind v1 Foundation Backbone & Pyramidal UNet Decoder**: Pretrained `terramind_v1_base` encodes `S2L2A`, `S1GRD`, and `DEM` tokens (`backbone_merge_method="mean"`)[cite: 6]. Multi-layer transformer representations from encoder blocks `[3, 5, 7, 11]` are reshaped into spatial feature maps (`LearnedInterpolateToPyramidal`) and decoded via a `UNetDecoder` (`[256, 128, 64, 32]`) into a coarse normalized height prediction[cite: 6].
3. **Stage 2 — 18-Channel Multi-Scale Terrain Spatial Refiner**: To recover fine forest stand edges and topographic boundaries smoothed by ViT patch tokenization, the coarse prediction is refined across 1×, 1/2×, and 1/4× spatial scales using dilated residual blocks (`ResConvBlock` with `GroupNorm` and `GELU`)[cite: 6]. A zero-initialized residual delta head (`fh_delta_head`) progressively learns high-frequency height refinements on top of TerraMind's coarse estimate, while an auxiliary multi-task convolutional head (`gn_head`) predicts standardized 3-band BIOMASS Ground Notch backscatter (`HH`, `HV`, `VV`) during training[cite: 6].
4. **88% Coordinate Dropout for OOD Transfer**: During training, geographic coordinate channels are randomly zeroed out for **88%** of samples (`coord_drop_prob = 0.88`), preventing the network from memorizing continental biomes while allowing seamless coordinate-free inference (`use_coords=False`) over unseen target countries such as Germany[cite: 1, 6].
5. **Speckle-Resistant Multi-Objective Loss (`SharpCanopyHeightLoss`)**: Optimization combines a tall-canopy weighted Huber loss (delta = 0.065, up-weighting stands > 15 m up to 1.5× to counter high-biomass saturation), a log-height relative Huber loss (delta = 0.08, weight 0.25) for 0–10 m regrowth precision, a batch moment-matching loss (weight 0.25) penalizing variance collapse and mean bias, a multi-scale (1×, 2 × 2, 4 × 4) masked structural gradient loss (weight 0.40) to preserve sharp stand edges while suppressing P-band PolInSAR phase speckle, and an auxiliary Ground Notch `SmoothL1` loss (weight 0.15)[cite: 6].
6. **Training Schedule & Seamless Tiled Inference**: Trained with `AdamW` (lr = 1.5e-4 for decoder/refiner heads, 0.15 × lr for the TerraMind encoder after a 3-epoch backbone warmup freeze, `CosineAnnealingLR` over 60 epochs, 16-bit mixed precision) and synchronized dihedral, radiometric, and modality-dropout augmentations[cite: 3, 5, 6]. At inference time, full satellite scenes and 0.5° × 0.5° regional tiles are processed using 256 × 256 sliding windows at 50% overlap (`stride = 128`), 4-fold dihedral Test-Time Augmentation (TTA), and 2D Hann window blending[cite: 1, 2].


## Results
### 1. Out-of-Distribution Validation Across Held-Out Global Biomes
To benchmark cross-biome transfer without geographic priors (`use_coords=False`), the lowest-validation-loss checkpoint (`checkpoints_v2`) was evaluated on complete, unseen ESA BIOMASS Level-2A acquisitions excluded from `patch_footprints.gpkg` across four contrasting global forest regimes (`validate_biomass_scenes.py`)[cite: 4]:

| Validation Region & Biome | Scene ID | All-Pixel RMSE (m) | All-Pixel MAE (m) | All-Pixel Bias (m) | All-Pixel R² | Forest (> 2 m) RMSE (m) | Forest (> 2 m) R² | Tall Canopy (> 20 m) Bias (m) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Amazon Central Brazil** *(Tropical Moist Broadleaf)* | `[SCENE_ID]` | `[XX.XX]` | `[XX.XX]` | `[+X.XX]` | `[0.XXX]` | `[XX.XX]` | `[0.XXX]` | `[+X.XX]` |
| **Eucalyptus Forest East Australia** *(Subtropical/Temperate Sclerophyll)* | `[SCENE_ID]` | `[XX.XX]` | `[XX.XX]` | `[+X.XX]` | `[0.XXX]` | `[XX.XX]` | `[0.XXX]` | `[+X.XX]` |
| **Taiga Siberia Russia** *(Boreal Needleleaf Taiga)* | `[SCENE_ID]` | `[XX.XX]` | `[XX.XX]` | `[+X.XX]` | `[0.XXX]` | `[XX.XX]` | `[0.XXX]` | `[+X.XX]` |
| **Temperate Mixed Forest West Russia** *(European Hemiboreal/Mixed)* | `[SCENE_ID]` | `[XX.XX]` | `[XX.XX]` | `[+X.XX]` | `[0.XXX]` | `[XX.XX]` | `[0.XXX]` | `[+X.XX]` |

*(Note: Populate the metric cells above directly from `validation_scenes_output_v2/validation_summary_*.json` and insert the 6-panel visual comparison figures `*_comparison_*.png` showing Sentinel-2 RGB, Sentinel-1 SAR, Copernicus DEM, BIOMASS Ground Truth, Predicted Height, and Error maps[cite: 4].)*

### 2. Wall-to-Wall Canopy Height Mapping of Germany
Using the coordinate-free OOD model (`use_coords=False`) with 4× dihedral TTA and 2D Hann blending (`infer_germany_forest_height.py`), a continuous wall-to-wall Forest Canopy Height map (and optional 3-band synthetic P-band Ground Notch backscatter in dB) was generated across Germany (5.8°E–15.1°E, 47.2°N–55.1°N) at the native training resolution (~0.0007° × 0.00045°, ~50 m ground sampling distance) from summer 2026 (`2026-06-15`) CDSE Sentinel-1/2 global mosaics and Copernicus DEM GLO-30[cite: 1].

- **Spatial & Ecological Patterns**: `[Describe observed regional gradients across Germany—e.g., tall coniferous and mixed montane stands in the Black Forest, Bavarian Forest, Harz, and Alpine foothills vs. managed lowland pine forests in Brandenburg/Lower Saxony and zero-height agricultural plains.]`


## Conclusions
- **Cross-Sensor Transferability**: Fine-tuning the multimodal **TerraMind v1** foundation model with a physics-informed, terrain-aware spatial refiner enables accurate reconstruction of ESA BIOMASS Level-2A Forest Canopy Height and Ground Notch backscatter from globally available Sentinel-2 optical, Sentinel-1 C-band SAR, and Copernicus DEM data[cite: 6].
- **Leak-Free Geographic Generalization**: Combining scene-level stratified splitting, 88% coordinate dropout during training, and masked topographic slope/relief features prevents geographic overfitting and enables zero-coordinate transfer (`use_coords=False`) to regions excluded from spaceborne P-band radar operations due to ITU restrictions, such as Germany and Central Europe[cite: 1, 5, 6].
- **Limitations & Future Work**: Current predictions inherit the ~50 m spatial posting of ESA BIOMASS Level-2A training products rather than native 10 m Sentinel-2 resolution[cite: 1], and C-band SAR/optical inputs can still experience moderate signal saturation in ultra-tall (> 40 m) tropical stands[cite: 6]. Future work will benchmark the Germany canopy height mosaic quantitatively against national Airborne Laser Scanning (ALS) / LiDAR digital canopy height models and NASA GEDI footprint data, and explore super-resolution refinement to 10 m grid spacing.


## <!--{ as="div" }--> Open Science
| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| :--- | :--- | :--- | :--- |
| **[ESA BIOMASS Level-2A (MAAP STAC)](https://catalog.maap.eo.esa.int/catalogue/)** | Dataset | ESA (Earth Explorer 7 / MAAP) | Provides P-band PolInSAR Forest Canopy Height (`BIO_FP_FH__L2A_`) and tri-polarization Ground Notch (`BIO_GN__L2A_`) reference targets used for model supervision and held-out global biome validation[cite: 2, 7]. |
| **[Copernicus Sentinel-1 & Sentinel-2 Global Mosaics (CDSE)](https://dataspace.copernicus.eu/)** | Dataset | European Commission / ESA (CDSE) | Supplies quarterly cloud-free Sentinel-2 L2A optical bands (`B02`, `B03`, `B04`, `B08`) and Sentinel-1 GRD C-band backscatter (`VV`, `VH`) streamed via STAC and S3 for global training and wall-to-wall Germany inference[cite: 2, 7]. |
| **[Copernicus DEM GLO-30](https://registry.opendata.aws/copernicus-dem/)** | Dataset | ESA / Copernicus (AWS Open Data) | Provides 30 m global digital elevation tiles used to compute standardized elevation, 33 × 33 local topographic relief, and border-eroded Sobel terrain slopes for SAR layover/foreshortening correction[cite: 2, 6]. |
| **[IBM/ESA TerraMind v1 (`terramind_v1_base`)](https://huggingface.co/ibm-esa-geospatial)** | Foundation Model | IBM Research & ESA Φ-lab | Multimodal Earth Observation foundation backbone fine-tuned via TerraTorch and PyTorch Lightning to fuse optical, SAR, and elevation representations[cite: 6]. |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)** | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Provides base layers and visualization tools for interactive exploration of vegetation indices and Earth observation indicators. |

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