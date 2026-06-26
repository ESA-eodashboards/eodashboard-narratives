---
cover-image: [COVER_IMAGE_URL]
date: [YYYY-MM-DD]
theme: [theme_name]
tags: [tag1,tag2,tag3]
---

# Urbanization monitoring from EO data <!--{ as="img" mode="hero" src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN1-Story-header-.png?raw=true" style="width: 100%; height:800px;" }-->
### Authors: Nguyen Manh HUNG¹, Dang Do Nam PHUONG², Tong Thi Huyen AI¹, Nguyen Huu CHUYEN³ <!--{ style="font-size:1.0rem;opacity:0.7;margin-top:1rem; color:Yellow" }-->
¹ [Vietnam National Space Center, Vietnam Acedamy of Science and Technology]  
² [Vietnam National University, Hanoi]  
³ [Department of National Remote Sensing, Ministry of Agriculture and Environment] <!--{ style="font-size:0.8rem;opacity:1;margin-top:1rem; color:Yellow; align="left"" }-->
...

#
*This story is based on results from **[ALOS-2 Ideathon Bridging Space Data and Societal Needs](https://vnsc.org.vn/en/news-events/vietnam-national-space-center-vietnam-academy-of-science-and-technology-organizes-workshop-on-application-ideas-for-alos-2-and-sar-satellite-data-in-vietnam/)**, organised by JAXA, VNSC and Keio University. The study, dedicated to **Urbanization monitoring from EO data**, was developed by participants from the following organizations:*

<p align="center">
  <img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/2d25ca89ebc5fd3f1dbf204779815d5946de4496/Jaxa_logo.svg" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/logo-VNSC-moi.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/Keio_University_Logo.png?raw=true" height="50" style="margin: 0 0px;"/>
</p>

## Challenge
Rapid urbanization is one of the major environmental and social challenges facing many countries today. In Asia and Africa, where most global urban expansion is taking place, cities are growing quickly and placing increasing pressure on land, infrastructure, natural resources, and communities.

In Vietnam, cities such as Hanoi are expanding rapidly through outward growth, new satellite urban areas, and changes in administrative boundaries. This process can lead to the loss of green spaces, more impervious surfaces, stronger Urban Heat Island effects, water quality issues, and pressure on biodiversity. At the same time, government agencies, planners, NGOs, and local communities need reliable and up-to-date spatial information to better understand these changes and support sustainable urban development.

#### Problem Statement
This study addresses the lack of timely and consistent spatial information on urban expansion in rapidly growing Vietnamese cities, especially Hanoi. Current data are often fragmented, outdated, or not updated frequently enough to support effective planning.

As a result, it is difficult to monitor how fast cities are expanding, which land use types are being converted, and how urban growth is affecting peri-urban areas. This project uses Earth observation data to monitor urban growth, detect land use changes, and provide practical information for sustainable planning and decision-making.

###### Current limitations of monitoring urban expansion:
At present, there is no continuous and synchronized satellite-based monitoring system for tracking urban sprawl and land use change in major Vietnamese cities. Existing data are often scattered across different sources and are not always easy to combine or use.

There is also a gap between scientific analysis and policy action. Even when satellite data are available, they are not always translated into clear and practical information for planners, policymakers, NGOs, or communities. A more systematic EO-based monitoring approach can help bridge this gap and support evidence-based urban governance.

## Objectives
* **Primary Objective:** 
To monitor **urbanization trends and urban area dynamics** in Hanoi using Earth Observation (EO) data through satellite image analysis and remote sensing techniques. Accordingly the specific Objectivesare:
- **Objective 1:** Monitoring Urban Expansion – To track the growth and sprawl of urban areas over time (2015–2025). <!--{ style="font-size:1rem;opacity:1; color:blue" }-->
- **Objective 2:** Assessing Land Use Dynamics – To develop detailed Land Use/Land Cover (LULC) maps with six classification categories: Built-up Land, Barren Land, Water Bodies, Forest, Agriculture, and Others. <!--{ style="font-size:1rem;opacity:1; color:blue" }-->
- **Objective 3:** Mapping Urban Growth Patterns – To generate spatial maps illustrating the direction and extent of urban changes. <!--{ style="font-size:1rem;opacity:1; color:blue" }-->
- **Objective 4:** Quantifying Urbanization Trends – To measure the rate of urban expansion and spatial patterns using indices such as the Impervious Surface Index (ISI), Urbanization Ratio (UR), and Annual Growth Rate (AGR). <!--{ style="font-size:1rem;opacity:1; color:blue" }-->
- **Objective 5:** Supporting Sustainable Planning – To provide planning-relevant information for assessing development trends and guiding future zoning strategies. <!--{ style="font-size:1rem;opacity:1; color:blue" }-->




## Use Case <!--{ as="eox-map" mode="tour" }-->
<!-- Map layers for Indonesia -->
<!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"nceo_africa_2017;:;AGB_map_2017v0m_COG;:;nceo_africa_2017;:;EPSG:3857","title":"nceo_africa_2017"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://nasa-maap-data-store/file-staging/nasa-map/nceo-africa-2017/AGB_map_2017v0m_COG.tif&resampling_method=nearest&bidx=1&colormap_name=gist_earth_r&rescale=0.0,400.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="6" center=[113.9213,-0.7893] projection="" animationOptions={duration:500}}-->
### Study Area 1
**Period of Interest:** 
Brief description of the study area in Indonesia and why it was selected.



<!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"nceo_africa_2017;:;AGB_map_2017v0m_COG;:;nceo_africa_2017;:;EPSG:3857","title":"nceo_africa_2017"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://nasa-maap-data-store/file-staging/nasa-map/nceo-africa-2017/AGB_map_2017v0m_COG.tif&resampling_method=nearest&bidx=1&colormap_name=gist_earth_r&rescale=0.0,400.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom=7" center=[32.3753, 70.3451] projection="" animationOptions={duration:500}}-->
### Study Area 2
Brief description of the study area 


## Data and Methods
### Datasets
Describe datasets used, e.g., SAR, optical, reference datasets, resolution, temporal coverage.

Category | Dataset | Description | Resolution | Temporal Coverage
--- | --- | --- | --- | ---
🛰️ SAR Data | [Dataset Name] | [Description] | [Resolution] | [Years]
🌍 Optical Data | [Dataset Name] | [Description] | [Resolution] | [Years]
📍 Reference Data | [Dataset Name] | [Description] | [Resolution] | [Years]

**Furhter information about the datasets:**  


### Methodology Workflow
Describe workflow: preprocessing, data fusion, indices, classification, etc.

<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;"> 
<img src="[WORKFLOW_IMAGE]" style="max-width: 100%; width: 1000px; height: auto;" alt="Analysis workflow" /> 
<p style="text-align: center; font-size: 1.2em; margin-top: 10px;"> <b>Figure [X].</b> Complete methodology workflow from data acquisition to analysis. </p> 
</div>

Explain classification rules, indices, thresholds, machine learning approach, and change detection methodology.

## Results
#### Initial findings:
Include description, key findings, and visualizations.
You can also add a Map Tour to show the datasets created and ingested on the EO Dashboard.

<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;"> 
<img src="[RESULT_IMAGE]" style="max-width: 100%; width: 1200px; height: auto;" alt="[ALT_TEXT]" /> 
<p style="text-align: center; margin-top: 10px;"> <b>Figure [X].</b> [Caption describing result image]. </p> 
</div>

Include quantitative results table if available; Explain differences across methods, data sources, or polarizations, etc.



...

## Conclusions
Summarize achievements, practical applications, limitations, and future vision.

Main Achievements:
1. [Achievement 1]  
2. [Achievement 2]  
3. [Achievement 3]  


Study Limitations and Considerations:
1. [Limitation 1]  
2. [Limitation 2]  
3. [Limitation 3]  

### Next Steps
Describe future directions, timelines, etc.
Future Vision:
[Describe operational systems, monitoring capabilities, and policy impact.]

## <!--{ as="div" }--> Open Science

| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| -------- | -------- | ------------------- | ---------------------- |
| [Dataset 1 Name & Link] | [SAR/Optical/Reference/Climate] | [Provider] | [Description / Usage] |
| [Dataset 2 Name & Link] | [SAR/Optical/Reference/Climate] | [Provider] | [Description / Usage] |
...

## References
* [Reference 1]  
* [Reference 2]  
* [Reference 3]  
...


