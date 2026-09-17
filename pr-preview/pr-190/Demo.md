# Air pollution risk mapping with Sentinel-5P and socio-environmental indicators/Challenge <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2021/08/monitoring_air_quality/23426746-1-eng-GB/Monitoring_air_quality_pillars.jpg" }-->
#### 

## Authors: Afshin Moazzam¹, Haipeng Zhu¹, Sveva Zanetti¹, Zacharias Lagouros² and Zoi Giakati²
> ¹ Politecnico di Milano ² University of Thessaloniki

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub from 14/09/2026 to 18/09/20266. It was developed by a team from the Politecnico di Milano and Univerity of Thessaloniki.*

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

The lifetime of NO<sub>2</sub> is short, oscillating from hours to days in the troposphere. During the day, the concertation is lower as it is removed by the process of photolysis.  NO<sub>2</sub> has also seasonal behavior, in which the concentration is high in the winter period where there is a reduced amount of solar radiation. In this case NO<sub>2</sub> has a lifetime of 1 – 3 days, indicating much more atmospheric pollution at that time. 

#### Danger to health and the environment

NO<sub>2</sub> is an important pollutant as its effects expand from human health to environment. Focusing on human health, it irritates airways in the human respiratory system, causing asthma, coughing, wheezing or difficulty breathing, affecting the children and the elderly more. 

NO<sub>2</sub> affects also the environment. More specifically, it contributes to the formation of HNO<sub>3</sub> and acid rain, polluting the ground, water etc., endangering the fauna and flora. Rain acid also affects cultural heritage by dissolving monuments (e.g. marble statues). 

Finally, NO<sub>2</sub> contributes to the degradation of landscape, by making the atmosphere hazy and difficult to see through. All these effects lead to socioeconomical consequences. The need for health assistance raw materials increases in the hospitals. Crops are destroyed hitting farmers' income and driving up food prices, while the monuments are damaged increasing the cost of maintenance.

## Objective
Given these negative implications of NO<sub>2</sub>, this study implements a spatial risk assessment pipeline for air pollution that combines Sentinel 5P/TROPOMI NO₂ data with population data and age distribution.

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=2.6456584324087107 center=[-10.569682342641302,7.8903138332408105] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Title
Text

## Data and Methods
#### Dataset
- **Source**
-   Population data over Milano
    -   Population data divided by "comuni": https://www.dati.lombardia.it/Statistica/CITTA-METROPOLITANA-MILANO-Popolazione-residente-t/excw-2uuh/about_data
    -   Population data divided by "quartieri": https://dati.comune.milano.it/dataset/ds205-sociale-caratteristiche-demografiche-territoriali-quartiere
-   Administrative border data over Milano
    -   Border of "comuni": https://www.istat.it/notizia/confini-delle-unita-amministrative-a-fini-statistici-al-1-gennaio-2018-2/
    -   Border of "quartieri": https://dati.comune.milano.it/dataset/ds964-nil-vigenti-pgt-2030
-   NO2 permanent station data
    -   Station data: https://www.dati.lombardia.it/Ambiente/Stazioni-qualit-dell-aria/ib47-atvt/about_data
    -   Sensor data: https://www.arpalombardia.it/temi-ambientali/aria/form-richiesta-dati-stazioni-fisse/
- **Temporal coverage**: 

## Methodology workflow

NO2 data prcessing workflow brings together satellite observations and ground measurements to estimate surface-level NO₂ across the Milan Metropolitan Area. The administrative boundary defines the study area and a common grid provides the spatial framework. 

Our analysis focuses on the data from 01/10/2024 to 30/09/2025 over the metropolitan area of Milano.
Since Nitrogen Dioxide is more present in winter than in summer, we divided the study in two periods:
- hot months: from april to semptember
- cold months: from october to march

We further divide the analisis over different weekdays, combining NO2 dava with population density data and administrative borders. 

#### Administrative borders

Milano province is divided into municipalities, called "comuni". Comune di Milano is the bigger one, which includes all the red area in the image below. To have a finer granularity we also considered the division in "quartieri", which are local areas inside the comune.

![Administrative borders in Milano](https://res.cloudinary.com/dzxw0pvmr/image/upload/v1789654544/Immagine_17-09-26_-_14.31_np4hs2.png)

#### Population density and age distribution

For each "quartiere", Comune di Milano provides data about the total number of inhabitants, as well as the number of underage people and the number of people over 80 years old.
Regione Lombardia instead provides, for each "comune", the number of data for every age.
To uniform the analysis, we just considered the total number of people in each area and the total number of people over the age of 80.

We aggregated population data with administrative border files, obtaining a shapefile in which the field correspond to the data about population.

The image below shows the tatal number of people in each administrative area. Some "quartieri" have no inhabitans, such as "Parco Sempione", which includes a park with an inhabitated castle.

![Total population in each area](https://res.cloudinary.com/dzxw0pvmr/image/upload/v1789654545/Immagine_17-09-26_-_15.18_x8kyik.png)

The map below shows the percentage of people over 80 in each neighbour. While the distribution is homogeneous in the provincial area, next to the city centre there is a higher concentration of old people.

![Percentage of old people](https://res.cloudinary.com/dzxw0pvmr/image/upload/v1789654544/Immagine_17-09-26_-_15.32_n8j7cy.png)

#### Sentinel-5P data retrival
Sentinel-5P/TROPOMI Level-2 NO₂ files from 1 September 2024 to 31 December 2025 are first listed in an inventory. HARP, a software toolkit designed by the Atmospheric Toolbox to read, process, and convert Sentinel-5P TROPOMI data into standardized formats, checks their geolocation data to identify the orbits covering Milan. The selected file paths are stored in a CSV inventory for reuse in later processing.

#### Ground station data
Regione Lombardia provides hourly NO2 data from a network of ground station. A first dataset contains sensor measurement, and the stationID links these observations to the station catalogue, which provides the coordinates and other metadata.

#### Sentinel image validation with ground-station
Observations from nine ground stations provide the reference measurements for calibration. The two datasets describe different quantities: ground stations measure surface NO₂ concentration in µg/m³, whereas the satellite measures the tropospheric NO₂ column.
 
Connecting these measurements requires alignment in both time and space. The midpoint between the start and end timestamps in each satellite filename serves as an approximate timing reference, converted to Milan local time. Ground observations within ±1 hour of that reference are averaged for each station. This timing remains an approximation because the file timestamps describe the full orbit segment, rather than the exact observation time over Milan.
 
For spatial alignment, each station is linked to the mean of the surrounding 3×3 cells. This step produce a paired dataset in which each row links one station and one satellite orbit, with the corresponding ground concentration and satellite column value.
 
The plot below show that the data have the same trend over the period, conferming that Sentinel-5P TROPOMI NO2 measurements can be used since they are strongly correlated to ground measurements

![01_raw_comparison_5549_satellite_center 2.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/4c3d60a6e1c8fb893dfada2cf47e0d2e4e8171a9/assets/SvevaZ/01rawcomparison5549satellitecenter-2-1789656316615.png)

#### Sentinel-5P clipping and rebinning


#### Zonal statistics


#### Index calculation


## Results


## Conclusions


## Open Science


## Contributors
Authors, contibutors, reviewers