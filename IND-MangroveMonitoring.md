---
cover-image: [COVER_IMAGE_URL]
date: [YYYY-MM-DD]
theme: [theme_name]
tags: [tag1,tag2,tag3]
---

# Mangroves for Coastal Erosion Control: Harnessing Satellite Imagery for Effective Monitoring <!--{ as="img" mode="hero" src="https://github.com/phkh1366/eoxhub-related/blob/main/08.%20Preferred%20Cover%20Photo.jpg?raw=true" style="width: 100%; height:800px;" }-->

### Authors: Garda Kalari Yustisiansyah<sup>1</sup>, Buchari<sup>2</sup>, Alit Aji<sup>3</sup>,Pratondi Ario Seno Sudiro<sup>4</sup>, Novie Indriasari<sup>5</sup>, Dede Dirgahayu<sup>5</sup><!--{ style="font-size:1.0rem;opacity:0.7;margin-top:1rem; color:Yellow" }-->

<div style="text-align:left; font-size:0.95rem; opacity:0.85; margin-top:1rem; color:Yellow;">

1. Ministry of Forestry (Mangroves for Coastal Resilience)  
2. Institut Pertanian Bogor  
3. Ministry of Agrarian Affairs and Spatial Planning/National Land Agency  
4. Indonesian Maritime Security Agency  
5. BRIN (National Research and Innovation Agency)

</div> 

#
This story is based on results from **[ALOS-2 Ideathon Bridging Space Data and Societal Needs](https://brin.go.id/news/122360/brin-tegaskan-pentingnya-data-satelit-dukung-ekosistem-mangrove)**, organised by JAXA, BRIN, Keio University and RESTEC. 
<p align="center">
  <img src="https://raw.githubusercontent.com/phkh1366/eoxhub-related/2d25ca89ebc5fd3f1dbf204779815d5946de4496/Jaxa_logo.svg" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/BRIN%20National%20Research%20and%20Innovation%20Agency.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/Keio_University_Logo.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/RESTEClogo-trans.png?raw=true" height="80" style="margin: 0 0px;"/>
</p>

The study, dedicated to **Mangroves for Coastal Erosion Control**, was developed by participants from the following organizations:
<p align="center">
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/ATRBPN%20Ministry%20Of%20Agrarian%20and%20Spatial%20Planning_National%20Land%20Agency.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/BRIN%20National%20Research%20and%20Innovation%20Agency.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/IPB%20Institut%20Pertanian%20Bogor.png?raw=true" height="50" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/Maritime%20Security%20Agency.png?raw=true" height="60" style="margin: 0 0px;"/>
  <img src="https://github.com/phkh1366/eoxhub-related/blob/main/Ministry%20of%20Forestry%20M4CR.png?raw=true" height="100" style="margin: 0 0px;"/>  
</p>



## Challenge <!--{ style="font-size:2.00rem;opacity:1;margin-top:1rem; color:Navy" }-->
Coastal erosion poses **a critical and ongoing threat to Indonesia's mangrove ecosystems.** The sheer scale of this environmental degradation is immense; between 2009 and 2019, Indonesia experienced a total net loss of 128,176 hectares of mangrove area.

This massive deforestation and degradation translates into direct **destruction for coastal zones**. For instance, localized areas like **Kuala Selat Village** experience intensive coastal abrasion and continuous seawater intrusion throughout the year, demonstrating the urgent need for monitoring. 

The **continued destruction of mangrove** areas deeply **affects both the ecosystem's biodiversity and the human populations** that rely on these coastal environments. Coastal communities face immediate threats to their safety and infrastructure due to unchecked seawater intrusion. 

Furthermore, the **economic stability of these regions is jeopardized, as the loss of mangroves directly impacts primary local livelihoods and commodities, such as coconut plantations in Riau and aquaculture in East Java.**

Addressing this crisis requires a robust spatial response, but Indonesia's current National Mangrove Map (PMN), organized by the Ministry of Forestry, suffers from several severe limitations. At present, mangrove monitoring remains limited, featureless regarding forest density, and largely inaccessible to the stakeholders who need it most. Specifically, the operational challenges include:
-	Reliance on Inefficient Methods: Conventional data collection is labor-intensive, primarily depending on slow ground checks.
-	Data Inaccuracies: Secondary data relies on open-source multispectral imagery, which is frequently inaccurate, obscured by clouds, and prone to classification errors like aquaculture ponds
-	Scale and Logistical Limitations: Scarce data limits mapping scales to 1:25,000, and updating annual spatial data across Indonesia's vast area remains highly difficult.

Developing a more **advanced and accessible** mangrove monitoring system is therefore essential. **High-quality Earth Obersvation** data can support targeted rehabilitation planning, improve biomass estimation, and strengthen blue carbon assessment, helping Indonesia protect its coastal ecosystems while advancing climate and resilience initiatives.


#### Problem Statement <!--{ style="font-size:2.0rem;opacity:1;margin-top:1rem; color:Navy" }-->
Existing monitoring methods rely heavily on **conventional, labor-intensive ground checks and open-source multispectral imagery**, which are frequently affected by **cloud cover and inaccuracies**. Furthermore, the scarcity of **reliable secondary data** and Indonesia’s large geographic area pose significant challenges when updating spatial data annually. 
**Consequently, current mangrove monitoring remains limited, featureless, and inaccessible, failing to provide the robust, up-to-date spatial data required to prevent coastal erosion.**


## Objectives <!--{ style="font-size:1.5rem;opacity:1;margin-top:1rem; color:Navy" }-->
**Primary Objective:** 
Mapping the **Multi-temporal analysis of mangrove gain/loss in Kuala Selat (Riau) and Pangpang Bay (East Java) using Logistic Model Tree (LMT)** to get the Mangrove Change Map (Gain and Loss) that is derived from SAR and multispectral band Satellite, highlighting areas of mangrove degradation and restoration potential in **Kuala Selat (Riau)** and **Pangpang Bay (East Java)**. 


## Case Study <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"s2-cloudless-2025","title":"Sentinel-2 Cloudless 2025"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2025_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"labels","title":"Labels"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' center=[103.706861,0.183472] zoom="8" animationOptions="{duration:500}" }-->
##### Kuala Selat 
**Kuala Selat** (0°11'00.5"N 103°42'24.7" E) is located in Riau Province, along the eastern coastline in Indragiri Hilir Regency on Sumatra Island.  Kuala Selat has a coastal landform with high salinity levels in the erosion area. The land cover in this area **is dominated by mangrove plants**, open fields, and coconut plantations, which are now **threatened by sea erosion**. 
Kuala Selat experiences intensive abrasion and year-round seawater intrusion, making it a prime example of a mangrove zonation that critically lacks biodiversity and requires urgent monitoring. Addressing these environmental vulnerabilities is vital, as the area is expected to support coconut plantations, which are the primary livelihood and economic commodity for communities throughout Riau Province.
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/02.%20Study%20Area%20Map%20Kuala%20Selat.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;"  /> 
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"> <b>Figure [1].</b> Study Area Map of Kuala Selat </p> 
</div>

### <!--{ layers='[{"type":"Tile","properties":{"id":"s2-cloudless-2025","title":"Sentinel-2 Cloudless 2025"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2025_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"labels","title":"Labels"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' center=[114.346111,-8.523806] zoom="12" animationOptions="{duration:500}" }-->
##### Pangpang Bay 
**Pangpang Bay** (8°31'25.7"S 114°20'46.0" E) is located in the easternmost part of East Java Province in a regency called Banyuwangi. With just a 30 km radius from Bali Island, Pangpang Bay has been designated as an Essential Ecosystem Area by the existence of an aquaculture pond based on the Decree of the Governor of East Java Number 188/338/KPTS/013/2020 concerning Essential Ecosystem Areas. It has at least 18 types of true mangrove biodiversity dominated by Ceriops tagal, Rhizophora apiculata, Bruguiera gymnorrhiza, and Rhizophora mucronata. This biodiversity-rich area is a bay that has the characteristic of calm water, but is still influenced by the ebb and flow of seawater at least twice a day.
This site serves as a valuable comparative area for Kuala Selat, showcasing a prime example of complex mangrove biodiversity successfully coexisting with human livelihoods like aquaculture. However, because the area still has the potential to experience abrasion and seawater intrusion, ongoing observation is essential. The primary goal of this monitoring is to identify exactly where and how mangrove biodiversity and community livelihoods can sustainably thrive together within these aquaculture ponds.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/02.%20Study%20Area%20Map%20Pangpang%20Bay.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;"  /> 
<p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;"> <b>Figure [2].</b> Study Area Map of Pangpang Bay </p>
</div>



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
 


