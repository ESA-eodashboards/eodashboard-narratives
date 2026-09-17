---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
official: false

---

# Title of the story/Challenge <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
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
This challenge assesses relative NO₂ pollution risk across the Milan Metropolitan Area by combining three components: Sentinel-5P/TROPOMI NO₂ hazard, population-density exposure and age-related vulnerability.

The hazard layer is derived from quality-filtered tropospheric NO₂ observations. Population density represents the number of residents potentially exposed in each grid cell. Age vulnerability is represented by the proportion of residents in sensitive age groups, here we took people under 18 and adults over 80.

All three components are normalised to a 0–1 scale and combined using a multiplicative index:

risk = normalised hazard × normalised exposure × normalised age vulnerability.

The result is a relative screening indicator showing where high NO₂ levels overlap with dense populations and more vulnerable age groups. It should not be interpreted as a direct health-risk or regulatory exceedance map.


## Objective
The objective of this study was to 


## Earth observations <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="" animationOptions={duration:500}}-->
#### Title
Text



## Data and Methods
#### Dataset
- **Source**: 
- **Temporal coverage**: 

#### Methodology workflow
Description


###### Ground-station harmonisation and regression calibration

NO2 data prcessing workflow brings together satellite observations and ground measurements to estimate surface-level NO₂ across the Milan Metropolitan Area. The administrative boundary defines the study area and a common grid provides the spatial framework. Sentinel-5P/TROPOMI Level-2 NO₂ files from 1 September 2024 to 31 December 2025 are first listed in an inventory. HARP then checks their geolocation data to identify the orbits covering Milan. The selected file paths are stored in a CSV inventory for reuse in later processing.

Hourly observations from nine ground stations provide the reference measurements for calibration. Sensor identifiers link these observations to the station catalogue, which supplies station names and coordinates. The two datasets describe different quantities: ground stations measure surface NO₂ concentration in µg/m³, whereas the satellite measures the tropospheric NO₂ column.

Connecting these measurements requires alignment in both time and space. The midpoint between the start and end timestamps in each satellite filename serves as an approximate timing reference, converted to Milan local time. Ground observations within ±1 hour of that reference are averaged for each station. This timing remains an approximation because the file timestamps describe the full orbit segment, rather than the exact observation time over Milan.

For spatial alignment, each station is linked to the mean of the surrounding 3×3 cells. This step produce a paired dataset in which each row links one station and one satellite orbit, with the corresponding ground concentration and satellite column value.

The paired observations form the basis of the regression calibration. Ordinary least-squares linear regression relates the satellite column to ground-level NO₂, with Ridge, Huber and Random Forest regression tested as alternatives. Cross-validation grouped by date compares model performance, while a separate validation holding out individual stations assesses the linear model’s ability to generalise across locations. Linear regression performs similarly to Ridge and is retained for its simplicity and interpretability. The resulting relationship provides the calibration needed to estimate surface-level NO₂ across the Milan grid.

## Results


## Conclusions



## <!--{ as="div" }--> Open Science
| **Name**                                                                                                                                                 | **Type**            | **Agency / Provider**                     | **Description / Usage**                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[DATASET NAME](LINK)** | Dataset             | DeepESDL / ESDC                           | Description how this dataset was used in this story |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)**                                    | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Provides base layers and visualization tools for interactive exploration of NDVI and other Earth observation indicators.                                                                                                                |

#### Notebook
Access the notebook to reproduce the study workflow.
<iframe width="100%" height="600" src="LINK TO NOTEBOOK" frameborder="0"></iframe>


#### References
- Reference 1

- Reference 2



## Contributors
Authors, contibutors, reviewers 

