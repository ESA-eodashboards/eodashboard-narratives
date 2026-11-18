---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
official: false

---

# Vegetation response to atmosphere-ocean circulations <!--{ as="img" mode="hero" src="https://cdn.pixabay.com/photo/2011/12/13/17/07/earth-11048_1280.jpg" }-->
## Authors: Theresa Mimi Freiß¹, Thomas Himmer¹ and Fabian Unterasinger¹
> ¹ Vienna University of Technology

<!-- Spatio-temporal dynamics of vegetation response in relation to the El Niño-Southern Oscillation-->

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

![RONI_1950.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c78f6483ad0c6f630909e0498cefeaf3e5d45d51/assets/thmimif/RONI1950-1794992576572.png)<figcaption>***Fig. 1:*** *Relative Oceanic Niño Index (RONI) from 1950 to 2026 indicating warm El Niño (positive, red) and cold La Niña (negative, blue) periods.*</figcaption>

These ENSO-driven variations in climate conditions result in altered weather patterns globally. Seasonal differences reveal whether an El Niño or La Niña period occurs in winter or summer.

![el_winter1.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/637f242ae961a9c2ba0753e9780fb156c1c5f254/assets/thmimif/elwinter1-1795000251975.png)<figcaption>***Fig. 2:*** *El Niño effects from December to February.*</figcaption>

![el_summer1.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/6f3393ebf5cbd98cb168cd3570c5ff0a03f049a2/assets/thmimif/elsummer1-1795000283074.png)<figcaption>***Fig. 3:*** *El Niño effects from June to August.*</figcaption>

![la_winter1.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e9d73b5cb2886282ded9f638a84ee46666478627/assets/thmimif/lawinter1-1795000306894.png)<figcaption>***Fig. 4:*** *La Niña effects from December to February.*</figcaption>

![la_summer1.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/9f04d681a2c8214a44cbe21881c2e1d92b25dbf2/assets/thmimif/lasummer1-1795000351654.png)<figcaption>***Fig. 5:*** *La Niña effects from June to August.*</figcaption>

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
- **Normalized Difference Vegetation Index (NDVI):** MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Reflectance Daily L3 Global 0.05 Deg CMG and Vegetation Indices, 0.25° spatial resolution
- **Gross Primary Productivity (GPP):** FLUXCOM, 0.25° spatial resolution

#### Methodology
Our analytical workflow includes:
1. **Data Retrieval:** Extraction of RONI indices and DeepESDL vegetation datasets.
2. **Preprocessing:** Time-series extraction and harmonic decomposition to isolate seasonal components.
3. **Correlation Analysis:** Evaluating lag-time responses between ENSO indices and vegetation anomalies across global biomes.
4. **Hotspot Identification:** Mapping geographical areas that show statistically significant vegetation response to atmospheric forcing.

- Extract ENSO indices from available NOAA datasets
-  Work global at very coarse resolution to identify big trends and differences in geographical areas or comapared to other times)
- Data preprocessing: time-series extraction, time-series decomposition, calculate lag times
- Additionally select study area and study period of an anomaly
- Potential study areas: Sub-saharan Africa (e.g. South Africa, Namibia, Kenya, Ghana), South America (Ecuador)
- Decide whether to focus on current El Niño (probably not enought data to evaluate laged effect on vegetation) or to focus on past events
- Analysis of correlations between VI anomalies and ENSO indices, of trends and anomalies, geographical hotspots of anomalies, lags between the datasets
- What makes El Niño events different from "normal" droughts/heatwaves?
- Comparing sites where ENSO causes different climatic anomalies and their different impact


## Results
The preliminary analysis generates:
- **Time-series correlation maps:** Identifying regions where vegetation lags behind ENSO cycles.
- **Anomaly Hotspots:** Regional focus areas (e.g., Sub-Saharan Africa and Ecuador) exhibiting high sensitivity.

Optional:
- **Tipping Point Analysis:** Exploration of long-term ecosystem resilience to understand if recurring ENSO cycles lead to permanent structural changes or degradation.

- Timeseries plots
- Plots of correlations and lag times
- Maps of potential hotspots of anomalies/negative trends/positive trends

Optional:
- Identification of "turning points"/tipping points with regard to larger time-series. Do ecosystem get more resilient or collapse?

## Conclusions


## Open Science
All processing workflows and data analysis scripts are developed within an open-science framework to ensure reproducibility and transparency in our findings regarding Earth system health.

| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| --- | --- | --- | --- |
| **[RONI](https://www.ncei.noaa.gov/access/monitoring/enso/sst#roni)** | Dataset | NOAA | Climate Oscillation Indices |
| **[ESDC](https://earthsystemdatalab.net/guide/data/pre-generated/ESDC/#ndvi)** | Dataset | DeepESDL | Vegetation Indices |
| **[DeepESDL](https://earthsystemdatalab.net/)** | Platform  | ESA EarthCODE | ESDC Vegetation Data |

#### Notebook
Access the notebook to reproduce the study workflow.
<iframe width="100%" height="600" src="link-to-notebook" frameborder="0"></iframe>

#### References
- Michael J. McPhaden et al. ,ENSO as an Integrating Concept in Earth Science.Science314,1740-1745(2006). DOI:10.1126/science.1132588
- National Oceanic and Atmospheric Administration (NOAA), Cold & Warm Episodes by Season - Relative Oceanic Niño Index (RONI):
Historical El Niño / La Niña episodes (1950–Present). https://cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/
- National Oceanic and Atmospheric Administration (NOAA), Weather Impacts of ENSO. https://www.noaa.gov/jetstream/enso_impacts
- DeepESDL, Earth System Data Cube (ESDC) v3.0.1. https://earthsystemdatalab.net/guide/data/pre-generated/ESDC/#gross_primary_productivity

## Contributors
Theresa Mimi Freiß, Thomas Himmer, and Fabian Unterasinger. 
