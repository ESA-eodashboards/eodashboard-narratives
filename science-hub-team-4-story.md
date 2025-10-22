---
cover-image: https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2022/10/svalbard/24544693-1-eng-GB/Svalbard_pillars.jpg
date: 2025-01-01
theme: theme_name
tags: some,tags

---

# Wet snow mapping with multimodal foundation models  <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2022/10/svalbard/24544693-1-eng-GB/Svalbard_pillars.jpg" }-->
### Authors: Leam Howe, Sean O Heir, Miguel Espinosa Minano (Univeristy of Leeds) <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

# 
*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2025. It was developed by a team from University of Leeds.*

## Challenge
Snow isn’t just snow — it varies widely in its characteristics and impacts. Two primary types are dry snow and wet snow, which differ in water content, density, grain size, and formation conditions. Dry snow is powdery and light, occurring in cold temperatures well below freezing, whereas wet snow contains higher water content, is denser, and forms near or above freezing temperatures.

Mapping wet snow is critical because it influences water resource management, flood prediction, climate research, agriculture, and disaster preparedness. Mapping wet snow accurately remains a challenge due to the complex interaction of radar signals with snow characteristics. While dry snow allows deeper penetration of C-band radar signals (up to 10 meters), wet snow’s higher liquid water content absorbs microwave radiation, limiting penetration to just a few centimeters. This leads to a strong contrast in radar backscatter intensity, with wet snow showing significantly lower backscatter compared to dry snow or snow-free ground.

Current mapping methods rely heavily on thresholding, filtering, and the availability of dry snow reference areas or optical imagery, which can be computationally expensive, regionally limited, and prone to errors in complex terrain. Moreover, these approaches struggle to distinguish wet snow from other wet surfaces like soil.

The emergence of Geospatial Foundation Models (FMs) — large AI models pre-trained on diverse satellite and airborne data — offers a new pathway. These models can fuse multi-modal signals (SAR, optical, thermal, DEM, and reanalysis data) and implicitly learn complex cues for wet snow detection without needing summer reference data, potentially overcoming existing limitations.

<div style="text-align: center;"> <img src="https://example.com/sentinel1-wet-snow-map.png" width="500"/> <p><b>Figure 1.</b> Sentinel-1 radar image highlighting wet snow distribution in Svalbard.</p> </div>

## Objective

The objective of this study was to develop a reproducible framework to classify snow types using Sentinel-1 data, focusing on wet snow detection. This involved downloading Sentinel-1 radar data for Svalbard, constructing an Earth System Data Lab (ESDL) data cube, and fine-tuning a Geospatial Foundation Model to perform semantic segmentation of snow types — distinguishing wet snow, dry snow, and no snow.

Predictions from the model were then validated against ground-truth data, enabling assessment of classification accuracy and operational potential for snow mapping applications.

## Use case <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"SSLC1_Seasonal_S1_AMP_hv_interferometric_coherence;:;2d96aa0d-5170-4979-b00e-e9e3eb1d3308;:;SSLC1_Seasonal_S1_AMP_hv_interferometric_coherence;:;EPSG:3857","title":"SSLC1_Seasonal_S1_AMP_hv_interferometric_coherence"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["S1_AMP_HV"],"TILED":true,"TIME":"2020-09-21T00:00:00Z/200-09-21T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="7.940926886189218" center=[17.92901856264105,78.07209721925807] projection="" animationOptions={duration:500}}-->
#### Svalbard
Svalbard, an Arctic archipelago, is an ideal testbed for wet snow mapping due to its extreme climate and diverse snow conditions. Accurate monitoring of wet snow here supports water resource management, flood risk assessment, and climate studies in this sensitive region. Using Sentinel-1 data, our model identifies and classifies snow types across Svalbard, providing valuable insights for environmental monitoring and decision-making in the Arctic.



<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;">
    <img 
        src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-4/Globe4_svalbard.png?raw=true" 
        style="max-width: 100%; width: 800px; height: auto;"
        alt="Use cases/forests locations"
    />
    <p style="text-align: center; font-size: 1.2em; margin-top: 10px;">
        <b>Figure X.</b> Use cases/forests locations.
    </p>
</div>




