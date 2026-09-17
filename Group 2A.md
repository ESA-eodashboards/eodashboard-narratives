# Unsupervised Mapping of Urban Thermal Environments in the Milan and Monza-Brianza area <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2022/07/land-surface_temperature_in_milan_on_18_june_2022/24345700-1-eng-GB/Land-surface_temperature_in_Milan_on_18_June_2022_pillars.jpg" }-->
#### 

## Authors: Thomas Martinoli¹, Yiyi Cen¹, Sara Reffinetti¹
> 1- Politecnico of Milan

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2026. It was developed by a team from the Politecnico of Milan.*

## 
<p align="center">
  <img src="https://cdn.freebiesupply.com/logos/large/2x/politecnico-di-milano-1-logo-png-transparent.png" alt="Politecnico di Milano" height="150" style="margin: 0 15px;"/>
</p>

## Challenge
Cities are never thermally uniform. A shaded, tree-covered street can feel very different from a nearby area dominated by buildings and paved surfaces, even when the two places are only a short distance apart. Vegetation, buildings, impervious surfaces, bare soil and water all influence how heat is absorbed, stored and released across the urban landscape.

But how well can a few predefined land-cover classes capture this complexity?

In this study, we explore whether distinct urban thermal environments can emerge directly from multi-variable Earth Observation data using unsupervised learning, without defining the classes in advance. The resulting clusters are then interpreted through their surface characteristics and thermal behaviour, and compared with existing land-cover products or Local Climate Zones.

## Objective
The objective of this study was to

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=10.5 center=[9.2078,45.5268] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### Milan and Monza-Brianza Area
Satellite imagery focusing on the Milan and Monza-Brianza metropolitan area, providing a clear overview of the urban geography under study.

## Data and Methods
#### Dataset
| Data source | Product | Variables | Spatial Resolution |
| :---: | :---: | :---: | :---: |
| **Sentinel-3** | SLSTR – SL_2_LST | Land Surface Temperature (LST) | ~1 km |
| **Landsat 8** | Collection 2 Level-2 | Land Surface Temperature (LST) | 30 m |
| **Sentinel-2** | MSI – Level-2A (L2A) | NDVI, NDRE, NDBI, BSI, mNDWI, Albedo | 20 m |
| **Copernicus CLMS*** | Tree Cover Density | Vegetation cover | 10 m |
| **Copernicus CLMS*** | Imperviousness | Impervious surfaces | 10 m |

*CLMS: Copernicus Land Monitoring Service

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


## Conclusions


## Open Science


## Contributors
Authors, contibutors, reviewers