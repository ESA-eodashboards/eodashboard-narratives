# Unsupervised Mapping of Urban Thermal Environments in the Milan and Monza-Brianza area <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
#### 

## Authors: Thomas Martinoli¹, Yiyi Cen¹, Sara Reffinetti¹
> 1- Politecnico of Milan

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2026. It was developed by a team from the Politecnico of Milan.*

## 
<p align="center">
  <img src="https://cdn.freebiesupply.com/logos/large/2x/politecnico-di-milano-1-logo-png-transparent.png" alt="Politecnico di Milano" height="150" style="margin: 0 15px;"/>
</p>

## Challenge

Urban environments are not spatially uniform. Vegetation, buildings, impervious surfaces, bare soil and water often occur within short distances and influence surface temperature in different ways. As a result, different parts of the same city can exhibit clearly different thermal conditions.

Urban environments are often described using predefined land-cover classes, such as built-up areas, vegetation or water. While these classifications are useful, real urban surfaces tend to vary continuously and often overlap or mix with one another. Fixed classes may therefore not fully capture this complexity.

This leads to our main research question:

**Can distinct urban thermal environments be identified directly from multi-variable Earth Observation data without defining the classes in advance?**


## Objective

The objective of this study is to use multi-variable Earth Observation data and unsupervised learning to develop a data-driven characterisation of urban environments in the Milan–Monza area.

By combining information related to temperature, vegetation and built-up characteristics, we use clustering to identify urban areas with similar environmental properties and then interpret their surface and thermal characteristics. Finally, the resulting clusters are compared with existing land-cover products and Local Climate Zones to understand how these data-driven urban types relate to established classification systems.

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=10.2 center=[9.2078,45.5268] layers='[{"type":"Tile","properties":{"id":"terrain-light","title":"Terrain Light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"study-area","title":"Study Area"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/AOI_Milan_Monza%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":"rgba(255,255,255,0.03)","stroke-color":"#d7191c","stroke-width":3}}]' animationOptions='{"duration":500}' }-->

#### Milan and Monza-Brianza Area

The study focuses on the Milan and Monza-Brianza area in northern Italy. The region includes dense urban areas, residential neighbourhoods, industrial and commercial zones, green spaces and peri-urban areas.

This spatial diversity makes the area well suited for investigating variations in urban surface characteristics and thermal conditions.


### <!--{ zoom=10.2 center=[9.2078,45.5268] layers='[{"type":"Tile","properties":{"id":"terrain-light","title":"Terrain Light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"tree-cover","title":"Tree Cover Density 2021"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/TCD_2021_100m_classes%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":["match",["get","class_id"],1,"rgba(198,233,192,0.60)",2,"rgba(77,175,74,0.70)",3,"rgba(0,100,0,0.85)","rgba(0,0,0,0)"]}},{"type":"Vector","properties":{"id":"study-area","title":"Study Area"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/AOI_Milan_Monza%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":"rgba(255,255,255,0)","stroke-color":"#d7191c","stroke-width":2}}]' animationOptions='{"duration":500}' }-->

#### Tree Cover Density

Tree cover varies substantially across the study area, from densely built urban zones with little vegetation to greener suburban and peri-urban areas.

Tree Cover Density describes the proportion of the surface covered by tree canopy and helps characterise the vegetation structure of the urban landscape.


### <!--{ zoom=10.2 center=[9.2078,45.5268] layers='[{"type":"Tile","properties":{"id":"terrain-light","title":"Terrain Light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"imperviousness","title":"Imperviousness Density 2021"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/Imperviousness_2021_100m_classes%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":["match",["get","class_id"],1,"rgba(245,220,180,0.60)",2,"rgba(230,130,80,0.72)",3,"rgba(170,30,30,0.85)","rgba(0,0,0,0)"]}},{"type":"Vector","properties":{"id":"study-area","title":"Study Area"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/AOI_Milan_Monza%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":"rgba(255,255,255,0)","stroke-color":"#d7191c","stroke-width":2}}]' animationOptions='{"duration":500}' }-->

#### Imperviousness Density

Impervious surfaces such as buildings, roads and paved areas are concentrated in the most urbanised parts of Milan and Monza-Brianza.

Imperviousness Density describes the proportion of sealed and artificial surfaces and provides an indication of built-up intensity across the study area.

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
