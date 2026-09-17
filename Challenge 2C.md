# Mapping urban heat risk <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/FrancescoMezza/torino-heat-exposure/main/Mole_Antonelliana_(Torino)_10.jpg" }-->
#### 

## Authors: Francesco Mezza¹, Sona Guliyeva², Filippos Kostikiadis³, and Sophia Dolla³
> ¹ Polytechnic University of Milan ² Polytechnic University of Turin  ³ Aristotle University of Thessaloniki

*This story is based on results from the Science Hub Challenge organised and hosted by ESA's ESRIN Science Hub in February 2024. The scope of the challenge was to develop a framework to identify urban areas that are potentially most vulnerable to heat exposure during heatwave events combining Earth Observation data with geospatial information. The method was implemented on the AVL platform by a team of Master students from the Polytechnic University of Milan, the Polytechnic University of Turin and Aristotle University of Thessaloniki. The data and code are made openly available.*

## 
<p align="center">
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="Ca' Foscari" height="120" style="margin: 0 15px;"/>
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="NOC" height="120" style="margin: 0 15px;"/>
  <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_250,h_250/https://markleisherproductions.com/wp-content/uploads/2021/01/logo-placeholder-png-2.png" alt="BAS" height="120" style="margin: 0 15px;"/>
</p>

## Heat exposure and vulnerability
Heat exposure refers to the presence of people, ecosystems, infrastructure or other assets in areas affected by excessive heat. It is influenced by temperature, humidity, wind, solar radiation and local geographical and urban characteristics. In urban areas, factors such as building materials, land cover, vegetation and the urban heat island (UHI) effect can create substantial spatial differences in heat exposure. 

Vulnerability describes the susceptibility of individuals or populations to adverse effects from heat. It is influenced by physiological, demographic, social and socioeconomic factors, as well as housing conditions and access to cooling, healthcare and other essential services. Certain groups, such as older adults, children and outdoor workers, may be particularly susceptible to heat-related impacts. 

According to the climate risk framework, risk results from the interaction between hazard, exposure and vulnerability. Thus, a heatwave represents the hazard, while heat exposure and vulnerability determine how strongly individuals and populations may be affected. 

## Method and datasets
The core question addressed was whether EO data could be combined with geospatial information to locate urban areas experiencing heightened heat stress during heatwave events. To achieve this, the used datasets were:
- **Sentinel-3 SLSTR (Land Surface Temperature - LST)**: Sentinel-3 is a European Earth Observation satellite mission developed to support Copernicus ocean, land, atmospheric, emergency, security, and cryospheric applications.The primary goal of the Sentinel-3 mission is to measure sea surface topography, sea and land surface temperature, and ocean and land surface color with high accuracy and reliability. This data is used to support ocean forecasting systems, environmental monitoring, and climate monitoring.

<p align="center"><img src="https://sentinels.copernicus.eu/documents/4634164/9bbb4317-7cb9-1c8b-a382-3ad82b6a28e4" width="600"/></p>
<p align="center" style="font-size: 0.85em; color: #666;"><em>Sentinel-3 satellite, ESA.</em></p>


- **High Resolution Layer Imperviousness**: The High Resolution Layer (HRL) Imperviousness by the Copernicus Land Monitoring Service (CLMS) captures the spatial distribution and change over time of artificially sealed and built-up areas in high-resolution and harmonized manner over entire 
Europe. The contained datasets offer valuable insights for a variety of domains and applications – from infrastructure planning, urban management and environmental monitoring to disaster preparedness, real estate and tourism.

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Torino%20-%20Imperviousness%202024.png?raw=true" width="600"/></p>

- **District and Popolutation Data (Municipality of Torino)**: Vector files to define the official administrative boundaries of the city (the 8 "circoscrizioni") and the number and age of inhabitants in each district. They were used to aggregate the raster data and calculate statistics for each.

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Vulnerability%20Map%20%20Over%2065%20by%20District%20(Turin).png?raw=true" width="600"/></p>

- **Green Areas Data (Municipality of Torino Open Data)**: Vector files retrieved from the city's official open data portal, mapping the precise polygons of public green spaces across the urban area (including parks, gardens, and tree-lined avenues). 

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Urban%20green%20areas.png?raw=true" width="600"/></p>

The team's methodology included the following steps and expected outcomes:

- **Data Retrieval & Anomaly Mapping**: Selecting a heatwave event over Turin between August 1-15 and retrieving Sentinel-3 Land Surface Temperature (LST) temperature observations for both the heatwave and a non-heatwave reference period to compute temperature anomalies.

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Nighttime%20LST%20Evolution%20-%20Turin%20Districts%20.png?raw=true" width="1000"/></p>

- **Deriving Spatial Indicators**: Using additional datasets (such as green cover by Comune di Torino and Copernicus High Resolution Layer Imperviousness) to describe the urban environment through indicators like vegetation cover, impervious surfaces, and built-up density.
- **Heat Exposure Index (HEI)**: Defining an index that combines thermal intensity with exposure indicators to map and rank the most exposed urban districts.

## Heat risk in Turin
The table indicates the districts that are more exposed to heat during heatwaves.
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/climate-change_v2.jpg?raw=true" width="1000"/></p>
The risk index ranges from 0-1, and is calculated based on: 

- Surface heat (daily Sentinel-3 LST, clipped 15–42 °C)

- Age vulnerability (% population over 65)

- Lack of greenery (inverse of green cover per district)

- Imperviousness (soil sealing)


## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=12 center=[7.6869,45.0703] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### Turin Urban Area
Satellite view of the metropolitan area of Turin, showcasing the urban landscape captured in high resolution. Below is the visualized risk map of the city.

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/05_age_distribution_dashboard.png?raw=true" width="1200"/></p>

## Risk Map
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Risk.png?raw=true" width="1500"/></p>

## Conclusions


## Open Science


## Contributors
Authors, contibutors, reviewers