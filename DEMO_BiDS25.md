# A Satellite Perspective on Urban Health: the case of New Delhi
How Earth Observation data reveals the interconnected challenges facing one of the world's most populous cities
 
  

#### 0. Setting the Scene: A City Under Stress

## Map Example <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"population_density;:;b0e07ca0-ffc4-4e24-93a4-e5f54d13e440;:;population_density;:;EPSG:3857","title":"population_density"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_POPULATION_DENSITY"],"TILED":true,"TIME":"2020-05-01T01:00:00Z/2020-05-02T00:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="5.218874813028399" center=[73.68994240802607,21.201400963870427] projection="" animationOptions={duration:500}}-->
#### New Delhi: home to over 30 million people 
In its metropolitan area, represents **one of the world's most densely populated urban centers**. 
This megacity faces a perfect storm of environmental and socio-economic challenges that directly impact public health. Through the lens of satellite data, we can observe how multiple stressors converge to create a complex urban health landscape.


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"population_density;:;b0e07ca0-ffc4-4e24-93a4-e5f54d13e440;:;population_density;:;EPSG:3857","title":"population_density"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_POPULATION_DENSITY"],"TILED":true,"TIME":"2020-05-01T01:00:00Z/2020-05-02T00:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.401339389024082" center=[77.07719595752367,28.66129569622332] projection="" animationOptions={duration:500}}-->


#### Population Densitiy:  The Foundation of Urban Vulnerability

The satellite data reveals New Delhi's extreme population concentration, with some areas exceeding 30,000 people per square kilometer. This density creates cascading effects: increased energy demand, higher pollution levels, greater strain on infrastructure, and amplified vulnerability to environmental hazards.
Key Insight: High population density acts as a multiplier for all other urban stressors, making environmental and health challenges more severe and widespread.


## 1. The Heat Crisis
In March 2022, India experienced one of its most severe heatwaves on record. New Delhi bore the brunt of this extreme weather event, with temperatures soaring above 45°C (113°F) for consecutive days.

## Houston <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Sentinel-3-SLSTR-L2-LST;:;2023-08-31T00:00:00Z;:;Sentinel-3-SLSTR-L2-LST;:;EPSG:3857","title":"Sentinel-3-SLSTR-L2-LST"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-3-SLSTR-L2-LST"],"TILED":true,"TIME":"2023-08-31T00:00:00Z/2023-08-31T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="5.834272716840864" center=[80.29945261498048,19.081938521754154] projection="" animationOptions={duration:500}}-->
#### The Urban Heat effect (CHANGE DATASET TO GCOM-C)
GCOM-C satellite data shows how Delhi's concrete landscape creates "heat islands" - urban areas significantly warmer than surrounding rural regions. These temperature differences can exceed 5-8°C, turning the city into a furnace during heatwave conditions.


## 2. The Air Quality
In March 2022, India experienced one of its most severe heatwaves on record. New Delhi bore the brunt of this extreme weather event, with temperatures soaring above 45°C (113°F) for consecutive days.



## Map Tour Example <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;9cc22158-1b1d-4b15-b0c7-a868e4288282;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2024-11-18T00:00:00Z/2024-11-18T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="5.6777895547601425" center=[80.02162874292893,19.096503146328843] projection="" animationOptions={duration:500}}-->

#### The Perfect Storm of Pollution: November 18, 2024
TROPOMI satellite data reveals extremely high concentrations of nitrogen dioxide (NO2) over Delhi during this period. The pollution spike resulted from multiple factors:

* **Massive crop burning**: Satellite fire maps show thousands of agricultural fires surrounding the city
* **Weather patterns**: Calm winds and temperature inversions trapped pollutants close to the ground
* **Urban emissions**: Vehicle exhaust and industrial activities added to the toxic mix

The Data Story: The overlay of fire detection data with NO2 concentrations clearly shows the connection between agricultural burning and urban air pollution, demonstrating how regional practices directly impact city-dwellers' health.

## 3. Economic Activity and Human Mobility

Lights Out: COVID-19's Socio-Economic Impact
When COVID-19 lockdowns hit Delhi in 2020, the city's nighttime lights dimmed dramatically - a clear indicator of reduced economic activity and human mobility.


## Exploring cities <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"JAXA_Nighttimelevel_Urban"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"JAXA-NIGHTTIMELEVEL-URBAN","styles":"","format":"image/png","time":"2019-01-01T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="9.9224951359818" center=[77.3150332431322,28.490762442253427] animationOptions={duration:500}}-->
#### Delhi
During Lockdown: April 2020
The contrast is striking. Nighttime lights decreased by 20-30% across much of Delhi during the lockdown period, indicating:Reduced commercial activity: Shops, restaurants, and businesses closed Limited transportation: Fewer vehicles on roads meant less street lighting usage
Changed residential patterns: People staying home, potentially using less electricity
Socio-Economic Implications: This reduction in nighttime lights correlates with significant economic hardship, job losses, and changes in daily life patterns that affected millions of Delhi residents.

## 4. Vulnerability and Urban Health

Mapping Inequality: The Global Gridded Relative Deprivation Index (GRDI) Version 1 represents a groundbreaking approach to mapping multidimensional poverty and deprivation. This dataset provides a comprehensive view of relative deprivation across the globe by assigning each 30 arc-second (~1 km) pixel a value between 0 (lowest deprivation) and 100 (highest deprivation).




 
## Map Tour Example <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"grdi-v1-raster;:;povmap-grdi-v1_2010-01-01_2021-12-31;:;grdi-v1-raster;:;EPSG:3857","title":"grdi-v1-raster"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/grdi-v1-raster/povmap-grdi-v1_2010-01-01_2021-12-31.tif&resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0.0,100.0","projection":"EPSG:3857"},"opacity":1}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="6.430596019869051" center=[74.75501559099638,26.762623451990436] projection="" animationOptions={duration:500}}-->
#### Assessing poverty and deprivation at unprecedented spatial resolution
What makes GRDI particularly valuable is its integration of six distinct dimensions of deprivation into a single, spatially explicit index. Rather than relying on a single poverty metric, GRDI combines demographic indicators (child dependency ratio), health outcomes (infant mortality rates), human development measures (Subnational Human Development Index), urbanization patterns (built-up area ratios), and economic activity proxies (nighttime light intensity and trends from 2012-2020). This multidimensional approach captures the complex, interconnected nature of deprivation that traditional income-based poverty measures often miss.


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"grdi-v1-raster;:;povmap-grdi-v1_2010-01-01_2021-12-31;:;grdi-v1-raster;:;EPSG:3857","title":"grdi-v1-raster"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/grdi-v1-raster/povmap-grdi-v1_2010-01-01_2021-12-31.tif&resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0.0,100.0","projection":"EPSG:3857"},"opacity":1}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.363467785428094" center=[76.62986663376584,28.626230989439875] projection="" animationOptions={duration:500}}-->
#### New Delhi's High GRDI Values:
In this context, New Delhi's remarkably high GRDI values (approaching 100) compared to surrounding areas present a fascinating case study of urban deprivation patterns. Despite being India's capital and a major economic center, New Delhi's high scores on this multidimensional index reveal the complex challenges facing megacities in the developing world.

The elevated deprivation values likely reflect several converging factors: high child dependency ratios driven by dense populations and demographic transitions, infrastructure systems strained beyond capacity affecting health outcomes like infant mortality, and the paradoxical relationship between urbanization and human development indicators. 

