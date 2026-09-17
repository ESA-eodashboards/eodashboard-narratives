# Mapping urban heat exposure and vulnerability <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
#### 

## Authors: Francesco Mezza¹, Sona Guliyeva², Filippos Kostikiadis³, and Sophia Dolla³
> ¹ Polytechnic University of Milan ² Polytechnic University of Turin  ³ Aristotle University of Thessaloniki

*This story is based on results from the Science Hub Challenge organised and hosted by ESA's ESRIN Science Hub in February 2024. The scope of the challenge was to develop a framework to identify urban areas that are potentially most vulnerable to heat exposure during heatwave events combining Earth Observation data with geospatial information. The method was implemented on the AVL platform by a team of Master students from the Polytechnic University of Milan, the Polytechnic University of Turin and Aristotle University of Thessaloniki. The data and code are made openly available.*

## 
<p align="center">
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="Ca' Foscari" height="80" style="margin: 0 15px;"/>
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="NOC" height="80" style="margin: 0 15px;"/>
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="BAS" height="80" style="margin: 0 15px;"/>
</p>

## Heat exposure and vulnerability


## Method and datasets
The core question addressed whether EO data could be combined with geospatial information to locate urban areas experiencing heightened heat stress during heatwave events. To achieve this, the team's methodology included the following steps and expected outcomes:

- **Data Retrieval & Anomaly Mapping**: Selecting a heatwave event over a European city and retrieving Sentinel-3 Land Surface Temperature (LST) temperature observations for both the heatwave and a non-heatwave reference period to compute temperature anomalies.
- **Deriving Spatial Indicators**: Using additional datasets (such as green cover by Comune di Torino and Copernicus High Resolution Layer Imperviousness) to describe the urban environment through indicators like vegetation cover, impervious surfaces, and built-up density.
- **Heat Exposure Index (HEI)**: Defining an index that combines thermal intensity with exposure indicators to map and rank the most exposed urban districts.

The main used datasets were:
- **Sentinel-3 SLSTR (Land Surface Temperature - LST)**: Sentinel-3 is a European Earth Observation satellite mission developed to support Copernicus ocean, land, atmospheric, emergency, security, and cryospheric applications.The primary goal of the Sentinel-3 mission is to measure sea surface topography, sea and land surface temperature, and ocean and land surface color with high accuracy and reliability. This data is used to support ocean forecasting systems, environmental monitoring, and climate monitoring.


- **High Resolution Layer Imperviousness**: The High Resolution Layer (HRL) Imperviousness by the Copernicus Land Monitoring Service (CLMS) captures the spatial distribution and change over time of artificially sealed and built-up areas in high-resolution and harmonized manner over entire Europe. The contained datasets offer valuable insights for a variety of domains and applications – from infrastructure planning, urban management and environmental monitoring to disaster preparedness, real estate and tourism.
- **GIS Data from the Municipality of Torino**: Vector files to define the official administrative boundaries of the city (the 8 "circoscrizioni"). They were used to aggregate the raster data and calculate statistics for each individual district.
-**Green Areas Data (Municipality of Torino Open Data)**: Vector files (shapefiles) retrieved from the city's official open data portal, mapping the precise polygons of public green spaces across the urban area (including parks, gardens, and tree-lined avenues).
## Objective
The objective of this study was to

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom=2.6456584324087107 center=[-10.569682342641302,7.8903138332408105] animationOptions='{"duration":500}' }-->
#### Title
Text

## Data and Methods
#### Dataset
- **Source**: 
- **Temporal coverage**: 

#### Methodology workflow
Description

## Results


## Conclusions


## Open Science


## Contributors
Authors, contibutors, reviewers