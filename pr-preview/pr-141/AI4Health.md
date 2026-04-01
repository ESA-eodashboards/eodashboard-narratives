---
cover-image: https://www.gmv.com/sites/default/files/styles/image_1000/public/content/image/2025/01/30/114/np_004_air4health.jpeg?itok=mtOfRfxA
date: 2025-01-01
theme: atmosphere
tags: air-quality,urban-health,machine-learning,digital-twins,climate-adaptation,heatwaves
official: false
---

# AIR4health: Earth Observation and AI towards Urban Climate and Air Quality Services for Human Health <!--{ as="img" mode="hero" src="https://www.gmv.com/sites/default/files/styles/image_1000/public/content/image/2025/01/30/114/np_004_air4health.jpeg?itok=mtOfRfxA" }-->
### A Digital Twin Solution for Compound Climate and Air Quality Monitoring and Forecasting <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## <!--{ nav="false" }-->
<div align="center">
	



*AIR4health is an [European Space Agency (ESA)](https://www.esa.int)-funded project under the ESA Digital Twin Earth Components programme, developed by [CoLAB +ATLANTIC](https://www.colabatlantic.com/), [GMV](https://www.gmv.com/), and the [Faculdade de Medicina de Lisboa](https://www.medicina.ulisboa.pt/).*
	
<img src="https://eof.esa.int/wp-content/uploads/2025/03/AIR4health-1024x606.png" alt="Faculdade de Medicina de Lisboa" height="80" style="margin: 0 15px;"/>

</div>

## <!--{ nav="false" }-->
<p align="center">
  <img src="https://eurogoos.eu/api/media/file/colab.png" alt="CoLAB +ATLANTIC" height="80" style="margin: 0 15px;"/>
  <img src="https://www.gmv.com/sites/default/files/content/image/2021/11/03/115/gmv_rgbredblack.png" alt="GMV" height="80" style="margin: 0 15px;"/>
  <img src="https://cdn.prod.website-files.com/652d692b07725fb22536129d/66b365b6316cd1b4aaaf471a_FMUL%20(1).png" alt="Faculdade de Medicina de Lisboa" height="80" style="margin: 0 15px;"/>
</p>

## Why AIR4health? The Local Nature of Climate Hazards

Climate and environmental hazards are **local**. Extreme heat, poor air quality, and compound events such as heatwaves combined with elevated ozone concentrations affect people differently depending on where they live, their neighbourhood, the street they walk on, the building they live in. Yet current weather forecasts and climate projections are good at telling us **when** an event will happen, but not **where** it will be most severe or **why** certain areas are disproportionately affected.

This gap between global forecasts and local reality has critical consequences. Between 8% and 16% of the EU population faces energy poverty, making them particularly vulnerable to both cold waves and heatwaves. Europe is warming faster than any other continent, and the most vulnerable groups, the elderly, children, and the energy poor, bear the brunt of climate impacts while being most overlooked in adaptation planning. At the same time, over half of deaths attributed to ground-level ozone in Europe are due to ozone originating outside the region, underscoring the need for fine-scale, local monitoring tools.

**AIR4health** addresses this challenge by developing domain-informed, data-driven Machine Learning (ML) models that downscale air quality and climate variables to the **1 km² grid level** across the Iberian Peninsula, detailed enough to resolve contrasts between neighbourhoods, fast enough to run in near-real-time, and scalable to other urban regions across Europe.

## The AIR4health Approach

The AIR4health framework fuses three complementary streams of information through machine learning:

**Observations** combine in-situ air quality and meteorological sensor data from approximately 680 stations across the Iberian Peninsula (sourced from EEA, NOAA, and WMO networks) with **Copernicus Sentinel-5P** satellite data providing 2 daily revisits with homogeneous spatial coverage, and CAMS Reanalysis atmospheric composition fields.

**Synoptic background conditions** are provided by **CAMS Reanalysis** (and CAMS Forecasts for near-real-time applications), capturing the large-scale atmospheric state driving pollution episodes and temperature extremes.

**Local time-fixed predictors** capture the landscape and urban features that modulate how regional conditions translate into neighbourhood-level impacts: topography and topographic wind exposure, vegetation density and phenology, urban density and imperviousness, sky view factor, and proximity to traffic lanes by road typology, all derived from Copernicus Land Monitoring Service (CLMS), OpenStreetMap, and the Copernicus Digital Elevation Model.

The result is a system that can answer not just **what** is happening and **when**, but critically **where**, providing the spatial specificity needed for targeted early warning, emergency response, and urban planning.

## Study Area: The Iberian Peninsula <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="6" center=[-4.5,39.5] projection="" animationOptions={duration:500}}-->
#### The Iberian Peninsula: AIR4health Area of Interest
The AIR4health model covers the full **mainland Iberian Peninsula**, encompassing 89,102 km² of mainland Portugal and 493,514 km² of mainland Spain: a total of **582,616 grid cells of 1 km²**. The domain spans a wide range of climatic zones, urban morphologies, and landscape types, from coastal Atlantic cities to inland semi-arid plateaus, making it an ideal testbed for a scalable, transferable approach.


### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="10" center=[-9.1393,38.7223] projection="" animationOptions={duration:500}}-->
#### Lisbon Metropolitan Area
**Lisbon** is the primary Portuguese study site and early adopter city. The metropolitan area's complex mix of coastal exposure, dense urban fabric, steep topography, and the moderating influence of the Tagus estuary creates strong neighbourhood-level contrasts in temperature and air quality, exactly the type of spatial heterogeneity the AIR4health downscaling model is designed to resolve at 1 km² resolution.

<center>
<img src="https://www.airculinaireworldwide.com/wp-content/uploads/2017/07/lisbon-portugal.jpg" width="400">
<span style="font-size:15px;">Lisbon, Portugal (Credit: Bigstock)</span>
</center>

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="10" center=[-3.7038,40.4168] projection="" animationOptions={duration:500}}-->
#### Madrid, Spain
**Madrid** sits on a high inland plateau at approximately 650 m elevation, with a continental climate characterised by hot, dry summers and cold winters. The city is a key hotspot for compound heatwave and ozone (HW+O3) events, with the surrounding road network, visible in the AIR4health road distance and road length density layers, driving strong spatial gradients in NO2 concentrations across urban, suburban, and rural areas.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg" width="400">
<span style="font-size:15px;">Madrid, Spain (Credit: Felipe Gabaldón)</span>
</center>

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="10" center=[-8.6291,41.1579] projection="" animationOptions={duration:500}}-->
#### Porto, Portugal
**Porto** and its metropolitan area represent the Atlantic coastal urban typology, milder summers but a dense urban fabric with significant industrial and traffic-related NO2 sources. Porto is part of the in-situ station network used to train and validate the AIR4health models, contributing to the ~680 stations across the Iberian Peninsula.

<center>
<img src="https://images.pexels.com/photos/27832057/pexels-photo-27832057.jpeg" width="400">
<span style="font-size:15px;">Aerial view of Porto, Portugal (Credit: Matej Simko)</span>
</center>

## Results

#### Use Case I: Compound Cold Wave and NO2 Events

Cold waves (CW) and elevated NO2 concentrations form a dangerous compound hazard for human health. During cold periods, atmospheric boundary layer height decreases, trapping pollutants near the surface. At the same time, domestic heating increases emissions, and the combination of cold stress and respiratory irritation from NO2 disproportionately affects vulnerable populations.



## Map Tour Example <!--{ as="eox-map" mode="tour" }--><!--{ nav="false" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;a3c40d64-5cbb-4439-9cf0-92cb3d67004d;:;Air Quality (tropospheric NO2 concetrations);:;EPSG:3857","title":"Air Quality (tropospheric NO2 concetrations)"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:3857","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2025-11-03T00:00:00Z/2025-11-03T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="6.88467092929458" center=[-7.554735387930261,39.513908165128726] projection="" animationOptions={duration:500}}-->
#### Results in the Iberian Peninsula during 2013-2023
The AIR4health model was applied across the full Iberian Peninsula for the period 2013–2023, demonstrating a critical limitation of the CAMS reanalysis: while CAMS correctly represents the large-scale NO2 field at 10 km resolution, it **systematically underestimates peak values** at urban and suburban stations, particularly in cities. Over the full validation period, CAMS detected only 9.5% of EU Directive exceedances (daily average exceeding 50 μg/m³), compared to 20.8% in in-situ measurements. The AIR4health downscaling model, incorporating Sentinel-5P data and local urban predictors, recovered 20.3% of exceedances, nearly matching ground truth and revealing the **urban hotspots** that coarse reanalysis misses.

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;eb648935-bc59-4640-b3fc-6271f2cc529d;:;Air Quality (tropospheric NO2 concetrations);:;EPSG:3857","title":"Air Quality (tropospheric NO2 concetrations)"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:3857","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2025-10-06T00:00:00Z/2025-10-06T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="8.682262003990788" center=[-9.674270284275172,38.740116045942955] projection="" animationOptions={duration:500}}-->
#### Case in point: January 2017 Compound CW+NO2 Event
A cold wave affecting mainland Portugal ran from 19 to 25 January 2017, seven consecutive days, with a maximum cold wave intensity of -8.5°C² and a maximum NO2 exceedance of 11.9 μg/m³. The downscaled AIR4health outputs captured the spatial distribution of this compound event at municipality level, enabling identification of the most exposed areas days in advance.

<center>
<img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/stories/AI4Health/Usecase1.png" width="400">
<span style="font-size:15px;">January 2017 Compound CW+NO2Event</span>
</center>




#### Use Case II: Compound Heatwave and Ozone Events

Heatwaves and elevated surface ozone (O3) form the other critical compound hazard addressed by AIR4health. High temperatures accelerate ozone formation from precursor pollutants, while ozone itself exacerbates heat stress on the respiratory and cardiovascular systems. Rural and suburban areas are particularly vulnerable to ozone exceedances, as ozone is consumed by urban NO2: the so-called NO2-to-O3 urban sink effect, meaning CAMS systematically **underestimates rural ozone** while overestimating it in cities.

## Map Tour Example <!--{ as="eox-map" mode="tour" }--><!--{ nav="false" }-->
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Total Column O₃ by Sentinel-5P TROPOMI (Daily);:;41942fe6-a55c-4b9a-a3ea-ca20ca89d174;:;Total Column O₃ by Sentinel-5P TROPOMI (Daily);:;EPSG:3857","title":"Total Column O₃ by Sentinel-5P TROPOMI (Daily)"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["S5P-L3GRD-TCO3-DAY"],"TILED":true,"TIME":"2025-03-01T00:00:00Z/2025-03-01T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="5.966518338621313" center=[-8.958578881412667,39.48857303692151] projection="" animationOptions={duration:500}}-->
#### Exceedances for ozone
Over 2013–2023, CAMS detected 11.95% of WHO Guideline exceedances for ozone (daily max 8-hour average exceeding 100 μg/m³), compared to 16.45% in ground truth. The AIR4health downscaling model improved this to 13.36%, better capturing the spatial pattern of rural exceedances revealed by Sentinel-5P observations.

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Sentinel-3-SLSTR-L2-LST;:;2023-08-14T00:00:00Z;:;Land Surface Temperature (Sentinel-3 SLSTR L2);:;EPSG:3857","title":"Land Surface Temperature (Sentinel-3 SLSTR L2)"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-3-SLSTR-L2-LST"],"TILED":true,"TIME":"2023-08-14T00:00:00Z/2023-08-14T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="6.094108784553673" center=[-8.237169446174358,39.52085969461095] projection="" animationOptions={duration:500}}-->
#### Case in point: July 2013 Compound HW+O3 Event
This extreme event ran from 5 to 10 July 2013, six consecutive days, with a maximum heatwave intensity of 49.0°C² and a maximum ozone exceedance of 40.7 μg/m³. The health consequences were severe: approximately **1,700 cumulative excess deaths** and **10,000 cumulative excess hospital admissions** above the baseline summer rate of ~300 deaths per day.

<center>
<img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/stories/AI4Health/Usecase2.png" width="400">
<span style="font-size:15px;">: July 2013 Compound HW+O3 Event</span>
</center>


Spatial analysis of the AIR4health outputs showed that all-cause mortality increased by a factor of 1.102 per unit of Excess Heat Factor and 1.042 per unit of excess ozone: demonstrating the compound amplification of health risk when both hazards co-occur.

## From Data to Decision

The AIR4health outputs are delivered through an **Integrated Seasonal Surveillance System**, a web and mobile platform developed in partnership with Portuguese health authorities (SNS, DGS, IPMA, Instituto Nacional de Saúde) that translates the downscaled model outputs into actionable health risk information for three groups of users:

<center>
<img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/stories/AI4Health/ai4healthsystem.png" width="800">
<span style="font-size:15px;">: AI4Health Surveillance System</span>
</center>



- **Residents** can check their geolocated risk level and receive personalised health advice, which they can share with family members.

- **Health duty officers** can monitor vulnerable neighbourhoods in near-real-time, track the evolution of compound risk indices, and report situation reports to management.

- **Municipal planners** can overlay compound risk maps with cool spaces and green infrastructure layers, and send targeted SMS alerts to at-risk populations.

The system displays a **Compound Risk Index** combining the Excess Heat Factor and ozone exceedances, with forecasts disaggregated by age group, directly addressing the needs identified in user consultation workshops. 

## Next Steps

AIR4health has confirmed both user requirements and user willingness to join the operational system. The next phase will focus on designing a full **Integrated Seasonal Surveillance System Software Development Roadmap**, expanding the training data to a multi-year time series, and testing scalability to other European urban regions. The system is also designed for **evolution with upcoming satellite missions**, particularly Sentinel-4, which will provide higher temporal resolution atmospheric composition data to further improve the near-real-time downscaling capabilities.

## Open Science

All datasets referenced in this story are freely and openly available.

| Name | Type | Agency / Provider | Description | Access/Source |
|---|---|---|---|---|
| [Copernicus Sentinel-5P TROPOMI: NO2](https://dataspace.copernicus.eu/browser/?collection=SENTINEL-5P) | Dataset | ESA / Copernicus | Tropospheric NO2 column density; 2 daily revisits over the Iberian Peninsula; used as key observation input to the AIR4health NO2 downscaling model and to identify urban hotspots missed by CAMS | [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/browser/?collection=SENTINEL-5P) |
| [Copernicus Sentinel-5P TROPOMI: O3](https://dataspace.copernicus.eu/browser/?collection=SENTINEL-5P) | Dataset | ESA / Copernicus | Tropospheric ozone column; used to improve spatial representation of the NO2-to-O3 urban sink effect in the HW+O3 downscaling use case | [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/browser/?collection=SENTINEL-5P) |
| [CAMS Reanalysis (CAMSRA)](https://ads.atmosphere.copernicus.eu/) | Dataset | ECMWF / Copernicus | Atmospheric composition reanalysis at 10 km resolution; provides synoptic background conditions (NO2, O3, air temperature) used as coarse-resolution input to the ML downscaling model | [Copernicus Atmosphere Data Store](https://ads.atmosphere.copernicus.eu/) |
| [Copernicus Land Monitoring Service: Tree Cover Density (TCD)](https://land.copernicus.eu/pan-european/high-resolution-layers/forests/tree-cover-density) | Dataset | EEA / Copernicus | Percentage tree cover used as green infrastructure predictor in the local features layer | [Copernicus Land Service](https://land.copernicus.eu/) |
| [Copernicus Land Monitoring Service: Imperviousness (IMD)](https://land.copernicus.eu/pan-european/high-resolution-layers/imperviousness) | Dataset | EEA / Copernicus | Degree of soil sealing used as urban density predictor | [Copernicus Land Service](https://land.copernicus.eu/) |
| [Copernicus Land Monitoring Service: Corine Land Cover (CLC)](https://land.copernicus.eu/pan-european/corine-land-cover) | Dataset | EEA / Copernicus | Land cover classification used to stratify the weighted sampling approach for model training | [Copernicus Land Service](https://land.copernicus.eu/) |
| [Copernicus DEM: Digital Elevation Model](https://spacedata.copernicus.eu/collections/copernicus-digital-elevation-model) | Dataset | ESA / Copernicus | Terrain elevation and derived Topographic Position Index (TPI) used to represent topographic wind exposure effects on local temperature and air quality | [Copernicus Data Space](https://spacedata.copernicus.eu/) |
| [EEA Air Quality e-Reporting (AQ E1a)](https://www.eea.europa.eu/data-and-maps/data/aqereporting-9) | Dataset | European Environment Agency | Verified hourly in-situ air quality measurements from ~680 stations across the Iberian Peninsula; used as ground truth response variable for model training and validation | [EEA Data Portal](https://www.eea.europa.eu/data-and-maps/data/aqereporting-9) |
| [WMO OSCAR/Surface Station Network](https://oscar.wmo.int/surface/) | Dataset | World Meteorological Organization | Meteorological in-situ observations complementing EEA stations for model training | [OSCAR/Surface](https://oscar.wmo.int/surface/) |
| [OpenStreetMap: Road Network](https://www.openstreetmap.org/) | Dataset | OpenStreetMap contributors | Road length density and road distance by typology (motorway, primary, secondary, tertiary, trunk) used as human activity predictors in the ML model | [openstreetmap.org](https://www.openstreetmap.org/) |
| [EOxCloudless Sentinel-2 Mosaic 2024](https://s2maps.eu/) | Dataset | EOX / ESA | Cloud-free Sentinel-2 basemap used for visualisation of the Iberian Peninsula study area | [s2maps.eu](https://s2maps.eu/) |