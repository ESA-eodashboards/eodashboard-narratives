---
cover-image: https://github.com/phkh1366/eoxhub-related/blob/main/Phil_cover_alos2_hv_composite.png?raw=true
date: 2026-10-06
theme: Environment
tags: Forest Monitoring,Deforestation,ALOS-2,L-band Radar
official: true
collections: collectionIdentifier1, collectionIdentifier2
---

# Through Cloud and Canopy: Tracking Forest Clearing in Mindanao with L-band Radar <!--{ as="img" mode="hero" src="https://github.com/phkh1366/eoxhub-related/blob/main/Phil_cover_alos2_hv_composite.png?raw=true" }-->

### Authors: Romer Kristi D. Aranas<sup>1</sup>; Pocholo Miguel De Lara<sup>2</sup>; Elmar Sobrevega<sup>3</sup>; Mariel Juanillo<sup>1</sup>; Karina Amit<sup>4</sup><!--{ style="font-size:2.0rem;opacity:0.7;margin-top:1rem; color:Yellow" }-->

<div style="text-align:left; font-size:1.5rem; opacity:0.85; margin-top:1rem; color:Yellow;">
1. Philippine Space Agency (PhilSA)  
2. Department of Science and Technology Advanced Science and Technology Institute (DOST-ASTI)  
3. Department of Environment and Natural Resources Forest Management Bureau (DENR-FMB)  
4. University of the Philippines – Diliman (UPD)  
</div>

## Introduction
This story is based on results from the **[ALOS-2 Ideathon: Bridging Space Data and Societal Need in Feb. 2025](https://philsa.gov.ph/news/philsa-jaxa-host-alos-2-ideathon-workshop-to-tackle-environmental-social-challenges/)**, organized by the Japan Aerospace Exploration Agency (JAXA), Philippine Space Agency (PhilSA), Keio University, Remote Sensing Technology Center of Japan (RESTEC), and University of the Philippines Department of Geodetic Engineering (UP-DGE). 
<p align="center">
  <img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/2d25ca89ebc5fd3f1dbf204779815d5946de4496/Jaxa_logo.svg" height="50" style="margin: 0 0px;"/>
  <img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/70e744b7293ec8103be20b1c8cde68caf8508c48/Philippine_Space_Agency_(PhilSA).svg" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/Keio_University_Logo.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/RESTEClogo-trans.png?raw=true" height="80" style="margin: 0 0px;"/>
  <img src="https://upload.wikimedia.org/wikipedia/en/3/3d/University_of_The_Philippines_seal.svg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original" height="70" style="margin: 0 0px;"/>
</p>

The study, dedicated to assessimg **Forest Clearing in Mindanao with L-band Radar** developed by participants from the following organizations:
<p align="center">
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/logos_strip.png?raw=true" height="50" style="margin: 0 0px;"/>
</p>


## Challenge <!--{ style="font-size:2.00rem;opacity:1;margin-top:1rem; color:Navy" }-->

### Background <!--{ style="font-size:1.30rem;opacity:1;margin-top:1rem; color:black" }-->

On the forested slopes of Davao de Oro, in southern Mindanao, the forest seldom disappears all at once. A trail is cut, a camp goes up, a plot is cleared for farming or small-scale gold mining, and then another. The province lost about 43,000 ha of tree cover between 2001 and 2023 (Global Forest Watch, 2024), and two of its towns, Laak and Nabunturan, are listed as illegal-logging hotspots in the Philippine Forestry Statistics (Lopez, 2024). The slopes are steep and mined for gold: on 6 February 2024, a landslide buried part of the gold-mining village of Masara, in Maco, killing nearly 100 people (Fabro, 2024).

Davao de Oro is part of a national story. The Philippines lost about 1.42 million hectares of tree cover between 2001 and 2022, roughly 7.6% of its 2000 extent, releasing on the order of 848 million tonnes of CO₂ (Global Forest Watch, 2024). The country also reports its forest emissions under the UNFCCC, through its forest reference level for REDD+ (UNFCCC, 2022). Rangers, local governments and national reporting all need timely maps of where and when the forest is cut. This story brings together the Philippine Space Agency (PhilSA) and the national forest agency (DENR-FMB) to ask what JAXA's L-band radar can add to those maps.

### Problem Statement <!--{ style="font-size:1.30rem;opacity:1;margin-top:1rem; color:black" }-->

Only satellites can watch every hectare of a frontier like this, but each one sees the forest differently:

- **Optical satellites** (NASA/USGS Landsat, ESA Sentinel-2) take sharp pictures, but only of the canopy top, and only on cloud-free days. Clouds can hide a slope for months.
- **C-band radar** (ESA Sentinel-1) sees through cloud, but its 5.6 cm waves bounce mostly off leaves and twigs.
- **L-band radar** (JAXA ALOS-2) uses 24 cm waves that pass through cloud and foliage and bounce off trunks and large branches. It senses the structure of the forest.

Each feeds a ready-made forest-loss product: the Landsat-based Hansen map, the RADD alerts from Sentinel-1, and the JICA–JAXA JJ-FAST alerts from ALOS-2 (Watanabe et al., 2021). They were built for different jobs, so we look at how they complement each other, not to rank them.

Two ALOS-2 measurements matter here: 
- HV (horizontal send, vertical receive) comes mostly from volume scattering among branches in the crown, so it drops when trees are removed. 
- HH also carries the bounce from the ground and between trunks and the ground, so it drops less, and the HH/HV ratio rises. 

We give changes in decibels (dB): a change of 1 dB is about a 26% change in the energy that returns to the satellite.
If L-band senses structure, it might see a clearing, or even the first cuts under the canopy, before the other satellites do. That would make it an early warning. We tested this idea with one question: When forest is cleared in Davao de Oro, when does each satellite detect it, and what does L-band add?

## Objectives <!--{ style="font-size:2.00rem;opacity:1;margin-top:1rem; color:Navy" }-->

##### Main Objective

Find out when JAXA's ALOS-2 L-band radar detects forest clearing in Davao de Oro, compared with Landsat, Sentinel-1 and Sentinel-2, and what it adds.

##### Specific Objectives

- Follow individual clearings in detail, and find the order in which each satellite and product (including JJ-FAST) detected them.
- Measure how often ALOS-2 detects a clearing, next to how often it makes false detections in undisturbed forest.
- Map L-band forest change across the province, and compare it with the Landsat and Sentinel-1 records.

## Case Study <!--{ as="eox-map" mode="tour" }-->

### ### <!--{ layers='[{"type":"Tile","properties":{"id":"s2-cloudless-2025","title":"Sentinel-2 Cloudless 2025"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2025_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"labels","title":"Labels"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' center=[126.02,7.55] zoom="10" animationOptions="{duration:500}" }-->
##### Davao de Oro 
The study area is the province of Davao de Oro. It covers forested mountains, the small-scale gold-mining frontier around Mt. Diwata (Diwalwal) and Maco, and farmland in the valleys.

With no field records, we let two independent satellite systems choose the clearings. A clearing in this story is a place where both the RADD alerts and the Hansen map recorded forest loss, within one year and 30 m of each other. From these we drew 40 clearings of 0.5–10 ha (2019–2024) at random. Next to each one we placed two control areas: nearby forest of the same size where no product ever recorded a change. To test JJ-FAST fairly, we also took 76 clearings that JJ-FAST chose itself.
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/fig1_study_area.png?raw=true" style="max-width: 100%; width: 1000px; height: auto;" />
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"><b>Figure [1].</b> Study area: Davao de Oro province over the ALOS-2 HV change composite, with the 40 clearings chosen by RADD and Landsat, the 76 chosen by JJ-FAST, the 230 control areas and the four case-study clearings.</p>
</div>

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/DavaoDeOro/ALOS_PALSAR_YEARLY_DavaoDeOro_2019.tif"}]},"properties":{"id":"palsar2-yearly-davaodeoro;:;2019-01-01T00:00:00Z;:;2","title":"palsar2-yearly-davaodeoro_HH_intro"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],["case",["==",1,1],8000,4000]],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="11.211742480403021" center=[126.21647159939053,7.633697812162609] projection="" animationOptions={duration:500}}-->
#### About PALSAR-2
PALSAR-2, aboard JAXA's ALOS-2 satellite, is an L-band Synthetic Aperture Radar (SAR). It emits its own microwave signal and measures the reflection, so it can image the ground day or night and through cloud cover. Its long wavelength (about 24 cm) also penetrates vegetation further than shorter-wavelength radars, interacting with branches and trunks rather than only the top of the canopy.
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFC1CWV3wr_iYKFg1lq5pQgwHX_crcJ0XK2KpncluZJQ&s" style="max-width: 100%; width: 450px; height: auto;" alt="ALOS-2 Satellite" /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure 2.</b> Advanced Land Observing Satellite-2 "DAICHI-2" (ALOS-2). Image: JAXA. </p> 
</div>
This story focuses on Davao de Oro, Mindanao, known as Compostela Valley until it was renamed by plebiscite in December 2019. The province sits in the Davao Region, bordered by Davao del Norte to the west, Agusan del Sur to the north, Davao Oriental to the east, and the Davao Gulf to the southwest.

Shown here is the *HH (co-polarized) channel*. At L-band, HH backscatter is dominated by surface scattering and by "double-bounce" reflections between the ground and tree trunks. It is therefore strongly influenced by surface roughness, soil moisture and terrain, as well as by forest structure. The steps that follow show both the *HH* and the *HV (cross-polarized) channel* for three selected years (2019, 2020 and 2024), using JAXA's annual 25 m PALSAR-2 mosaics over Davao de Oro. HV backscatter is driven by volume scattering within the canopy and responds more strongly to forest structure and biomass, which makes it the primary channel for forest monitoring. A localized, persistent decrease in HV relative to an earlier year is a candidate sign of forest loss or degradation. Because radar sees through cloud, such changes can be tracked in a region where frequent cloud cover often hides the ground from optical satellites.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/DavaoDeOro/ALOS_PALSAR_YEARLY_DavaoDeOro_2019.tif"}]},"properties":{"id":"palsar2-yearly-davaodeoro;:;2019-01-01T00:00:00Z;:;0","title":"palsar2-yearly-davaodeoro_DavaoDeOro_2019_HH"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],["case",["==",1,1],8000,4000]],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="11.211742480403021" center=[126.21647159939053,7.633697812162609] projection="" animationOptions={duration:500}}-->
#### Establishing a Baseline (2019, HH)
Davao de Oro is a mountainous province with a mosaic of tropical forest, smallholder farms, plantations and gold-mining areas; the province's name refers to its gold deposits. This 2019 composite is the reference point of the record. It is not untouched forest, but the state of the landscape at the start of the series, against which later years are compared. Note the strong bright and dark patterns along the mountain ridges: much of this comes from topography (slopes facing toward or away from the radar), not from differences in land cover.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/DavaoDeOro/ALOS_PALSAR_YEARLY_DavaoDeOro_2019.tif"}]},"properties":{"id":"palsar2-yearly-davaodeoro;:;2019-01-01T00:00:00Z;:;1","title":"palsar2-yearly-davaodeoro_DavaoDeOro_2019_HV"},"style":{"variables":{"band":2},"color":["case",[">",["band",2],0],["interpolate",["linear"],["/",["band",2],["case",["==",2,1],8000,4000]],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="11.211742480403021" center=[126.21647159939053,7.633697812162609] projection="" animationOptions={duration:500}}-->
#### Baseline Canopy Structure (2019, HV)
The same year, now in the HV channel. Forest generally appears brighter here than cleared or cultivated land, because tree canopies produce strong volume scattering. This view is the baseline for the change-detection approach. One limitation is worth keeping in mind: in dense tropical forest the L-band HV signal saturates.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/DavaoDeOro/ALOS_PALSAR_YEARLY_DavaoDeOro_2020.tif"}]},"properties":{"id":"palsar2-yearly-davaodeoro;:;2020-01-01T00:00:00Z;:;0","title":"palsar2-yearly-davaodeoro_DavaoDeOro_2020_HH"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],["case",["==",1,1],8000,4000]],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="11.211742480403021" center=[126.21647159939053,7.633697812162609] projection="" animationOptions={duration:500}}-->
#### One Year On (2020, HH)
Moving forward one year. Comparing this view with 2019 shows how much of the landscape stays stable from year to year, which is what allows localized changes to stand out. Not every difference means a change on the ground. Annual composites are built from acquisitions on different dates, so variations in soil and vegetation moisture can shift backscatter. A difference between two years is therefore a candidate to investigate, not a confirmed disturbance.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/DavaoDeOro/ALOS_PALSAR_YEARLY_DavaoDeOro_2020.tif"}]},"properties":{"id":"palsar2-yearly-davaodeoro;:;2020-01-01T00:00:00Z;:;1","title":"palsar2-yearly-davaodeoro_DavaoDeOro_2020_HV"},"style":{"variables":{"band":2},"color":["case",[">",["band",2],0],["interpolate",["linear"],["/",["band",2],["case",["==",2,1],8000,4000]],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="11.211742480403021" center=[126.21647159939053,7.633697812162609] projection="" animationOptions={duration:500}}-->
#### Canopy Structure, One Year On (2020, HV)
The 2020 HV composite. This is the comparison the change-detection approach is built on. A localized drop in HV backscatter relative to the 2019 baseline, which persists in later years and cannot be explained by terrain or moisture, flags an area where the forest may have been cleared or degraded. 

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/DavaoDeOro/ALOS_PALSAR_YEARLY_DavaoDeOro_2024.tif"}]},"properties":{"id":"palsar2-yearly-davaodeoro;:;2024-01-01T00:00:00Z;:;0","title":"palsar2-yearly-davaodeoro_DavaoDeOro_2024_HH"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],["case",["==",1,1],8000,4000]],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="11.211742480403021" center=[126.21647159939053,7.633697812162609] projection="" animationOptions={duration:500}}-->
#### Five Years Later (2024, HH)
The most recent composite in the series, five years after the baseline, shown first in HH. Clearing does not always darken HH. Freshly felled trunks and debris lying on the ground can create strong double-bounce reflections and temporarily increase HH backscatter, while bare soil, roads and mining pits usually appear darker or brighter depending on their roughness and moisture. 

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/DavaoDeOro/ALOS_PALSAR_YEARLY_DavaoDeOro_2024.tif"}]},"properties":{"id":"palsar2-yearly-davaodeoro;:;2024-01-01T00:00:00Z;:;1","title":"palsar2-yearly-davaodeoro_DavaoDeOro_2024_HV"},"style":{"variables":{"band":2},"color":["case",[">",["band",2],0],["interpolate",["linear"],["/",["band",2],["case",["==",2,1],8000,4000]],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="11.211742480403021" center=[126.21647159939053,7.633697812162609] projection="" animationOptions={duration:500}}-->
#### Canopy Structure, Five Years Later (2024, HV)
The 2024 HV composite, the key comparison against the 2019 baseline. Forest cleared between 2019 and 2024 should appear as areas that are clearly darker here than in the baseline, since the canopy that produced the volume scattering is gone. Regrowth or new tree plantations can partly restore the HV signal over time, so older clearings may look less pronounced than recent ones. 

## Methodology Workflow & Data

#### Data Used

| Dataset | Agency / provider | Resolution | Period | Use in this story |
| --- | --- | --- | --- | --- |
| ALOS-2 PALSAR-2 ScanSAR Level 2.2 (HH, HV) | JAXA | 25 m, every ~42 days | 2014–present | L-band time series at each clearing and control area |
| ALOS-2 PALSAR-2 yearly mosaics (HH, HV) | JAXA | 25 m, yearly | 2015–2024 | L-band change across the province |
| JJ-FAST deforestation alerts | JICA–JAXA, from ALOS-2 ScanSAR | alerts of ~2 ha and more, every ~42 days | Sep 2018–Mar 2024 | The operational L-band alert |
| Global Forest Change v1.11 / v1.12 (Hansen et al.) | Univ. of Maryland, from NASA/USGS Landsat | 30 m, yearly | 2001–2023 / 2001–2024 | Forest in 2000; Landsat loss year |
| RADD forest-disturbance alerts | Wageningen University, from ESA Copernicus Sentinel-1 | 10 m, weekly | 2020–present | Date of the first C-band alert |
| Sentinel-2 L1C with Cloud Score+ | ESA Copernicus; Google | 10 m, every ~5 days | 2016–2024 | Sentinel-2 date of each clearing |
| AW3D30 digital surface model v3.2 | JAXA | 30 m | static | Removing slopes steeper than 30° |

### Methodology
We worked at two scales, in three steps (Figure 3), with Google Earth Engine and Python.

1. **Date each clearing.** We followed the greenness (NDVI) of each clearing compared with the forest around it. The clearing happened between the last cloud-free Sentinel-2 image that still showed forest and the first that showed it cleared. We call that first cleared image the Sentinel-2 date. We also recorded the first RADD alert, the Landsat loss year and any JJ-FAST alert.
2. **Test ALOS-2 at each clearing and its control areas.** We followed the L-band signal in every ALOS-2 ScanSAR image since 2014. Each clearing has its own normal level, learned from a three-year period that ends a year before it was cut. We tested single images, and six-month averages that a second average three months later must confirm. The same test ran on the control areas, so any detection there is a false detection.
3. **Map the whole province.** In the yearly ALOS-2 mosaics, we compared every forest pixel with the forest around it, and marked pixels whose signal changed by more than three times the normal year-to-year variation, two years in a row. We compared them with Landsat, RADD and control forest.

All detection rules were fixed before we looked at the control results. The technical appendix gives full details.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/Phi_fig2_workflow.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;" />
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"><b>Figure [3].</b> Workflow.</p>
</div>

## Results

### Key Findings

Clearing S31 is a 3-hectare opening near Mt. Diwata (126.124°E, 7.896°N), among small farms and dirt roads. All four satellites saw it, but not at the same time (Figure 4).

- **Sentinel-2** saw forest on 14 January 2020 and a clearing on 27 January.
- **RADD (Sentinel-1)** alerted on 18 January, inside that window.
- **Landsat** recorded the loss in 2020.
- **ALOS-2** detected it in a single image on 11 May 2020, and the six-month test confirmed it on 7 October 2020: about four and nine months after the others.

By the end of 2020, crops, grass or regrowth had made the clearing look almost as green as the forest to Sentinel-2. ALOS-2 saw something different. In late 2021, HV was still about 1 dB below the clearing's normal level and HH/HV about 1 dB above it, while the control areas stayed flat. The ground looked green again, but the forest structure had not come back. L-band was not first here, but it kept a record of the lost forest structure long after the ground turned green.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/Phil_fig3_S31_case.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;" />
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"><b>Figure [4].</b> Clearing S31: (A) Sentinel-2 greenness, (B) ALOS-2 HV and (C) HH/HV, each as clearing minus surrounding forest, with the Landsat loss year, RADD alert, Sentinel-2 date and ALOS-2 detections. Grey lines: the two control areas.</p>
</div>

S31 is only one pattern. Figure 5 puts four clearings on one time line.

- **S04 (1.0 ha, 2020): too small for L-band.** RADD alerted on 5 June 2020, six weeks before Sentinel-2 dated the clearing (17–22 July). ALOS-2 stayed within its normal variation. At 25 m, one hectare is only a handful of radar pixels: a job for 10 m sensors.
- **S09 (0.8 ha, 2021): no satellite is always first.** Cloud hid the slope from 23 April to 22 July 2021, yet Sentinel-2 still saw the clearing first. The ALOS-2 six-month test detected it on 22 September, 11 days before RADD's alert on 3 October. The signal here is noisy, so we treat that detection with caution.
- **S39 (7.3 ha, 2023): only the average sees it.** RADD alerted on 15 March 2023, before Sentinel-2 dated the clearing (24 March–18 April). Single ALOS-2 images showed only scattered dips, but the HH/HV ratio rose by about 1.4 dB and stayed high. The six-month test detected it on 4 October 2023, about six months after clearing. Averaging brings out even a large clearing, at the cost of time.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/Phil_fig4_case_timeline.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;" />
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"><b>Figure [5].</b> When each satellite first detected the four case-study clearings.</p>
</div>

Across all 40 clearings, each tested next to two control areas (80 in total):

- **RADD is usually first.** It alerted a median of 29 days before the Sentinel-2 date. Sentinel-2 dated 35 of the 40 clearings, and Landsat agreed on the year for 27 of those 35.
- **ALOS-2 is slower, but finds most clearings.** The six-month test detected 29 of 40 clearings (72%), a median of 255 days after RADD. It also made false detections at 10 of 80 control areas (12%). Single images found only 3.
- **Early detections are rare.** At three clearings, ALOS-2 came before both RADD and Sentinel-2. That is about as many as the false-detection rate would produce by chance.
- **The L-band change lasts.** Lined up on the day Sentinel-2 last saw forest (Figure 5), clearings look like undisturbed forest before the cut. Afterwards, HV drops by about 0.5–1 dB and HH/HV rises by about 0.5–0.9 dB, and both stay changed for at least two years. Meanwhile, 33 of 35 clearings looked green again to Sentinel-2 after a median of 110 days.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/Phil_fig5_lband_signal.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;" />
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"><b>Figure [6].</b> The L-band signal around the time of clearing: median and spread for 34 dated clearings (pink) and 68 control areas (grey). Day 0 is the last Sentinel-2 image that showed forest.</p>
</div>

JJ-FAST (JICA–JAXA Forest Early Warning System in the Tropics) is the operational ALOS-2 alert. Between September 2018 and March 2024, it raised 129 alerts in Davao de Oro (439 ha in total). None of them touched our 40 clearings, but most of those clearings are smaller than JJ-FAST is built for. Its published algorithm targets clearings of about 2 ha and more (Watanabe et al., 2021); here, 96 of its 129 alerts are 2 ha or larger and only one is under 1 ha. Just 15 of our 40 clearings are 2 ha or more, and one of those was cleared after March 2024. So the fair test is 14 clearings, and JJ-FAST alerted at none of them. That fits its design: pan-tropical, with conservative thresholds that keep false alerts low. JAXA's own validation in the Brazilian Amazon found that it captured about 45% of deforestation, with about 64% of its alerts correct (JICA & JAXA, 2023).

So we turned the roles around and let JJ-FAST choose 76 clearings. In the table, Sentinel-2 confirms a clearing when its greenness stays low for at least 60 days, not just a short dip that may be cloud shadow; the ground can turn green again later.

|  | 40 clearings chosen by RADD + Landsat | 76 clearings chosen by JJ-FAST |
| --- | --- | --- |
| Sentinel-2 confirms the clearing | 27 / 40 | 11 / 76 |
| Landsat records loss / RADD alerts | chose them | 17 / 76 and 5 / 76 |
| JJ-FAST alerts | 0 / 40 (0 / 14 of 2 ha or more, in its period) | chose them |
| ALOS-2 six-month test detects | 29 / 40 | 21 / 29 with a date from another satellite |
| False detections in control areas (JJ-FAST; six-month test) | 0 / 80; 10 / 80 | 0 / 150; 7 / 150 |

- **JJ-FAST is quiet in undisturbed forest.** It raised no alert at any of the 230 control areas.
- **Many of its alerts have no optical match.** Across the province, 65 JJ-FAST alerts lie in forest where neither Landsat nor RADD recorded loss. They may be degradation under the canopy that optical sensors cannot see, clearings too small for Landsat, or false alerts. We have not yet checked them.
- **When Sentinel-2 confirms the clearing, JJ-FAST is close behind:** a median of 41 days after the Sentinel-2 date, at those 11 clearings.

The yearly ALOS-2 mosaics tell the same story at a coarser scale (Figure 6):

- **A real signal, at a low false-detection rate.** ALOS-2 marked 7.7% of the forest that Landsat mapped as lost in 2017–2023 but only 0.5% of control forest. A lost pixel is about 15 times more likely to be marked than undisturbed forest.
- **Bigger clearings are easier to see:** 5.3% of the loss in areas under 0.5 ha, and 9.6% in areas over 2 ha.
- **Rarely first.** ALOS-2 marked 45% of this loss in the same year as Landsat, 41% later and 13% earlier.
- **Most of what it marks is unconfirmed.** Against about 1,000 ha of Landsat-mapped loss, ALOS-2 also marked about 4,500 ha that neither Landsat nor RADD recorded. The false-detection rate explains about 1,300 ha of that. The rest lies near forest edges, steep slopes and known clearings: possible degradation, or noise that needs checking.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/Phil_fig6_hv_change_composite.png?raw=true" style="max-width: 100%; width: 1000px; height: auto;" />
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"><b>Figure [7].</b> ALOS-2 HV change composite (red = 2015, green = 2020, blue = 2024). Grey: stable forest; red and magenta: L-band loss after 2015; blue: gain by 2024 (plantations, regrowth). The yellow strip on the eastern edge has no 2024 coverage.</p>
</div>

With one ALOS-2 image every six weeks and clearings of a hectare or two, L-band radar is not the earliest warning in Davao de Oro. Its value is different: its signal still shows the lost forest structure after the ground looks green again to optical satellites.

Each mission has its own job:

- **Sentinel-1 / RADD:** the fastest alert through cloud.
- **Sentinel-2:** dates a clearing within weeks, whenever the sky clears.
- **Landsat:** the long, year-by-year record of forest loss.
- **JJ-FAST (ALOS-2):** an operational L-band alert, almost silent in undisturbed forest, whose unconfirmed alerts point to where L-band may add the most.
- **ALOS-2, read as six-month averages:** a cloud-proof confirmation that the forest structure is gone, which lasts after the ground turns green again.

This agrees with work elsewhere in the tropics: combined radar and optical alerts beat any single system (Reiche et al., 2024; Balling et al., 2024), and L-band senses early clearing where C-band does not (Flores-Anderson et al., 2026).

Since November 2022, JAXA has released ALOS-2 ScanSAR data free of charge (JAXA, 2022). That is what made this study possible for a national team. The same open data, code and design, with clearings and control areas tested side by side, can be applied to other cloudy, forested provinces in Southeast Asia and the wider Asia-Pacific.

### What we cannot claim yet

- that ALOS-2 warns earlier: early detections were rare, and no more frequent than chance;
- reliable detection of clearings under about 1 ha;
- that the L-band-only change, or JJ-FAST's unconfirmed alerts, are real degradation, until someone checks them on the ground or in imagery.

## Limitations

- **Clearings chosen by other satellites.** RADD and Landsat chose the 40 clearings. This is a fair test of timing but it favors clearings that optical and C-band sensors detect well, and it cannot show what L-band detects but others miss.
- **No field records.** All reference dates come from satellites. At 7 of the 40 clearings, Sentinel-2 dated a change more than a year after RADD, probably a later event at the same place.
- **Small and steep clearings.** At 25 m, ALOS-2 resolves clearings of about 1 ha and more. Slopes over 30° were removed, so some steep mining slopes are not assessed.

## Future Work

- **Check what only L-band sees.** For more robust results, it would be good to look at the 65 unconfirmed JJ-FAST alerts, and identified L-band-only areas, using high-resolution imagery and using field validation.
- **Test on documented encroachment sites with field records.** This research focused on sites identified using satellites on documented forest encroachment areas. Using field records would provide ground validation and also provide information on whether the actual encroachment cases could have been detected using L-band or other remote sensing imagery earlier.
- **Build on ALOS-4 and NISAR.** JAXA's ALOS-4 has a much wider swath and coupled with NISAR, would open the way to an L-band layer which could complement the CopPhil forest monitoring service.
- **Work with the JJ-FAST team.** Explore how JJ-FAST's low false-alert design and the averaging approach could work together for small clearings in Southeast Asia.

## Acknowledgment

We thank the Japan Aerospace Exploration Agency (JAXA) for ALOS-2 PALSAR-2 data. PhilSA, UP Department of Geodetic Engineering, Keio University, and RESTEC for  organizing the ALOS-2 Ideathon. JICA and JAXA for making the JJ-FAST alerts openly available. We also thank ESA and the Copernicus programme (Sentinel-1, Sentinel-2), NASA and USGS (Landsat), the University of Maryland (Global Forest Change) and Wageningen University (RADD alerts) for making this possible.

## References

- Balling, J., Slagter, B., van der Woude, S., Herold, M., & Reiche, J. (2024). ALOS-2 PALSAR-2 ScanSAR and Sentinel-1 data for timely tropical forest disturbance mapping: A case study for Sumatra, Indonesia. International Journal of Applied Earth Observation and Geoinformation, 132, 103994. https://doi.org/10.1016/j.jag.2024.103994
- European Space Agency. (n.d.). Copernicus Sentinel-1 and Sentinel-2 [Satellite imagery]. Copernicus Data Space Ecosystem. https://dataspace.copernicus.eu
- Fabro, K. A. (2024, February 21). Landslide in Philippines mining town kills nearly 100, prompts calls for action. Mongabay. https://news.mongabay.com/2024/02/landslide-in-philippines-mining-town-kills-nearly-100-prompts-calls-for-action/
- Flores-Anderson, A. I., Cardille, J. A., Kellndorfer, J., Meyer, F. J., & Olofsson, P. (2026). On the sensitivity of SAR C- and L-band dual-polarized data for detection of early deforestation in the tropics. Remote Sensing of Environment, 333, 115133. https://doi.org/10.1016/j.rse.2025.115133
- Global Forest Watch. (2024). Philippines and Davao de Oro: Tree cover loss [Data set]. World Resources Institute. https://www.globalforestwatch.org
- Hansen, M. C., Potapov, P. V., Moore, R., Hancher, M., Turubanova, S. A., Tyukavina, A., Thau, D., Stehman, S. V., Goetz, S. J., Loveland, T. R., Kommareddy, A., Egorov, A., Chini, L., Justice, C. O., & Townshend, J. R. G. (2013). High-resolution global maps of 21st-century forest cover change. Science, 342(6160), 850–853. https://doi.org/10.1126/science.1244693
- Japan Aerospace Exploration Agency. (2022). ALOS-2 PALSAR-2 ScanSAR products (Level 2.2), public release of 7 November 2022. Earth Observation Research Center. https://www.eorc.jaxa.jp/ALOS/en/dataset/palsar2_l22_e.htm
- Japan Aerospace Exploration Agency. (n.d.). ALOS-2 PALSAR-2 ScanSAR Level 2.2 and Global PALSAR-2/PALSAR yearly mosaic [Data sets]. Earth Observation Research Center. https://www.eorc.jaxa.jp/ALOS/en/
- Japan Aerospace Exploration Agency. (n.d.). ALOS World 3D – 30 m (AW3D30) version 3.2 [Data set]. Earth Observation Research Center.
- JICA & JAXA. (2023). JJ-FAST Technical Note, version 9.1. Earth Observation Research Center, JAXA. https://www.eorc.jaxa.jp/jjfast/support/JJ-FAST_Technical_Note_v9_20230711.pdf
- JICA & JAXA. (n.d.). JJ-FAST: JICA-JAXA Forest Early Warning System in the Tropics [Data set]. Earth Observation Research Center, JAXA. https://www.eorc.jaxa.jp/jjfast/
- Lopez, R. F. (2024, May 11). Seven things data tell us about the deforestation and devastating floods in Davao Region. PressOne.PH. https://pressone.ph/seven-things-data-tell-us-about-the-deforestation-and-devastating-floods-in-davao-region/
- OCHA & PSA-NAMRIA. (n.d.). Philippines subnational administrative boundaries (COD-AB, v03) [Data set]. Humanitarian Data Exchange. https://data.humdata.org/dataset/cod-ab-phl
- Reiche, J., Balling, J., Pickens, A. H., Masolele, R. N., Berger, A., Weisse, M. J., Mannarino, D., Gou, Y., Slagter, B., Donchyts, G., & Carter, S. (2024). Integrating satellite-based forest disturbance alerts improves detection timeliness and confidence. Environmental Research Letters, 19(5), 054011. https://doi.org/10.1088/1748-9326/ad2d82
- Reiche, J., Mullissa, A., Slagter, B., Gou, Y., Tsendbazar, N.-E., Odongo-Braun, C., Vollrath, A., Weisse, M. J., Stolle, F., Pickens, A., Donchyts, G., Clinton, N., Gorelick, N., & Herold, M. (2021). Forest disturbance alerts for the Congo Basin using Sentinel-1. Environmental Research Letters, 16(2), 024005.
- United Nations Framework Convention on Climate Change. (2022). Philippine forest reference level.
- U.S. Geological Survey. (n.d.). Landsat 8–9 OLI/TIRS [Satellite imagery]. Earth Resources Observation and Science Center. https://www.usgs.gov/landsat-missions
- Watanabe, M., Koyama, C. N., Hayashi, M., Nagatani, I., Tadono, T., & Shimada, M. (2021). Refined algorithm for forest early warning system with ALOS-2/PALSAR-2 ScanSAR data in tropical forest regions. Remote Sensing of Environment, 265, 112643. https://doi.org/10.1016/j.rse.2021.112643

---

## Production Notes from the Original Word Template

> If you want to have a related background photo, behind your title page, please copy and paste the image here.

### Example of the title page

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
<img src="assets/title_page_example.jpg" style="max-width: 100%; width: 1200px; height: auto;" />
</div>

### Submission checklist

- ☐ Story text (this document)
- ☐ Study area map
- ☐ Workflow diagram
- ☐ At least 3 result figures
- ☐ Logos of participating organizations
- ☐ Dataset links
- ☐ References
- ☐ Preferred cover image

**Share folder:**  
https://drive.google.com/drive/folders/1beG5mR7IgxairBRyPZn1Idyss2BoxlKZ?usp=sharing

<!-- Before publishing:
1. Confirm the organizer replacing XXXXXXXXXXX.
2. Replace the temporary cover with the preferred cover image if desired.
3. Replace local assets/... paths with the final hosted/public image URLs required by the EO Dashboard deployment.
-->
