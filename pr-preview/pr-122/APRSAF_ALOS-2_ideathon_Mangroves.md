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

Conventional data collection still primarily depending on ground checks
Secondary data rely on multispectral Open-Source imagery, often cloud-covered and inaccurate
Map scale is limited to 1:25,000 due to scarce secondary data
Difficulties when updating annual spatial data due to wide area
Result: Mangrove Monitoring remains:

LIMITED in temporal coverage
FEATURELESS in detailed characteristics
INACCESSIBLE for comprehensive analysis
The integration of satellite data with ground-level observations enhances the accuracy of monitoring efforts. By combining satellite imagery with field surveys, experts can better understand the local factors influencing mangrove survival and coastal erosion. This combined approach supports more targeted and effective interventions to restore mangrove habitats and prevent further erosion.
In conclusion, mangrove ecosystems are vital for combating coastal erosion, and satellite imagery plays a crucial role in monitoring their health and effectiveness. With the power of remote sensing technology, we can protect and restore mangrove forests, safeguard coastal communities, and mitigate the devastating impacts of climate change.

## Objectives
* Primary Objective: Mapping the Multi-temporal analysis of mangrove gain/loss in Kuala Selat (Riau) and Pangpang Bay (East Java) using Logistic Model Tree (LMT).

* Next Step: Investigating the use of time-series datasets to detect coastal erosion/accretion changes in Kuala Selat (Riau) and Pangpang Bay (East Java), and comparing shoreline positions or backscatter boundaries across years.
* Expected Outcomes
Mangrove Change Map (Gain and Loss) — derived from SAR and multispectral band Satellite, highlighting areas of mangrove degradation and restoration potential in Kuala Selat (Riau) and Pangpang Bay (East Java).
Stakeholder Analysis  The mangrove monitoring system involves a complex network of stakeholders working together to leverage satellite data for coastal ecosystem management:


## Use Case <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"nceo_africa_2017;:;AGB_map_2017v0m_COG;:;nceo_africa_2017;:;EPSG:3857","title":"nceo_africa_2017"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://nasa-maap-data-store/file-staging/nasa-map/nceo-africa-2017/AGB_map_2017v0m_COG.tif&resampling_method=nearest&bidx=1&colormap_name=gist_earth_r&rescale=0.0,400.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="8.764622104553196" center=[103.24623176388639,0.1368563282370303] projection="" animationOptions={duration:500}}-->
### Kuala Selat, Riau
**Period of Interest: 2021 & 2024**
Located in Riau province, Kuala Selat represents a significant mangrove ecosystem along the eastern coast of Sumatra. This region experiences substantial tidal influence and coastal dynamics, making it an ideal case study for monitoring mangrove response to erosion pressures.

<!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"nceo_africa_2017;:;AGB_map_2017v0m_COG;:;nceo_africa_2017;:;EPSG:3857","title":"nceo_africa_2017"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://nasa-maap-data-store/file-staging/nasa-map/nceo-africa-2017/AGB_map_2017v0m_COG.tif&resampling_method=nearest&bidx=1&colormap_name=gist_earth_r&rescale=0.0,400.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="10.935879818894897" center=[114.31582537876655,-8.37994420828106] projection="" animationOptions={duration:500}}-->
### Pangpang Bay, East Java
Period of Interest: 2021 & 2024
Pangpang Bay in East Java showcases different coastal conditions with distinct mangrove community structures. The bay's semi-enclosed nature provides a contrasting environment for comparative analysis of mangrove dynamics.

<div style="text-align: center;"> <img src="https://raw.githubusercontent.com/placeholder/study-areas-map.jpg" width="800"/> <p><b>Figure 2.</b> Study area locations showing Kuala Selat (Riau) and Pangpang Bay (East Java) within Indonesia's extensive coastal mangrove belt.</p> </div>



## Data and Methods
Datasets
This study utilizes high-resolution SAR (Synthetic Aperture Radar) data combined with optical satellite imagery to overcome the limitations of traditional monitoring approaches:

Category	Dataset	Description	Resolution	Temporal Coverage
🛰️ SAR Data	ALOS-2 L2.2 SCANSAR	Primary radar dataset for mangrove detection	~100m	2021 & 2024
ALOS-2 PALSAR-2 STRIPMAP Level 2.1	High-resolution SAR (if available)	~10m	2021 & 2024
🌍 Optical Data	Visual Band Open Source Satellite	Multispectral imagery for validation	Variable	2021 & 2024
📍 Reference Data	Indonesia Mangrove Map (PMN)	National baseline mangrove coverage	1:25,000	Current
Advantages of SAR Data:

Cloud-penetrating capability ensures year-round monitoring
Sensitive to vegetation structure and moisture content
Day/night acquisition capability
Excellent for detecting mangrove presence through canopy characteristics
Methodology Workflow
<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;"> <img src="https://raw.githubusercontent.com/placeholder/methodology-workflow.jpg" style="max-width: 100%; width: 1000px; height: auto;" alt="Analysis workflow" /> <p style="text-align: center; font-size: 1.2em; margin-top: 10px;"> <b>Figure 3.</b> Complete methodology workflow from data acquisition through Logistic Model Tree classification to mangrove change detection. </p> </div>
1. Data Acquisition and Preprocessing
ALOS PALSAR 2.2 Data: Acquired dual-polarization SAR imagery covering study areas
Sentinel-2 Level 2A: Downloaded multispectral optical imagery for validation
Preprocessing Steps:
Radiometric calibration of SAR backscatter
Terrain correction using digital elevation models
Speckle filtering for noise reduction
Co-registration of multi-temporal images
2. Training Dataset Generation
Generated training samples from high-confidence mangrove and non-mangrove areas
Utilized existing National Mangrove Map as reference base
Validated training areas through visual interpretation and field knowledge
Created balanced training dataset representing various mangrove conditions
3. Logistic Model Tree (LMT) Classification
The study employs Logistic Model Tree (LMT) as the primary classification algorithm. LMT combines:

Decision Tree Structure:

[x] Backscattering Value (HH or HV ALOS-2 Palsar)
    ├─ RULE 1:
    │  If eps = N-S
    │  Or eps = 17-8
    ├─ Potential Forest / Land Unit (HV Polarity)
    │
    └─ RULE 2:
          If eps = S-E / E-S HH Polarity
          and OR (N)(SW)
          ├─ Potential Forest (Non-Mangrove)
          └─ Mangrove Forest
Key Features:

Integrates logistic regression models at tree nodes
Handles both HV and HH polarization data
Distinguishes between mangrove and non-mangrove forest based on backscatter patterns
Considers geographic orientation effects on backscatter
References:

[1] Pham et al. (2018) - Application of LMT for land cover classification
[2] Balakhrisynet al. (2020) - Mangrove mapping using machine learning
4. Decision Tree Classification
Applied Decision Tree Classifier using selected training criteria
Integrated both HV and HH polarization signatures
Generated preliminary mangrove/non-mangrove classifications
Optimized tree depth to prevent overfitting
5. Multi-temporal Change Analysis
Mangrove Map 2021: Generated from 2021 ALOS-2 data
Mangrove Map 2024: Generated from 2024 ALOS-2 data
Change Detection: Pixel-by-pixel comparison identifying:
Gain: Areas where mangrove appeared between 2021-2024
Loss: Areas where mangrove disappeared between 2021-2024
Stable: Areas maintaining mangrove coverage
6. Validation and Accuracy Assessment
Cross-validation with Sentinel-2 optical imagery
Comparison with existing National Mangrove Map (PMN)
Field verification data integration (where available)
Accuracy metrics calculation (overall accuracy, user's/producer's accuracy)
Initial Findings
Kuala Selat, Riau - 2024 Classification Results
The initial analysis of Kuala Selat demonstrates the effectiveness of combining different polarization data and classification rules for mangrove detection:

<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;"> <img src="https://raw.githubusercontent.com/placeholder/kuala-selat-results.jpg" style="max-width: 100%; width: 1200px; height: auto;" alt="Kuala Selat classification results" /> <p style="text-align: center; margin-top: 10px;"> <b>Figure 4.</b> Classification results for Kuala Selat 2024 showing (left) HV polarization reclassification, (center) HH polarization reclassification, and (right) mangrove extent overview with MVI classification. </p> </div>
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
<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;"> <img src="https://raw.githubusercontent.com/placeholder/combined-rules-results.jpg" style="max-width: 100%; width: 1000px; height: auto;" alt="Combined classification rules results" /> <p style="text-align: center; margin-top: 10px;"> <b>Figure 5.</b> Comparison of classification approaches: (left) Rule 2: HV + MVI Classification and (right) Rule 2: HH + MVI Classification for 2024. </p> </div>
Explanation of Area Differences
The variations in detected mangrove area across different methods reveal important insights:

1. Different Data Sources:

National map vs. SAR interpretation: The National Mangrove Map shows broader coverage as it integrates multiple data sources
Interpretation differences: Broader coverage in national maps versus optical data from different resolution and methods
2. Sensor Sensitivity:

HH detects: Trees/shrubs/herbs (usually with canopy/woody parts) - often wetter
HV detects: All above plus trees/shrubs with different structure
3. Classification Rule Effects:

Adding HV or HH with MVI (Mangrove Vegetation Index): Results in fewer classification areas due to more restrictive criteria
Rules combining polarizations: Help isolate true mangroves from similar vegetation types
MVI integration: Enhances specificity, reducing false positives
4. Cloud Coverage Differences:

ALOS has better cloud penetration than optical data
Optical data from different seasons: May show different coverage areas, masks, and speckle nature
Temporal dynamics: Cloud coverage affects optical data availability and accuracy
5. Accuracy Varies by Data Combination:

Rule 2 + optical data from different periods of acquisition: Better for monitoring
Different rules may be more suitable: Depending on specific mangrove characteristics and local conditions
ALOS data advantages: Overcome cloud percentage limitations better than optical sensors
Next Steps
The project follows a structured timeline to advance from initial analysis to comprehensive mangrove monitoring:

Project Timeline and Activities
Activity	Period	Deliverables
Analyzing the relation between ALOS PALSAR-2 2.2 and Sentinel-2 2A and any other datasets possibilities regarding the use of mangrove analysis	Oct 2024 - Nov 2024	Correlation analysis, data fusion methodology
Data Acquisition and Processing	Nov 2024 - Dec 2024	Processed SAR and optical datasets, validated training data
Data Visualization, literature strengthening	Dec 2024 - Mar 2025	Final maps, technical reports, peer-reviewed publications
Research Activities in Detail
Phase 1: Multi-sensor Integration Analysis (Oct-Nov 2024)
Investigate synergies between ALOS PALSAR-2 SAR and Sentinel-2 optical data
Test various data fusion approaches for improved mangrove classification
Evaluate additional datasets (e.g., Sentinel-1, Landsat) for complementary information
Develop optimal data combination strategies
Phase 2: Comprehensive Data Processing (Nov-Dec 2024)
Acquire complete time-series datasets for both study areas
Implement standardized preprocessing workflows
Generate training and validation datasets
Apply LMT classification algorithms
Produce multi-temporal mangrove maps
Phase 3: Synthesis and Dissemination (Dec 2024-Mar 2025)
Create interactive visualization tools for stakeholder engagement
Conduct thorough literature review and contextualization
Prepare technical documentation and user guides
Develop capacity building materials
Submit findings to scientific journals
Future Research Directions
1. Coastal Erosion/Accretion Detection:

Implement shoreline change detection algorithms
Compare backscatter boundary positions across years
Quantify erosion rates in mangrove-fronted coastlines
Assess mangrove effectiveness in erosion mitigation
2. Enhanced Temporal Resolution:

Expand analysis to annual time-series (2019-2024)
Detect seasonal variations in mangrove phenology
Monitor restoration project effectiveness
Track rapid changes following extreme events
3. Integration with Climate and Oceanographic Data:

Correlate mangrove changes with sea-level rise data
Analyze relationship with storm frequency and intensity
Incorporate tidal regime information
Link to sediment dynamics
4. Operational Monitoring System:

Develop near-real-time processing capabilities
Create automated change alert system
Design user-friendly dashboards for stakeholders
Establish protocols for regular updates to National Mangrove Map
5. Expansion to Other Regions:

Apply methodology to additional Indonesian coastal areas
Test transferability to different mangrove types
Compare results across various environmental settings
Support national-scale mangrove inventory
Conclusions
This study demonstrates the potential of integrating SAR and optical satellite imagery for comprehensive mangrove monitoring in Indonesia. Key findings and implications include:

Main Achievements
1. Methodology Development:

Successfully applied Logistic Model Tree (LMT) classification to distinguish mangroves from other forest types
Demonstrated the value of combining HV and HH polarizations for improved accuracy
Established reproducible workflow applicable to other Indonesian coastal regions
2. Data Source Evaluation:

Confirmed advantages of SAR data (ALOS PALSAR-2) over optical imagery for tropical coastal monitoring
Identified optimal combinations of polarizations and indices for mangrove detection
Quantified differences between classification approaches
3. Initial Mapping Results:

Generated preliminary mangrove extent maps for Kuala Selat (Riau) showing areas ranging from 23,876 to 34,447 hectares depending on classification rules
Provided baseline data for future change detection analysis
Identified areas requiring field validation
Practical Applications
Supporting Coastal Management:

Enhanced mapping capabilities can improve targeting of restoration efforts
Better monitoring supports evaluation of mangrove protection policies
Data supports marine spatial planning and coastal zone management
Addressing National Mangrove Map Limitations:

SAR-based approach overcomes cloud cover challenges
More frequent updates possible compared to current PMN system
Higher spatial detail in critical areas
Improved temporal monitoring capabilities
Climate Change Adaptation:

Baseline data for tracking mangrove response to sea-level rise
Support for nature-based solutions to coastal erosion
Monitoring ecosystem resilience under changing conditions
Quantifying carbon sequestration in coastal blue carbon ecosystems
Study Limitations and Considerations
1. Validation Requirements:

Need for extensive field validation to confirm classification accuracy
Limited ground truth data for remote coastal areas
Challenges in accessing mangrove areas for verification
2. Methodological Refinements:

Further optimization of LMT parameters needed
Investigation of seasonal effects on classification
Testing of alternative machine learning algorithms
3. Data Availability:

Dependency on ALOS-2 acquisition schedule
Cost considerations for large-scale operational implementation
Need for consistent data access policies
Future Vision
The framework established in this study provides a foundation for developing an operational mangrove monitoring system for Indonesia. This system would:

Provide regular updates to the National Mangrove Map
Support early warning systems for coastal erosion
Enable rapid assessment of mangrove loss or degradation
Guide adaptive management strategies
Inform policy decisions on coastal protection and restoration
By leveraging advances in satellite remote sensing, machine learning, and cloud computing, Indonesia can enhance its capacity to protect and restore vital mangrove ecosystems while safeguarding coastal communities from erosion and climate change impacts.

The integration of satellite monitoring with stakeholder engagement, as illustrated in the stakeholder analysis, ensures that scientific insights translate into actionable conservation and management strategies.

<!--{ as="div" }--> Open Science
Data Sources
Name	Type	Agency / Provider	Description / Usage
ALOS-2 PALSAR-2 L2.2 SCANSAR	Dataset	JAXA	Synthetic Aperture Radar data providing dual-polarization (HH/HV) backscatter for mangrove detection through cloud cover
ALOS-2 PALSAR-2 STRIPMAP Level 2.1	Dataset	JAXA	High-resolution SAR imagery (10m) for detailed mangrove structural analysis
Sentinel-2 Level 2A	Dataset	ESA Copernicus	Multispectral optical imagery for validation and complementary analysis
Indonesia National Mangrove Map (PMN)	Dataset	Ministry of Environment and Forestry	Baseline national mangrove coverage map at 1:25,000 scale
Tools and Methods
Name	Type	Description
Logistic Model Tree (LMT)	Algorithm	Machine learning classifier combining decision trees with logistic regression for mangrove classification
SAR Preprocessing	Methodology	Radiometric calibration, terrain correction, and speckle filtering of radar imagery
Mangrove Vegetation Index (MVI)	Index	Specialized vegetation index optimized for mangrove detection in SAR data
Collaborating Institutions
<p align="center"> <img src="https://raw.githubusercontent.com/placeholder/brin-logo.png" alt="BRIN" height="80" style="margin: 0 15px;"/> <img src="https://raw.githubusercontent.com/placeholder/atr-bpn-logo.png" alt="ATR/BPN" height="80" style="margin: 0 15px;"/> <img src="https://raw.githubusercontent.com/placeholder/ipb-logo.png" alt="IPB" height="80" style="margin: 0 15px;"/> <img src="https://raw.githubusercontent.com/placeholder/bakamla-logo.png" alt="BAKAMLA" height="80" style="margin: 0 15px;"/> <img src="https://raw.githubusercontent.com/placeholder/klhk-logo.png" alt="Ministry of Forestry" height="80" style="margin: 0 15px;"/> </p>
References
Pham, T. D., Yoshino, K., & Bui, D. T. (2018). Biomass estimation of Sonneratia caseolaris (l.) Engler at a coastal area of Hai Phong city (Vietnam) using ALOS-2 PALSAR imagery and GIS-based multi-layer perceptron neural networks. GIScience & Remote Sensing, 55(3), 329-353.
Balakrishnan, N., et al. (2020). Machine learning approaches for mangrove mapping using remote sensing data. Remote Sensing Applications: Society and Environment, 18, 100305.
Kuenzer, C., Bluemel, A., Gebhardt, S., Quoc, T. V., & Dech, S. (2011). Remote sensing of mangrove ecosystems: A review. Remote Sensing, 3(5), 878-928.
Ghorbanian, A., Kakooei, M., Amani, M., Mahdavi, S., Mohammadzadeh, A., & Hasanlou, M. (2021). Improved land cover map of Iran using Sentinel imagery within Google Earth Engine and a novel automatic workflow for land cover classification using migrated training samples. ISPRS Journal of Photogrammetry and Remote Sensing, 167, 276-288.
Giri, C., Ochieng, E., Tieszen, L. L., et al. (2011). Status and distribution of mangrove forests of the world using earth observation satellite data. Global Ecology and Biogeography, 20(1), 154-159.
Murdiyarso, D., Purbopuspito, J., Kauffman, J. B., Warren, M. W., Sasmito, S. D., Donato, D. C., ... & Kurnianto, S. (2015). The potential of Indonesian mangrove forests for global climate change mitigation. Nature Climate Change, 5(12), 1089-1092.
This study is part of Indonesia's efforts to enhance coastal resilience through improved mangrove ecosystem monitoring and management, supporting both biodiversity conservation and climate change adaptation strategies.

