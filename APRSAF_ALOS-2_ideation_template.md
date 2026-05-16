---
cover-image: [COVER_IMAGE_URL]
date: [YYYY-MM-DD]
theme: [theme_name]
tags: [tag1,tag2,tag3]
---

# Story Title <!--{ as="img" mode="hero" src="[COVER_IMAGE_URL]" }-->
### Authors: AUTHOR_NAME¹, AUTHOR_NAME², AUTHOR_NAME³ <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
¹ [Affiliation 1]  
² [Affiliation 2]  
³ [Affiliation 3]  
...

#
*This story is based on results from [WORKSHOP/CONFERENCE/PROJECT]([LINK]), organised by [ORGANIZATION]([LINK]). The study, dedicated to **STUDY_TOPIC**, was developed by participants from the following organizations:*

<p align="center">
  <img src="[LOGO_URL_1]" alt="[ALT_TEXT]" height="80" style="margin: 0 15px;"/>
  <img src="[LOGO_URL_2]" alt="[ALT_TEXT]" height="80" style="margin: 0 15px;"/>
  ...
</p>

## Challenge
Write about the broader context and importance of the challenge addressed in the story.

#### Problem Statement
Describe the specific problem(s) your study addresses, including limitations of current methods.

###### Current limitations of [FIELD/ISSUE]:

Describe existing challenges, e.g., data limitations, monitoring gaps, methodological issues.

## Objectives
* Primary Objective: [Describe primary objective of the study/project.]
* Next Step: [Describe follow-up or secondary objectives.]

*Expected Outcomes:*

- Outcome 1
- Outcome 2  
- Outcome 3

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


