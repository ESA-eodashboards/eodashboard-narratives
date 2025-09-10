# Urban Health: the case of New Delhi
This story will show Earth observation data reveals the interconnected challenges facing one of the **world's most populous cities**. This analysis examines New Delhi through satellite-derived health and urban indicators, exploring four key indicators: **Population Density** (NASA),  **Heatwave Patterns** (JAXA/ESA), **Air Quality** (ESA), **Socio-Economic Activity** (NASA).

A final indicato, the **Global Gridded Relative Deprivation Index (GRDI)** synthesizes these dimensions, showing how New Delhi's high density and elevated poverty rates amplify vulnerability to these interconnected health-related stressors.
  


#### 1. Setting the Scene: A City Under Stress 

## Map Example <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"population_density;:;b0e07ca0-ffc4-4e24-93a4-e5f54d13e440;:;population_density;:;EPSG:3857","title":"population_density"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_POPULATION_DENSITY"],"TILED":true,"TIME":"2020-05-01T01:00:00Z/2020-05-02T00:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="5.218874813028399" center=[73.68994240802607,21.201400963870427] projection="" animationOptions={duration:500}}-->
#### Population Densitiy:  The Foundation of Urban Vulnerability
The **Gridded Population of the World** dataset, consists of estimates of human population density (number of persons per square kilometer). **High population density can act as a multiplier for other urban stressors**, since it creates a cascating effect: increased energy demand, higher pollution levels, greated strain on infrasctructure might lead to amplified vulnerability to environmental hazards.  

<center>
<img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/NASAPopulation/NASAPopulation_legend.png" width="400">

</center>



### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"population_density;:;b0e07ca0-ffc4-4e24-93a4-e5f54d13e440;:;population_density;:;EPSG:3857","title":"population_density"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_POPULATION_DENSITY"],"TILED":true,"TIME":"2020-05-01T01:00:00Z/2020-05-02T00:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.401339389024082" center=[77.07719595752367,28.66129569622332] projection="" animationOptions={duration:500}}-->


#### New Delhi: home to over 30 million people 
In its metropolitan area, represents **one of the world's most densely populated urban centers**.  The darked shade of this datasets, reveals New Delhi's extreme population concentration, (with some areas exceeding 10000 people per square kilometer). 

<center>
<img src="https://images.pexels.com/photos/25469898/pexels-photo-25469898/free-photo-of-crowd-on-street-in-delhi-in-india.jpeg" width="400">
	
<span style="font-size:15px;">A crowded New Dehli Street. Source: Photo by Puran on Pexels [CC BY](https://creativecommons.org/licenses/by/2.0/)</span>
</center>







## 2. Urban Heatwaves  
In March 2022, India experienced one of its most severe heatwaves on record. New Delhi bore the brunt of this extreme weather event, with temperatures soaring above 45°C (113°F) for consecutive days.

## New Dehli <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Sentinel-3-SLSTR-L2-LST;:;2023-08-31T00:00:00Z;:;Sentinel-3-SLSTR-L2-LST;:;EPSG:3857","title":"Sentinel-3-SLSTR-L2-LST"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-3-SLSTR-L2-LST"],"TILED":true,"TIME":"2023-08-31T00:00:00Z/2023-08-31T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="5.834272716840864" center=[80.29945261498048,19.081938521754154] projection="" animationOptions={duration:500}}-->
#### The Urban Heat effect (CHANGE DATASET TO GCOM-C)
GCOM-C satellite data shows how Delhi's concrete landscape creates "heat islands" - urban areas significantly warmer than surrounding rural regions. These temperature differences can exceed 5-8°C, turning the city into a furnace during heatwave conditions.


## 3. Air Quality
Delhi's air quality challenges represent a complex intersection of **urban pollution** and **regional environmental factors**. 


## Map Tour Example <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;9cc22158-1b1d-4b15-b0c7-a868e4288282;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2024-11-18T00:00:00Z/2024-11-18T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="5.6777895547601425" center=[80.02162874292893,19.096503146328843] projection="" animationOptions={duration:500}}-->

#### Tracking down pollution
Earth observing satellites like the **TROPOMI instrument** on the  are being used to map air pollution worldwide. One of the variables that it can provide information is on tropospheric **nitrogen dioxide (NO2)** which is linked to pollutant sectors such as **traffic and industrial activities**. 


<center>
<img src="https://github.com/eurodatacube/eodash-assets/blob/main/collections/N1_NO2/N1_NO2_legend.png?raw=true" width="400">

</center>

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;9cc22158-1b1d-4b15-b0c7-a868e4288282;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2024-11-18T00:00:00Z/2024-11-18T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="8.010646952488841" center=[76.27467813141472,28.104211017431737] projection="" animationOptions={duration:500}}-->
#### November 2024: Recording breaking pollution in Dehli
On November 18th, Dehli recorded  **pollution levels were more than 50 times higher** than the World Health Organization’s recommended safe limit, creating a public health emegency that forced school closures and esitrcted outdoor activities. In several areas of the city,
<center>
<img src="https://d3i6fh83elv35t.cloudfront.net/static/2024/11/2024-11-18T110820Z_218494839_RC2H7BA6CRTJ_RTRMADP_3_INDIA-POLLUTION-1024x683.jpg" width="400">
	
<span style="font-size:15px;">New Delhi, India, November 18, 2024. Credit: REUTERS/Anushree Fadnavis)</span>
</center>



Air pollution in northern India rises every year, particularly in winter, as farmers **burn crop residue in agricultural areas**. The burning coincides with colder temperatures, which trap the smoke in the air. The smoke is then blown into cities, where auto emissions add to the pollution.



## 3. Economic Activity and Human Mobility

A city's nightime lights, can offer a reliable proxy for economic activity, population density and energy consuption. In global scale events, such as the COVID-19, lockdwon measures imposed worldwide affected human activities, which can be another element of pressure on the dyncamis of a city population. 


## Map Example <!--{ as="eox-map" mode="tour" }--> 
### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"JAXA_Nighttimelevel_Urban;:;94325551-cd9f-4ff3-8060-62edb1fdb4b6;:;JAXA_Nighttimelevel_Urban;:;EPSG:3857","title":"JAXA_Nighttimelevel_Urban"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["JAXA-NIGHTTIMELEVEL-URBAN"],"TILED":true,"TIME":"2019-01-01T00:00:00Z/2019-01-01T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="8.801051427050638" center=[76.45047736627924,28.45290111543406] projection="" animationOptions={duration:500}}-->
#### Delhi in Lockdown
The **Nighttime Light Urban (NLTU)** dataset, derived fom Suomi NPP sallite observations,  captures the intensity of artificial lighting across urban areas—a reliable proxy for economic activity, population density, and energy consumption. 
This colors represented in the dataset could be interpretated the following way: **pink, red and yellow** correspond to areas where a decrease in nighttime light level occurred (indicating a presumed reduction in social activity), **green, violet and blue** are areas where an increase occurred (indicating a presumed increase in social activity), and **white areas** correspond to apparent no changes.

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"JAXA_Nighttimelevel_Urban;:;94325551-cd9f-4ff3-8060-62edb1fdb4b6;:;JAXA_Nighttimelevel_Urban;:;EPSG:3857","title":"JAXA_Nighttimelevel_Urban"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["JAXA-NIGHTTIMELEVEL-URBAN"],"TILED":true,"TIME":"2019-01-01T00:00:00Z/2019-01-01T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="10.21661032859757" center=[77.01604331902165,28.5130617877376] projection="" animationOptions={duration:500}}-->
#### Delhi in Lockdown
In 2020, the city's nighttime lights dimmed dramatically. Nighttime lights decreased by **20-30%** across much of Delhi during the lockdown period, potentially indicating: reduced commercial activity like shops, restaurants, and businesses closed. However, in some residential patterns, in the outskirs, could indicate people staying home.

The decrease of activity could be linked to significant economic hardship, job losses, and changes in daily life patterns that affected millions of Delhi residents.

## 4. Vulnerability and Urban Health

**Mapping Inequality**: The Global Gridded Relative Deprivation Index (GRDI) Version 1 represents a groundbreaking approach to mapping multidimensional poverty and deprivation. This dataset provides a comprehensive view of relative deprivation across the globe by assigning each 30 arc-second (~1 km) pixel a value between **0 (lowest deprivation) and 100 (highest deprivation)**.


#### Assessing poverty and deprivation at unprecedented spatial resolution
What makes GRDI particularly valuable is its integration of **six distinct dimensions** of deprivation into a single, spatially explicit index. Rather than relying on a single poverty metric, GRDI combines demographic indicators (child dependency ratio), health outcomes (infant mortality rates), human development measures (Subnational Human Development Index), urbanization patterns (built-up area ratios), and economic activity proxies (nighttime light intensity and trends from 2012-2020). This multidimensional approach captures the complex, interconnected nature of deprivation that traditional income-based poverty measures often miss.

## Map Example <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"grdi-v1-raster;:;povmap-grdi-v1_2010-01-01_2021-12-31;:;grdi-v1-raster;:;EPSG:3857","title":"grdi-v1-raster"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/grdi-v1-raster/povmap-grdi-v1_2010-01-01_2021-12-31.tif&resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0.0,100.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="8.557000965002848" center=[76.56531671200712,28.41353375429155] projection="" }-->


   

#### New Delhi's High GRDI Values:
In this context, New Delhi's remarkably high GRDI values (approaching 100) compared to surrounding areas present a fascinating case study of urban deprivation patterns. Despite being India's capital and a major economic center, New Delhi's high scores on this multidimensional index reveal the complex challenges facing megacities in the developing world.

The elevated deprivation values likely reflect several converging factors: high child dependency ratios driven by dense populations and demographic transitions, infrastructure systems strained beyond capacity affecting health outcomes like infant mortality, and the paradoxical relationship between urbanization and human development indicators. 



  

