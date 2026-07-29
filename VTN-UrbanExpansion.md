---
cover-image: https://image.vietnamnews.vn/uploadvnnews/Article/2026/3/18/491117_urban.jpg
date: 2026-08-01
theme: Economy
tags: Urbanization,Vietnam
official: true
collections: collectionIdentifier1, collectionIdentifier2
---

# Urbanization monitoring from EO data <!--{ as="img" mode="hero" src="https://github.com/phkh1366/eoxhub-related/blob/main/VTN1-Story-header-.png?raw=true" style="width: 100%; height:800px;" }-->
### Authors: Nguyen Manh HUNG¹, Dang Do Nam PHUONG², Tong Thi Huyen AI¹, Nguyen Huu CHUYEN³ <!--{ style="font-size:1.0rem;opacity:0.7;margin-top:1rem; color:Yellow" }-->
¹ [Vietnam National Space Center, Vietnam Acedamy of Science and Technology]  
² [Vietnam National University, Hanoi]  
³ [Department of National Remote Sensing, Ministry of Agriculture and Environment] <!--{ style="font-size:0.8rem;opacity:1;margin-top:1rem; color:Yellow" }-->
...

#
This story is based on results from **[ALOS-2 Ideathon Bridging Space Data and Societal Needs](https://vnsc.org.vn/en/news-events/vietnam-national-space-center-vietnam-academy-of-science-and-technology-organizes-workshop-on-application-ideas-for-alos-2-and-sar-satellite-data-in-vietnam/)**, organised by JAXA, VNSC, Keio University and RESTEC. 
<p align="center">
  <img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/2d25ca89ebc5fd3f1dbf204779815d5946de4496/Jaxa_logo.svg" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/logo-VNSC-moi.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/Keio_University_Logo.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/RESTEClogo-trans.png?raw=true" height="80" style="margin: 0 0px;"/>
</p>

The study, dedicated to **Urbanization monitoring from EO data**, was developed by participants from the following organizations:
<p align="center">
  <img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/2d25ca89ebc5fd3f1dbf204779815d5946de4496/Jaxa_logo.svg" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/logo-VNSC-moi.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/vietnam-national-university-logo-png_seeklogo-514017.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/VTNlogo.png?raw=true" height="40" style="margin: 0 0px;"/>
</p>


## Challenge <!--{ style="font-size:2.00rem;opacity:1;margin-top:1rem; color:Navy" }-->
Rapid urbanization is one of the major environmental and social challenges facing many countries today. In Asia and Africa, where most global urban expansion is taking place, cities are growing quickly and placing increasing pressure on land, infrastructure, natural resources, and communities.

In Vietnam, cities such as Hanoi are expanding rapidly through outward growth, new satellite urban areas, and changes in administrative boundaries. This process can lead to the loss of green spaces, more impervious surfaces, stronger Urban Heat Island effects, water quality issues, and pressure on biodiversity. At the same time, government agencies, planners, NGOs, and local communities need reliable and up-to-date spatial information to better understand these changes and support sustainable urban development.

#### Problem Statement <!--{ style="font-size:2.0rem;opacity:1;margin-top:1rem; color:Navy" }-->
This study addresses the lack of timely and consistent spatial information on urban expansion in rapidly growing Vietnamese cities, especially Hanoi. Current data are often fragmented, outdated, or not updated frequently enough to support effective planning.

As a result, it is difficult to monitor how fast cities are expanding, which land use types are being converted, and how urban growth is affecting peri-urban areas. This project uses Earth observation data to monitor urban growth, detect land use changes, and provide practical information for sustainable planning and decision-making.

###### Current limitations: <!--{ style="font-size:1.50rem;opacity:0.7;margin-top:1rem; color:Navy" }-->
At present, there is no continuous and synchronized satellite-based monitoring system for tracking urban sprawl and land use change in major Vietnamese cities. Existing data are often scattered across different sources and are not always easy to combine or use.

There is also a gap between scientific analysis and policy action. Even when satellite data are available, they are not always translated into clear and practical information for planners, policymakers, NGOs, or communities. A more systematic EO-based monitoring approach can help bridge this gap and support evidence-based urban governance.

## Objectives <!--{ style="font-size:1.5rem;opacity:1;margin-top:1rem; color:Navy" }-->
**Primary Objective:** 
To monitor **urbanization trends and urban area dynamics** in Hanoi using Earth Observation (EO) data through satellite image analysis and remote sensing techniques. Accordingly the specific Objectivesare: <!--{ style="font-size:1rem;opacity:1; margin-top:0px; margin-bottom:0px; color:blue" }-->

- **Objective 1:** Monitoring Urban Expansion – To track the growth and sprawl of urban areas over time (2015–2025). <!--{ style="font-size:1rem;opacity:1; margin-top:0px; margin-bottom:0px; color:blue" }-->
- **Objective 2:** Assessing Land Use Dynamics – To develop detailed Land Use/Land Cover (LULC) maps with six classification categories: Built-up Land, Barren Land, Water Bodies, Forest, Agriculture, and Others. <!--{ style="font-size:1rem;opacity:1; color:blue"; margin-top:0px; margin-bottom:0px; }-->
- **Objective 3:** Mapping Urban Growth Patterns – To generate spatial maps illustrating the direction and extent of urban changes. <!--{ style="font-size:1rem;opacity:1; color:blue" }-->
- **Objective 4:** Quantifying Urbanization Trends – To measure the rate of urban expansion and spatial patterns using indices such as the Impervious Surface Index (ISI), Urbanization Ratio (UR), and Annual Growth Rate (AGR). <!--{ style="font-size:1rem;opacity:1; color:blue" }-->
- **Objective 5:** Supporting Sustainable Planning – To provide planning-relevant information for assessing development trends and guiding future zoning strategies. <!--{ style="font-size:1rem;opacity:1; color:blue" }--> 


## Case Study <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"s2-cloudless-2025","title":"Sentinel-2 Cloudless 2025"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2025_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"labels","title":"Labels"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' center=[105.85,21.03] zoom="13" animationOptions="{duration:500}" }-->

##### Hanoi 
Hanoi serves as the primary political, economic, and cultural hub of Vietnam, having experienced one of the nation's most accelerated urbanization rates throughout the last twenty years.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/1-Hanoi-CaseStudy.jpg?raw=true" style="max-width: 100%; width: 1200px; height: auto;"  /> 
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"> <b>Figure [1].</b> Study area </p> 
</div>

Geographically situated within the Red River Delta, the city encompasses approximately 3,360 km², positioning it as one of the most expansive capital cities in Southeast Asia in terms of land area. Recent census data from 2024 indicates a population of nearly 8.7 million, ranking Hanoi as Vietnam’s second-largest city by population density. 
The city's urban footprint has been steadily pushing outward into suburban districts, including Gia Lam, Long Bien, Ha Dong, Hoang Mai, Soc Son, and Dong Anh. This rapid physical growth is driven by the extensive development of transportation networks, modern residential zones, and industrial clusters. Such profound modifications to land use and natural topography have placed considerable strain on local natural resources and the quality of the urban environment.  
## Suburban districts <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"s2-cloudless-2025","title":"Sentinel-2 Cloudless 2025"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2025_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"labels","title":"Labels"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' center=[105.85,21.03] zoom="15" animationOptions="{duration:500}" }-->

##### Gia Lam
Gia Lam is located to the east of central Hanoi and represents one of the important suburban expansion areas. Urban growth in this district is associated with new residential development, transport connections, and conversion of agricultural land.

### <!--{ center=[105.91,21.03] zoom="15" animationOptions="{duration:800}" }-->

##### Long Bien

Long Bien lies northeast of Hanoi’s historical center, across the Red River. It has experienced strong urban development due to improved connectivity, commercial growth, and expansion of residential areas.

### <!--{ center=[105.78,20.97] zoom="15" animationOptions="{duration:800}" }-->

##### Ha Dong

Ha Dong is located southwest of central Hanoi and has become one of the city’s major urban expansion zones. Its growth reflects the development of modern residential areas, road infrastructure, and urban services.

### <!--{ center=[105.86,20.98] zoom="15" animationOptions="{duration:800}" }-->

##### Hoang Mai

Hoang Mai is situated in the southern part of Hanoi. The district has seen rapid transformation from peri-urban and mixed land-use areas into dense residential and transport-linked urban zones.

### <!--{ center=[105.85,21.25] zoom="15" animationOptions="{duration:800}" }-->

##### Soc Son

Soc Son is located in northern Hanoi and includes more rural and peri-urban landscapes. Urban pressure in this area is influenced by transport infrastructure, industrial activities, and proximity to Noi Bai International Airport.

### <!--{ center=[105.85,21.15] zoom="15" animationOptions="{duration:800}" }-->

##### Dong Anh

Dong Anh lies north of the Red River and is considered a strategic area for Hanoi’s future urban expansion. Development in this district is linked to infrastructure projects, residential growth, and industrial zones.



### <!--{ center=[105.85,21.15] zoom="15" animationOptions="{duration:800}" }-->

##### Urban growth pressure

This rapid physical growth is driven by the extensive development of transportation networks, modern residential zones, and industrial clusters. Such profound modifications to land use and natural topography have placed considerable strain on local natural resources and the quality of the urban environment.

## Methodology Workflow & Data


The analytical workflow of this project is established upon the optimal integration of multi-sensor data sources within the Google Earth Engine (GEE) cloud computing platform, enabling high-performance processing of big geospatial data with superior precision and consistency. 


| Dataset | Provider | Resolution | Period | Purpose |
|---|---|---:|---|---|
| Landsat | USGS | 30m | 2015 | Band extraction, NDVI/NDWI/NDBI calculation, cloud masking, and LULC classification. |
| Sentinel-2 | ESA | 10m | 2020–2025 | Spectral band extraction, vegetation index calculation, and LULC classification. |
| ALOS-2/PALSAR-2 | JAXA | 25m | 2015–2025 | Pre-processing (calibration), speckle filtering, decibel (dB) conversion, and HH/HV polarization feature extraction for ML classification. |
| PlanetScope | Planet Labs | 3m | 2020, 2025 | High-resolution validation and sample collection support. |
| SRTM | NASA | 30m |  | Digital Elevation Model (DEM) for classification support. |


The initial phase focuses on rigorous pre-processing, encompassing atmospheric correction for optical spectral bands and advanced terrain correction for ALOS-2 PALSAR-2 Radar data to eliminate geometric and radiometric distortions.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/2-Methodology.png?raw=true" style="max-width: 100%; width: 1000px; height: auto;" alt="Analysis workflow" /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 10px;"> <b>Figure [2].</b> Complete methodology workflow from data acquisition to analysis. </p> 
</div>

Following this, the system executes the extraction of core biophysical features through representative surface indices, such as the Normalized Difference Vegetation Index (NDVI), Normalized Difference Built-up Index (NDBI), and Normalized Difference Water Index (NDWI), while integrating Digital Elevation Model (DEM) data to characterize three-dimensional landscape structural variations.
At the core of this methodology is the deployment of the Random Forest (RF) machine learning algorithm a robust classification model capable of handling complex non-linear correlations between spectral features. This algorithm is trained to automatically identify and categorize surfaces into six primary land cover classes: Built-up, Barren land, Water, Forest, Agriculture, and Others. The synergy between distinct spectral indices and advanced machine learning algorithms not only ensures exceptional accuracy for the classification maps but also provides a scientific analytical framework to quantify the expansion of impervious surfaces during the process of compact urbanization.


## Results
By leveraging massive Earth Observation (EO) archives, this project has successfully decoded the complex narrative of Hanoi’s urban surface transformation during the strategic period of 2015–2025. The central output of this research is a high-resolution, multi-temporal Land Use and Land Cover (LULC) mapping system, which enables the precise identification of not only the location but also the directional vectors of cover type transitions.

<div style="display: flex; flex-direction: column; align-items: center; margin: 5px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/3-LULC%20Maps.png?raw=true" style="max-width: 100%; width: 900px; height: auto;" alt="Analysis workflow" /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure [3].</b> Land use/land cover map of Hanoi for the years. </p> 
</div>
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/d99cbbe44f92394618df91dd5708ee7f56ad1e21/4-SankeyChart.jpg" style="max-width: 100%; width: 500px; height: auto;"/> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure [4].</b> Changes in the proportion of land-use and LULC classes in the study area from 2015 to 2025. </p> 
</div>
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/5-Chart.png?raw=true" style="max-width: 100%; width: 500px; height: auto;"  /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure [5].</b> The chart shows the change in area of objects in the period from 2015 to 2025. </p> 
</div>

The models provide visual evidence of the aggressive expansion of impervious surfaces representing concrete infrastructure spreading in corridors from the historical urban core toward peri-urban areas and satellite towns. Notably, the study scientifically quantifies the rate of urbanization through the Annual Growth Rate (AGR) index, helping to isolate and identify 'hot growth phases' of infrastructure linked to transportation network expansions and industrial zones.

</div>
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/6-UrbanExpan.png?raw=true" style="max-width: 100%; width: 400px; height: auto;"  /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure [6].</b> Urban Expansion in Ha Noi city over 10 years. </p> 
</div>

The surge in the Impervious Surface Index (ISI) across the urban change maps reflects more than just the scale of physical development; it highlights areas under significant micro-atmospheric pressure. These findings confirm that EO data is an irreplaceable tool for providing a holistic and accurate overview of urban dynamics, establishing a robust foundation for analyzing environmental impacts and evaluating planning efficiency. <!--{ style="font-size:1rem;opacity:1; margin-top:0px; margin-bottom:0px; margin-left:50px" }-->

</div>
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/7-Rate.jpg?raw=true" style="max-width: 100%; width: 600px; height: auto;"  /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure [7].</b> The distribution of Urbanization ratio and Urban growth rate in Ha Noi city over 10 years. </p> 
</div>


## Limitations
Despite the systematic approach employed in this study, several limitations should be acknowledged. First, the dependency on cloud-masking techniques for optical datasets (Landsat/Sentinel-2) may hinder data acquisition during the rainy season. Second, the 25m spatial resolution of ALOS-2 SAR data limits the capacity for detailed urban mapping at a micro-scale. Third, the validation process is contingent upon the availability of field survey data and high-resolution imagery. Additionally, the six-class LULC classification system may lack the granularity required to distinguish specific urban land-use types, such as residential, industrial, and commercial zones. Furthermore, this study does not yet integrate socio-economic datasets to provide a comprehensive analysis of the drivers of urbanization. Finally, the research scope is geographically limited to Hanoi and has not yet been extended to other urban centers.

## Future Development
To enhance the scope and impact of this study, future research will focus on several key directions. We plan to:  

- **1:** Expand the geographical coverage by applying our methodology to other major Vietnamese cities, such as Ho Chi Minh City, Da Nang, and Hai Phong. 
- **2:**  Enrich our monitoring indices by incorporating water quality assessment, the Green Space Index, and population density tracking. 


## References
1.	Seto KC, Fragkias M, Güneralp B, Reilly MK (2011) A Meta-Analysis of Global Urban Land Expansion. PLOS ONE 6(8): e23777. https://doi.org/10.1371/journal.pone.0023777
2.	Angel, S., Parent, J., Civco, D. L., Blei, A., & Potere, D. (2011). The dimensions of global urban expansion: Estimates and projections for all countries, 2000-2050. Progress in Planning, 75(2), 53–107. https://doi.org/10.1016/j.progress.2011.04.001.
3.	United Nations Human Settlements Programme (UN-Habitat). (2016). World Cities Report 2016: Urbanization and Development - Emerging Futures. https://unhabitat.org/world-cities-report-2016 
4.	Talukdar, S., Singha, P., Mahato, S., Shahfahad, Pal, S., Liou, Y.-A., & Rahman, A. (2020). Land-Use Land-Cover Classification by Machine Learning Classifiers for Satellite Observations—A Review. Remote Sensing, 12(7), 1135. 
 


