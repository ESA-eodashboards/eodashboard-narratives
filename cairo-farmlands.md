---
cover-image: https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/3-agriculture-crops.jpg
date: 2025-01-01
theme: atmosphere
tags: carbon,crops,co2
official: true
---

# Farmlands North of Cairo absorb so much atmospheric CO2 it can be measured from space <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/3-agriculture-crops.jpg" }-->
### Satellite observations of solar-induced fluorescence shed light on plant photosynthetic activity<!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Crops Consume Cairo’s CO2

Cairo, the capital city of Egypt, is home to more than 20 million people, making it the most populated city in Africa. The city is located on the fertile floodplain of the Nile River and is surrounded by farmland, with a high concentration of farmland to the north. The farmland stands out in satellite imagery against the drier deserts of Egypt, and during the growing season crops absorb atmospheric carbon dioxide (CO2) that can be measured from space.

The following maps show examples of the changes of atmospheric CO2 concentrations based on the growth and photosynthetic activity of crops on nearby farms.

We can observe the emission of CO2 from cars, power plants, and other fossil-fuel burning activities from space using the Japanese Aerospace Exploration Agency’s Greenhouse gasses Observing Satellite (GOSAT). We can also observe how crops on surrounding farmlands consume CO2 by looking at solar-induced chlorophyll fluorescence (SIF). SIF is an innovative measurement that serves as a proxy of plant photosynthetic activity. Crops and other plants absorb white light from the sun and when photosynthesis occurs, they emit some of the unused energy from the sun as a red glow, known as SIF.

By combining GOSAT data, TROPOMI SIF data, surface wind data, and a statistical megacity emission inventory, we can monitor daily atmospheric changes of CO2. GOSAT observes tropospheric partial column density of carbon dioxide (CO2) over global megacities and provides the CO2 enhancement from lower atmosphere (0-4 km) density minus upper atmosphere (4-12 km) density.

In this research, researchers from the Japanese Aerospace Exploration Agency demonstrate how CO2 levels over Cairo change over time based on trends in combustion, SIF levels, and wind direction.

Egypt has two growing seasons, one in the summer and one in the winter. In the summer, the map below shows there were low CO2 levels over Cairo, correlated with high SIF.

<center>
<img src="https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/Wind_Cairo_2018-06-30_rev.png" width="30%">
	
<img src="https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/Wind_Cairo_2019-02-01_rev.png" width="30%">
	
<img src="https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/Wind_Cairo_2019-10-05_rev.png" width="30%">
	
Wind direction and speed over Cairo on 2018-06-30, 2019-02-01 and 2019-10-05.
	

## Earth Observations

_Data source: <https://www.eorc.jaxa.jp/GOSAT/GPCG/index_GOSAT.html>_

**TROPOMI SIF** in monthly average [mW/m2/sr/nm] TROPOMI solar-induced chlorophyll fluorescence (SIF) shows the photosynthetic activity of plant ecosystem. Plant absorbs sunlight but re-emit a small fraction of energy as SIF, which is strongly related to carbon uptake of CO2 through photosynthesis over plant area.

_Data source: Koehler, P., & Frankenberg, C. (2020). Ungridded TROPOMI SIF (at 740nm) (Version 1.0) [Data set]. CaltechDATA. <https://doi.org/10.22002/D1.1347>_

**TROPOMI NO2 column density** in daily [mol/m3] TROPOMI observes nitrogen dioxide (NO2) column density with a high resolution of 5 km. NO2 is an air pollution trace gas as a result of anthropogenic activities along with fossil fuel combustion such as oil refinery, power plant, steelwork and automobile transportation the same as the CO2 emission. However, NO2 reduction is processed by decomposition different from CO2 uptake.

_Data source: <https://data-portal.s5p-pal.com/products/no2.html>_

**Windrose in hourly frequency**

Windrose shows the frequency of winds blowing from directions and speed over an hour around GOSAT overpass time in the target city.

_Acknowledgments: The windrose was produced by using wind data from Windergroud.com._

Explore in more details these datasets by clicking on the **Dashboard** button at the top of the page or directly from the links below:

- [GOSAT-2 CO2 on Cairo](https://www.eodashboard.org/explore?indicator=N2_CO2_jaxa_gosat)
- [OCO-2 CO2 Global](https://www.eodashboard.org/explore?indicator=N2_CO2_mean)
- [TROPOMI NO2](https://www.eodashboard.org/explore?indicator=N1_NO2)
- [TROPOMI SIF](https://www.eodashboard.org/explore?indicator=SIF)

## Map Tour Example <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Tile","properties":{"id":"osm"},"source":{"type":"OSM"}}]' center=[15,48] zoom="5" animationOptions="{duration:500}" }-->
### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"EOxCloudless 2021"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2021_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="10.316288840107912" center=[31.091596890300035,30.153847605728885] animationOptions={duration:500}}-->
#### Cairo, Egypt
This Copernicus Sentinel-2 view of Cairo, Egypt, reveals a rapidly expanding metropolis located at the southern end of the Nile Delta - one of the world’s fastest-growing cities. This urban sprawl is encroaching on what was once prime farmland, as grey urbanized areas continue to consume the green cropland along the Nile River, which represents Egypt’s only arable land. About 96 percent of Egypt’s total areais classified as desert, lacking forests, permanent meadows, or pastures. This increases the pressure on this limited fertile land. Despite its small size, this land is highly productive, sustaining an average of 8 persons per acre (20 per hectare) and often being cropped more than once a year.
### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"N2_CO2_jaxa_gosat-2018-06-30T11:59:59Z"},"source":{"type":"TileWMS","urls":["https://gpwmap.jaxa.jp/wms"],"params":{"layers":"EODASH:XCO2-GOSAT-Cairo","styles":"","format":"image/png","time":"2018-06-30T11:59:59Z"}}},{"type":"Tile","properties":{"id":"EOxCloudless 2021"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2021_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="10.316288840107912" center=[31.091596890300035,30.153847605728885] animationOptions={duration:500}}-->
#### CO2 observed on 30 June 2018
**GOSAT lower tropospheric CO2 enhancement** in daily [ppm] GOSAT tropospheric partial column observes global changes of the carbon dioxide (CO2) enhancement; the CO2 density difference between lower atmosphere (0-4 km) influenced by CO2 net flux, i.e., surface emission and uptake, minus upper atmosphere (4-12 km) as background. The report on GOSAT partial column density products was submitted to UNFCCC for the first global stocktake as space-based surface GHG Emission Indicator (GEI) over the city.
### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"N2_CO2_jaxa_gosat-2019-02-01T11:59:59Z"},"source":{"type":"TileWMS","urls":["https://gpwmap.jaxa.jp/wms"],"params":{"layers":"EODASH:XCO2-GOSAT-Cairo","styles":"","format":"image/png","time":"2019-02-01T11:59:59Z"}}},{"type":"Tile","properties":{"id":"EOxCloudless 2021"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2021_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="10.316288840107912" center=[31.091596890300035,30.153847605728885] animationOptions={duration:500}}-->
#### CO2 observed on 01 February 2019
### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"N2_CO2_jaxa_gosat-2019-10-05T11:59:59Z"},"source":{"type":"TileWMS","urls":["https://gpwmap.jaxa.jp/wms"],"params":{"layers":"EODASH:XCO2-GOSAT-Cairo","styles":"","format":"image/png","time":"2019-10-05T11:59:59Z"}}},{"type":"Tile","properties":{"id":"EOxCloudless 2021"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2021_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="10.316288840107912" center=[31.091596890300035,30.153847605728885] animationOptions={duration:500}}-->
#### CO2 observed on 10 May 2019


### References
	
* [NASA Earth Observatory](https://earthobservatory.nasa.gov/features/Lights2/lights_soil5.php)
* [Britannica](https://www.britannica.com/place/Egypt/Agriculture-and-fishing)
	
	