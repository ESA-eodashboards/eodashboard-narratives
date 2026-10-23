---
cover-image: https://raw.githubusercontent.com/phkh1366/eoxhub-related/refs/heads/main/VTN-Cover2.JPG
date: 2026-08-01
theme: Economy
tags: Urbanization,Vietnam
official: false
collections: collectionIdentifier1, collectionIdentifier2
---

# Urbanization monitoring from EO data <!--{ as="img" mode="hero" src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN-Cover2.JPG?raw=true" }-->

#### Authors: Nguyen Manh HUNG¹, Dang Do Nam PHUONG¹, Tong Thi Huyen AI¹, Nguyen Huu CHUYEN² <!--{ style="font-size:1.0rem;opacity:0.7;margin-top:1rem; color:Yellow" }-->

<div style="text-align:left; font-size:0.95rem; opacity:0.85; margin-top:1rem; color:Yellow;">
¹ Vietnam National Space Center, Vietnam Academy of Science and Technology<br>
² Department of National Remote Sensing, Ministry of Agriculture and Environment
</div>

## <!--{ nav="false" }-->
#### Introduction
<!--{nav="false" style="font-size:2.00rem;opacity:1;margin-top:1rem; color:Navy" }-->
This story is based on results from **[ALOS-2 Ideathon: Bridging Space Data and Societal Needs](https://vnsc.org.vn/en/news-events/vietnam-national-space-center-vietnam-academy-of-science-and-technology-organizes-workshop-on-application-ideas-for-alos-2-and-sar-satellite-data-in-vietnam/)**, organised by JAXA, VNSC, Keio University and RESTEC.

<p align="center">
<img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/2d25ca89ebc5fd3f1dbf204779815d5946de4496/Jaxa_logo.svg" height="50" style="margin:0 0px;"/>
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/logo-VNSC-moi.png?raw=true" height="50" style="margin:0 0px;"/>
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/Keio_University_Logo.png?raw=true" height="50" style="margin:0 0px;"/>
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/RESTEClogo-trans.png?raw=true" height="80" style="margin:0 0px;"/>
</p>

The study, dedicated to **Urbanization monitoring from EO data**, was developed by participants from the following organizations:

<p align="center">
<img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/2d25ca89ebc5fd3f1dbf204779815d5946de4496/Jaxa_logo.svg" height="50" style="margin:0 0px;"/>
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/logo-VNSC-moi.png?raw=true" height="50" style="margin:0 0px;"/>
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTNlogo.png?raw=true" height="40" style="margin:0 0px;"/>
</p>

## Challenge <!--{ style="font-size:2.00rem;opacity:1;margin-top:1rem; color:Navy" }-->
### Rapid Urbanization and Sustainable Urban Development<!--{ style="font-size:1.50rem;opacity:1;margin-top:1rem; color:Navy" }-->
Rapid urbanization in Vietnam, particularly in Hanoi, is driving significant land use changes, loss of green spaces, increasing impervious surfaces, and environmental challenges such as the Urban Heat Island (UHI) effect. However, fragmented and outdated spatial data make it difficult to monitor urban expansion, especially in peri-urban areas, and assess its environmental impacts.

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN-Field.png?raw=true" style="max-width:100%;width:1200px;height:auto;" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [1].</b> Overview of Hanoi showing the extent of urbanized areas.</p>
</div>

The lack of a **systematic, continuous satellite-based monitoring system** limits evidence-based urban planning, sustainable land management, and progress toward the Sustainable Development Goals (SDGs). **Timely and reliable Earth Observation (EO) data are essential** to bridge this information gap and support informed decision-making for sustainable urban development.

## Objective <!--{ style="font-size:1.5rem;opacity:1;margin-top:1rem; color:Navy" }-->
**Primary Objective:**
To **monitor and quantify urbanization and land-cover changes in Hanoi using multi-temporal Earth Observation data from 2015 to 2025**. Accordingly the specific Objectives are: <!--{ style="font-size:1rem;opacity:1; margin-top:0px; margin-bottom:0px; color:blue" }-->
- **Objective 1**: Map land cover — Generate LULC maps for 2015, 2020, and 2025 using multi-source satellite data.
- **Objective 2**: Detect urban expansion — Identify where built-up areas expanded and how urban growth patterns changed over the 10-year period.
- **Objective 3**: Quantify urbanization — Measure changes using built-up area, Urbanization Ratio (UR), Impervious Surface Index (ISI), and Annual Growth Rate (AGR).
- **Objective 4**: Support urban planning — Provide spatial evidence for monitoring development and guiding sustainable urban planning.

The four objectives above define the main analytical and planning-oriented outputs of the study.

## Use case <!--{ as="eox-map" mode="tour" nav="false" style="width:50%;max-width:50%;background:transparent;background-color:transparent;color:#FFFFFF;" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"s2-cloudless-2025","title":"Sentinel-2 Cloudless 2025"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2025_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"labels","title":"Labels"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' center=[105.85,21.03] zoom="11" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:transparent;background-color:transparent;color:#FFFFFF;box-sizing:border-box;" }-->

#### Hanoi
Hanoi serves as the primary political, economic, and cultural hub of Vietnam, having experienced one of the nation's most accelerated urbanization rates throughout the last twenty years. Geographically situated within the Red River Delta, the city encompasses approximately 3,360 km², positioning it as one of the most expansive capital cities in Southeast Asia in terms of land area.

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN-fig1-AoI.jpg?raw=true" style="max-width:100%;width:1200px;height:auto;" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [2].</b> Study area</p>
</div>

Recent census data from 2024 indicates a population of nearly 8.7 million, Hanoi is one of Vietnam's largest cities by population. The city's urban footprint has been steadily pushing outward into suburban districts, including Gia Lam, Long Bien, Ha Dong, Hoang Mai, Soc Son, and Dong Anh. This rapid physical growth is driven by the extensive development of transportation networks, modern residential zones, and industrial clusters. Such profound modifications to land use and natural topography have placed considerable strain on local natural resources and the quality of the urban environment. Consequently, leveraging Earth Observation (EO) technologies for the systematic monitoring and quantification of Hanoi's urban sprawl has become a critical requirement for evidence-based sustainable planning and efficient territorial management.

### <!--{ center=[105.9618,21.0256] zoom="15" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:transparent;background-color:transparent;color:#FFFFFF;box-sizing:border-box;" }-->

#### Gia Lam
Gia Lam is located to the east of central Hanoi and represents one of the important suburban expansion areas. Urban growth in this district is associated with new residential development, transport connections, and conversion of agricultural land.

### <!--{ center=[105.91,21.03] zoom="15" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:transparent;background-color:transparent;color:#FFFFFF;box-sizing:border-box;" }-->

#### Long Bien
Long Bien lies northeast of Hanoi’s historical center, across the Red River. It has experienced strong urban development due to improved connectivity, commercial growth, and expansion of residential areas.

### <!--{ center=[105.78,20.97] zoom="15" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:transparent;background-color:transparent;color:#FFFFFF;box-sizing:border-box;" }-->

#### Ha Dong
Ha Dong is located southwest of central Hanoi and has become one of the city’s major urban expansion zones. Its growth reflects the development of modern residential areas, road infrastructure, and urban services.

### <!--{ center=[105.86,20.98] zoom="15" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:transparent;background-color:transparent;color:#FFFFFF;box-sizing:border-box;" }-->

#### Hoang Mai
Hoang Mai is situated in the southern part of Hanoi. The district has seen rapid transformation from peri-urban and mixed land-use areas into dense residential and transport-linked urban zones.

### <!--{ center=[105.85,21.25] zoom="14" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:transparent;background-color:transparent;color:#FFFFFF;box-sizing:border-box;" }-->

#### Soc Son
Soc Son is located in northern Hanoi and includes more rural and peri-urban landscapes. Urban pressure in this area is influenced by transport infrastructure, industrial activities, and proximity to Noi Bai International Airport.

### <!--{ center=[105.85,21.15] zoom="14" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:transparent;background-color:transparent;color:#FFFFFF;box-sizing:border-box;" }-->

#### Dong Anh
Dong Anh lies north of the Red River and is considered a strategic area for Hanoi’s future urban expansion. Development in this district is linked to infrastructure projects, residential growth, and industrial zones.

### <!--{ center=[105.85,21.08] zoom="11" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:transparent;background-color:transparent;color:#FFFFFF;box-sizing:border-box;" }-->

#### Urban growth pressure
This rapid physical growth is driven by the extensive development of transportation networks, modern residential zones, and industrial clusters. Such profound modifications to land use and natural topography have placed considerable strain on local natural resources and the quality of the urban environment.

## ALOS-2 ScanSAR L2.2 Timeseries <!--{ as="eox-map" mode="tour" nav="false" style="width:50%;max-width:50%;background:#333333;background-color:rgba(35,35,35,0.92);color:#FFFFFF;" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/Hanoi/ALOS_PALSAR_YEARLY_Hanoi_2015.tif"}]},"properties":{"id":"palsar2-yearly-hanoi;:;2015-01-01T00:00:00Z;:;0","title":"Hanoi_2015"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],8000],0,["color",8,32,76,1],0.18,["color",28,78,128,1],0.38,["color",73,132,180,1],0.58,["color",161,169,119,1],0.78,["color",230,135,44,1],0.92,["color",214,69,33,1],1,["color",255,245,200,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]' center=[105.85,21.03] zoom="11.5" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:#333333;background-color:rgba(35,35,35,0.92);color:#FFFFFF;box-sizing:border-box;" }-->

The **Advanced Land Observing Satellite-2 (ALOS-2)**, operated by the Japan Aerospace Exploration Agency (**JAXA**), is an Earth observation satellite equipped with the **Phased Array type L-band Synthetic Aperture Radar-2 (PALSAR-2)**. Unlike optical sensors, PALSAR-2 uses microwave radar signals, allowing observations **during both day and night and under cloudy conditions**.

Its **L-band SAR** is particularly useful for monitoring land-surface characteristics, vegetation structure, forests, agriculture, disasters, and changes in built-up areas. In this case study, ALOS-2 PALSAR-2 annual mosaic data are used to examine the spatial evolution of **Hanoi between 2015, 2020, and 2025**. By comparing the radar backscatter patterns across these years, changes in the extent and density of urban and peri-urban areas can be visually assessed.

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFC1CWV3wr_iYKFg1lq5pQgwHX_crcJ0XK2KpncluZJQ&s" style="max-width:100%;width:450px;height:auto;" alt="ALOS-2 Satellite" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [3].</b> Advanced Land Observing Satellite-2 "DAICHI-2" (ALOS-2)</p>
</div>

#### Hanoi (2015)
The starting point of the study: Hanoi's urban core stands out against surrounding farmland and water bodies. This 2015 view marks the beginning of a ten-year PALSAR-2 record over Hanoi, rendered here in the HH (co-polarized) channel of JAXA's annual yearly mosaic. This all-weather L-band record is what allows the study to track urban expansion continuously, without the seasonal cloud gaps that limit the optical datasets used elsewhere in this analysis.

Early outward growth begins along the main transport corridors leading out of the city center.

<div style="width:100%; box-sizing:border-box; margin:16px 0 0 0; padding:10px 12px; background:rgba(38,38,38,0.9); border-radius:6px; color:#FFFFFF; font-size:0.88rem;">
  <div style="font-weight:600; margin-bottom:7px; color:#FFFFFF;">ALOS-2 PALSAR-2 HH — Urban-feature visualization scale</div>
  <div style="height:14px; width:100%; border-radius:3px; background:linear-gradient(to right, rgb(8,32,76) 0%, rgb(28,78,128) 18%, rgb(73,132,180) 38%, rgb(161,169,119) 58%, rgb(230,135,44) 78%, rgb(214,69,33) 92%, rgb(255,245,200) 100%);"></div>
  <div style="display:flex; justify-content:space-between; margin-top:4px; color:#FFFFFF;">
    <span>0</span><span>2,000</span><span>4,000</span><span>6,000</span><span>8,000</span>
  </div>
  <div style="margin-top:7px; font-size:0.82rem; color:#FFFFFF;">Lower HH values appear in dark blue tones, while higher values appear in orange to light cream tones, helping urban and built-up features stand out more clearly.</div>
</div>


### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/Hanoi/ALOS_PALSAR_YEARLY_Hanoi_2020.tif"}]},"properties":{"id":"palsar2-yearly-hanoi;:;2020-01-01T00:00:00Z;:;0","title":"Hanoi_2020"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],8000],0,["color",8,32,76,1],0.18,["color",28,78,128,1],0.38,["color",73,132,180,1],0.58,["color",161,169,119,1],0.78,["color",230,135,44,1],0.92,["color",214,69,33,1],1,["color",255,245,200,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]' center=[105.85,21.03] zoom="11.5" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:#333333;background-color:rgba(35,35,35,0.92);color:#FFFFFF;box-sizing:border-box;" }-->

#### Hanoi (2020)
Growth thickens along Ha Dong and Gia Lam, with new built-up clusters visible beyond the historic core.

<div style="width:100%; box-sizing:border-box; margin:16px 0 0 0; padding:10px 12px; background:rgba(38,38,38,0.9); border-radius:6px; color:#FFFFFF; font-size:0.88rem;">
  <div style="font-weight:600; margin-bottom:7px; color:#FFFFFF;">ALOS-2 PALSAR-2 HH — Urban-feature visualization scale</div>
  <div style="height:14px; width:100%; border-radius:3px; background:linear-gradient(to right, rgb(8,32,76) 0%, rgb(28,78,128) 18%, rgb(73,132,180) 38%, rgb(161,169,119) 58%, rgb(230,135,44) 78%, rgb(214,69,33) 92%, rgb(255,245,200) 100%);"></div>
  <div style="display:flex; justify-content:space-between; margin-top:4px; color:#FFFFFF;">
    <span>0</span><span>2,000</span><span>4,000</span><span>6,000</span><span>8,000</span>
  </div>
  <div style="margin-top:7px; font-size:0.82rem; color:#FFFFFF;">Lower HH values appear in dark blue tones, while higher values appear in orange to light cream tones, helping urban and built-up features stand out more clearly.</div>
</div>


### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://workspace-ui-public.eodashboard-operations.hub-otc-sc.eox.at/api/public/share/public-ef89cd51-75/stories/alos2-ideation/Hanoi/ALOS_PALSAR_YEARLY_Hanoi_2024.tif"}]},"properties":{"id":"palsar2-yearly-hanoi;:;2024-01-01T00:00:00Z;:;0","title":"Hanoi_2024"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],8000],0,["color",8,32,76,1],0.18,["color",28,78,128,1],0.38,["color",73,132,180,1],0.58,["color",161,169,119,1],0.78,["color",230,135,44,1],0.92,["color",214,69,33,1],1,["color",255,245,200,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]' center=[105.85,21.03] zoom="11.5" animationOptions="{duration:1000}" style="width:50%;max-width:50%;background:#333333;background-color:rgba(35,35,35,0.92);color:#FFFFFF;box-sizing:border-box;" }-->

#### Hanoi (2024)
Peri-urban districts, Hoang Mai, Long Bien, Dong Anh, show denser built-up returns, marking the mid-study acceleration.

<div style="width:100%; box-sizing:border-box; margin:16px 0 0 0; padding:10px 12px; background:rgba(38,38,38,0.9); border-radius:6px; color:#FFFFFF; font-size:0.88rem;">
  <div style="font-weight:600; margin-bottom:7px; color:#FFFFFF;">ALOS-2 PALSAR-2 HH — Urban-feature visualization scale</div>
  <div style="height:14px; width:100%; border-radius:3px; background:linear-gradient(to right, rgb(8,32,76) 0%, rgb(28,78,128) 18%, rgb(73,132,180) 38%, rgb(161,169,119) 58%, rgb(230,135,44) 78%, rgb(214,69,33) 92%, rgb(255,245,200) 100%);"></div>
  <div style="display:flex; justify-content:space-between; margin-top:4px; color:#FFFFFF;">
    <span>0</span><span>2,000</span><span>4,000</span><span>6,000</span><span>8,000</span>
  </div>
  <div style="margin-top:7px; font-size:0.82rem; color:#FFFFFF;">Lower HH values appear in dark blue tones, while higher values appear in orange to light cream tones, helping urban and built-up features stand out more clearly.</div>
</div>


## Data and Methods
The analytical workflow of this project is established upon the optimal integration of multi-sensor data sources within the Google Earth Engine (GEE) cloud computing platform, enabling high-performance processing of big geospatial data with superior precision and consistency.

**Sentinel-2** optical and **ALOS-2 PALSAR-2** SAR imagery provide complementary observations of Hanoi's urban landscape. Optical data capture spectral characteristics of vegetation, built-up areas, and water, whereas SAR provides information related to surface structure and roughness. Combining the two data types therefore provides richer information for land-cover mapping and urban monitoring.

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN-Optical-SAR-View.png?raw=true" style="max-width:100%;width:1000px;height:auto;" alt="Analysis workflow" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [4].</b> Optical and SAR observations of Hanoi. Sentinel-2 imagery highlights spectral characteristics, while ALOS-2 PALSAR-2 imagery provides complementary information on surface and structural properties.</p>
</div>

**Why combine optical and SAR?** Optical imagery describes surface and vegetation properties, while SAR provides complementary structural information that can improve characterization of complex urban landscapes.

The study combines optical, radar, and topographic data within Google Earth Engine (GEE). The datasets were pre-processed, co-registered, and integrated to generate land-cover features. Spectral indices, including NDVI, NDBI, and NDWI, were calculated from optical imagery, while ALOS-2 PALSAR-2 provided complementary radar information.

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN-FlowchartHQ.png?raw=true" style="max-width:100%;width:1000px;height:auto;" alt="Analysis workflow" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [5].</b> Overall methodological workflow for multi-source EO-based LULC mapping and urban change analysis in Hanoi.</p>
</div>

Key features were derived from the satellite data using NDVI, NDBI, and NDWI, together with topographic information from the DEM. These features were used to distinguish major land-cover types.

Random Forest was selected as the main classification model because it can handle multiple, non-linear input features. The classified maps provide the basis for measuring land-cover change and urban expansion.

How does the monitoring work?
1) Observe — collect satellite observations;
2) Combine — integrate optical, radar, and topographic information;
3) Classify — identify major land-cover types;
4) Compare — analyse maps from different years;
5) Measure — quantify urban expansion and growth;
6) Support decisions — provide spatial evidence for planning.

## Results
Hanoi experienced substantial land-cover change between 2015 and 2025. The most prominent change was the expansion of built-up areas, accompanied by changes in agriculture, vegetation, water, barren land, and other surfaces. The spatial pattern shows that urban expansion was concentrated around the existing urban core and extended outward into peri-urban areas.

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN-LULCmaps.png?raw=true" style="max-width:100%;width:900px;height:auto;" alt="Analysis workflow" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [6].</b> Land use/land cover map of Hanoi for the years.</p>
</div>

**Key findings**: Built-up land increased from 18.1% of the study area in 2015 to 25.2% in 2020 and 32.8% in 2025, an increase of 14.7 percentage points over the decade. Agriculture remained the largest class, accounting for 38.3%, 40.2%, and 38.0% in 2015, 2020, and 2025, respectively. Barren land decreased from 7.1% to 3.9%, while the proportion of Other land decreased from 21.8% to 11.2%.

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN-Chart.jpg?raw=true" style="max-width:100%;width:500px;height:auto;" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [7].</b> LChanges in the proportion of land-cover classes in Hanoi from 2015 to 2025.</p>
</div>

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN-Chart2.png?raw=true" style="max-width:100%;width:500px;height:auto;" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [8].</b> Changes in area of different land-cover and land-use classes in the period from 2015 to 2025.</p>
</div>

The maps show that built-up areas expanded from the established urban core toward surrounding peri-urban areas and along major development corridors. The Annual Growth Rate (AGR) further highlights locations where urban expansion was more concentrated during the study period.

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN-Spatial%20Expansion.jpg?raw=true" style="max-width:100%;width:400px;height:auto;" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [9].</b> Spatial expansion of built-up areas in Hanoi from 2015 to 2025.</p>
</div>

<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0;">
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/7-Rate.jpg?raw=true" style="max-width:100%;width:600px;height:auto;" />
<p style="text-align:center;font-size:0.9em;font-style:italic;margin-top:5px;margin-bottom:1px;"><b>Figure [10].</b> Spatial distribution of the Urbanization Ratio and Annual Growth Rate in Hanoi from 2015 to 2025</p>
</div>

## Conclusions
Hanoi's urbanization is spatially uneven. Higher urbanization and growth are concentrated around the established urban area and major development corridors, while less-developed areas retain larger proportions of agricultural and vegetated land. Urbanization Ratio indicates the proportion of built-up surfaces, while Annual Growth Rate highlights areas experiencing faster expansion.

Classification reliability should be reported together with the maps using the available validation results, such as Overall Accuracy (OA), Kappa, and class-wise accuracy. No values are added here because the current Dashboard draft does not provide them.

The spatial increase in impervious surfaces provides an additional indication of urban intensification. Together, the LULC maps and urbanization indicators show not only how much Hanoi has changed, but also where development has been concentrated.

#### Limitations
Several limitations should be considered. First, optical observations can be affected by clouds, particularly during the rainy season. Second, the 25 m spatial resolution of ALOS-2 PALSAR-2 limits very detailed urban mapping. Third, validation depends on the availability of high-resolution imagery and field observations. Finally, the six-class LULC scheme does not distinguish detailed urban functions such as residential, commercial, and industrial areas.

#### Future Development
Future development will focus on three directions: (1) Expand — apply the monitoring framework to other major Vietnamese cities; (2) Integrate — combine urban expansion with green-space, water-quality, population, and air-quality indicators; and (3) Operationalize — develop an interactive EO dashboard with time-series visualization, cross-city comparison, and planning-oriented indicators.

## Open Science

| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| --- | --- | --- | --- |
| **[ALOS-2 PALSAR-2](https://www.eorc.jaxa.jp/ALOS/en/alos-2/a2_about_e.htm)** | Dataset | JAXA | 25 m L-band SAR data (2015/07/22; 2020/03/25; 2025/01/22), calibrated, speckle filtered and converted to dB to extract HH/HV polarisation features for the Random Forest classification. |
| **[Global PALSAR-2/PALSAR Yearly Mosaic on Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_PALSAR_YEARLY_SAR_EPOCH)** | Data Access Platform | Google Earth Engine / JAXA EORC | Source of the ALOS-2 PALSAR-2 yearly mosaics (HH polarisation) shown in the story's map tour for 2015, 2020 and 2024. |
| **[Landsat 8](https://www.usgs.gov/landsat-missions)** | Dataset | USGS | 30 m optical imagery (2015/07/01) used for band extraction, NDVI/NDWI/NDBI calculation, cloud masking and LULC classification. |
| **[Sentinel-2](https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2)** | Dataset | ESA / Copernicus | 10 m optical imagery (2020/03/09;–2025/01/12) used for spectral band extraction, vegetation index calculation and LULC classification. |
| **PlanetScope** | Dataset | Planet Labs | 3 m imagery (2020/11/13; 2025/01/12) used for high-resolution validation and training sample collection. |
| **[SRTM](https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003)** | Dataset | NASA | 30 m Digital Elevation Model used to support the classification. |
| **[EO Dashboard](https://eodashboard.org)** | Platform / Web Tool | ESA, NASA, JAXA | Hosts the interactive map tours of Hanoi, its suburban districts and the ALOS-2 PALSAR-2 time series. |

### References <!--{ nav="false" }-->
1. Angel, S., Parent, J., Civco, D. L., Blei, A., & Potere, D. (2011). The dimensions of global urban expansion: Estimates and projections for all countries, 2000-2050. Progress in Planning, 75(2), 53–107. https://doi.org/10.1016/j.progress.2011.04.001.
2. Belgiu, M., & Drăguţ, L. (2016). Random forest in remote sensing: A review of applications and future directions. ISPRS Journal of Photogrammetry and Remote Sensing, 114, 24–31. https://doi.org/10.1016/j.isprsjprs.2016.01.011.
3. Bui Thi, N. L., Nguyen Manh, H., Vu Anh, T., Dao Duy, T., Asami, H., & Nguyen Cong, G. (2026). Urban development management in Dien Bien Phu City: An integrated approach using multi-source remote sensing, machine learning, and planning maps. Vietnam Journal of Earth Sciences, 4(48), 513–514. https://doi.org/10.15625/2615-9783/24668.
4. Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., & Moore, R. (2017). Google Earth Engine: Planetary-scale geospatial analysis for everyone. Remote Sensing of Environment, 202, 18–27. https://doi.org/10.1016/j.rse.2017.06.031.
5. Hung, N. M., Anh, T. V., Duy, T. D., Mai, S. Le, Cong, G. N., Le, H., & Thu, T. (2025). Urban Expansion Monitoring Using Sentinel-1 and Sentinel-2 Data Fusion on Google Earth Engine. International Conference on Earth, Mine and Environmental Sciences for Green, Sustainable, and Prosperous Development in the Era of a Nation’s Rise (EME2025), 2, 180–189. https://doi.org/10.15625/vap.2025.0196.
6. Hung, N. M., Tuan, V. A., Khac, D. V., Toan, D. D., Son, L. M., Binh, T. T., & Giang, N. C. (2026). Quantifying the Spatiotemporal Impacts of Urban Expansion on Urban Heat Island Intensity Using Multispectral Remote Sensing Data. IOP Conference Series: Earth and Environmental Science, 1633(1), 012027. https://doi.org/10.1088/1755-1315/1633/1/012027.
7. Joshi, N., Baumann, M., Ehammer, A., Fensholt, R., Grogan, K., Hostert, P., Jepsen, M., Kuemmerle, T., Meyfroidt, P., Mitchard, E., Reiche, J., Ryan, C., & Waske, B. (2016). A Review of the Application of Optical and Radar Remote Sensing Data Fusion to Land Use Mapping and Monitoring. Remote Sensing, 8(1), 70. https://doi.org/10.3390/rs8010070.
8. Nguyen Manh, H., Vu Anh, T., Dao Duy, T., Son, L. M., Nguyen Hong, Q., & Le Thi Thu, H. (2026). Multi-Sensor Satellite Imagery and Machine Learning for Mapping Land Cover Dynamics and Assessing the Urban Heat Island–Air Quality Relationship in Hanoi. In V. A. Tran, L. Q. Nguyen, X. T. Tran, Q. M. Nguyen, S. Choosumrong, & V. Raghavan (Eds.), GeoInformatics for Spatial-Infrastructure Development in Earth & Allied Sciences. GIS-IDEAS 2026. Lecture Notes in Civil Engineering (Vol. 941, pp. 418–451). Springer Nature Switzerland. https://doi.org/10.1007/978-3-032-39470-5_21.
9. Nguyen, H. M., Dao, T. D., Vu, C. D., Luong, D. N., Khuc, T., Le, S. M., & Nguyen, T. G. (2026). Assessing coastal urbanization and land use efficiency from multi-temporal optical imagery using machine learning: case study in Ha Long City. Journal of Mining and Earth Sciences, 67(4), 42–59. https://doi.org/10.46326/JMES.2026.67(4).05.
10. Seto KC, Fragkias M, Güneralp B, Reilly MK (2011) A Meta-Analysis of Global Urban Land Expansion. PLOS ONE 6(8): e23777. https://doi.org/10.1371/journal.pone.0023777.
11. Shimada, M., Itoh, T., Motooka, T., Watanabe, M., Shiraishi, T., Thapa, R., & Lucas, R. (2014). New global forest/non-forest maps from ALOS PALSAR data (2007–2010). Remote Sensing of Environment, 155, 13–31. https://doi.org/https://doi.org/10.1016/j.rse.2014.04.014.
12. Talukdar, S., Singha, P., Mahato, S., Shahfahad, Pal, S., Liou, Y.-A., & Rahman, A. (2020). Land-Use Land-Cover Classification by Machine Learning Classifiers for Satellite Observations—A Review. Remote Sensing, 12(7), 1135.
13. United Nations Human Settlements Programme (UN-Habitat). (2016). World Cities Report 2016: Urbanization and Development - Emerging Futures. https://unhabitat.org/world-cities-report-2016.

#### Image and visualisation credits
- **Cover and header image:** Original to the study.
- **Figures 1:** Original to the study.
- **Figure 2 (ALOS-2 satellite):** Japan Aerospace Exploration Agency (JAXA).

### Disclaimer:
This paper is currently undergoing final editorial review. Minor revisions may be made during the publication process; however, no substantial changes to the scientific findings or conclusions are anticipated.

