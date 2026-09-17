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
Air pollution risk mapping with Sentinel-5P and socio-environmental indicators

## Objective
The objective of this study was to design and implement a spatial risk assessment pipeline for air pollution that combines Sentinel 5P/TROPOMI NO₂ data with population, land cover, road density and distance to industrial zones

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

#### Methodology workflow

Our analysis focuses on the data from 01/10/2024 to 30/09/2025 over the metropolitan area of Milano.
Since Nitrogen Dioxide is more present in winter than in summer, we divided the study in two periods:
- hot months: from april to semptember
- cold months: from october to march

We further divide the analisis over different weekdays, combining NO2 dava with population density data and administrative borders.


**Administrative borders**

Milano province is divided into municipalities, called "comuni". Comune di Milano is the bigger one, which includes all the red area in the image below. To have a finer granularity we also considered the division in "quartieri", which are local areas inside the comune.

![Administrative borders in Milano](https://github.com/SvevaZ/eodashboard-narratives/blob/SvevaZ/test1/assets/aapopescu/Borders.png)

**Population density and age distribution**

For each "quartiere", Comune di Milano provides data about the total number of inhabitants, as well as the number of underage people and the number of people over 80 years old.
Regione Lombardia instead provides, for each "comune", the number of data for every age.
To uniform the analysis, we just considered the total number of people in each area and the total number of people over the age of 80.

We aggregated population data with administrative border files, obtaining a shapefile in which the field correspond to the data about population.

The image below shows the tatal number of people in each administrative area. Some "quartieri" have no inhabitans, such as "Parco Sempione", which includes a park with an inhabitated castle.

![Total population in each area](https://github.com/SvevaZ/eodashboard-narratives/blob/SvevaZ/test1/assets/aapopescu/Total_pop.png)

The map below shows the percentage of people over 80 in each neighbour. While the distribution is homogeneous in the provincial area, next to the city centre there is a higher concentration of old people.

![Percentage of old people](https://github.com/SvevaZ/eodashboard-narratives/blob/SvevaZ/test1/assets/aapopescu/Old%20people)

## Results


## Conclusions


## Open Science


## Contributors
Authors, contibutors, reviewers