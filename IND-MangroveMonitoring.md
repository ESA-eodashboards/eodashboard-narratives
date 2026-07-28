---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
official: true
collections: collectionIdentifier1, collectionIdentifier2
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
By integrating high-resolution Synthetic Aperture Radar (SAR) data with optical satellite imagery, this research addresses the shortcomings of conventional monitoring methods: 


| Name | Provider | Resolution | Temporal Coverage | Purpose |
|---|---|---|---|---|
| ALOS-2 L2.2 ScanSAR | JAXA (Japan Aerospace Exploration Agency) | Primary L-band SAR dataset (60–100 m) | 2021 and 2024 | Used for large-scale mangrove detection, area calculation, and change analysis. Its high penetration capability makes it suitable for dense mangrove canopies. |
| Sentinel-2 L2A | Copernicus | Visible bands (10 m) | 2021 and 2024 | Used for validation of ScanSAR-derived products and visualization of the study area. |
| Indonesia’s National Mangrove Map | Ministry of Forestry, Indonesia | - | 2021 and 2024 | Used to compare the total mangrove area with the ALOS-2 analysis. |
| Indonesia’s administrative boundary | Geospatial Information Agency (BIG), Indonesia | 1:25,000 scale | 2021 and 2024 | Used to divide the ALOS-2, Sentinel-2, and PMN datasets according to Indonesia’s official administrative boundaries. |

The methodology leverages a multi-sensor approach, integrating ALOS PALSAR-2 radar data with Sentinel-2 Level 2A optical imagery. Using GIS geoprocessing tools and raster functions, the data is preprocessed by applying a 5x5 Frost speckle filter to extract HH and HV backscattering coefficients, and by calculating a Mangrove Vegetation Index (MVI) from Sentinel-2 imagery to construct the foundational training datasets.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/03.%20WorkflowDiagramGeneral.png?raw=true" style="max-width: 100%; width: 1000px; height: auto;" alt="Analysis workflow" /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 10px;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/03.%20WorkflowDiagramTechnical.png?raw=true" style="max-width: 100%; width: 1000px; height: auto;" alt="Analysis workflow" /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 10px;">
<b>Figure [3].</b> Complete methodology workflow from data acquisition to analysis. </p> 
</div>
Classification is driven by a Decision Tree utilizing a sequential Logistic Model Tree. First, Rule 1 applies radar backscattering (HH > -15.5 and HV > -17.9) to separate combined forest cover from non-forest areas (rice paddies and water bodies). Next, Rule 2 applies the optical MVI filters for values strictly between 4.5 and 20 to successfully isolate mangrove forests from terrestrial forests. The spatial processing steps are structured as a technical workflow within a GIS environment like ArcGIS Pro. This operational setup, "Raster Functions," for on-the-fly data processing and index calculations, alongside established "Geoprocessing Toolboxes" to handle heavier analytical tasks, such as filtering, dataset generation, and decision tree logic. Custom "Symbology Features" are then applied to the resulting layers to visually categorize the distinct backscattering ranges and classification outputs. 
By executing this automated workflow, the model generates independent mangrove distribution maps for specific years, such as 2021 and 2024. Comparing these temporal classifications ultimately produces a final Mangrove Change Map that identifies precise areas of mangrove gain and loss to support continuous ecosystem monitoring.


## Results
To provide comprehensive visualizations of the main findings and supporting spatial analyses, this project generated a series of multi-temporal classification maps for two contrasting coastal environments: Kuala Selat and Pangpang Bay. The spatial outputs include baseline Sentinel-2 Mangrove Vegetation Index (MVI) maps, alongside ALOS PALSAR-2 backscattering reclassification maps for both HH and HV polarizations across the years 2021 and 2024. The core visualizations, however, are the "Rule 2" classification maps; these intersect the radar and optical datasets to visually delineate the strictest, "true positive" mangrove extents. Furthermore, to support these algorithmic findings with foundational background information, high-resolution optical basemaps are included to facilitate a robust visual validation process, allowing for the direct interpretation of mangrove textures and site associations against the processed data.

<div style="display: flex; flex-direction: column; align-items: center; margin: 5px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/kualaselat_HH_HV_MVI_2024.png?raw=true" style="max-width: 100%; width: 900px; height: auto;" alt="Analysis workflow" /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure [4]. (a,b)</b> ALOS-2 HH and HV Reclassification after backscattering coefficient process and speckle filtering. <b>(c)</b> Mangrove Vegetation Index from Sentinel-2A Vectorization</p> 
</div>
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/kualaselat_Reclassification.png?raw=true" style="max-width: 100%; width: 800px; height: auto;"/> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure [5].</b> ALOS-2 different combinations reclassification results in Kuala Selat for 2021 and 2024 </p> 
</div>
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
</div>
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/Pangpang_Reclassification.png?raw=true" style="max-width: 100%; width: 800px; height: auto;"/> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure [6].</b> ALOS-2 different combinations reclassification results in Pangpang Bay for 2021 and 2024 </p> 
</div>
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
To systematically quantify the spatial results, the geodetically measured areas were extracted and formatted into comparative statistical tables and clustered column charts. These quantitative visualizations detail the total mangrove area in hectares, plotting the results side-by-side across four specific indicators: the baseline Indonesia Mangrove Map (PMN), the optical MVI, Rule 2 (HH + MVI), and Rule 2 (HV + MVI). By mapping these variables against the 2021 and 2024 timelines for both study sites, the charts explicitly illustrate the localized trajectories of mangrove decline. Ultimately, these graphs provide the necessary statistical backing to demonstrate how the strict, multi-sensor methodology effectively filters out the "false positives" and overestimations frequently found in conventional national mapping efforts.

</div>
<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;"> 
<img src="https://github.com/phkh1366/eoxhub-related/blob/main/AreaComparsion.png?raw=true" style="max-width: 100%; width: 400px; height: auto;"  /> 
<p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 5px;"> <b>Figure [7].</b> Mangrove Areas Comparison 2021 and 2024 Chart at Kuala Selat and Pangpang Bay. </p> 
</div>


## Limitations
The limitations of the current work include, but are not limited to:
1.	The calculated mangrove area of “Rule 2: HH + MVI” and “Rule 2: HV and MVI” in our analysis is notably lower than the figures reported in the National Mangrove Map (PMN) due to the implementation of a significantly stricter classification methodology. To ensure baseline geodetic accuracy, the total area was precisely measured via ArcGIS Calculate Geometry using a World Cylindrical projected coordinate system. The core variance from the Rule 2 combination is that integrating SAR HH or HV with optical MVI, which is designed specifically to enhance the detection of "true positive" or ground truth mangroves. While standalone optical indices like the MVI yield statistics closer to the National Map, both often inadvertently capture "false positives" such as aquaculture ponds, cloud-shrouded areas, and other classification errors. By incorporating SAR data, which actively measures physical structure, volume, and moisture rather than just surface reflectance, our model successfully penetrates cloud cover and detects hidden degradation at lower canopies. Ultimately, this dual-sensor approach filters out the inaccuracies inherent in optical-only data, resulting in a highly accurate, albeit smaller, calculation of true mangrove extent.
2.	The difference value of mangrove area from calculated mangrove area, MVI, and PMN can also occur due to the resolution difference between Sentinel-2 (which is used as a based of PMN and MVI) and ALOS-2 SCANSAR type. Sentinel-2 has a resolution of 10 m in the visible band, while ALOS-2 SCANSAR spatial resolution varies from 60m to 100m, depending on the swath length. 


## Future Development
The future development will include investigating the use of time-series datasets to detect coastal erosion/accretion changes in Kuala Selat (Riau) and Pangpang Bay (East Java), and comparing shoreline positions or backscatter boundaries across years. The outcome, Coastal Erosion and Accretion Map, will visualize shoreline changes and backscatter boundary shifts across multiple years.


## References
Spatial Data Processing Methodology:
-	Pham, T. D., Bui, D. T., Yoshino, K., & Le, N. N. (2018). Optimized rule-based logistic model tree algorithm for mapping mangrove species using ALOS PALSAR imagery and GIS in the tropical region. Environmental earth sciences, 77(5), 159.
-	Baloloy, A. B., Blanco, A. C., Ana, R. R. C. S., & Nadaoka, K. (2020). Development and application of a new mangrove vegetation index (MVI) for rapid and accurate mangrove mapping. ISPRS Journal of Photogrammetry and Remote Sensing, 166, 95-117.
-	Pham, T. D., & Yoshino, K. (2012, November). Mangrove analysis using ALOS imagery in Hai Phong City, Vietnam. In Remote Sensing of the Marine Environment II (Vol. 8525, pp. 161-168). SPIE.
-	Pham, T. D., & Yoshino, K. (2016, June). Characterization of mangrove species using ALOS-2 PALSAR in Hai Phong city, Vietnam. In IOP Conference Series: Earth and Environmental Science (Vol. 37, No. 1, p. 012036). IOP Publishing.
-	Pham, T. D., Bui, D. T., Yoshino, K., & Le, N. N. (2018). Optimized rule-based logistic model tree algorithm for mapping mangrove species using ALOS PALSAR imagery and GIS in the tropical region. Environmental earth sciences, 77(5), 159.
-	Sari, S. P., & Rosalina, D. (2016). Mapping and monitoring of mangrove density changes on tin mining area. Procedia Environmental Sciences, 33, 436-442.
-	Tien Bui, D., Tuan, T. A., Klempe, H., Pradhan, B., & Revhaug, I. (2016). Spatial prediction models for shallow landslide hazards: a comparative assessment of the efficacy of support vector machines, artificial neural networks, kernel logistic regression, and logistic model tree. Landslides, 13(2), 361-378.
-	Pham, T. D., & Yoshino, K. (2017). Aboveground biomass estimation of mangrove species using ALOS-2 PALSAR imagery in Hai Phong City, Vietnam. Journal of Applied Remote Sensing, 11(2), 026010-026010.
-	Darmawan, S., Takeuchi, W., Vetrita, Y., Wikantika, K., & Sari, D. K. (2015). Impact of topography and tidal height on ALOS PALSAR polarimetric measurements to estimate aboveground biomass of mangrove forest in Indonesia. Journal of Sensors, 2015(1), 641798.
-	Darmawan, S., Takeuchi, W., Vetrita, Y., Winarso, G., Wikantika, K., & Sari, D. K. (2014, June). Characterization of mangrove forest types based on ALOS-PALSAR in overall Indonesian archipelago. In IOP Conference Series: Earth and Environmental Science (Vol. 20, No. 1, p. 012051). IOP Publishing.
-	Pham, T. D., & Yoshino, K. (2016, June). Characterization of mangrove species using ALOS-2 PALSAR in Hai Phong city, Vietnam. In IOP Conference Series: Earth and Environmental Science (Vol. 37, No. 1, p. 012036). IOP Publishing.
-	Pham, T. D., & Yoshino, K. (2016, June). Characterization of mangrove species using ALOS-2 PALSAR in Hai Phong city, Vietnam. In IOP Conference Series: Earth and Environmental Science (Vol. 37, No. 1, p. 012036). IOP Publishing.
-	Pham, T. D., & Yoshino, K. (2012, November). Mangrove analysis using ALOS imagery in Hai Phong City, Vietnam. In Remote Sensing of the Marine Environment II (Vol. 8525, pp. 161-168). SPIE.
Datasets:
-	Rosenqvist, A., Shimada, M., Suzuki, S., Ohgushi, F., Tadono, T., Watanabe, M., ... & Aoki, E. (2014). Operational performance of the ALOS global systematic acquisition strategy and observation plans for ALOS-2 PALSAR-2. Remote Sensing of Environment, 155, 3-12.
-	Murray, N.J., Worthington, T.A., Bunting, P., Duce, S., Hagger, V., Lovelock, C.E., Lucas, R., Saunders, M.I., Sheaves, M., Spalding, M., Waltham, N.J., Lyons, M.B. (2022). High-resolution mapping of losses and gains of Earth's tidal wetlands. Science. doi:10.1126/science.abm9583
-	 Government of Indonesia. (2019). Law Number 27 of 2025 concerning the protection and management of mangrove ecosystems. State Gazette of the Republic of Indonesia, 2025 Number 27.
-	Clark Labs. (2015). Clark Labs | Geospatial Software for Monitoring and Modeling the Earth System [online]. Clark Labs. Available from: http://www.clarklabs.org 
Scope Area:
-	Raharja, A. B., Widigdo, B., & Sutrisno, D. (2014). Kajian potensi kawasan mangrove di kawasan pesisir Teluk Pangpang, Banyuwangi. Depik, 3(1).
-	Sulastini, D., Dyah, S. M. W., Ssusilo, U., & Widiastuti, R. R. W. (2011). Seri Buku Informasi dan Potensi Mangrove Taman Nasional Alas Purwo. Balai Taman Nas. Alas Purwo. Bayuwangi.
-	Luthfiana, N., & Zamaya, Y. (2025, June). Alternative livelihoods for communities affected by coastal abrasion disasters case study on Kuala Selat village, Kateman district, Indragiri hilir regency, Piau province. In IOP Conference Series: Earth and Environmental Science (Vol. 1518, No. 1, p. 012020). IOP Publishing.
-	Lekatompessy, R. L., & Maturbongs, E. E. (2021). Faktor-Faktor Dalam Upaya Mengatasi Abrasi Di Pesisir Pantai Di Wilayah Kabupaten Merauke. Dialogue: Jurnal Ilmu Administrasi Publik, 3(1), 1-13.
-	Adhitama, S. Y., Puspitasari, D., Budiman, L. S., & Musthofa, A. (2025). Exploring Dynamics and Effective Strategies for Tidal Flood Risk Reduction in Indonesia's Coastal Cities. ASEAN Journal on Science and Technology for Development, 42(2), 6.
-	Arifanti, V. B., Kauffman, J. B., Subarno, Ilman, M., Tosiani, A., & Novita, N. (2022). Contributions of mangrove conservation and restoration to climate change mitigation in Indonesia. Global Change Biology, 28(15), 4523-4538.

 


