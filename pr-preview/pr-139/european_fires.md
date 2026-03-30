---
cover-image: https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/8-wildfires.jpg
date: 2025-01-01
theme: atmosphere
tags: wildfires,forests,co,carbon-monoxide
official: true
collections: N1_CO
---

# Evaluating Fire Impact on Populated Areas in Europe <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/8-wildfires.jpg" }-->
### How the 2022 Gironde wildfire affected urban areas near Bordeaux, France <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## <!--{ nav="false" }-->
<div align="center">

*This trilateral story, produced in collaboration by the [European Space Agency (ESA)](https://www.esa.int), the [National Aeronautics and Space Administration (NASA)](https://www.nasa.gov/), and the [Japan Aerospace Exploration Agency (JAXA)](https://global.jaxa.jp/), is part of the joint narratives featured on [EO Dashboard](https://eodashboard.org/), showcasing the power of open Earth observation data.*

</div>

## <!--{ nav="false" }-->
<p align="center">
  <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/logos/esa.jpg" alt="ESA" height="80" style="margin: 0 15px;"/>
  <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/logos/nasa.jpeg" alt="NASA" height="80" style="margin: 0 15px;"/>
  <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/logos/jaxa.jpeg" alt="JAXA" height="80" style="margin: 0 15px;"/>
</p>

## Wildfire Impacts and Carbon Emissions

The wildfire season during the summer of 2022 in Europe was exceptional, marked by a high number of observed fires, a large extent of burned area, and remarkably high atmospheric emissions linked to these fires. According to data from the [European Forest Fire Information System (EFFIS)](https://effis.jrc.ec.europa.eu/), fires were reported in 26 out of the 27 European countries, collectively burning 837,212 hectares. A significant portion of these wildfires happened in July, with Spain, Portugal, France, and Italy experiencing the most damages.

The selected wildfire incident for this analysis occurred in the **Gironde region** of southwestern France, near the city of Bordeaux, in 2022. The significant fire event started on **July 17, 2022**, lasted for two weeks while burning approximately 7,000 hectares of land. Notably, the [Copernicus Atmosphere Monitoring Service (CAMS)](https://atmosphere.copernicus.eu/) recorded exceptionally elevated levels of carbon monoxide emissions throughout the duration of this event.

## Satellite Data for Wildfire Analysis

Earth observation satellites provide a powerful toolset to monitor wildfire events, assess their extent, and measure their impact on air quality in nearby populated areas. This analysis combines three complementary data sources:


##  Satellite observations<!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"osm","title":"Background"},"source":{"type":"OSM"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Gironde;:;2022-07-17T00:00:00Z;:;Sentinel2_TrueColor;:;EPSG:3857","title":"Sentinel-2 True Color"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-2-L2A-TRUE-COLOR"],"TILED":true,"TIME":"2022-07-17T00:00:00Z/2022-07-17T23:59:59Z"}},"visible":true}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="11.5" center=[-0.706357,44.452587] projection="" animationOptions={duration:500}}-->
#### Copernicus Sentinel-2
**Sentinel-2** optical imagery is used to visualize the fire event and map the burned area at 10–20 metre resolution. The true colour image captured on July 17, 2022, the day the fire started, clearly showing the fire plume extending westward from the Gironde forest toward the urban areas near Bordeaux.
<center>
<img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2012/02/sentinel-2/9658480-3-eng-GB/Sentinel-2_pillars.jpg" width="400">

<span style="font-size:15px;">Copernicus Sentinel-2 </span>
</center>
S2 data across 13 spectral bands, ranging from visible to shortwave infrared wavelengths. In the image, we are seeing a **true color composite**, since it uses the Red (Band 4), Green (Band 3), and Blue (Band 2) bands, similar to how the **human eye perceives color**. This allows us to view the landscape as it would appear in **real life**.

**Sentinel-2** optical imagery is used to visualize the fire event and map the burned area at 10–20 metre resolution. The true colour image captured on July 17, 2022, the day the fire started, clearly shows the fire plume extending westward from the Gironde forest toward the urban areas near Bordeaux.

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"GHS-BUILT-S-R2023A;:;098f4020-76ad-445e-9d4b-cf42150b3093;:;GHS-BUILT-S-R2023A;:;EPSG:3857","title":"GHS-BUILT-S-R2023A"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:3857","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["GHS_BUILT_S"],"TILED":true,"TIME":"2030-01-01T00:00:00Z/2030-01-01T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="11.5" center=[-0.706357,44.452587] projection="" animationOptions={duration:500}}-->
#### EC-JRC Global Human Settlement Layer (GHS-BUILT)
**The EC-JRC Global Human Settlement (GHS) Layer** provides global data on total built-up surface from 1975 to 2030, derived from Sentinel-2 composite and Landsat imagery. This layer is used to identify and isolate populated areas within the analysis zone, enabling a targeted assessment of where people were most exposed to the fire emissions.
The **GHS Built-Up Surface layer** shows the total built-up surface in the Gironde region near Bordeaux. This layer, derived from Sentinel-2 composite and Landsat imagery, is used to identify populated areas that may have been exposed to carbon monoxide emissions from the July 2022 wildfire.

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"osm","title":"Background"},"source":{"type":"OSM"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"CO_3_daily;:;2022-07-17T00:00:00Z;:;AWS_VIS_CO_3DAILY_DATA;:;EPSG:3857","title":"TROPOMI CO"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:3857","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_VIS_CO_3DAILY_DATA"],"TILED":true,"TIME":"2022-07-17T00:00:00Z/2022-07-19T23:59:59Z"}},"visible":true}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="11.5" center=[-0.706357,44.452587] projection="" animationOptions={duration:500}}-->
#### Copernicus Sentinel-5P TROPOMI — Carbon Monoxide, 17 July 2022
**Copernicus Sentinel-5P TROPOMI** carbon monoxide (CO) data is then queried specifically over those populated areas using the Sentinel Hub Statistical API. The resulting time series reveals a clear and sharp increase in CO concentration on July 17, 2022, coinciding precisely with the start of the fire, with elevated standard deviation values persisting in the following days — consistent with records showing that the highest carbon emissions in France in 2022 were recorded between June and August.
<center>
<img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2017/06/sentinel-5p/17040704-2-eng-GB/Sentinel-5P_pillars.jpg" width="400">

<span style="font-size:15px;">Copernicus Sentinel-5P carrying the TROPOMI instrument</span>
</center>
**TROPOMI CO** observations over the Gironde region on the day the fire started. The elevated carbon monoxide concentrations are clearly visible over and downwind of the fire area, extending westward toward the populated areas near Bordeaux.



## From Satellite to Impact Assessment

The analysis workflow links these three data sources in a coherent chain: Sentinel-2 imagery defines the geographic extent of the fire event; the GHS layer identifies which parts of that extent are populated; and Sentinel-5P CO data quantifies the atmospheric exposure of those populations during and after the fire. This integrated approach demonstrates how open Earth observation data — freely accessible through platforms such as the [Euro Data Cube (EDC)](https://eurodatacube.com/) and the [EO Dashboard](https://eodashboard.org/) — can be combined to produce actionable insights about the human and environmental impacts of extreme wildfire events.

As climate change drives more frequent and intense fire seasons across Europe and globally, workflows such as this one become increasingly important for early warning, emergency response, and post-event impact assessment.
 


## <!--{ as="div" }--> Open Science

All datasets referenced in this story are freely and openly available. Sentinel-2 and Sentinel-5P data are distributed without charge through the Copernicus Open Access Hub and Sentinel Hub. The GHS layer is openly available from the EC-JRC. No registration is required to access the EO Dashboard interactive maps.

| Name | Type | Agency / Provider | Description | Access/Source |
|---|---|---|---|---|
| [Sentinel-2 L2A (View on EO Dashboard)](https://eodashboard.org/explore?indicator=N1_CO&x=-0.706357&y=44.452587&z=11.5) | Dataset | ESA / Copernicus | Multispectral optical imagery at 10–20 m resolution; true colour composite (B4, B3, B2) used to visualize the Gironde wildfire extent and smoke plume on July 17, 2022 | [Copernicus Data Space Ecosystem](https://browser.dataspace.copernicus.eu/?zoom=5&lat=46.19504&lng=5.80078&themeId=DEFAULT-THEME&visualizationUrl=U2FsdGVkX1%2FRnh2w7l5k0kKUHgPZa%2BxlYzw4zIvweSw1oSyS5IRocKMwqhmDelzrOFfnzxBRm5dJ%2BynAs3v8%2FWEd%2Fb%2BH7KF8elSHCQ7luAl0aS%2FN%2Frcxa9lmK3yBr4%2Bk&datasetId=S5_CO_CDAS&fromTime=2026-03-30T00%3A00%3A00.000Z&toTime=2026-03-30T23%3A59%3A59.999Z&layerId=CO_VISUALIZED) |
| [GHS-BUILT-S R2023A (View on EO Dashboard)](https://eodashboard.org/explore/?x=-0.0004&y=0.0072&z=2.9432&template=expert&indicator=GHSBUILT&datetime=2030-01-01) | Dataset | European Commission / JRC | Global built-up surface grid derived from Sentinel-2 composite and Landsat; multitemporal 1975–2030; 10 m resolution; queried via Sentinel Hub Statistical API (BYOC ID: 0c7aa265-50f9-4947-9980-2ee5ae204803) to identify populated areas exposed to fire emissions near Bordeaux | [JRC Data Catalogue](https://data.jrc.ec.europa.eu/dataset/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea) |
| [Sentinel-5P TROPOMI CO (View on EO Dashboard)](https://eodashboard.org/explore?indicator=N1_CO) | Dataset | ESA / Copernicus | Daily atmospheric column CO concentrations derived from TROPOMI; 3-day composite; global coverage; used to measure the increase in CO over populated areas near Bordeaux from July 1 to August 9, 2022, revealing a sharp spike coinciding with the start of the fire on July 17 | [Copernicus Data Space Ecosystem](https://browser.dataspace.copernicus.eu/?zoom=5&lat=50.16282&lng=20.78613&themeId=DEFAULT-THEME&visualizationUrl=U2FsdGVkX18ap7R7%2FgJjBi%2Fih4bm1FV08yOYisxWyjEEbZQYQeT8l3GIxM%2F9leeC%2BvH0qTpn9rpF5IKWK74yZ4wct8zO9gXeCzp56QS%2FcXzK3nQg4D8grbyC7wpFmWss&datasetId=S5_CO_CDAS&fromTime=2026-03-30T00%3A00%3A00.000Z&toTime=2026-03-30T23%3A59%3A59.999Z&layerId=CO_VISUALIZED&demSource3D=%22MAPZEN%22&cloudCoverage=30&dateMode=SINGLE) |
| [Copernicus Atmosphere Monitoring Service (CAMS)](https://atmosphere.copernicus.eu/) | Service | ECMWF / Copernicus | Provides data and forecasts on atmospheric composition including wildfire CO emissions; referenced to confirm that the highest carbon emissions in France in 2022 were recorded between June and August | [atmosphere.copernicus.eu](https://atmosphere.copernicus.eu/) |
| [European Forest Fire Information System (EFFIS)](https://effis.jrc.ec.europa.eu/) | Platform | EC / JRC | Near-real-time monitoring of forest fires across Europe; source of the 2022 burned area statistics reporting 837,212 hectares across 26 out of 27 EU countries | [effis.jrc.ec.europa.eu](https://effis.jrc.ec.europa.eu/) |
| [EO Dashboard](https://eodashboard.org/explore) | Platform | ESA / NASA / JAXA | Trilateral open Earth observation dashboard providing interactive maps of TROPOMI trace gas datasets and other EO products | [eodashboard.org](https://eodashboard.org/explore) |


The following Notebook evaluates fire impact on populated areas on a European site.

<iframe width="95%" style="min-height: 70vh" src="https://esa-eodashboards.github.io/eodashboard-notebooks/notebooks/fire-impact-analysis" frameborder="0"></iframe>