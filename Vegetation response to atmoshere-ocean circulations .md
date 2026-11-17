---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
official: false

---

# Vegetation response to atmoshere-ocean circulations <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
## Authors:  Theresa Mimi Freiß¹, Thomas Himmer¹ and Fabian Unterasinger¹  <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
> ¹ Vienna University of Technology

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in **November 2026**. It was developed by a team from the **Vienna University of Technology**.*

##  <!--{ nav="false"}-->
<p align="left">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/a1/TU_Wien-Logo.svg?utm_source=de.wikipedia.org&utm_campaign=index&utm_content=original" alt="Ca' Foscari" height="80" style="margin: 0 15px;"/>
</p>


## Challenge
Atmoshere-ocean circulations significantly impact our environmental and socioeconomic systems worldwide.
The El Niño-Southern Oscillation (ENSO) is one of the most influencial climate variation altering weather patterns in various regions around the globe. 
The year-to-year conditions in the tropical Pacific Ocean fluctuate between unusually warm (El Niño) and cold (La Niña).
Typical timescales of these fluctuations span from two to seven years and effect the atmospheric pressure pattern between the tropical Indian and Pacific Oceans.
The altered environmental conditions of ENSO lead to variations in primary production patterns in the carbon cycle.
This challenge focuses on vegetation response to these atmoshere-ocean circulations.

## Objective
The objective of this study was to identify the impact of ENSO events/years (La Niña and El Niño) on vegetation dynamics compared to non-La Niña and El Niño years.
The goal is to answer how and what are the spatio-temporal scales at which vegetation responds to ENSO events?

## Earth observations <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="" animationOptions={duration:500}}-->
#### Title
Text



## Data and Methods
#### Dataset
Datasets of this study comprised indicators for ENSO, as well as for vegetation.

**NOAA Climate Oscillation Indices**
- **Source**: 
- **Temporal coverage**: 
- Relative Oceanic Niño Index (RONI):

**ESDC Vegetation Indices**
- **Source**: 
- **Temporal coverage**: 
-  Near Infrared Reflectance of Vegetation (NIRv):


#### Methodology workflow
Description

- Compute ENSO indices from SST over the required regions or extract ENSO indices from available datasets NOAA
- Select study area and study period (or probably work global at very coarse resolution to identify big trends and differences in geographical areas or comapared to other times)
- Potential study areas: Sub-saharan Africa (e.g. South Africa, Namibia, Kenya, Ghana), South America (Ecuador)
- Decide whether to focus on current El Niño (probably not enought data to evaluate laged effect on vegetation) or to focus on past events
- Data preprocessing: time-series extraction, time-series decomposition
- Analysis of correlations between VI anomalies and ENSO indices, of trends and anomalies, geographical hotspots of anomalies, lags between the datasets
- What makes El Niño events different from "normal" droughts/heatwaves?
- Comparing sites where ENSO causes different climatic anomalies and their different impact




## Results
- Timeseries plots
- Plots of correlations and lag times
- Maps of potential hotspots of anomalies/negative trends/positive trends

Possible further experiments (not expected)
- Identification of "turning points"/tipping points with regard to larger time-series. Do ecosystem get more resilient or collapse?

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
- Michael J. McPhaden et al. ,ENSO as an Integrating Concept in Earth Science.Science314,1740-1745(2006).DOI:10.1126/science.1132588





## Contributors
Theresa Mimi Freiß, Thomas Himmer and Fabian Unterasinger, contibutors, reviewers 

