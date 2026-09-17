# Air pollution risk mapping with Sentinel-5P and socio-environmental indicators/Challenge <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2021/08/monitoring_air_quality/23426746-1-eng-GB/Monitoring_air_quality_pillars.jpg" }-->
#### 

## Authors: Afshin Moazzam¹, Haipeng Zhu¹, Sveva Zanetti¹, Zacharias Lagouros² and Zoi Giakati²
> ¹ Politecnico di Milano ² University of Thessaloniki

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub from 14/09/2026 to 18/09/2026. It was developed by a team from the Politecnico di Milano and University of Thessaloniki.*

## 
<p align="center">
  <img src="https://datascience.deib.polimi.it/wp-content/uploads/2016/02/polimi-logo.png" alt="Politecnico" height="80" style="margin: 0 15px;"/>
  <img src="https://edurank.org/assets/img/uni-logos/aristotle-university-of-thessaloniki-logo.png" alt="Thessaloniki logo" height="80" style="margin: 0 15px;"/>
</p>

## Challenge
This challenge combine sentinel-5P TROPOMI data with social indicators, such as population density and age distribution, to derive a risk map over the region of Milano, highlighting the areas the population, and in particular fragile population, is more exposed to pollutants.

The analysis focused on Nitrogen Dioxide, which is one of the compounds measured by sentinel-5P

#### Nitrogen Dioxide

Nitrogen Dioxide (NO<sub>2</sub>) is one of the Nitrogen Oxides (NOx) compounds together with Nitrogen Monoxide (NO). NO<sub>2</sub> comes from both natural and anthropogenic sources. Usually is emitted in small quantities from combustion processes (e.g. emissions from cars, trucks and buses, power plants, and off-road equipment) along with NO. NO<sub>2</sub> can also be formed by the oxidation of NO. This process is known as the first part of the NOx cycles, where NO<sub>2</sub> is produced from the interaction of NO with Ozone (O<sub>3</sub>), based on the following equation:

NO+O<sub>3</sub>→ NO<sub>2</sub>+O<sub>2</sub>  (1)

This cycle continues with the dissolution of NO2 via photolysis which is one of the primary sinks of it (during daytime):

NO<sub>2</sub>+hv→NO+O (2)

Even though this process seems effective for removing the NO2 from the atmosphere, improving the air quality, it creates secondary problems, such as acid rain shifting the problem form the atmosphere to the ground.

The lifetime of NO<sub>2</sub> is short, oscillating from hours to days in the troposphere. During the day, the concertration is lower as it is removed by the process of photolysis.  NO<sub>2</sub> has also seasonal behavior, in which the concentration is high in the winter period where there is a reduced amount of solar radiation. In this case NO<sub>2</sub> has a lifetime of 1 – 3 days, indicating much more atmospheric pollution at that time. 

#### Danger to health and the environment

NO<sub>2</sub> is an important pollutant as its effects expand from human health to environment. Focusing on human health, it irritates airways in the human respiratory system, causing asthma, coughing, wheezing or difficulty breathing, affecting the children and the elderly more. 

NO<sub>2</sub> affects also the environment. More specifically, it contributes to the formation of HNO<sub>3</sub> and acid rain, polluting the ground, water etc., endangering the fauna and flora. Acid rain also affects cultural heritage by dissolving monuments (e.g. marble statues). 

Finally, NO<sub>2</sub> contributes to the degradation of landscape, by making the atmosphere hazy and difficult to see through. All these effects lead to socioeconomical consequences. The need for health assistance raw materials increases in the hospitals. Crops are destroyed hitting farmers' income and driving up food prices, while the monuments are damaged increasing the cost of maintenance.

## Objective
Given these negative implications of NO<sub>2</sub>, this study implements a spatial risk assessment pipeline for air pollution that combines Sentinel 5P/TROPOMI NO₂ data with population data and age distribution.

## Data and Methods
#### Dataset

###### Sentinel-5P TROPOMI NO₂ Data

The main dataset we used is Sentinel-5P TROPOMI data, and in particular NO₂ measurements, available in the Copernicus Dataspace portal: https://dataspace.copernicus.eu/

The TROPOspheric Monitoring Instrument (TROPOMI) is a passive grating spectrometer that provides daily global coverage. The satellite operates in a sun-synchronous orbit with an equator-crossing time of approximately 13:30 local solar time and an orbital period of about 101.5 minutes. Combined with a wide swath width of 2,600 km, this temporal resolution ensures near-daily observations for most locations worldwide.  


The NO₂ data are provided in NetCDF-4 format, following standard Climate and Forecast (CF) metadata conventions. These files report the NO₂ tropospheric column density (expressed in mol/m²).
Since 6 August 2019, NO₂ data are available with a spatial resolution of 3.5 x 5.5 Km (across x along track)

###### Complementary Data Sources
-   Population data over Milano
    -   Population data divided by "comuni": https://www.dati.lombardia.it/Statistica/CITTA-METROPOLITANA-MILANO-Popolazione-residente-t/excw-2uuh/about_data
    -   Population data divided by "quartieri": https://dati.comune.milano.it/dataset/ds205-sociale-caratteristiche-demografiche-territoriali-quartiere
-   Administrative border data over Milano
    -   Border of "comuni": https://www.istat.it/notizia/confini-delle-unita-amministrative-a-fini-statistici-al-1-gennaio-2018-2/
    -   Border of "quartieri": https://dati.comune.milano.it/dataset/ds964-nil-vigenti-pgt-2030
-   NO2 permanent station data
    -   Station data: https://www.dati.lombardia.it/Ambiente/Stazioni-qualit-dell-aria/ib47-atvt/about_data
    -   Sensor data: https://www.arpalombardia.it/temi-ambientali/aria/form-richiesta-dati-stazioni-fisse/

## Methodology workflow
The analysis focuses on the data from 01/10/2024 to 30/09/2025 over the metropolitan area of Milano.
Since Nitrogen Dioxide is more present in winter than in summer, the study is divided in two periods:
- hot months: from April to Semptember
- cold months: from October to March

The analysis is further divided over different weekdays, providing a risk map for every day of the week (Monday, Tuesday ...) both for the hot and cold periods, which accounts for population density and age distribution.

#### Administrative borders

Milano province is divided into municipalities, called "comuni". Comune di Milano is the bigger one, which includes all the red area in the image below. To have a finer granularity we also considered the division in "quartieri", which are local areas inside the comune.

![Administrative borders in Milano](https://res.cloudinary.com/dzxw0pvmr/image/upload/v1789654544/Immagine_17-09-26_-_14.31_np4hs2.png)

#### Population density and age distribution

For each "quartiere", Comune di Milano provides data about the total number of inhabitants, as well as the number of underage people and the number of people over 80 years old.
Regione Lombardia instead provides, for each "comune", the number of data for every age.
To uniform the analysis, we just considered the total number of people in each area and the total number of people over the age of 80.

We aggregated population data with administrative border files, obtaining a shapefile in which the field correspond to the data about population.

The image below shows the total number of people in each administrative area. Some "quartieri" have no inhabitants, such as "Parco Sempione", which includes a park with an inhabitated castle.

![Total population in each area](https://res.cloudinary.com/dzxw0pvmr/image/upload/v1789654545/Immagine_17-09-26_-_15.18_x8kyik.png)

The map below shows the percentage of people over 80 in each neighbourhood. While the distribution is homogeneous in the provincial area, next to the city centre there is a higher concentration of old people.

![Percentage of old people](https://res.cloudinary.com/dzxw0pvmr/image/upload/v1789654544/Immagine_17-09-26_-_15.32_n8j7cy.png)

#### Sentinel-5P data retrieval
Sentinel-5P/TROPOMI Level-2 NO₂ files from 1 September 2024 to 31 December 2025 are first listed in an inventory. HARP, a software toolkit designed by the Atmospheric Toolbox to read, process, and convert Sentinel-5P TROPOMI data into standardized formats, checks their geolocation data to identify the orbits covering Milan. The selected file paths are stored in a CSV inventory for reuse in later processing.

#### Ground station NO₂ data
Regione Lombardia provides hourly NO₂ data from a network of ground station. A first dataset contains sensor measurement, and the stationID links these observations to the station catalogue, which provides the coordinates and other metadata.

#### Sentinel-5P image validation with ground-station
Observations from nine ground stations provide the reference measurements for calibration. The two datasets describe different quantities: ground stations measure surface NO₂ concentration in µg/m³, whereas the satellite measures the tropospheric NO₂ column.
 
Connecting these measurements requires alignment in both time and space. The midpoint between the start and end timestamps in each satellite filename serves as an approximate timing reference, converted to Milan local time. Ground observations within ±1 hour of that reference are averaged for each station. This timing remains an approximation because the file timestamps describe the full orbit segment, rather than the exact observation time over Milan.
 
For spatial alignment, each station is linked to the mean of the surrounding 3×3 cells. This step produce a paired dataset in which each row links one station and one satellite orbit, with the corresponding ground concentration and satellite column value.
 
The plot below show that the data have the same trend over the period, confirming that Sentinel-5P TROPOMI NO₂ measurements can be used since they are strongly correlated to ground measurements

![01_raw_comparison_5549_satellite_center 2.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/4c3d60a6e1c8fb893dfada2cf47e0d2e4e8171a9/assets/SvevaZ/01rawcomparison5549satellitecenter-2-1789656316615.png)

#### Sentinel-5P rebinning and clipping

HARP library allows to retrive the selected files, and is able to rebin the data to a common raster grid using the bin_spatial function, as explained in section 6.3.1 of https://eo4society.esa.int/wp-content/uploads/2022/01/ATMO01_AirQuality_Monitoring.pdf.
The chosen grid is 1x1 km, and after the rebinning the data of different days are all referred to the same common grid, while previously each pixel had a different footprint.

Using the administrative boundaries, the data have been clipped to Milan metropolitan area and have later been classified into the 14 groups, one for each day of the week, divided in hot and cold period.

The group data have them been processed, obtaining the average NO₂ concentration for each group.

#### Zonal statistics
Zonal statistics were performed in QGIS to derive district-level NO<sub>2</sub> information from the gridded raster dataset and append it to the existing district polygon layer. Each district polygon was used as a spatial zone, and QGIS identified the raster cells located within or intersecting its boundary. The mean NO<sub>2</sub> concentration for each district was calculated from the valid raster-cell values associated with that zone. Where precise pixel–polygon intersection was applied, partially intersected raster cells were weighted according to the proportion of their area overlapping the district, while fully covered cells received a weight of one. 
The resulting mean was calculated as the weighted sum of NO<sub>2</sub> pixel values divided by the total pixel-intersection weight. 

The output vector file retained the original district geometry and demographic attributes, with an additional field containing the district-level mean NO<sub>2</sub> value.

![b1.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/7bd9420b5910cd2f63e746c9342da38839896e25/assets/SvevaZ/b1-1789677967536.png)
![b2.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/6c1ee630869aee5c6bb706d04cdca76dbe596e6c/assets/SvevaZ/b2-1789678046681.png)
#### Index calculation
The risk mapping framework combined three components for each spatial unit: mean NO<sub>2</sub> concentration as the **hazard**, the proportion of residents aged 80 years or more as the **susceptible/exposed population component**, and population density as an indirect **vulnerability and service-pressure proxy**.
 
The elderly-share variable was calculated as:
 
E<sub>i</sub> = P<sub>80+,i</sub> / P<sub>i</sub>
 
where P<sub>80+,i</sub> is the number of residents aged 80+ and P<sub>i</sub> is total population. It therefore naturally ranges from 0 to 1. Where total population was zero, the elderly share was assigned a value of 0 to prevent division-by-zero errors and to represent the absence of resident population potentially exposed in that spatial unit.
 
Population density was first derived as:
 
D<sub>i</sub> = P<sub>i</sub> / A<sub>i</sub>
 
where A<sub>i</sub> is polygon area in km², and was then rescaled using min–max normalization:
 
¯D<sub>i</sub> = (D<sub>i</sub> - D<sub>min</sub>) / (D<sub>max</sub> - D<sub>min</sub>)
 
This transformed density values to the 0–1 interval while retaining the relative ordering among areas. Mean NO<sub>2</sub> was also min–max normalized:
 
¯H<sub>i,t</sub> = (H<sub>i,t</sub> - H<sub>min</sub>) / (H<sub>max</sub> - H<sub>min</sub>)
 
where H<sub>i,t</sub> is the mean NO<sub>2</sub> value for area i at time t. Crucially, H<sub>min</sub> and H<sub>max</sub> were calculated from the pooled NO<sub>2</sub> values across all 14 GeoPackages.
 
The final relative risk-priority index was calculated as a weighted linear combination:
 
Risk<sub>i,t</sub> = 0.50¯H<sub>i,t</sub> + 0.30E<sub>i</sub> + 0.20¯D<sub>i</sub>
 
The largest weight was assigned to NO<sub>2</sub> because it is the direct environmental hazard, while the elderly share received the second-largest weight. Population density was given a lower weight as an indirect proxy. It should be interpreted as a **relative spatial prioritization indicator**.

## Results
The results below show the risk map for each day of the week, divided by cold days (left column) and hot days (right column)

![block1.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/7f439238b0833c4ef947498ed0e10355fc5b580e/assets/SvevaZ/block1-1789675271217.png)
![block2.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/626c62a9c7c9c451b643b311e890fed1f9619599/assets/SvevaZ/block2-1789675283568.png)
![block3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/5194e7c3f823823001df2c931f8287faee6ea9ab/assets/SvevaZ/block3-1789675335624.png)

The analysis of tropospheric nitrogen dioxide reveals marked seasonal and weekly variations across the Milan metropolitan area. In the analysed period, the largest NO<sub>2</sub> columns occur during the cold season, when enhanced emissions and unfavourable meteorological conditions combine to promote pollutant accumulation.
 
During winter, emissions from road transport, industrial activity and residential heating are frequently confined within a shallow and stable planetary boundary layer. Weak winds and persistent temperature inversions suppress vertical mixing and limit regional ventilation, allowing pollutants to accumulate near major emission areas. These conditions are characteristic of the Po Valley, whose surrounding Alpine and Apennine topography restricts atmospheric exchange under stagnant weather regimes.
 
Seasonal changes in atmospheric chemistry further contribute to the observed contrast. Lower solar irradiance and reduced concentrations of hydroxyl radicals slow the conversion of NO<sub>2</sub> into nitric acid and other reservoir or removal products, increasing the effective atmospheric lifetime of NO<sub>x</sub>. During the warmer months, stronger photochemical activity and deeper boundary-layer mixing generally promote faster chemical processing and more efficient dilution, resulting in lower mean tropospheric NO<sub>2</sub> columns.
 
Seasonality also influences the magnitude of the weekly cycle. Lower road traffic and commercial activity during the weekend are associated with reduced anthropogenic NO<sub>x</sub> emissions. In summer, faster chemical processing and stronger vertical mixing allow the atmospheric NO<sub>2</sub> burden to respond relatively quickly to these reductions. In winter, weaker dispersion and a longer effective NO<sub>x</sub> lifetime can sustain an elevated regional background, making the weekend decrease less pronounced.
 
Within the analysed dataset, Thursday shows the largest mean NO<sub>2</sub> concentration in both seasonal subsets. This pattern may reflect the combined influence of sustained working-week emissions and incomplete day-to-day removal. Mean columns begin to decline on Friday and reach their lowest levels during the weekend.
 
Spatially, the strongest NO<sub>2</sub> enhancements are centred on the densely populated Milan metropolitan area, with elevated columns extending towards parts of the northern and north-western peri-urban region. This distribution reflects the interaction between spatially heterogeneous emission sources, atmospheric transport and the restricted ventilation of the Po Basin.

## Conclusions
Relating Sentinel-5P/TROPOMI NO<sub>2</sub> observations to ground-based air-quality measurements involves several methodological challenges that should be carefully addressed. TROPOMI measures the tropospheric NO<sub>2</sub> vertical column in mol/m², while ground stations measure near-surface NO<sub>2</sub> concentration in µg/m³; consequently, the two datasets describe different atmospheric quantities. Their relationship is influenced by boundary-layer height, vertical mixing, meteorological conditions, cloud coverage, local emission sources, and atmospheric transport. Further challenges arise from the difference between the satellite pixel footprint and the fine spatial variability of urban pollution, as well as from the need to align satellite overpass observations with hourly ground-station records. Addressing these issues through robust spatial aggregation, time matching, quality filtering, and validation with local stations is essential for an accurate interpretation of satellite-derived NO<sub>2</sub> patterns.
 
Despite these challenges, Sentinel-5P/TROPOMI offers important advantages for urban air-pollution analysis. Its near-daily temporal coverage makes it possible to investigate changes in NO<sub>2</sub> across seasons and days of the week, while its broad spatial coverage enables monitoring over large metropolitan and regional areas in a consistent way. This is particularly valuable where ground-monitoring networks are sparse, unevenly distributed, or expensive to install and maintain. In this study, the processed satellite data captured clear seasonal and weekly patterns in NO<sub>2</sub> over the Milan metropolitan area, including generally higher values during the cold season and differences between working days and weekends.
 
The risk-priority maps show the value of combining satellite-derived NO<sub>2</sub> information with population density and the proportion of vulnerable residents. The resulting index should be interpreted as a relative spatial prioritisation tool rather than as a direct estimate of personal exposure or a substitute for regulatory ground stations. Nevertheless, it can help identify populated urban locations where elevated pollution patterns overlap with a higher concentration of potentially vulnerable residents. This information can support more targeted mitigation strategies, including traffic-management measures, local emission-reduction actions, the placement of additional ground-monitoring stations, and interventions designed to reduce exposure among vulnerable groups. Overall, the approach demonstrates how daily, large-area TROPOMI observations can complement conventional monitoring and provide an accessible, scalable basis for urban air-pollution risk assessment.

## Open Science

Hassaan, M.A., Abdallah, S.M., Shalaby, ES.A. et al. Assessing vulnerability of densely populated areas to air pollution using Sentinel-5P imageries: a case study of the Nile Delta, Egypt. Sci Rep 13, 17406 (2023). [https://doi.org/10.1038/s41598-023-44186-4](https://doi.org/10.1038/s41598-023-44186-4)


[https://sentinels.copernicus.eu/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-nitrogen-dioxide](https://sentinels.copernicus.eu/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-nitrogen-dioxide)

[S[&]T, & ESA. HARP [Computer software]. [link](https://github.com/stcorp/harp)

[https://eo4society.esa.int/wp-content/uploads/2022/01/ATMO01_AirQuality_Monitoring.pdf](https://eo4society.esa.int/wp-content/uploads/2022/01/ATMO01_AirQuality_Monitoring.pdf)

[https://www.eea.europa.eu/en/topics/in-depth/air-pollution](https://www.eea.europa.eu/en/topics/in-depth/air-pollution)

## Contributors
Afshin Moazzam, Haipeng Zhu, Sveva Zanetti, Zacharias Lagouros and Zoi Giakati