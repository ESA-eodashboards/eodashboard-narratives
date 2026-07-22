---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
official: true
collections: collectionIdentifier1, collectionIdentifier2
---

# Satellites, Fields, and the Future of Rice Yield Estimation <!--{ as="img" mode="hero" src="https://github.com/phkh1366/eoxhub-related/blob/main/Thai-cover.JPG?raw=true" }-->
### Authors: Jatuporn Nontasiri<sup>1</sup>, Natnaphat Subtaweepollert<sup>1</sup>, Matawee Srisawat<sup>2</sup>,Nathaphat Kingkaew<sup>3</sup>, Suppanut Makrak<sup>3</sup>, Premwadee Traitangwong<sup>4</sup><!--{ style="font-size:1.0rem;opacity:0.7;margin-top:1rem; color:Yellow" }-->

<div style="text-align:left; font-size:0.95rem; opacity:0.85; margin-top:1rem; color:Yellow;">

1. Office of Agricultural Economics  
2. Geo-Informatics and Space Technology Development Agency  
3. Rice Department 
4. Thai Meteorological Department  

</div> 

#
This story is based on results from **ALOS-2 Ideathon Bridging Space Data and Societal Needs**, organised by JAXA, GISTDA, Keio University and RESTEC. 
<p align="center">
  <img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/2d25ca89ebc5fd3f1dbf204779815d5946de4496/Jaxa_logo.svg" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/GISTDA_LOGO.png?raw=true" height="70" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/Keio_University_Logo.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/RESTEClogo-trans.png?raw=true" height="80" style="margin: 0 0px;"/>
</p>

The study, dedicated to **Earth Observation (EO) Platform for Rice Yield Estimation** project developed by participants from the following organizations:
<p align="center">
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/Bluelogo_EN1_0.jpg?raw=true" height="60" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/GISTDA_LOGO.png?raw=true" height="60" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/RiceDepartment_Thai.webp?raw=true" height="60" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/TMD_Logo.webp?raw=true" height="60" style="margin: 0 0px;"/>
 
</p>

## Challenge <!--{ style="font-size:2.00rem;opacity:1;margin-top:1rem; color:Navy" }-->
### Background <!--{ style="font-size:1.30rem;opacity:1;margin-top:1rem; color:black" }-->
Rice is central to food security and the agricultural economy of Thailand, but accurately estimating production remains difficult. Climate variability, extreme weather, pests, and changing farming practices can rapidly affect crop growth. Conventional methods, such as field surveys and crop-cutting experiments, provide valuable information but are costly, time-consuming, and limited in spatial coverage. This can delay the production estimates needed for agricultural planning, market management, crop insurance, and early response to possible shortages.

Earth Observation offers a faster and more scalable approach. Optical and radar satellite data can monitor rice fields throughout the growing season, including during cloudy conditions. By combining vegetation indices, radar backscatter, field measurements, and statistical models, this study develops a method for estimating rice yield across large areas.

More timely and reliable yield information can help government agencies, farmers, insurers, exporters, and agribusinesses make better decisions. It can also strengthen climate resilience, improve food security assessments, and support more sustainable agricultural management in Thailand.

### Problem Statment <!--{ style="font-size:1.30rem;opacity:1;margin-top:1rem; color:black" }-->
Earth Observation (EO) represents a transformative approach for operational rice yield estimation by integrating multi-source remote sensing observations with advanced analytical and predictive modeling techniques. The synergistic use of optical and Synthetic Aperture Radar (SAR) satellite data enables continuous, large-scale monitoring of rice growth and improves the accuracy and timeliness of yield prediction. An EO-based operational framework enhances agricultural decision-making, strengthen climate resilience, improve market and food security planning, and supporting the transition toward sustainable, data-driven agricultural management at regional and national scales.

## Objectives <!--{ style="font-size:2.00rem;opacity:1;margin-top:1rem; color:Navy" }-->
- Investigate the **relationships between rice growth stage, key rice biophysical parameters, and rice yield** to identify the most significant predictors for yield estimation.
- **Evaluate and compare the potential of optical sensor and SAR** remote sensing data for **rice yield estimation** across different rice growth stages.
- **Develop an operational rice yield estimation model** by integrating satellite-derived variables, rice biophysical parameters, and a Linear Regression Model (LRM) to improve the accuracy and spatial representation of yield estimates.
- Optimize the performance of Earth Observation (EO)- based platform for operational rice yield estimation through model calibration, validation, and implementation for large-scale agricultural monitoring.


## Case Study <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"s2-cloudless-2025","title":"Sentinel-2 Cloudless 2025"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2025_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"labels","title":"Labels"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' center=[100.00,14.47] zoom="11" animationOptions="{duration:500}" style="width: 50%; max-width: 60%; box-sizing: border-box;"}-->
##### Suphan Buri
is located in the central region of Thailand (Figure 1). The province covers an area of approximately 5,358 km² and lies at elevations ranging from 3 to 10 m above mean sea level. The topography is predominantly characterized by flat alluvial plains with slopes of approximately 0–3%, making the area highly suitable for intensive agricultural production. Small upland areas are primarily located in the western part of the province. The southeastern region represents the lowest elevation, averaging approximately 3m above mean sea level, whereas the northern part reaches elevations of approximately 10m.
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/StudyArea_Suphan1.jpg?raw=true" style="max-width: 100%; width: 1200px; height: auto;"  /> 
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"> <b>Figure [1].</b> Study area map of Central Thailand (Suphan Buri province).</p> 
</div> 

### <!--{ layers='[{"type":"Tile","properties":{"id":"openstreetmap","title":"OpenStreetMap"},"source":{"type":"XYZ","urls":["https://tiles.maps.eox.at/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpg"],"attributions":"Data © OpenStreetMap contributors; rendering © EOX"}}]' center=[100.05,14.40] zoom="13" animationOptions="{duration:500}" style="width: 60%; max-width: 100%; box-sizing: border-box;"}-->

The Tha Chin River flows through Thailand’s central plains and passes through Suphan Buri Province, where it supports an extensive network of irrigation canals and agricultural areas.
Suphan Buri is situated within the Tha Chin River Basin, with the Tha Chin River (also known locally as the Suphan Buri River) flowing from north to south through the province. The province possesses a well-developed irrigation network consisting of rivers, canals, reservoirs, ponds, and wetlands. The Krasiew Dam serves as one of the principal water sources supporting irrigation and agricultural activities. Administratively, the province comprises 10 districts: Mueang Suphan Buri, Derm Bang Nang Buat, Dan Chang, Bang Pla Ma, Si Prachan, Don Chedi, Song Phi Nong, Sam Chuk, U Thong, and Nong Ya Sai.

Agriculture is the dominant land use in Suphan Buri Province, with rice cultivation occupying the largest proportion of the agricultural area. The province is recognized as one of Thailand's major rice-producing regions due to its fertile alluvial soils, extensive irrigation infrastructure, and favorable climatic conditions. Rice is cultivated throughout the year under an irrigated production system, with two principal cropping seasons. The wet-season (main-season) rice crop is grown from May to October, while the dry-season (off-season) rice crop extends from November to April of the following year. The availability of irrigation water enables intensive rice cultivation and multiple cropping cycles annually, making Suphan Buri an ideal study area for developing and evaluating Earth Observation (EO)-based rice monitoring and yield estimation models.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/Fig2FieldSurvey.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;"  /> 
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"> <b>Figure [2].</b> Ground truth collection in study area.
</div>

## Methodology Workflow & Data
Rice growth and yield were assessed by integrating multi-source Earth Observation data with field measurements. Sentinel-2 optical imagery was used to calculate vegetation indices such as NDVI and EVI, while Sentinel-1 C-band and ALOS-2 L-band SAR data provided information on crop structure, biomass, moisture, and surface conditions under all-weather conditions. UAV imagery was also collected during field surveys to generate high-resolution NDVI maps.

Field measurements were conducted at five major rice growth stages—seedling, tillering, panicle development, flowering, and harvesting. Key biophysical variables, including plant height, leaf area index, chlorophyll content, biomass, and crop-cutting yield, were recorded for each experimental plot.

The satellite and UAV data were pre-processed and matched with the field observations. Average remote-sensing values were extracted from the central area of each plot to reduce mixed-pixel and boundary effects. Correlation analysis was then used to identify the variables most strongly related to rice yield.

Significant variables were incorporated into linear and multiple regression models developed for different growth stages and provinces. The selected models were applied to satellite imagery to generate spatial rice-yield maps within mapped rice-growing areas. Model accuracy was evaluated by comparing predicted yields with crop-cutting measurements using RMSE and MAPE.
| Dataset | Provider | Resolution | Period | Purpose |
|:---:|:---:|:---:|:---:|:---:|
| **Optical:** Sentinel-2A and Sentinel-2B MSI | ESA | 10–60 m | 1 May–31 October 2025 | Calculate vegetation indices, such as NDVI and EVI |
| **Radar:** Sentinel-1A and Sentinel-1B SLC IW, VV and VH polarizations | ESA | 5 × 20 m | 1 May–31 October 2025 | Calculate backscatter coefficients, such as sigma nought (σ⁰), gamma nought, and beta nought |
| ALOS-2 Level 2.2 ScanSAR, HH and HV polarizations | JAXA | 25 m | 1 May–31 October 2025 | Calculate backscatter coefficients |
| Drone imagery | OAE | — | 1 May–31 October 2025 | Analyze NDVI |
| Field data | OAE | — | 1 May–31 October 2025 | Collect rice biophysical variables from 29 sample units |
| Statistical rice yield data | OAE | — | 2024 | Validate accuracy |
| Rice area interpreted from Sentinel-2 | OAE | — | 2025 | Mask rice-growing areas after applying the model to satellite imagery |
| Administrative boundary | LDD | — | 2013 | — |

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/Flowchart.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;"  /> 
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"> <b>Figure [3].</b> Conceptual framework.
</div>

## Results
The findings indicate that satellite imagery is suitable for rice yield prediction model development, as it provides sufficient temporal coverage across all rice growth stages. Nevertheless, the usefulness of optical Sentinel-2 imagery is constrained by cloud contamination, with only approximately 40% of vegetation index observations being available for analysis. 
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/yieldPixelBased.jpg?raw=true" style="max-width: 100%; width: 1200px; height: auto;"  /> 
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"> <b>Figure [4].</b> Result of rice yield estimation using the significant dry total biomass and the VV polarization.
</div>
Furthermore, the results demonstrated that rice dry biomass and Sentinel-1 SAR imagery in the VV polarization during the harvesting stage were the most effective variables for predicting rice yield.
After masking rice cultivated area from raster output with Multiple Linear Regression (MLR) model, the work uses zonal statistic for average and maximum value of rice yield pixel in sub-district level. Zonal statistic is normally use for assessing vegetation indices within administrative boundaries or analyzing soil across different region. Zonal statistic operation calculates statistics on cell values of a raster (a value raster) within the zones defined by another dataset. The Maximum is the highest value in each zone is assigned to all cell in that zone whilst the Mean is the average of the values in each zone is assigned to all output cells in that zone.
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/MeanAPE.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;"  /> 
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"> <b>Figure [5].</b> The Mean Absolute Percentage Error (MAPE) in Suphan Buri Province with average and maximum zonal statistic.
</div>

The results demonstrated that the multiple linear regression (MLR) model integrating Sentinel-1 SAR imagery in the VV polarization with total dry biomass at the harvesting stage provided a statistically significant model for rice yield estimation. 
Based on the mean zonal statistic, the model estimated rice production in Suphan Buri Province at 906,089.23 tons, with a root mean square error (RMSE) of 9.96 tons. In contrast, the model based on the maximum zonal statistic estimated production at 959,933.53 tons, with an RMSE of 12.34 tons. The lower RMSE and Mean Absolute Percentage Error (MAPE) obtained using the mean zonal statistic (30.59%) compared with the maximum zonal statistic (31.25%) indicate that the mean zonal statistic provides more accurate and reliable estimates of rice production. Therefore, the mean zonal statistic is recommended for rice production estimation using Sentinel-1 SAR data and MLR models.

