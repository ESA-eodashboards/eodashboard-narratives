# Heat Risk Mapping - Turin case study <!--{ as="img" mode="hero" src="https://media.istockphoto.com/id/636399938/it/foto/paesaggio-urbano-di-torino-allalba.jpg?s=612x612&w=0&k=20&c=yemCm6bo7EFGa_CcPZfKIZ5lNfNY7e3tjfi-xITU0hU=" }-->
#### 

### Authors: Francesco Mezza¹, Sona Guliyeva², Filippos Kostikiadis³, and Sophia Dolla³ <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
> ¹ Polytechnic University of Milan 
² Polytechnic University of Turin  
³ Aristotle University of Thessaloniki

## <!--{ nav="false" }-->
<div align="center">

*This story is based on results from the Science Hub Challenge organised and hosted by ESA's ESRIN Science Hub in September 2026. The scope of the challenge was to develop a framework to identify urban areas that are potentially most vulnerable to heat exposure during heatwave events combining Earth Observation data with geospatial information. The method was implemented on the AVL platform by a team of a PhD candidate and Master students from the Polytechnic University of Milan, the Polytechnic University of Turin and Aristotle University of Thessaloniki. The data and code are made openly available.*
</div>

## 
<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRykXzo6XdIiDH7WzjEsW9AwJ6HNyaLZ0fDqJoJExBiZOHf7FN_rZqcggo&s=10" alt="ESA Logo" height="120" style="margin: 0 15px;"/>
  <img src="https://lanuovacopisteria.it/wp-content/uploads/2026/01/politecnico-di-torino-polito.jpg" alt="Politecnico di Torino" height="120" style="margin: 0 15px;"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/89/Aristotle_University_of_Thessaloniki_logo.svg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original" alt="Aristotle University of Thessaloniki" height="120" style="margin: 0 15px;"/>
</p>

## Challenge
**Heat exposure** refers to the presence of people, ecosystems, infrastructure or other assets in areas affected by **excessive heat**. It is influenced by temperature, humidity, wind, solar radiation and local geographical and **urban characteristics**. In urban areas, factors such as **building materials**, land cover, **vegetation** and the **urban heat island (UHI)** effect can create substantial spatial differences in heat exposure.

**Vulnerability** describes the **susceptibility** of individuals or populations to adverse effects from heat. It is influenced by **physiological**, **demographic**, social and **socioeconomic factors**, as well as housing conditions and access to cooling, healthcare and other essential services. Certain groups, such as **older adults**, **children** and **outdoor workers**, may be particularly susceptible to heat-related impacts.

Torino's geographic setting in the **Po Valley basin** creates a physical microclimate prone to **atmospheric stagnation**, weak ventilation, and pollutant entrapment. Enclosed by the Alpine arc to the west and north, the basin acts as a **thermal trap** during persistent heat domes. In the **summer of 2026**, as an African anticyclone pushed temperatures across Italy past **40°C**, Turin's eight districts did not all suffer equally. A resident of a **low-density** neighborhood and a resident of a paved, **high-density** one lived through the same heatwave in very different modalities.

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Torino%20sentinel.png?raw=true" width="400"/></p>
<p align="center" style="font-size: 0.85em; color: #666;"><em> Optical Satellite Image over the Area of Turin.</em></p>

This study delivers a **spatialized framework** for mapping **urban heat exposure** and **social vulnerability** across Torino's administrative districts (circoscrizioni), linking **satellite observations** with climate analysis and demographic vulnerability.

## Objective
 The primary objectives of this challenge are to:
1. **Select one heatwave** events over a turin
2. **Retrieve Sentinel-3 LST observations** and air temperature during a heatwave and reference (non-heatwave) periods
3. **Compute LST**
4. **Derive spatial indicators** describing the urban environment (e.g. vegetation cover, impervious surfaces, built-up density)
5. **Define a heat exposure index**, combining both thermal intensity and exposure indicators, and identify/rank the most exposed urban districts.

### Overall aim
As extreme heat becomes a climate threat to European cities, we can **no longer rely on simple weather forecasts** to protect our most vulnerable citizens. That’s why we performed a **dynamic, EO-based Thermal Risk Analysis** for Turin.
According to the climate risk framework, **risk results from the interaction between hazard, exposure and vulnerability**. Thus, a heatwave represents the **hazard**, while **heat exposure and vulnerability** determine how strongly individuals and populations may be affected.


## Use case
Our index proves that heat vulnerability isn't just about the weather—it's a structural crisis driven by concrete and aging populations. This tool empowers city planners to pinpoint exact 'thermal traps', transforming broad climate goals into targeted, life-saving, actions exactly where they are needed most.


## Data and methods

#### Dataset
The used datasets were:
| Category | Link | Description |
|:-:|:-:|:-:|
| 🛰️ **Satellite Imagery / EO** | [Sentinel-3 SLSTR L2 LST](https://sentiwiki.copernicus.eu/web/s3-slstr-products) | Daily (nighttime-pass) Land Surface Temperature, 1–15 Aug 2026 — the core heat-hazard layer of the index. *(Copernicus / ESA)* |
| | Sentinel-2 MSI L2A (`COPERNICUS/S2_SR_HARMONIZED`) | Cloud-masked median composite used for NDVI/NDBI. *(Copernicus, via [Google Earth Engine](https://earthengine.google.com/))* |
| 🌍 **Land Cover & Climate** | [Imperviousness HRL 2024](https://land.copernicus.eu/en/products/high-resolution-layer-imperviousness) | Soil sealing %, one of the 4 index components. *(Copernicus Land Monitoring Service)* |
| | [ThermalTrace](https://thermaltrace.climate.copernicus.eu/) | ERA5 / UTCI daily temperature, used to select the heatwave window. *(Copernicus C3S / ECMWF)* |
| 📍 **Geospatial & Vector Data** | [Geoportale Piemonte](https://igr.piemonte.it/) | District boundaries, urban green areas, population by age and district. *(Città di Torino open geodata CC BY 4.0)* |
| | [OpenStreetMap](https://osmnx.readthedocs.io)| Hospitals, schools, elderly-care facility locations. *(OSM contributors, via Overpass API)* |
| 💻 **Platforms / Tools** | [EO Dashboard](https://eodashboard.org/explore/?x=7.6869&y=45.0703&z=10.0000&datetime=2026-08-13&template=expert) | Base layers and visualization tools for interactive exploration. *(EO Dashboard Consortium: ESA, NASA, JAXA)* |



#### Methodology workflow
The team's methodology included the following steps and expected outcomes:

**1. Data Retrieval & Anomaly Mapping**

- Selecting a time series over Turin between August 1-15, 2026
- Retrieving Sentinel-3 Land Surface Temperature (LST) observations for the period to understand the temperature pattern


**2. Deriving Spatial Indicators**

- Using additional datasets (such as green cover by Comune di Torino and Copernicus High Resolution Layer Imperviousness) to describe the urban environment through indicators like vegetation cover, impervious surfaces, and built-up density.

**3. Heat Risk Index** 

- Defining an index that combines thermal intensity with exposure indicators to map and rank the most exposed urban districts.
- Hazard, exposure, and vulnerability are the key drivers of physical climate risk.
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/climate-change_v2.jpg?raw=true" width="1000"/></p>

## Results

The final risk index, scaled between 0 and 1, is calculated as the average of four normalized key factors: surface heat, age vulnerability, lack of greenery, and soil sealing.
This climate risk represents the combination of three fundamental elements: the physical climate event or trend (Hazard), the elements present in hazard-prone areas (Exposure), and the resilience or lack thereof of the exposed elements to the hazard (Vulnerability).

- **Surface heat (nightly Sentinel-3 LST)**: The 15-panel grid illustrates how nighttime temperatures fluctuate geographically. The maps reveal severe localized urban heat islands; while some areas effectively cool down overnight (shown in dark purple/black), specific districts consistently trap and retain high heat (glowing orange and yellow), preventing nighttime thermal relief.

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Nighttime%20LST%20Evolution%20-%20Turin%20Districts%20.png?raw=true" width="500"/></p>

- **Age vulnerability (percentage of population over 65)**: The demographic data demonstrate aging populations, showing a stark volume of residents in the red "65 and Older" category across all areas. The spatial vulnerability map pinpoints the exact risk concentration: District 2 is the most highly exposed with 28.6% of its population over 65, followed by District 8 (27.3%) and District 3 (26.8%), while District 6 remains relatively less vulnerable at 23.2%.

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Vulnerability%20Map%20%20Over%2065%20by%20District%20(Turin).png?raw=true" width="400"/></p>

- **Lack of greenery (inverse of green cover per district)**: The urban green areas map exposes a geographical divide in natural cooling infrastructure. While the eastern edge and specific peripheral zones feature dense, contiguous vegetation, the central and western urban core suffers from highly fragmented and sparse green coverage, directly indicating areas that will score high for "lack of greenery".

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Urban%20green%20areas.png?raw=true" width="400"/></p>

- **Imperviousness (soil sealing)**: The  imperviousness map reveals a  geographic divide in Torino's soil sealing. Central and western districts (like District 1, District 3, District 4, and District 5) feature near 100% impenetrable artificial surfaces (shown in black), acting as a massive thermal battery that elevates urban heat exposure. Conversely, the eastern periphery (District 7 and  District 8) remains highly permeable and unpaved (shown in white).
 
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/Torino%20-%20Imperviousness%202024.png?raw=true" width="400"/></p>


## Analysis <!--{ as="eox-map" mode="tour" position="right" }-->

### <!--{ zoom=11 center=[7.6869,45.0703] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}},{"type":"Tile","properties":{"id":"heat-index-overlay"},"url":"https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/06_heat_exposure_index_map.png?raw=true"}]' animationOptions='{"duration":500}' }-->
#### Turin Overview
An overview of the city of Turin, showcasing the urban landscape and surrounding geography.

### <!--{ zoom=14 center=[7.68,45.07] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Historical Center
Focusing on the highly dense historical center where heat trapping is most prominent.

### <!--{ zoom=13 center=[7.63,45.04] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Industrial South-West
Examining the industrial belt which experiences significant soil sealing.

### <!--{ zoom=13 center=[7.71,45.05] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### Borgo Po Green Buffer
The green hills providing a natural cooling buffer effect for the city.

### <!--{ zoom=13 center=[7.68,45.1] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Northern Districts
Areas with lower heat vulnerability due to younger population demographics.

### <!--{ zoom=13 center=[7.68,45.1] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Heat Risk Index
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/06_heat_exposure_index_map.png?raw=true" width="1400"/></p>

Although socio-demographic data remains constant, temperatures (LST) change daily, continuously altering the level and distribution of risk across neighbourhoods. Consequently, emergency planners cannot rely on a single static risk map, as the most vulnerable areas shift over time.

### <!--{ animationOptions='{"duration":500}' }-->
#### Daily Risk Ranking
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/07_daily_vulnerability_ranking%20(1).png?raw=true" width="1000"/></p>

<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/percentages.png?raw=true" width="1000"/></p>

As shown in the graphs, Surface Heat (LST) contributes only a small fraction (5.9% to 8.7%) to the total risk index. The vast majority of the vulnerability is instead driven by stable factors like Age and Lack of Greenery.

### <!--{ animationOptions='{"duration":500}' }-->
#### Critical Facilities
<p align="center"><img src="https://github.com/FrancescoMezza/torino-heat-exposure/blob/main/09_critical_facilities_map.png?raw=true" width="1000"/></p>

The image maps critical facilities (hospitals, schools, and elderly care facilities) across Turin's districts based on their risk score. It highlights that the most vulnerable central and western districts, shown in dark red, contain a dense concentration of these sensitive locations.

## Conclusions
Turin's heat vulnerability is structurally dictated by urban morphology and demographics, not daily weather. The historical center and south-western industrial belt form extreme-risk zones due to severe soil sealing, lack of vegetation, and aging populations.

Conversely, Borgo Po's vast forested hills demonstrate a green buffer effect that drastically lowers thermal risk. Meanwhile, northern districts show lower vulnerability simply because their younger populations are statistically less heat-sensitive. 

Ultimately, the city's most impermeable, concrete-dense environments perfectly align with its oldest demographics, creating persistent thermal traps.

In conclusion, while socio-demographic variables remain static, daily fluctuations in Land Surface Temperature (LST) continuously alter the spatial distribution and relative ranking of risk across neighbourhoods. This dynamic has critical implications for contingency planning: it highlights the inadequacy of relying on a single, static risk map. Because neighborhood vulnerability shifts over time, effective emergency management requires dynamic, day-to-day assessment tools rather than fixed spatial representations.

To mitigate urban heat, the city must prioritize de-paving wide avenues and planting shade trees to reduce surface temperatures. In the dense historical center, micro-interventions like green roofs and highly reflective materials are essential to cool narrow streets.

To protect the aging population, the city should establish accessible cooling centers and implement early warning systems. Additionally, deploying mobile health units and strengthening neighborhood networks will ensure isolated elderly residents stay safe during extreme heatwaves.

## Open Science

## <!--{ nav="false"}--> References
### Earth Observation data
* Sentinel-3 SLSTR Level-2 LST — Copernicus / ESA
* Sentinel-2 MSI Level-2A (COPERNICUS/S2_SR_HARMONIZED) — Copernicus, via Google Earth Engine
* Imperviousness High Resolution Layer 2024 — Copernicus Land Monitoring Service

### Meteorological context
* ThermalTrace — daily air / UTCI feels-like temperature, ERA5, Copernicus C3S / ECMWF
* Beretta, S. “Meteo oggi 4 agosto: bollino rosso in 25 città su 27, punte di 41°C”, Quotidiano Motori, 4 Aug 2026 — nationwide red-alert heatwave, corroborating the analysis window

### Geospatial Information (Città di Torino, via Geoportale Piemonte)
* District boundaries (circoscrizioni) and urban green areas — Comune di Torino open geodata, e.g. Geoportale Piemonte catalog record (CC BY 4.0)
* Population by age and district (“B1 Pop per età annuale e circoscrizione 2025”) — Comune di Torino open data
* https://dutchclimaterisk.nl/climate-risk/risk-assessment-guidance/
* https://heat.gov/who-is-most-at-risk-to-extreme-heat/at-risk-older-adults/
* https://www.sciencedirect.com/science/article/pii/S2212096325000452

### Points of interest
* OpenStreetMap contributors — hospitals, schools, elderly-care facilities, queried via Overpass API / osmnx

## <!--{ nav="false"}--> Contributors
- Francesco Mezza — Coding and data processing
- Sona Guliyeva — Project lead and supervision
- Sophia Dolla — Theoretical framework
- Filippos Kostikiadis — Theoretical framework