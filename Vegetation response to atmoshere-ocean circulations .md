# Vegetation response to atmosphere-ocean circulations <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
#### An analysis of the spatio-temporal dynamics of vegetation in relation to the El Niño-Southern Oscillation.

## Authors: Theresa Mimi Freiß¹, Thomas Himmer¹ and Fabian Unterasinger¹
> ¹ Vienna University of Technology

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in **November 2026**. It was developed by a team from the **Vienna University of Technology**.*

## 
<p align="left">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/a1/TU_Wien-Logo.svg?utm_source=de.wikipedia.org&utm_campaign=index&utm_content=original" alt="TU Wien" height="80" style="margin: 0 15px;"/>
</p>

## Challenge
Atmosphere-ocean circulations significantly impact our environmental and socioeconomic systems worldwide. The El Niño-Southern Oscillation (ENSO) is one of the most influential climate variations, altering weather patterns across the globe. Year-to-year conditions in the tropical Pacific Ocean fluctuate between unusually warm (El Niño) and cold (La Niña) phases. These fluctuations, typically spanning two to seven years, disrupt atmospheric pressure patterns between the tropical Indian and Pacific Oceans. The resulting shifts in environmental conditions directly influence primary production patterns within the global carbon cycle. This challenge investigates the sensitivity of vegetation to these atmosphere-ocean circulations.

## Objective
This study aims to quantify the impact of ENSO events (La Niña and El Niño years) on vegetation dynamics compared to neutral baseline conditions. 
By analyzing long-term climate oscillation indices alongside vegetation specific Earth observation data, we seek to identify the spatio-temporal scales at which vegetation exhibits a response to ENSO-driven forcing.

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=2.6 center=[-10.5,7.8] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Tile","properties":{"id":"ESDC_nirv"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn"}}]' animationOptions='{"duration":500}' }-->
#### Global scale
The global perspective allows us to broadly observe climate anomalies and their relationship to vegetation health. By utilizing coarse-resolution data, we can identify large-scale trends and regional or temporal differences.

### <!--{ zoom=2.8 center=[-150,0] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Tile","properties":{"id":"ESDC_nirv"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn"}}]' animationOptions='{"duration":500}' }-->
#### ENSO
In the tropical Pacific-Indian Ocean interaction zone, ENSO dynamics drive major shifts in atmospheric pressure and sea surface temperatures. The Relative Oceanic Niño Index (RONI) serves as a key indicator, distinguishing between El Niño (warm) and La Niña (cold) conditions.

### <!--{ zoom=4 center=[-50,0] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Tile","properties":{"id":"ESDC_nirv"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn"}}]' animationOptions='{"duration":500}' }-->
#### Anomalies
When analyzing the correlation between ENSO indices and vegetation index anomalies, we observe distinct spatio-temporal patterns. Negative vegetation anomalies often coincide with ENSO-driven extreme precipitation shifts, revealing sensitive regional ecosystems that experience delayed responses to ocean-atmospheric forcing.

## Data and Methods
#### Dataset
This study utilizes climate and vegetation indices to assess ecosystem sensitivity.

**NOAA Climate Oscillation Indices**
- **Relative Oceanic Niño Index (RONI):** A 3-month running mean of tropical-adjusted Niño 3.4 SST anomalies (1991–2020 base period), covering 1950–2026.

**ESDC Vegetation Indices**
- **Near Infrared Reflectance of Vegetation (NIRv):** Derived from MODIS/Terra+Aqua BRDF/Albedo data at a 0.25° spatial resolution and 8-day temporal cadence.

#### Methodology
Our analytical workflow includes:
1. **Data Retrieval:** Extraction of RONI indices and DeepESDL vegetation datasets.
2. **Preprocessing:** Time-series extraction and harmonic decomposition to isolate seasonal components.
3. **Correlation Analysis:** Evaluating lag-time responses between ENSO indices and vegetation anomalies across global biomes.
4. **Hotspot Identification:** Mapping geographical areas that show statistically significant vegetation response to atmospheric forcing.

## Results
The preliminary analysis generates:
- **Time-series correlation maps:** Identifying regions where vegetation lags behind ENSO cycles.
- **Anomaly Hotspots:** Regional focus areas (e.g., Sub-Saharan Africa and Ecuador) exhibiting high sensitivity.
- **Tipping Point Analysis:** Exploration of long-term ecosystem resilience to understand if recurring ENSO cycles lead to permanent structural changes or degradation.

## Conclusions
Preliminary findings suggest that vegetation response to ENSO is non-uniform and highly dependent on regional moisture availability. Future work will focus on refining lag-time estimates to better predict vegetation recovery after extreme ENSO-driven drought events.

## Open Science
All processing workflows and data analysis scripts are developed within an open-science framework to ensure reproducibility and transparency in our findings regarding Earth system health.

## Contributors
Theresa Mimi Freiß, Thomas Himmer, and Fabian Unterasinger. 

![globe_transparent_background.jpg](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c4ed21918274ec4cea124699c59c4862babc5840/assets/thmimif/globetransparentbackground-1794928378057.jpg)