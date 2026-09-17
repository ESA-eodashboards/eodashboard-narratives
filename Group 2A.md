# Unsupervised Mapping of Urban Thermal Environments in the Milan and Monza-Brianza area <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
#### 

## Authors: Thomas Martinoli¹, Yiyi Cen¹, Sara Reffinetti¹
> 1- Politecnico of Milan

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2026. It was developed by a team from the Politecnico of Milan.*

## 
<p align="center">
  <img src="https://cdn.freebiesupply.com/logos/large/2x/politecnico-di-milano-1-logo-png-transparent.png" alt="Politecnico di Milano" height="80" style="margin: 0 15px;"/>
</p>

## Challenge
Describe challenge

## Objective
The objective of this study was to

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom=2.6456584324087107 center=[-10.569682342641302,7.8903138332408105] animationOptions='{"duration":500}' }-->
#### Title
Text

## Data and Methods
#### Dataset
| Dataset | Variables | Spatial Resolution |
| :---: | :---: | :---: |
| **Sentinel-3 SLSTR** | Land Surface Temperature (LST) | ~1 km |
| **Landsat 8–9** | Land Surface Temperature (LST) | 30 m |
| **Sentinel-2 MSI** | Spectral indices | 20 m |
| **Copernicus Tree Cover Density** | Vegetation cover | 10 m |
| **Copernicus Imperviousness** | Impervious surfaces | 10 m |

#### Methodology workflow
1. Extraction and selection
2. Aggregation and resample
3. Merge
4. Normalization
5. PCA
6. Clustering
7. Interpolation
8. Comparison

## Results


## Conclusions


## Open Science


## Contributors
Authors, contibutors, reviewers