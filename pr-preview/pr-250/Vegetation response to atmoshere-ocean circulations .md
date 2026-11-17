# Vegetation response to atmoshere-ocean circulations <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
#### 

## Authors:  Theresa Mimi Freiß¹, Thomas Himmer¹ and Fabian Unterasinger¹
> ¹ Vienna University of Technology

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in **November 2026**. It was developed by a team from the **Vienna University of Technology**.*

## 
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
The study contributes to answering the question of how and what the spatio-temporal scales at which vegetation responds to ENSO events are.

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Tile","properties":{"id":"ESDC_kndvi"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn"}}]' zoom=2.6 center=[-10.5,7.8] animationOptions='{"duration":500}' }-->
#### Global scale
The global perspective allows us to observe broad climate patterns and their relationship to vegetation productivity across major biomes.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Tile","properties":{"id":"ESDC_kndvi"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn"}}]' zoom=2.8 center=[-150,0] animationOptions='{"duration":500}' }-->
#### ENSO
From the tropical Pacific and Indian Ocean interaction zone, where ENSO dynamics drive major shifts in atmospheric pressure and sea surface temperature the Relative Oceanic Niño Index (RONI) is derived.
It distincts between unusually warm El Niño (red) and cold La Niña (blue)

![RONI_1950.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/7e7b36a5828df2276b62fec20cb411b6bfd5598a/assets/thmimif/RONI1950-1794923954055.png)

## Data and Methods
#### Dataset
Datasets of this study comprised indicators for ENSO, as well as for vegetation.

**NOAA Climate Oscillation Indices**
- **Relative Oceanic Niño Index (RONI):**
 3-Month Running Mean of Tropical-Adjusted Niño 3.4 SST Anomalies of the 1991–2020 base period, time period 1950-2026, monthly

**ESDC Vegetation Indices**
-  **Near Infrared Reflectance of Vegetation (NIRv):** MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Reflectance Daily L3 Global 0.05 Deg CMG and Vegetation Indices, spacial resolution of 0.25°, 8-day temporal resolution
-  NDVI


#### Methodology workflow
The methodology follows steps of retreaval and processing of climate oscillation and vegetation indices data to compare and analyse them and further derive correlations, trends and anomalies:

- Extract ENSO indices from available datasets NOAA (RONI)
- Read DeepESDL ESDC Vegetation Indices data: extract indices of interest
- First focus is on a global scale (to identify big trends and differences in geographical areas or comapared to other times?)
- Data preprocessing: time-series extraction, time-series decomposition
- Look at different lag times
- Select study area and study period for a more detailed investigation
- Potential study areas: Sub-saharan Africa (e.g. South Africa, Namibia, Kenya, Ghana), South America (Ecuador)
- 
- Decide whether to focus on current El Niño (probably not enought data to evaluate laged effect on vegetation) or to focus on past events
- Analysis of correlations between vegetation indices anomalies and ENSO indices, of trends and anomalies, geographical hotspots of anomalies, lags between the datasets
- What makes El Niño events different from "normal" droughts/heatwaves?
- Comparing sites where ENSO causes different climatic anomalies and their different impact

## Results
- Timeseries plots
- Plots of correlations and lag times
- Maps of potential hotspots of anomalies/negative trends/positive trends

Possible further experiments (not expected)
- Identification of "turning points"/tipping points with regard to larger time-series. Do ecosystem get more resilient or collapse?

## Conclusions


## Open Science


## Contributors
Theresa Mimi Freiß, Thomas Himmer and Fabian Unterasinger, contibutors, reviewers