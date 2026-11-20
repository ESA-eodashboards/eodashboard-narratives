---
cover-image: https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Title_600x400.png
date: 2026-11-20
theme: esa-biomass-terramind
tags: biomass, terramind, forest-canopy-height, sar, sentinel-1, sentinel-2, foundation-models
official: false

---

# Forest Canopy Height Beyond the BIOMASS Mission: Learning P-band Forest Structure from Sentinel Data with TerraMind <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Title_600x400.png" }-->
## Authors: Torben Dedring¹  <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
> ¹ Ruhr-Universität Bochum

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in **11/2026**. It was developed by a team from **Ruhr-Universität Bochum**.*

##  <!--{ nav="false"}-->
<p align="center">
  <img src="https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/RUB_Logo.png" alt="Ruhr-Universität Bochum" height="80" style="margin: 0 15px;"/>
  <img src="https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/indygis_Logo.png" alt="indygis" height="80" style="margin: 0 15px;"/>
</p>


## Challenge
ESA's BIOMASS mission (Earth Explorer 7), launched in April 2025, is the first satellite to carry a spaceborne P-band (~70 cm wavelength) Synthetic Aperture Radar (SAR). Its long wavelength penetrates dense forest canopies down to the ground, allowing retrieval of vertical forest structure such as Forest Canopy Height (FH). However, BIOMASS is a research mission with a planned lifetime of about five and a half years. Its acquisitions are also strip-based and, due to frequency-allocation restrictions, unavailable over some regions. Sentinel-1 (C-band SAR) and Sentinel-2 (optical), in contrast, provide continuous global coverage and are planned to continue for decades within the Copernicus programme. On their own, however, they are less sensitive to forest structure: optical reflectance saturates in dense multi-layered forests and C-band radar mainly interacts with the upper canopy.

## Objective
The objective of this study is to learn, while BIOMASS is in orbit, how its P-band canopy height relates to freely available Sentinel-2, Sentinel-1 and Copernicus DEM data. To do so, we adapted **TerraMind v1**, a deep-learning foundation model for Earth observation developed by IBM and ESA Φ-lab, and trained it on BIOMASS canopy height across globally distributed forest regions. Once trained, such a model needs only Sentinel and DEM data. It could therefore continue to provide BIOMASS-like canopy height estimates after the BIOMASS mission has ended, and fill gaps between BIOMASS acquisitions.

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
Sentinel-2 comes from the 2026 quarterly mosaic of the BIOMASS acquisition quarter, or the nearest available quarter. Sentinel-1 comes from the global mosaics over the same area; their acquisition period could not always be matched to the BIOMASS date. All data are streamed as Cloud-Optimized GeoTIFFs and resampled to the BIOMASS grid.

| Modality | Product | Source | Preprocessing | Normalization |
| :--- | :--- | :--- | :--- | :--- |
| **Canopy Height (label)** | ESA BIOMASS L2A Forest Height | ESA MAAP STAC | Defines the reference grid; values above 75 m masked | Scaled by 38 m; outputs limited to 0–75 m |
| **Ground Notch (auxiliary label)** | ESA BIOMASS L2A Ground Notch (HH, HV, VV) | ESA MAAP STAC | Converted to dB | Standardized per polarization |
| **Optical (S2)** | Sentinel-2 L2A 2026 quarterly mosaics (B02, B03, B04, B08) | Copernicus Data Space Ecosystem | Reflectance × 10,000; resampled to the BIOMASS grid | TerraMind pretraining statistics for the foundation model; dataset statistics for the refiner |
| **Radar (S1)** | Sentinel-1 GRD global mosaics (VV, VH) | Copernicus Data Space Ecosystem | Converted to dB; resampled to the BIOMASS grid | TerraMind pretraining statistics for the foundation model; dataset statistics for the refiner |
| **Terrain (DEM)** | Copernicus DEM GLO-30 | AWS Open Data | Bilinear resampling to the BIOMASS grid; relief and slope derived | TerraMind pretraining statistics for the foundation model; dataset statistics for the refiner |

### Training & Validation Split
About 15% of each region is held out for validation, chosen so that validation and training pixels overlap as little as possible. Within each region, BIOMASS scenes with overlapping footprints are grouped, and whole groups go to validation, which gives zero pixel overlap. Where all scenes of a region overlap into one group, the region is instead divided into 0.5° grid cells and whole cells are held out. No patch is discarded.


## Earth observations <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Vector","properties":{"id":"trainvalfootprints","title":"Training & Validation Footprints (Train vs. Val)"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/TrainValRegions.geojson","format":"GeoJSON"},"visible":true,"style":{"stroke-color":["match",["get","split"],"train","#0077ff","val","#ff3300","#ff9900"],"stroke-width":2,"fill-color":["match",["get","split"],"train","rgba(0, 119, 255, 0.25)","val","rgba(255, 51, 0, 0.35)","rgba(255, 153, 0, 0.25)"]}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="2.1" center=[-10.569682342641302,7.8903138332408105] projection="EPSG:3857" animationOptions={duration:500}}-->
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
- **Augmentation**: Patches are randomly flipped and rotated, Sentinel-2 brightness and haze and Sentinel-1 calibration and speckle are slightly perturbed, and in 5% of cases Sentinel-2 or Sentinel-1 is removed entirely. This makes the model robust to sensor differences and missing data.
- **Weight averaging**: The model used for validation and mapping is a running average of the trainable weights over roughly the last 1,000 training steps. This smooths out jumps between epochs and reduces overfitting to individual training scenes.

The model is trained for 12 epochs (passes over the training data), with a learning rate that decreases gradually towards zero. The version with the lowest validation RMSE (epoch 10) is kept.

### Loss Function
During training, the model minimises a weighted sum of four terms. For every valid pixel *i*, *h<sub>i</sub>* is the BIOMASS canopy height and *ĥ<sub>i</sub>* the predicted height, both in metres.

<style>
.lf-eq{font-family:"Cambria Math","STIX Two Math","Latin Modern Math","Times New Roman",serif;font-size:1.3rem;text-align:center;margin:1.4rem 0 0.4rem;line-height:2.2}
.lf-term{position:relative;display:inline-block;padding:0 3px;border-bottom:1px dotted currentColor;cursor:help;outline:none}
.lf-term:hover,.lf-term:focus{background:rgba(0,119,255,0.10);border-radius:4px}
.lf-hint{text-align:center;font-size:0.85rem;opacity:0.7;margin:0 0 1.2rem}
</style>
<div class="lf-eq">
<i>ℒ</i> =
<span class="lf-term" tabindex="0" title="𝗛𝗲𝗶𝗴𝗵𝘁 𝗹𝗼𝘀𝘀 (𝗛𝘂𝗯𝗲𝗿)&#10;The main term: it penalises the difference between predicted and BIOMASS height, and is less sensitive to outliers in the noisy labels than a squared error.&#10;&#10;Formula: Σᵢ wᵢ · H( ĥᵢ/38 m − hᵢ/38 m ) / Σᵢ wᵢ&#10;H: Huber loss with δ = 0.065 · wᵢ: pixel weight"><i>ℒ</i><sub>Huber</sub></span>
+ 0.25&thinsp;<span class="lf-term" tabindex="0" title="𝗟𝗼𝗴-𝗵𝗲𝗶𝗴𝗵𝘁 𝗹𝗼𝘀𝘀&#10;Measures errors relative to tree height, so that mistakes in low forest and regrowth count as much as in tall forest.&#10;&#10;Formula: Σᵢ wᵢ · H( ln(1 + ĥᵢ/10 m) − ln(1 + hᵢ/10 m) ) / Σᵢ wᵢ&#10;H: Huber loss with δ = 0.08 · wᵢ: pixel weight"><i>ℒ</i><sub>log</sub></span>
+ 0.10&thinsp;<span class="lf-term" tabindex="0" title="𝗖𝗼𝗮𝗿𝘀𝗲 𝘀𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲 𝗹𝗼𝘀𝘀&#10;Compares height changes between neighbouring blocks of about 180 m and 370 m, so the map keeps stand boundaries at the scale BIOMASS can resolve.&#10;&#10;Formula: Σₛ ½ · mean[ S( ∇ĥ⁽ˢ⁾ − ∇h⁽ˢ⁾ ) ],  s ∈ {2, 4}&#10;S: Smooth-L1 loss with β = 0.03 · ∇h⁽ˢ⁾: height differences between neighbouring s × s blocks (in x and y, on h/38 m)"><i>ℒ</i><sub>struct</sub></span>
+ 0.05&thinsp;<span class="lf-term" tabindex="0" title="𝗚𝗿𝗼𝘂𝗻𝗱 𝗡𝗼𝘁𝗰𝗵 𝗹𝗼𝘀𝘀 (𝗮𝘂𝘅𝗶𝗹𝗶𝗮𝗿𝘆)&#10;Asks the model to also predict the BIOMASS ground backscatter, which helps it learn the ground and canopy structure.&#10;&#10;Formula: mean over pixels i and p ∈ {HH, HV, VV} of S( ĝᵢ,ₚ − gᵢ,ₚ )&#10;S: Smooth-L1 loss with β = 0.35 · g: standardised Ground Notch backscatter (dB)"><i>ℒ</i><sub>GN</sub></span>
</div>
<p class="lf-hint">Hover over a term for a short explanation (on touch devices, see “Show the individual terms” below).</p>

The height terms are averaged with a per-pixel weight *w<sub>i</sub>* = *b<sub>i</sub>* · *s<sub>i</sub>*:
- *b<sub>i</sub>* is the **height-balance weight**: the inverse square root of how often the pixel's height class (0–5, 5–10, …, 40–50, > 50 m) occurs in the batch, normalised to a mean of 1 and limited to 0.25–4. Rare heights, both low and tall, therefore count more.
- *s<sub>i</sub>* is the **scene weight**: 0.25 for scenes whose median height is implausible for their region, otherwise 1.

<details>
<summary><b>Show the individual terms</b></summary>
<div style="font-family:'Cambria Math','STIX Two Math','Latin Modern Math','Times New Roman',serif;font-size:1.1rem;line-height:2.1;margin:0.8rem 0 0.4rem 1rem">
<i>ℒ</i><sub>Huber</sub> = ( Σ<sub><i>i</i></sub> <i>w<sub>i</sub></i> )<sup>−1</sup> Σ<sub><i>i</i></sub> <i>w<sub>i</sub></i> · <i>H</i><sub>0.065</sub>( <i>ĥ<sub>i</sub></i>/38 m − <i>h<sub>i</sub></i>/38 m )<br>
<i>ℒ</i><sub>log</sub> = ( Σ<sub><i>i</i></sub> <i>w<sub>i</sub></i> )<sup>−1</sup> Σ<sub><i>i</i></sub> <i>w<sub>i</sub></i> · <i>H</i><sub>0.08</sub>( ln(1 + <i>ĥ<sub>i</sub></i>/10 m) − ln(1 + <i>h<sub>i</sub></i>/10 m) )<br>
<i>ℒ</i><sub>struct</sub> = Σ<sub><i>s</i> ∈ {2, 4}</sub> ½ · ⟨ <i>S</i><sub>0.03</sub>( ∇<i>ĥ</i><sup>(<i>s</i>)</sup> − ∇<i>h</i><sup>(<i>s</i>)</sup> ) ⟩<br>
<i>ℒ</i><sub>GN</sub> = ⟨ <i>S</i><sub>0.35</sub>( <i>ĝ<sub>i,p</sub></i> − <i>g<sub>i,p</sub></i> ) ⟩<sub><i>i</i>, <i>p</i> ∈ {HH, HV, VV}</sub>
</div>
<div style="font-size:0.9rem;margin-left:1rem">
<i>H</i><sub>δ</sub>: Huber loss (quadratic for errors below δ, linear above) · <i>S</i><sub>β</sub>: Smooth-L1 loss with threshold β · ⟨ ⟩: mean over valid pixels · ∇<i>h</i><sup>(<i>s</i>)</sup>: differences between neighbouring <i>s</i> × <i>s</i>-averaged blocks in x and y, on <i>h</i>/38 m · <i>g</i>: standardised BIOMASS Ground Notch backscatter (dB).
</div>
<ul style="font-size:0.9rem;margin:0.6rem 0 0 1rem">
<li><b>Height loss (Huber)</b>: The main term: it penalises the difference between predicted and BIOMASS height, and is less sensitive to outliers in the noisy labels than a squared error.</li>
<li><b>Log-height loss</b>: Measures errors relative to tree height, so that mistakes in low forest and regrowth count as much as in tall forest.</li>
<li><b>Coarse structure loss</b>: Compares height changes between neighbouring blocks of about 180 m and 370 m, so the map keeps stand boundaries at the scale BIOMASS can resolve.</li>
<li><b>Ground Notch loss (auxiliary)</b>: Asks the model to also predict the BIOMASS ground backscatter, which helps it learn the ground and canopy structure.</li>
</ul>
</details>


### Map Production
Large areas are predicted in overlapping 256 × 256 pixel windows that are blended smoothly to avoid seams. Each window is predicted four times (original, flipped and rotated) and the results are averaged.




## Results
### Validation on Unseen BIOMASS Scenes
During training, the selected model (epoch 10) reached an RMSE of 9.16 m and an R² of 0.35 on the validation patches, and an RMSE of 8.85 m after aggregation to roughly the 200 m BIOMASS product resolution.

The map below shows one of the unseen validation scenes, in the Amazon, step by step: the three inputs, the BIOMASS reference and the model prediction.


## Validation Scene: Amazon, Central Brazil <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Image","properties":{"id":"Amazon_Central_Brazil_s2","title":"Sentinel-2 input"},"source":{"type":"ImageStatic","url":"https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Amazon_S2.png","imageExtent":[-6443542.97,-732757.04,-6350363.04,-580001.53],"projection":"EPSG:3857","crossOrigin":"anonymous","interpolate":false},"visible":true}]' center=[-57.4648,-5.8856] zoom="9.1" projection="EPSG:3857" animationOptions={duration:500}}-->
#### Sentinel-2 input
True-colour composite (red, green, blue) of the 2026 quarterly Sentinel-2 mosaic of the BIOMASS acquisition quarter.

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
The model's prediction from Sentinel-2, Sentinel-1 and DEM only, on the same colour scale. Agreement with BIOMASS: RMSE 6.5 m, bias +1.2 m, r = 0.43. The large-scale pattern is reproduced, but the prediction is smoother than the BIOMASS label.

<img src="https://raw.githubusercontent.com/tdedring/eodashboard-narratives/refs/heads/tdedring/terramindbiomass/assets/tdedring/Amazon_Legend_Height.png" width="300"/>


## Validation Across All Unseen Scenes
The model is then evaluated on one complete BIOMASS scene per region that was never part of the training data. Metrics are computed at the ~92 m pixel level against the BIOMASS label (0–75 m), without geographic coordinates. Bias is prediction minus BIOMASS.

| Validation Region | <span class="lf-term" tabindex="0" title="𝗥𝗼𝗼𝘁-𝗺𝗲𝗮𝗻-𝘀𝗾𝘂𝗮𝗿𝗲 𝗲𝗿𝗿𝗼𝗿&#10;Typical size of the difference between predicted and BIOMASS height; large errors count more than small ones.&#10;&#10;RMSE = √( mean[ (ĥᵢ − hᵢ)² ] )&#10;ĥᵢ: predicted height · hᵢ: BIOMASS height, over all valid pixels of the scene">RMSE (m)</span> | <span class="lf-term" tabindex="0" title="𝗠𝗲𝗮𝗻 𝗮𝗯𝘀𝗼𝗹𝘂𝘁𝗲 𝗲𝗿𝗿𝗼𝗿&#10;Average size of the difference between predicted and BIOMASS height, regardless of its sign; less affected by single large errors than RMSE.&#10;&#10;MAE = mean[ &#124;ĥᵢ − hᵢ&#124; ]&#10;ĥᵢ: predicted height · hᵢ: BIOMASS height, over all valid pixels of the scene">MAE (m)</span> | <span class="lf-term" tabindex="0" title="𝗕𝗶𝗮𝘀 (𝗺𝗲𝗮𝗻 𝗲𝗿𝗿𝗼𝗿)&#10;Average difference between predicted and BIOMASS height: positive values mean the model overestimates, negative values that it underestimates.&#10;&#10;Bias = mean[ ĥᵢ − hᵢ ]&#10;ĥᵢ: predicted height · hᵢ: BIOMASS height, over all valid pixels of the scene">Bias (m)</span> | <span class="lf-term" tabindex="0" title="𝗖𝗼𝗲𝗳𝗳𝗶𝗰𝗶𝗲𝗻𝘁 𝗼𝗳 𝗱𝗲𝘁𝗲𝗿𝗺𝗶𝗻𝗮𝘁𝗶𝗼𝗻&#10;Share of the variation in BIOMASS height that the prediction explains: 1 is perfect, 0 is no better than the scene's mean height, negative is worse.&#10;&#10;R² = 1 − Σ(ĥᵢ − hᵢ)² / Σ(hᵢ − h̄)²&#10;ĥᵢ: predicted height · hᵢ: BIOMASS height, over all valid pixels of the scene">R²</span> | <span class="lf-term" tabindex="0" title="𝗣𝗲𝗮𝗿𝘀𝗼𝗻 𝗰𝗼𝗿𝗿𝗲𝗹𝗮𝘁𝗶𝗼𝗻&#10;How consistently predicted and BIOMASS heights rise and fall together (−1 to 1), regardless of any constant offset.&#10;&#10;r = cov(ĥ, h) / (σ_ĥ · σ_h)&#10;ĥᵢ: predicted height · hᵢ: BIOMASS height, over all valid pixels of the scene">r</span> | <span class="lf-term" tabindex="0" title="𝗧𝗮𝗹𝗹-𝗰𝗮𝗻𝗼𝗽𝘆 𝗯𝗶𝗮𝘀&#10;Bias computed only over pixels where BIOMASS height exceeds 20 m; negative values show that tall forest is underestimated.&#10;&#10;Bias = mean[ ĥᵢ − hᵢ ] over pixels with hᵢ > 20 m&#10;ĥᵢ: predicted height · hᵢ: BIOMASS height, over all valid pixels of the scene">Bias, tall canopy > 20 m (m)</span> |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Amazon, Central Brazil** *(Tropical moist broadleaf)* | 6.49 | 4.55 | +1.18 | 0.152 | 0.43 | −0.83 |
| **Eucalyptus Forest, East Australia** *(Subtropical/temperate sclerophyll)* | 5.77 | 4.55 | −1.50 | −1.024 | −0.02 | −1.50 |
| **Taiga, Siberia** *(Boreal needleleaf)* | 28.88 | 26.76 | −24.09 | −3.920 | −0.29 | −28.68 |
| **Temperate Mixed Forest, West Russia** *(Hemiboreal mixed)* | 17.43 | 13.97 | −6.37 | −0.067 | 0.36 | −10.41 |

- **Amazon**: The best agreement (RMSE 6.5 m, r = 0.43, almost no bias in tall forest). The model reproduces the large-scale pattern, such as lower canopy along rivers and floodplains, but its map is smoother than the BIOMASS label.
- **Eucalyptus Forest**: A low RMSE (5.8 m), but no correlation with BIOMASS (r = −0.02). BIOMASS heights in this scene vary little (standard deviation about 4 m), so the low RMSE mainly reflects this narrow range; the model does not reproduce the spatial pattern.
- **Taiga**: A large negative bias (−24.1 m). This most likely reflects a scene-wide offset: the BIOMASS heights of this scene are far higher than those of the training scenes from the same region, which the model cannot reproduce from Sentinel data.
- **Temperate Mixed Forest**: A moderate correlation (r = 0.36), with tall forest underestimated by about 10 m. 10.5% of this scene overlaps training footprints; these pixels were excluded from the metrics.

Hover over a metric name in the table for a short explanation. Negative R² values mean that, for that scene, the predictions agree less well with BIOMASS than the scene's average BIOMASS height would.

## Conclusions
- **Feasibility**: A frozen Earth observation foundation model with a small, terrain-aware refiner can learn BIOMASS-like canopy height from globally available Sentinel-2, Sentinel-1 and Copernicus DEM data. On unseen scenes, agreement ranges from good in the Amazon (RMSE 6.5 m, r = 0.43) to poor where BIOMASS scenes are offset from the training data, as in the Siberian taiga.
- **Beyond the mission**: Because the trained model needs no P-band input, it offers a way to extend BIOMASS-like canopy height estimates in time, beyond the lifetime of the mission, using the long-term Sentinel and Copernicus data streams.
- **Labels set the limit**: Repeat BIOMASS passes agree at only r = 0.18, and whole scenes can be offset by 10–25 m. Model accuracy must be read as agreement with BIOMASS, and improving label quality (e.g. using the BIOMASS quality layer) is as important as improving the model.
- **Limitations**: Only one validation scene per region in four regions; Sentinel-1/2 inputs are mosaics rather than single acquisitions, and the Sentinel-1 acquisition period could not always be matched to the BIOMASS date; and whether the relation learned in 2026 stays valid for later years, as forests and sensors change, has not yet been tested.
- **Future work**: Test the model on Sentinel data from other years against later BIOMASS acquisitions; compare with independent references such as NASA GEDI and airborne laser scanning; include the BIOMASS quality layer; and extend validation to more scenes and regions.

## <!--{ as="div" }--> Open Science
| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| :--- | :--- | :--- | :--- |
| **[ESA BIOMASS Level-2A (MAAP STAC)](https://catalog.maap.eo.esa.int/catalogue/)** | Dataset | ESA (Earth Explorer 7 / MAAP) | P-band Forest Canopy Height (labels) and Ground Notch (auxiliary labels) used for training and validation. |
| **[Copernicus Sentinel-1 & Sentinel-2 Global Mosaics (CDSE)](https://dataspace.copernicus.eu/)** | Dataset | European Commission / ESA (CDSE) | Sentinel-2 quarterly optical mosaics and Sentinel-1 C-band radar global mosaics used as model inputs for training and validation. |
| **[Copernicus DEM GLO-30](https://registry.opendata.aws/copernicus-dem/)** | Dataset | ESA / Copernicus (AWS Open Data) | 30 m global elevation used for elevation, relief and slope. |
| **[IBM/ESA TerraMind v1](https://huggingface.co/ibm-esa-geospatial)** | Foundation Model | IBM Research & ESA Φ-lab | Pretrained multimodal Earth observation foundation model, used frozen via TerraTorch. |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)** | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Base layers and tools for interactive exploration of Earth observation indicators. |

#### References
- **ESA BIOMASS Mission**: Quegan, S., et al. (2019). The European Space Agency BIOMASS mission: Measuring forest above-ground biomass from space. *Remote Sensing of Environment*, 227, 44–60. https://doi.org/10.1016/j.rse.2019.03.032
- **TerraMind Foundation Model**: Jakubik, J., et al. (2025). TerraMind: Large-Scale Generative Multimodality for Earth Observation. *IBM Research & ESA Φ-lab*. https://huggingface.co/ibm-esa-geospatial
- **TerraTorch Framework**: Gomes, C., et al. (2025). TerraTorch: The Geospatial Foundation Models Toolkit for PyTorch. https://github.com/IBM/terratorch


## Contributors
- **Torben Dedring** (Ruhr-Universität Bochum) — Methodology, model architecture, data pipeline, validation and StoryMap curation.