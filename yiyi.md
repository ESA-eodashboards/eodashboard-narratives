---
cover-image: https://placehold.co/600x400/png
date: 2026-09-17
theme: theme_name
tags: urban-heat,earth-observation,unsupervised-learning,milan,monza
official: false
---

# Unsupervised Mapping of Urban Thermal Environments in the Milan and Monza-Brianza Area <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->

## Authors: Thomas Martinoli¹, Yiyi Cen¹ and Sara Reffinetti¹ <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

> ¹ Politecnico di Milano

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2026. It was developed by a team from Politecnico di Milano.*

## <!--{ nav="false"}-->

<p align="center">
  <img src="https://cdn.freebiesupply.com/logos/large/2x/politecnico-di-milano-1-logo-png-transparent.png"
       alt="Politecnico di Milano"
       height="150"
       style="margin: 0 15px;"/>
</p>


## Challenge

Urban environments are highly heterogeneous. Vegetation, buildings, impervious surfaces, bare soil and water can occur within short distances and influence surface temperature in different ways. As a result, thermal conditions can vary considerably even within the same city.

Urban areas are often described using predefined land-cover classes. While these classifications are useful, they may not fully capture the gradual transitions and complex combinations of surface characteristics that shape local thermal environments.

This raises an important question:

**Can distinct urban thermal environments be identified directly from Earth Observation data without defining the classes in advance?**


## Objective

The objective of this study is to identify and characterise distinct urban thermal environments from combinations of temperature, vegetation and built-up characteristics using unsupervised learning, without relying on predefined land-cover classes.


## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->


### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false}]}]' zoom="9.5" center=[9.19,45.52] projection="" animationOptions={duration:800} }-->

#### Milan and Monza-Brianza Area

The Milan and Monza-Brianza area includes dense urban centres, residential neighbourhoods, industrial and commercial zones, green spaces and peri-urban areas.

These different surface types occur within relatively short distances, providing strong spatial contrasts for studying urban environmental and thermal conditions.

The area was also selected because the main Earth Observation datasets required for the analysis provide overlapping coverage for the selected period.


### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"kNDVI - TEST LAYER"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"},"visible":true},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"},"visible":true}]}]}]}]' zoom="10.5" center=[9.19,45.52] projection="" animationOptions={duration:800} }-->

#### Vegetation — Test Layer

Vegetation varies considerably across the urban landscape. Trees and other green surfaces can influence local thermal conditions through shading and evapotranspiration.

Sentinel-2 vegetation indices and Tree Cover Density allow us to observe differences in vegetation cover and greenness across the Milan and Monza-Brianza area.

*This kNDVI layer is used only to test the EO Dashboard map-layer transition. It will later be replaced by the vegetation data used in this study.*


## Data and Methods

#### Dataset

| Data source | Product | Variables | Spatial Resolution |
| :---: | :---: | :---: | :---: |
| **Sentinel-3** | SLSTR – SL_2_LST | Land Surface Temperature (LST) | ~1 km |
| **Landsat 8** | Collection 2 Level-2 | Land Surface Temperature (LST) | 30 m |
| **Sentinel-2** | MSI – Level-2A | NDVI, NDRE, NDBI, BSI, MNDWI, Albedo | 20 m |
| **Copernicus CLMS** | Tree Cover Density | Tree canopy cover | 10 m |
| **Copernicus CLMS** | Imperviousness Density | Impervious surface cover | 10 m |

*CLMS: Copernicus Land Monitoring Service*

Summer 2021 (June–August, JJA) was selected to represent warm-season conditions and because the main datasets used in the study were simultaneously available during this period.


#### Methodology workflow

1. Data extraction and selection
2. Temporal compositing and spatial aggregation
3. Grid alignment and feature merging
4. Normalization
5. PCA
6. Clustering
7. Cluster interpretation
8. Comparison


## Results

Results will present the PCA analysis, the final cluster map, the interpretation of the identified urban environmental types and their comparison with thermal conditions and existing land-cover classifications.


## Conclusions

To be completed after the final clustering and comparison results are available.


## <!--{ as="div" }--> Open Science

| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| --- | --- | --- | --- |
| **Sentinel-2 MSI** | Dataset | Copernicus / ESA | Multispectral imagery used to derive vegetation and built-up surface indices. |
| **Tree Cover Density** | Dataset | Copernicus Land Monitoring Service | Used to describe tree canopy cover across the study area. |
| **Imperviousness Density** | Dataset | Copernicus Land Monitoring Service | Used to describe the proportion of sealed and artificial surfaces. |
| **Land Surface Temperature** | Dataset | ESA / USGS | Used to characterise and compare thermal conditions across the study area. |
| **EO Dashboard** | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Used for interactive visualisation and storytelling of Earth Observation data and project results. |


#### Notebook

Access the notebook to reproduce the study workflow.

<iframe width="100%" height="600" src="LINK TO NOTEBOOK" frameborder="0"></iframe>


#### References

- References will be added here.


## Contributors

Authors, contributors and reviewers