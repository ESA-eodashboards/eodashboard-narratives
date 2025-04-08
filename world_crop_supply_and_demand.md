# Satellites are providing insights into agricultural production, crop conditions, and food supply <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/eurodatacube/eodash/master/app/public/data/story-images/Agriculture.jpeg" }-->
### Read more about satellite data applications for environmental impacts on world cereal supply and demand <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Satellite data applications for environmental impacts on world crop (cereal) supply and demand
 
**Advances in satellite monitoring** deliver a treasure-trove of data that scientists study and analyze for the betterment of humankind. These discoveries can help identify trends that better predict occurrences such as climate change and global warming. Since 2020, researchers at the European Space Agency, (ESA), the Japanese Space Agency, (JAXA), and NASA have been working together on a joint dashboard to combine their satellite data and openly share findings in an effort to elevate and protect the quality of life for the global population.

Providing insight into agricultural production, crop conditions, and food supply are among some of the most impactful information afforded by Earth observing satellites. Information derived from the data retrieved can affect the price we pay at grocery stores, policy implementation from regional to global scales, and food security around the world. Not only can satellite data tell us about current and near-future food and commodity crop conditions, but researchers are also studying the long-term trends in climate change and its effects on our food supply in support of agricultural resilience.

As demonstrated by recent global crises including the COVID-19 pandemic and the ongoing Russian war in Ukraine, the globally interconnected nature of the agrifood system has been thrust into the spotlight. These extreme disruptions to the global food supply underscore the importance of global agriculture monitoring, both of major producing countries and those who are major importers and therefore most vulnerable to food insecurity. A key example of international coordination in support of better food information is the **G20 GEOGLAM Crop Monitor** developed in response to a request from the G20 Agricultural Market Information System (AMIS). The Crop Monitor provides a public good of open, timely, science-driven information on crop conditions in support of market transparency. The GEOGLAM Crop Monitor Initiative are supported by the [global agriculture community](https://cropmonitor.org/index.php/about/amis-partners-cm/) and national space agencies - including the NASA Harvest Consortium and US-based institutions, JAXA and JASMIN, ESA and several European institutions, ministries of agriculture across the globe and many more. It reflects an international, multi-source, consensus assessment of crop growing conditions, status, and agro-climatic factors likely to impact global production, focusing on the major producing and trading countries for the four primary crops monitored by AMIS (wheat, maize, rice, and soybean) as well as on the countries most at risk to food insecurity and their primary staple crops.

## Map Example <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Vector","properties":{"id":"Administrative zones ADM0"},"source":{"type":"Vector"}},{"type":"Tile","properties":{"id":"N6_geoglam-2025-01-01T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap=%7B%221%22%3A%20%5B120%2C%20120%2C%20120%2C%20255%5D%2C%222%22%3A%20%5B130%2C%2065%2C%200%2C%20255%5D%2C%223%22%3A%20%5B66%2C%20207%2C%2056%2C%20255%5D%2C%224%22%3A%20%5B245%2C%20239%2C%200%2C%20255%5D%2C%225%22%3A%20%5B241%2C%2089%2C%2032%2C%20255%5D%2C%226%22%3A%20%5B168%2C%200%2C%200%2C%20255%5D%2C%227%22%3A%20%5B0%2C%20143%2C%20201%2C%20255%5D%7D&url=s3://veda-data-store/geoglam/CropMonitor_202501.tif"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="3.1699250014423126" center=[16.790831657981713,22.201786861954943] }-->

## Why We Monitor Agricultural Production

Any extreme event such as conflict, severe weather, or environmental abnormalities pose threats to agricultural production and may shock the system which is why it is so critical to have them accessible, transparent, timely, and global information afforded by satellite data. For example, based on community consensus and available satellite data we understand that at the end of February 2022, conditions are generally favourable for wheat and rice production, while mixed for maize and soybeans. We also know that winter wheat is mostly dormant in the northern hemisphere, with some areas of production raising some concern in Europe, Ukraine, and the US. In the southern hemisphere, maize is under mixed conditions in Argentina and southern Brazil. While rice conditions are favourable in most countries except for Vietnam and Brazil, soybeans are under mixed conditions in Argentina and southern Brazil. Satellite data helps us monitor these global crop conditions on a regular basis, especially in times and places where ground access is dangerous or limited.

**GEOGLAM Crop Monitor for AMIS and Early Warning synthesis map showing where crops are grown around the world, and the current crop conditions as of April 28, 2022. (source: <https://cropmonitor.org/>)**

![](https://www.eodashboard.org/data/story-images/AMIS_EW_synthesis_202205.jpeg)

## What We Monitor

With the help of satellites, we are able to monitor crops throughout the growing seasons and can use a combination of satellite derived time series to quantify critical indicators related to crop health for a specific region and crop over time. One such example of satellite-derived products are the GEOGLAM-NASA Harvest Agrometeorological (AGMET) Earth Observation Indicators, which are supported by the global remote sensing community and updated every 7-12 days to ensure that users are provided with the most up to date information. Displaying climate, environmental, and vegetative variables that impact agricultural outcomes, the AGMET Indicators were born from an agricultural stakeholder-identified need for a simple way to visualize and frequently monitor crop health with the ultimate goal of identifying potential cropping concerns as the growing season progresses and before a food shortage materializes. Satellite data provides a wealth of information to meet these needs including:

### Agromet parameters

##### 1. Normalized Difference Vegetation Index (NDVI): A measure of crop health
Showing global normalized difference vegetation index (NDVI) is a simple graphical indicator that can be used to analyze remote sensing measurements, often from a space platform, assessing whether or not the target being observed contains live green vegetation. As a crop season progresses, NDVI values will increase during early crop growth and development of leafy vegetation, will reach the peak as the crop fully develops and reaches maturity (before senescence), and then will decrease again as the crop matures and as the leafy vegetation begins to die off. How the NDVI values progress over the course of the season and the individual peak values can help predict the productivity of the crops and be compared to previous seasons.

![](https://www.eodashboard.org/data/story-images/NDVI%20AGMET.png)
*The AGMET Indicators use satellite data to measure key indicators of crop health, including NDVI and NDVI anomalies. (source: <https://cropmonitor.org/tools/agmet/>)*

##### 2. Surface soil moisture: A measure of water stored in the ground and available to crops  

Like NDVI, surface soil moisture is a key component for crop production that can be measured using satellite data (such as ESA’s SMOS instrument, JAXA’s GCOM-W instrument and NASA’s SMAP instrument). The amount of moisture in the soil will depend on meteorological conditions that can also be measured with the help of satellite data (precipitation, temperature, etc.) as well as sun exposure, wind, runoff/drainage, and soil type. If there is less water in the soil, it will be more difficult for crop roots to take up that water, resulting in a crop that is under greater stress. If the stress continues, the crop will wilt and eventually die. However, if the soil is above field capacity and the pores are oversaturated with water, then oxygen levels are restricted and it can be detrimental for the crop. This is why soil moisture is a key indicator of what may ultimately be a successful or failed crop.

These are just a few examples of the types of measurements that satellite missions can provide, but just as important as the information itself is how we analyze it and apply it. Because of the global coverage, frequent revisit rate, and repeatability of satellite data, we are able to successfully explore food security questions, climate change affects, and agricultural production around the world.

![](https://www.eodashboard.org/data/story-images/SoilMoisture.png)
*Soil moisture can be measured using satellite data and directly affects crop growth. (source: <https://cropmonitor.org/tools/agmet/>)*

## Global / Regional monitor
### 2022 drought in the U.S. Southern Plains region

##### a) NASA Harvest-GEOGLAM AGMET


The Southern Plains are a major wheat producing region in the U.S. and is monitored closely from planting to harvest given the importance of this major commodity crop. The AGMET Indicator graphic for the 2022 Southern Plains winter wheat season (above) shows below-average cumulative precipitation, NDVI, and soil moisture, consistent with drought conditions trending throughout the Southern Plains. U.S. winter wheat is typically harvested over the summer months but due to the drought conditions affecting the region, there is concern over the potential yields. With the help of satellite data, we understand several months ahead of the harvest that we might expect lower than average production as a result of the environmental indicators measured. With this knowledge comes the ability to respond and prepare appropriately while simultaneously providing market transparency.

![](https://www.eodashboard.org/data/story-images/AMIS-United%20States%20of%20America-Southern%20Plains-Winter%20Wheat-2022.jpeg)
*Southern Plains (USA) Winter Wheat 2022*

##### b) JAXA JASMIN/Japan JASMAI with MAFF

JAXA with Japanese MAFF provide agrometeorological information including Precipitation, Drought Index, Soil Moisture, Solar Radiation, Surface Temperature, Vegetation Index and anomaly, etc. Rainfall, Agriculture, Land, GPM Core Observatory, SHIZUKU (GCOM-W), MODIS, Multiple Satellites (GSMaP) bi-Monthly on JASMIN for Asia and on JASMAI for selected world areas. By using JAXA WMS with JASMIN/JASMAI products, the anomaly of Southern Plain in the US can be zoomed in with visualized map. The following are examples of composite averaged NDVI and NDVI anomaly.

![](https://www.eodashboard.org/data/story-images/Averaged%20NDVI.png?raw=true)

The following time series indicators reflect the precipitation, soil moisture and NDVI variables from Japan JASMIN/JASMAI for Kansas, USA.

- Chart 1

- Chart 2

- Chart 3

