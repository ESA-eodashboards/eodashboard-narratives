---
cover-image: https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Mangrove%2C_Lamongan_Regency%2C_East_Java%2C_Indonesia_1.jpg/1200px-Mangrove%2C_Lamongan_Regency%2C_East_Java%2C_Indonesia_1.jpg?20170630152721
date: 2025-01-01
theme: theme_name
tags: some,tags

---

# Mangroves for Coastal Erosion Control: Harnessing Satellite Imagery for Effective Monitoring <!--{ as="img" mode="hero" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Mangrove%2C_Lamongan_Regency%2C_East_Java%2C_Indonesia_1.jpg/1200px-Mangrove%2C_Lamongan_Regency%2C_East_Java%2C_Indonesia_1.jpg?20170630152721" }-->
### Authors: Novie Indriasari¹, Alit Aji², Buchari³, Pratondi Ario Seno Sudiro⁴, Dede Dirgahayu¹, Garda K Yustisiansyah⁵ <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
¹ National Research and Innovation Agency
² Ministry of Agrarian and Spatial Planning/National Land Agency
³ IPB University
⁴ Maritime Security Agency
⁵ Ministry of Forestry - Mangrove for Coastal Resilience Project

#
*This story is based on results from the [ALOS-2 Ideathon Workshop at APRSAF in December 2025](https://philsa.gov.ph/news/philsa-jaxa-host-alos-2-ideathon-workshop-to-tackle-environmental-social-challenges/), organised by the [Japan Aerospace Exploration Agency (JAXA)](https://global.jaxa.jp/). The study, dedicated to **Mangroves and the harnessing of satellite imagery for effective monitoring** was developed by participants from the following organizations:*

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Main_Logo_of_National_Research_and_Innovation_Agency_of_Indonesia.svg/250px-Main_Logo_of_National_Research_and_Innovation_Agency_of_Indonesia.svg.png" alt="Ca' Foscari" height="80" style="margin: 0 15px;"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/The_Agrarian_Affairs_and_Spatial_Planning_%28Indonesia%29.svg/1200px-The_Agrarian_Affairs_and_Spatial_Planning_%28Indonesia%29.svg.png" alt="NOC" height="80" style="margin: 0 15px;"/>
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUjojp4CFC36lejnD_BogDA8PvyzDu04FwDA&s" alt="BAS" height="80" style="margin: 0 15px;"/>
	  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxQuzsCzTpob6VQTB4hvJ1_LuZCN5wPAgkow&s" alt="BAS" height="80" style="margin: 0 15px;"/>
		  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7HHDDe-VOVlgZsP4QhvArszJJXn97D_m0Kw&s" alt="BAS" height="80" style="margin: 0 15px;"/>
</p>



## Challenge
Coastal erosion is a growing threat to many regions around the world, especially in areas that rely on the health of their shorelines for livelihood and ecological stability. The destruction of natural coastal buffers, such as mangrove forests, has exacerbated this issue, leaving coastlines vulnerable to the forces of wind, waves, and rising sea levels. As climate change accelerates, the urgency to protect and restore mangrove ecosystems has never been more critical.

Mangroves, with their complex root systems, provide a natural barrier against coastal erosion by stabilizing sediments and reducing the impact of tidal forces. These coastal forests are highly efficient in trapping sediment, which helps to build up and strengthen shorelines, preventing the encroachment of the sea. Beyond their role in erosion control, mangroves also support biodiversity, enhance carbon sequestration, and provide essential resources for local communities.

#### Problem Statement
Indonesia faces a critical challenge in protecting its extensive mangrove areas from coastal erosion. The current situation can be characterized by three interconnected issues:

Coastal erosion threatens mangrove area → Indonesia needs advance mangrove monitoring system → Indonesia's current National Mangrove Map (PMN) still has several limitations


###### Current limitations of mangrove monitoring:

Mangrove monitoring still relies heavily on ground surveys and cloud-prone open-source imagery, often limiting map detail to 1:25,000. Updating data annually is challenging over large areas, leaving monitoring efforts temporally sparse, structurally shallow, and difficult to access for comprehensive analysis. Integrating satellite imagery with field observations improves accuracy and insight, helping identify local drivers of mangrove loss and coastal erosion. This combined approach supports more effective restoration and protection strategies. **Mangroves are vital for coastal resilience**, and remote sensing provides a powerful way to monitor, protect, and restore these ecosystems in the face of climate change.

## Objectives
* Primary Objective: Mapping the Multi-temporal analysis of mangrove gain/loss in Kuala Selat (Riau) and Pangpang Bay (East Java) using Logistic Model Tree (LMT).

* Next Step: Investigating the use of time-series datasets to detect coastal erosion/accretion changes in Kuala Selat (Riau) and Pangpang Bay (East Java), and comparing shoreline positions or backscatter boundaries across years.
* Expected Outcomes
Mangrove Change Map (Gain and Loss) — derived from SAR and multispectral band Satellite, highlighting areas of mangrove degradation and restoration potential in Kuala Selat (Riau) and Pangpang Bay (East Java).
Stakeholder Analysis  The mangrove monitoring system involves a complex network of stakeholders working together to leverage satellite data for coastal ecosystem management:


## Use Case <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"nceo_africa_2017;:;AGB_map_2017v0m_COG;:;nceo_africa_2017;:;EPSG:3857","title":"nceo_africa_2017"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://nasa-maap-data-store/file-staging/nasa-map/nceo-africa-2017/AGB_map_2017v0m_COG.tif&resampling_method=nearest&bidx=1&colormap_name=gist_earth_r&rescale=0.0,400.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="8.764622104553196" center=[103.24623176388639,0.1368563282370303] projection="" animationOptions={duration:500}}-->
#### Kuala Selat, Riau
**Period of Interest: 2021 & 2024**
Located in Riau province, Kuala Selat represents a significant mangrove ecosystem along the eastern coast of Sumatra. This region experiences substantial tidal influence and coastal dynamics, making it an ideal case study for monitoring mangrove response to erosion pressures.





### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"nceo_africa_2017;:;AGB_map_2017v0m_COG;:;nceo_africa_2017;:;EPSG:3857","title":"nceo_africa_2017"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://nasa-maap-data-store/file-staging/nasa-map/nceo-africa-2017/AGB_map_2017v0m_COG.tif&resampling_method=nearest&bidx=1&colormap_name=gist_earth_r&rescale=0.0,400.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="10.935879818894897" center=[114.31582537876655,-8.37994420828106] projection="" animationOptions={duration:500}}-->
#### Pangpang Bay, East Java
Period of Interest: 2021 & 2024
Pangpang Bay in East Java showcases different coastal conditions with distinct mangrove community structures. The bay's semi-enclosed nature provides a contrasting environment for comparative analysis of mangrove dynamics.
<div style="text-align: center;"> <img src="https://i0.wp.com/www.forestsnews.org/wp-content/uploads/2025/10/52208703239_ff1aecaaa4_k.jpg?fit=623%2C415&ssl=1" width="800"/> <p><b>Figure 2.</b> Study area locations showing Pangpang Bay (East Java) within Indonesia's extensive coastal mangrove belt.</p> </div>



## Data and Methods
### Datasets
This study utilizes high-resolution SAR (Synthetic Aperture Radar) data combined with optical satellite imagery to overcome the limitations of traditional monitoring approaches:

* 🛰️ SAR Data	ALOS-2 L2.2 SCANSAR	Primary radar dataset for mangrove detection	~100m	2021 & 2024
ALOS-2 PALSAR-2 STRIPMAP Level 2.1	High-resolution SAR (if available)	~10m	2021 & 2024
* 🌍 Optical Data	Visual Band Open Source Satellite	Multispectral imagery for validation	Variable	2021 & 2024
* 📍 Reference Data	Indonesia Mangrove Map (PMN)	National baseline mangrove coverage	1:25,000	Current
Advantages of SAR Data:

### Methodology Workflow
The analysis employs a multi-stage approach combining SAR and optical satellite data with machine learning classification techniques. The workflow begins with data acquisition and preprocessing, where ALOS PALSAR-2 2.2 time-series data is collected alongside Sentinel-2 Level 2A optical imagery. The SAR data undergoes speckle filtering and front-end preprocessing, while backscattering coefficients for both HH and HV polarizations are extracted. Concurrently, the Sentinel-2 data is processed to derive the Mangrove Vegetation Index (MVI) threshold, which serves as an additional discriminatory parameter for mangrove identification.
The core classification methodology utilizes a Logistic Model Tree (LMT) approach, which integrates decision tree logic with logistic regression at each node. Training datasets are first generated from known mangrove and non-mangrove areas, incorporating both ground-truth data and expert knowledge. These training samples are then used to develop a Decision Tree Method that generates rule sets specifically tailored for mangrove classification.
<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;"> <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/Comunity_led_JAXA/Mangroves/methodology_mangrove_story.png?raw=true" style="max-width: 100%; width: 1000px; height: auto;" alt="Analysis workflow" /> <p style="text-align: center; font-size: 1.2em; margin-top: 10px;"> <b>Figure 3.</b> Complete methodology workflow from data acquisition through Logistic Model Tree classification to mangrove change detection. </p> </div>
The LMT implements a hierarchical classification structure with two primary decision rules. Rule 1 evaluates backscattering values from the HH and HV polarizations of ALOS-2 PALSAR data, using threshold criteria (σ°HH > 15.5 and σ°HV > 17.6) to distinguish between non-highly agricultural, water bodies, and other land cover types versus potential terrestrial forest and mangrove forest. Pixels meeting these initial backscatter criteria proceed to Rule 2, which further refines the classification by incorporating the MVI from Sentinel-2 data and considering additional HV or HH polarization signatures with a 20dB upper threshold. This second rule successfully separates terrestrial forest from mangrove forest based on the combined spectral and structural characteristics unique to mangrove ecosystems.

Following the Decision Tree Classifier application, separate mangrove maps are generated for both 2021 and 2024 using their respective satellite acquisitions. The final stage involves change detection analysis, where the two temporal maps are compared pixel-by-pixel to produce a comprehensive Mangrove Change Map. This output identifies areas of mangrove gain (newly established mangrove areas) and loss (degraded or converted mangrove areas) over the three-year period, providing critical insights into coastal ecosystem dynamics and the effectiveness of mangroves in coastal erosion control.





## Results
#### Initial findings: Kuala Selat, Riau - 2024 Classification Results
The initial analysis of Kuala Selat demonstrates the effectiveness of combining different polarization data and classification rules for mangrove detection:

<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;"> <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/Comunity_led_JAXA/Mangroves/initial_findings.png?raw=true" style="max-width: 100%; width: 1200px; height: auto;" alt="Kuala Selat classification results" /> <p style="text-align: center; margin-top: 10px;"> <b>Figure 4.</b> Classification results for Kuala Selat 2024 showing (left) HV polarization reclassification, (center) HH polarization reclassification, and (right) mangrove extent overview with MVI classification. </p> </div
ALOS PALSAR Reclassification Results
HV Polarization Results:

Successfully identified dense mangrove canopy structures
Captured mangrove extent along coastal fringes
Distinguished between mangrove and terrestrial forest based on backscatter intensity
HH Polarization Results:

Enhanced detection of mangrove structural complexity
Improved discrimination of mangrove from other vegetation types
Complementary information to HV polarization
Quantitative Results - Kuala Selat 2024
No	Data Source	Mangrove Area (Ha)
1	Indonesia Mangrove Map	47,901
2	Rule 1: HV	34,447
3	Rule 2: HH + MVI	32,141
4	Rule 2: HV + MVI	23,876
<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;"> <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/Comunity_led_JAXA/Mangroves/initial_findings_2.png?raw=true" style="max-width: 100%; width: 1000px; height: auto;" alt="Combined classification rules results" /> <p style="text-align: center; margin-top: 10px;"> <b>Figure 5.</b> Comparison of classification approaches: (left) Rule 2: HV + MVI Classification and (right) Rule 2: HH + MVI Classification for 2024. </p> </div>


#### Explanation of Area Differences
Differences in detected mangrove area across methods highlight several factors:

* **1) Data Sources**:
National mangrove maps show broader coverage because they integrate multiple datasets, while SAR and optical interpretations vary by resolution and methodology.

* **2) Sensor Sensitivity**:
HH polarization mainly detects woody vegetation in wetter conditions, whereas HV captures a wider range of vegetation structures, leading to area differences.

* **2) Classification Rules**:
Combining HH or HV with the Mangrove Vegetation Index (MVI) applies stricter criteria, reducing mapped area but improving mangrove specificity and lowering false positives.

* **3)Cloud Coverage**:
ALOS SAR penetrates clouds more effectively than optical sensors. Seasonal differences and cloud masking in optical data affect coverage and accuracy.

* **4) Data Combination Accuracy**:
Certain rule–data combinations (e.g., Rule 2 with multi-temporal optical data) are better suited for monitoring, while ALOS data generally performs better in cloudy regions.
## Next Steps
The project progresses from multi-sensor analysis to operational mangrove monitoring between Oct 2024 and Mar 2025, integrating ALOS PALSAR-2 SAR and Sentinel-2 optical data to improve mangrove classification and mapping. Key outputs include processed datasets, multi-temporal mangrove maps, visualizations, and scientific publications. Future work expands toward coastal change detection, higher-resolution time series, climate data integration, near-real-time monitoring systems, and national-scale application across Indonesia.

## <!--{ as="div" }--> Open Science

| **Name**                                                                                          | **Type**          | **Agency / Provider**                     | **Description / Usage**                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[ALOS-2 L2.2 PALSAR-2 SCANSAR](https://www.eorc.jaxa.jp/ALOS/en/palsar_fnf/fnf_index.htm)**     | Dataset (SAR)     | JAXA (Japan Aerospace Exploration Agency) | Primary L-band SAR dataset (~100 m) used for large-scale mangrove detection and change analysis. High penetration capability makes it suitable for dense mangrove canopies. Temporal coverage: 2021 & 2024. |
| **ALOS-2 PALSAR-2 STRIPMAP Level 2.1**                                                            | Dataset (SAR)     | JAXA                                      | High-resolution L-band SAR data (~10 m), used when available for detailed mangrove structure analysis and validation of SCANSAR-derived products. Temporal coverage: 2021 & 2024.                           |
| **Visual Band Open Source Satellite Data**                                                        | Dataset (Optical) | Multiple Open Providers                   | Multispectral optical imagery used for visual interpretation and validation of mangrove extent and condition. Resolution varies by sensor. Temporal coverage: 2021 & 2024.                                  |
| **Indonesia Mangrove Map (PMN)**                                                                  | Reference Dataset | Government of Indonesia                   | National baseline mangrove coverage map at 1:25,000 scale. Used as reference data for validation and comparison of detected mangrove extent. Current version.                                               |
| **[Sentinel-1 SAR](https://sentinel.esa.int/web/sentinel/missions/sentinel-1)**                   | Dataset (SAR)     | ESA (European Space Agency)               | C-band SAR GRD data at 10 m resolution. Provides complementary radar information for moisture conditions and coastal dynamics relevant to mangrove ecosystems.                                              |
| **[Sentinel-2 MSI](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)**                   | Dataset (Optical) | ESA (European Space Agency)               | Multispectral optical imagery at 10 m resolution used for land cover discrimination and visual validation of mangrove areas.                                                                                |
| **[ECMWF ERA5 Reanalysis](https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5)** | Dataset (Climate) | ECMWF                                     | Climate reanalysis data providing environmental context (precipitation, temperature anomalies) supporting interpretation of mangrove dynamics.                                                              |

## References
* Pham, T. D., Yoshino, K., & Bui, D. T. (2018). Biomass estimation of Sonneratia caseolaris (l.) Engler at a coastal area of Hai Phong city (Vietnam) using ALOS-2 PALSAR imagery and GIS-based multi-layer perceptron neural networks. GIScience & Remote Sensing, 55(3), 329-353.
* Balakrishnan, N., et al. (2020). Machine learning approaches for mangrove mapping using remote sensing data. Remote Sensing Applications: Society and Environment, 18, 100305.
Kuenzer, C., Bluemel, A., Gebhardt, S., Quoc, T. V., & Dech, S. (2011). Remote sensing of mangrove ecosystems: A review. Remote Sensing, 3(5), 878-928.

* Ghorbanian, A., Kakooei, M., Amani, M., Mahdavi, S., Mohammadzadeh, A., & Hasanlou, M. (2021). Improved land cover map of Iran using Sentinel imagery within Google Earth Engine and a novel automatic workflow for land cover classification using migrated training samples. ISPRS Journal of Photogrammetry and Remote Sensing, 167, 276-288.

* Giri, C., Ochieng, E., Tieszen, L. L., et al. (2011). Status and distribution of mangrove forests of the world using earth observation satellite data. Global Ecology and Biogeography, 20(1), 154-159.

* Murdiyarso, D., Purbopuspito, J., Kauffman, J. B., Warren, M. W., Sasmito, S. D., Donato, D. C., ... & Kurnianto, S. (2015). The potential of Indonesian mangrove forests for global climate change mitigation. Nature Climate Change, 5(12), 1089-1092.
This study is part of Indonesia's efforts to enhance coastal resilience through improved mangrove ecosystem monitoring and management, supporting both biodiversity conservation and climate change adaptation strategies.

