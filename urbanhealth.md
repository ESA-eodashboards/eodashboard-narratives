

# Urban Health in Megacities: the case of New Delhi and its surroundings <!--{ as="img" mode="hero" src="https://live.staticflickr.com/3600/3409479660_54cc371386_b.jpg " }-->
### Insights from urban health collected from open satellite data <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## New Delhi
###### A city of 30 million
New Delhi, in India, is one of the **most densely populated urban centers on Earth**. Like many megacities, it faces numerous challenges that threaten the health and well-being of its residents. By combining satellite observations with ground-based and socio-economic data, researchers can track these challenges across key dimensions of urban health. This story shows how the combination of **free, open data and tools** from three space agencies, [ESA](www.esa.int), NASA, and JAXA can be used to measure and monitor the city’s vulnerability to extreme heat, hazardous air, and the cascading risks of life in a megacity under strain.

## Nighttime lights <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"JAXA_Nighttimelevel_Urban;:;94325551-cd9f-4ff3-8060-62edb1fdb4b6;:;JAXA_Nighttimelevel_Urban;:;EPSG:3857","title":"JAXA_Nighttimelevel_Urban"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["JAXA-NIGHTTIMELEVEL-URBAN"],"TILED":true,"TIME":"2019-01-01T00:00:00Z/2019-01-01T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="10.029351763615878" center=[76.91622386287241,28.57071242662896] projection="" }-->
The Nighttime Light Urban (NLTU) dataset, derived from Suomi NPP satellite observations operated jointly by NASA and NOAA, captures the intensity of artificial lighting across urban areas—a reliable proxy for economic activity, population density, and energy consumption.In 2020, the city’s nighttime lights dimmed dramatically. Nighttime light levels **decreased & across much of Delhi**, as shown by the shades of **pink and red**, indicating a presumed reduction in social activity during the lockdown period. 

## Air Polution <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;507caad9-d5f5-45df-982c-c4558792e367;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2024-12-16T00:00:00Z/2024-12-16T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="6.573919052742737" center=[76.34022547744158,27.57212175552418] projection="" animationOptions={duration:500}}-->
#### November 18 2024: Delhi
On November 18th, Delhi recorded pollution levels more than 50 times higher than the World Health Organization’s recommended safe limit, creating a public health emergency that forced school closures and restricted outdoor activities. In several areas of the city, residents wore masks outdoors and authorities issued health advisories.
<center>
<img src="https://github.com/eurodatacube/eodash-assets/blob/main/collections/N1_NO2/N1_NO2_legend.png?raw=true" width="400">
</center>




### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;92f8905b-7a2a-433d-a7df-dd77483c5c0c;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2024-12-23T00:00:00Z/2024-12-23T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="10.041750788326192" center=[77.0060094694946,28.395012117393648] projection="" animationOptions={duration:500}}-->
#### December 2024: Gurugram 
In the city of Gurugram, located just southwest of New Delhi and part of the National Capital Region, high-density residential and industrial zones contribute to significant local emissions. 
In December, the city experienced a pronounced peak in NO2 concentrations, mirroring the severe pollution trends observed in the capital  the previous month.
<center> <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-6/stories/DEMO_BiDS25/NO2_Gurugram.png?raw=true" width="400">
<span style="font-size:15px;"> NO2 Concentrations in Gurugram city</span>
</center>


## Heatwaves <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://obs.eu-nl.otc.t-systems.com/eodashboardtutorial/LST_202407.tiff?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=DZPPJ23QUW6DYLDCKEYP%2F20250926%2Feu-nl%2Fs3%2Faws4_request&X-Amz-Date=20250926T091943Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=dd3dc4ae70a632916fb0659975190b11cff3cfdf3861f40aa1b9d4a40e5b3dd2"}]},"properties":{"id":"LST-gcom-c-2024-07;:;2024-07-01T00:00:00Z;:;0","title":"GCOM C LST "},"style":{"color":["case",["==",["band",1],0],["color",0,0,0,0],["between",["-",["*",["band",1],0.02],273.15],["var","vmin"],["var","vmax"]],["interpolate",["linear"],["-",["*",["band",1],0.02],273.15],0,[252,253,191,1],10,[254,176,120,1],20,[241,96,93,1],30,[183,55,121,1],40,[114,31,129,1],50,[44,17,95,1],60,[0,0,4,1]],["color",0,0,0,0]],"variables":{"vmin":0,"vmax":60}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="7.4152" center=[76.5517,23.149299999999997] projection="" }-->
#### Heatwaves in Northern India
A **severe heatwave occurs if the maximum temperature exceeds 45 degrees Celsius or is 6.5 degrees or more above normal**. In India experienced one of its most severe and longest heatwaves on record. 
The GCOM mission operated by JAXA (Japan Aerospace Exploration Agency) allows to retrieve Land Surface Temperature. This measures how hot the land surface is (not air temperature). The dataset presents a monthly average of the month of June in 2024.The heatwave occurred during the Indian dry season, which typically lasts from March to July, with peak temperatures in April and May.  <center>
<img src=" https://raw.githubusercontent.com/eurodatacube/eodash-assets/70f3505e8da505786ddd439dec6a9b90682887ba/collections/GCOM/legend_CGOM_LST_Celsius.png" width="400">

</center>

 
 

##
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

## Vulenrability <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"grdi-v1-raster;:;povmap-grdi-v1_2010-01-01_2021-12-31;:;grdi-v1-raster;:;EPSG:3857","title":"grdi-v1-raster"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/grdi-v1-raster/povmap-grdi-v1_2010-01-01_2021-12-31.tif&resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0.0,100.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.461966019517797" center=[77.01681906615504,28.50216563223246] projection="" animationOptions={duration:500}}-->
#### GDRI: New Delhi and Guruguram
 The Global Gridded Relative Deprivation Index (GRDI) Version 1 maps **multidimensional-based poverty and deprivation**, providing a comprehensive view of relative deprivation by assigning each pixel (~1 km) a value between **0 (lowest deprivation) and 100 (highest deprivation)**.
 
 
<center> <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/grdi-v1-built/cm_legend.png" width="400">

</center>


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"grdi-vnl-slope-raster;:;povmap-grdi-v1_VNL-slope_2012-01-01_2020-12-31;:;grdi-vnl-slope-raster;:;EPSG:3857","title":"grdi-vnl-slope-raster"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/grdi-vnl-slope-raster/povmap-grdi-v1_VNL-slope_2012-01-01_2020-12-31.tif&resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0.0,100.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="8.94954925760493" center=[77.08406842046404,28.390974407710885] projection="" animationOptions={duration:500}}-->
####VNL slope in two contrasting cities
Annual VNL data between 2012 and 2020 (VNL slope) considered the slope as a dimension where **higher values (increasing brightness) imply decreasing deprivation** and **lower values (decreasing brightness) imply increasing deprivation**.
<center>
  <div style="display: flex; justify-content: center; gap: 20px;">
    <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-6/stories/DEMO_BiDS25/gdri%20value.png?raw=true" width="400">
    <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-6/stories/DEMO_BiDS25/vnl_slope.png?raw=true" width="400">
  </div>
</center>

New Delhi’s much higher VNL slope (64 vs. 49) highlights its scale and intensity as the national capital, with denser population and more diverse economic activity. Despite the corporate hub that Gurugruam has become in the past years, perhaps that growth was more evident prior to 2012 - or maybe night activity does not follow those trends.


LONG STORY
# Urban Health and Megacities: the case of New Delhi <!--{ as="img" data-fallback-src="" mode="hero" src="https://live.staticflickr.com/3600/3409479660_54cc371386_b.jpg" }-->
### Satellite perspective provide urban health indicators <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->
# 
New Delhi, in India, is one of the most **densely populated urban centers on Earth**. Like many megacities, it faces numerous challenges that threaten the health and well-being of its residents.

By combining satellite observations with ground-based and socio-economic data, researchers can track these challenges across key dimensions of urban health. This story shows how the combination of free, open data and tools from three space agencies, ESA, NASA, and JAXA can be used to measure and monitor the city’s vulnerability to extreme heat, hazardous air, and the cascading risks of life in a megacity under strain.

## Population density <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"population_density;:;b0e07ca0-ffc4-4e24-93a4-e5f54d13e440;:;population_density;:;EPSG:3857","title":"population_density"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_POPULATION_DENSITY"],"TILED":true,"TIME":"2020-05-01T01:00:00Z/2020-05-02T00:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="5.218874813028399" center=[73.68994240802607,21.201400963870427] projection="" animationOptions={duration:500}}-->
#### The weight of numbers: crowded reality
**High population density can act as a multiplier for other urban stressors**, creating a cascading effect: increased energy demand, higher pollution levels, and greater strain on infrastructure can all lead to amplified vulnerability to environmental hazards.

The image shows the  **Gridded Population of the World (GPW)** dataset, consisting of estimates of human population density (number of persons per square kilometer). This dataset, developed by  is like a **high-resolution heatmap of humanity**: it helps not only to see *how many people* leave on Earth, but also *where they are*.  

<center>
<img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/NASAPopulation/NASAPopulation_legend.png" width="400">

</center>



### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"population_density;:;b0e07ca0-ffc4-4e24-93a4-e5f54d13e440;:;population_density;:;EPSG:3857","title":"population_density"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_POPULATION_DENSITY"],"TILED":true,"TIME":"2020-05-01T01:00:00Z/2020-05-02T00:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.401339389024082" center=[77.07719595752367,28.66129569622332] projection="" animationOptions={duration:500}}-->


#### New Delhi: A Megacity of 30 Million 
In its metropolitan area, New Delhi is among the planet’s most crowded metropolitan regions. The darker shades from GWP dataset reveal the city’s extreme population concentration, with areas exceeding 10,000 people per square kilometer.

<center>
<img src="https://images.pexels.com/photos/25469898/pexels-photo-25469898/free-photo-of-crowd-on-street-in-delhi-in-india.jpeg" width="400">
	
<span style="font-size:15px;">A crowded New Dehli Street. Source: Photo by Puran on Pexels [CC BY](https://creativecommons.org/licenses/by/2.0/)</span>
</center>

 


# 
### Urban Heatwaves
Urban heat represents one of the most direct and deadly threats to public health in megacities like Delhi. Unlike other environmental stressors that may take years to manifest their health effects, extreme heat kills within hours—making it a silent but immediate danger for Delhi's 30+ million residents.


## Urban Heatwaves <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://s3.ap-northeast-1.wasabisys.com/je-pds/cog/v1/JAXA.G-Portal_GCOM-C.SGLI_standard.L3-LST.daytime.v3_global_monthly/2024-07/1/E000.00-E090.00/E000.00-N00.00-E090.00-N90.00-LST.tiff"}]},"properties":{"id":"GCOM_global_monthly;:;2024-07-01T00:00:00Z;:;0","title":"GCOM"},"style":{"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["-",["band",1],15000],["-",17000,15000]],0,[13,8,135,1],0.1,[75,3,161,1],0.2,[125,3,168,1],0.3,[168,34,150,1],0.4,[203,70,121,1],0.5,[229,107,93,1],0.6,[248,148,65,1],0.7,[253,195,40,1],0.8,[240,249,33,1],1,[240,249,33,1]],["color",0,0,0,0]]}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="6.971467762147654" center=[75.11901894077282,27.76044673808103] projection="" animationOptions={duration:500}}-->
#### Heatwaves in Northern India
 A heatwave is officially declared when the maximum temperature exceeds 40 degrees Celsius and is at least 4.5 degrees above normal. A **severe heatwave occurs if the maximum temperature exceeds 45 degrees Celsius or is 6.5 degrees or more above normal**. The GCOM mission operated by JAXA (Japan Aerospace Exploration Agency) allows to retrieve Land Surface Temperature. This measures how hot the land surface is (not air temperature). The dataset presents a monthly average of the month of June in 2024. 
 
 <center>
<img src=" https://raw.githubusercontent.com/eurodatacube/eodash-assets/70f3505e8da505786ddd439dec6a9b90682887ba/collections/GCOM/legend_CGOM_LST_Celsius.png" width="400">

</center>


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://s3.ap-northeast-1.wasabisys.com/je-pds/cog/v1/JAXA.G-Portal_GCOM-C.SGLI_standard.L3-LST.daytime.v3_global_monthly/2024-07/1/E000.00-E090.00/E000.00-N00.00-E090.00-N90.00-LST.tiff"}]},"properties":{"id":"GCOM_global_monthly;:;2024-07-01T00:00:00Z;:;0","title":"GCOM"},"style":{"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["-",["band",1],15000],["-",17000,15000]],0,[13,8,135,1],0.1,[75,3,161,1],0.2,[125,3,168,1],0.3,[168,34,150,1],0.4,[203,70,121,1],0.5,[229,107,93,1],0.6,[248,148,65,1],0.7,[253,195,40,1],0.8,[240,249,33,1],1,[240,249,33,1]],["color",0,0,0,0]]}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.389550914375219" center=[76.6932693292333,28.470907278677743] projection="" animationOptions={duration:500}}-->
#### June 2024: recording-breaking temperatures
In June 2024, India experienced one of its most severe and longest heatwaves on record. The heatwave occurred during the Indian dry season, which typically lasts from March to July, with peak temperatures in April and May.

<center> <img src="https://th-i.thgim.com/public/incoming/ifa6rc/article68228316.ece/alternates/LANDSCAPE_1200/07_Standalone_Hot_Weather_Mirage_29_05_Delhi.jpg" width="400">

<span style="font-size:15px;">A mirage appears on Kartavya Path on a hot day in the Capital on May 29, 2024. Photo Credit: SHIV KUMAR PUSHPAKAR
</span>

</center>

New Delhi bore the brunt of this extreme weather event, with temperatures soaring above 45°C. The extreme summer heat in Delhi pushed its peak power demand to an all-time high of 8,302 MW on Wednesday afternoon, officials said. This demonstrates how extreme temperatures sharply increase urban energy demand while simultaneously posing serious risks to public health.


# 
### Air Quality
Delhi's **air quality** challenges represent a complex intersection of **urban pollution** and **regional environmental factors**. 


## Air Quality <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;9cc22158-1b1d-4b15-b0c7-a868e4288282;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2024-11-18T00:00:00Z/2024-11-18T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="5.6777895547601425" center=[80.02162874292893,19.096503146328843] projection="" animationOptions={duration:500}}-->

#### Tracking down pollution
Earth-observing satellites like the **TROPOMI** instrument on the **Sentinel-5P satellite** (operated by the European Space Agency, ESA) are being used to map air pollution worldwide. One of the variables it provides information on is tropospheric nitrogen dioxide (NO2), which is linked to pollutant sources such as traffic and industrial activities.


<center>
<img src="https://github.com/eurodatacube/eodash-assets/blob/main/collections/N1_NO2/N1_NO2_legend.png?raw=true" width="400">

</center>

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;9cc22158-1b1d-4b15-b0c7-a868e4288282;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2024-11-18T00:00:00Z/2024-11-18T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="8.010646952488841" center=[76.27467813141472,28.104211017431737] projection="" animationOptions={duration:500}}-->
#### November 2024: Recording breaking pollution in Dehli
On November 18th, Delhi recorded pollution levels **more than 50 times higher** than the World Health Organization’s recommended safe limit, creating a public health emergency that forced school closures and restricted outdoor activities. In several areas of the city, residents wore masks outdoors and authorities issued health advisories.

<center> <img src="https://d3i6fh83elv35t.cloudfront.net/static/2024/11/2024-11-18T110820Z_218494839_RC2H7BA6CRTJ_RTRMADP_3_INDIA-POLLUTION-1024x683.jpg" width="400">

<span style="font-size:15px;">New Delhi, India, November 18, 2024. Credit: REUTERS/Anushree Fadnavis</span>

</center>

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;4d82f040-8a45-42a0-9a50-f697b71b6890;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2024-12-30T00:00:00Z/2024-12-30T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.886748420127219" center=[76.9451509006783,28.464743066069005] projection="" animationOptions={duration:500}}-->
#### December 2024: Gurugram 
In the city of Gurugram, located just southwest of New Delhi and part of the National Capital Region, high-density residential and industrial zones contribute to significant local emissions. 

<center>
<img src="https://github.com/eurodatacube/eodash-assets/blob/main/collections/N1_NO2/N1_NO2_legend.png?raw=true" width="400">

</center>

In December, the city experienced a pronounced peak in NO2 concentrations, mirroring the severe pollution trends observed in the capital  the previous month.

<center> <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-6/stories/DEMO_BiDS25/NO2_Gurugram.png?raw=true" width="400">

<span style="font-size:15px;"> NO2 Concentrations in Gurugram city</span>

</center>



### <!--{ layers='[{ "type": "Group", "properties": { "id": "OverlayGroup", "title": "Overlay Layers" }, "layers": [ { "type": "Tile", "properties": { "id": "overlay_bright;:;EPSG:3857", "title": "Overlay labels" }, "source": { "type": "XYZ", "url": "//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png", "projection": "EPSG:3857" } } ] },{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Balaton;:;2023-06-01T00:00:00Z;:;Lakes_S2L2A;:;EPSG:3857","title":"Lakes_S2L2A"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-2-L2A-TRUE-COLOR"],"TILED":true,"TIME":"2024-11-20T00:00:00Z/2024-12-19T23:59:59Z"}},"visible":true}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"osm","title":"Background"},"source":{"type":"OSM"}}]}]' zoom="13.124544090347598" center=[76.75465522601512,28.07212891153435] projection="" animationOptions={duration:500}}-->

#### Pollution sources
Air pollution in northern India rises every year, particularly in winter, as farmers burn crop residue in agricultural areas. The burning coincides with colder temperatures, which trap the smoke in the air. The smoke is then blown into cities, where auto emissions add to the pollution. 
<center>
<img src="https://images.indianexpress.com/2017/10/crop-burning.jpg" width="400">
	
<span style="font-size:15px;">Delhi air pollution: A (crop) burning issue. Credit:  Express Photo -  Harmeet Sodhi)</span>
</center>


For NO2, the main sources are mainly human-made, with the combustion of fossil fuels in vehicles, power plants, and industrial processes being the largest contributors. In this true color imagery from **Sentinel-2** (bands 4, 3, and 2 — red, green, and blue; operated by the European Space Agency, ESA), the view is similar to what the human eye sees. While it is not specifically designed for detecting fires, crop burning, or measuring specific gases, it allows observation of smoke plumes coming from surrounding areas of New Delhi. **Despite what Sentinel-2 shows, one cannot determine the exact type of gas or confidently trace its source**.




#
### Human Activity

A city's **nighttime lights** can offer a reliable proxy for economic activity, population density, and energy consumption. During global-scale events, such as COVID-19, lockdown measures imposed worldwide affected human activities, adding another element of pressure on the dynamics of a city's population.

## Human Activity <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"JAXA_Nighttimelevel_Urban"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"JAXA-NIGHTTIMELEVEL-URBAN","styles":"","format":"image/png","time":"2019-01-01T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="9.9224951359818" center=[77.3150332431322,28.490762442253427] animationOptions={duration:500}}-->

#### Delhi in Lockdown
The **Nighttime Light Urban (NLTU)** dataset, derived from Suomi NPP satellite observations operated jointly by NASA and the National Oceanic and Atmospheric Administration (NOAA), captures the intensity of artificial lighting across urban areas—a reliable proxy for economic activity, population density, and energy consumption.

<center> <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-6/stories/DEMO_BiDS25/nightime_legend.png?raw=true" width="400">

<span style="font-size:15px;"> City's activity</span>
</center>

In 2020, the city’s nighttime lights dimmed dramatically. Nighttime light levels decreased by 20–30% across much of Delhi, as shown by the **shades of pink and red**, which correspond to areas where a **decline in nighttime light levels occurred**. This indicates a **presumed reduction in social activity** during the lockdown period, potentially reflecting decreased commercial activity as shops, restaurants, and businesses closed. This decline could be linked to significant economic hardship, widespread job losses, and changes in daily life that affected millions of Delhi residents.

The heart of the city, however, shown in **white**, may represent unchanged activity, while some residential areas on the outskirts, indicated by **violet, and blue** shades, show an increase in nighttime lights and presumably increased activity, possibly reflecting people **staying at home due to lockdown measures**.

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"grdi-vnl-slope-raster;:;povmap-grdi-v1_VNL-slope_2012-01-01_2020-12-31;:;grdi-vnl-slope-raster;:;EPSG:3857","title":"grdi-vnl-slope-raster"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/grdi-vnl-slope-raster/povmap-grdi-v1_VNL-slope_2012-01-01_2020-12-31.tif&resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0.0,100.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.9224951359818" center=[77.3150332431322,28.490762442253427] projection="" animationOptions={duration:500}}-->
#### Nighttime lights patterns...a link with poverty?
Also based on Visibile Nighttime Lights (VNL) data, but for a longer period of time, from 2012 and 2020, researchers at NASA Socioeconomic Data and Applications Center (SEDAC). calculated a linear regression slope for each area (the VNL slope) and used it as a measure of change in nighttime brightness over time. Higher slope values, indicating **increasing brightness, were interpreted as signs of decreasing deprivation**, while lower or negative slope values, indicating decreasing brightness, were taken as signs of **increasing deprivation**. This VNL slope forms one of six key indicators used to create a groundbreaking global index of poverty and deprivation across the world.
<center> <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/grdi-v1-built/cm_legend.png" width="400">

</center>
 

#
### Vulnerability
Mapping inequality:  a groundbreaking approach to mapping multidimensional poverty and deprivation: the **Global Gridded Relative Deprivation Index (GRDI) Version 1**.

## Vulnerability <!--{ as="eox-map" mode="tour" }-->


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"grdi-v1-raster;:;povmap-grdi-v1_2010-01-01_2021-12-31;:;grdi-v1-raster;:;EPSG:3857","title":"grdi-v1-raster"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/grdi-v1-raster/povmap-grdi-v1_2010-01-01_2021-12-31.tif&resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0.0,100.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.9224951359818" center=[77.3150332431322,28.490762442253427] projection="" animationOptions={duration:500}}-->
#### The Global Gridded Relative Deprivation Index (GRDI)
 The Global Gridded Relative Deprivation Index (GRDI) Version 1 maps **multidimensional-based poverty and deprivation**, providing a comprehensive view of relative deprivation by assigning each pixel (~1 km) a value between **0 (lowest deprivation) and 100 (highest deprivation)**.
 
 
<center> <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/grdi-v1-built/cm_legend.png" width="400">

</center>
 

Together wiht the nighgtime intensity trends from 2012-2020, it integrates of **five more distinct dimensions** of deprivation into a single, spatially explicit index, combinining demographic indicators (**child dependency ratio**), health outcomes (**infant mortality rates**), human development measures (**Subnational Human Development Index**) and urbanization patterns (**built-up area ratios**).  
 

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"grdi-v1-raster;:;povmap-grdi-v1_2010-01-01_2021-12-31;:;grdi-v1-raster;:;EPSG:3857","title":"grdi-v1-raster"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/grdi-v1-raster/povmap-grdi-v1_2010-01-01_2021-12-31.tif&resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0.0,100.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="3.362222743276048" center=[9.878639621810514,31.523043898653583] projection="" animationOptions={duration:500}}-->
#### Mapping poverty and deprivation Worldwide
 The GRDI dataset allows to capture the complex, interconnected nature of deprivation that traditional income-based poverty measures often miss, representing a **groundbreaking approach** to mapping multidimensional poverty and deprivation across the world - while **combining the power of satellite data and ground truth, national levels data**.
 
 <center> <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/grdi-v1-built/cm_legend.png" width="400">
</center>
 
#
### Open datasets used in the story


## <!--{ as="div" }--> Open Science
The ability to track extreme heat, hazardous air, human activity, and deprivation in megacities like New Delhi depends on open access to global satellite datasets and socio-economic indicators. Missions and datasets from ESA, NASA, JAXA, and open research consortia provide the information needed to monitor risks and resilience in urban environments.

| **Name**                                                | **Type**            | **Agency / Provider**                     | **Description / Usage**                                                                                                                        |
| ------------------------------------------------------- | ------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Gridded Population of the World (GPW)](https://www.earthdata.nasa.gov/data/projects/gpw)**               | Dataset             | NASA SEDAC                                | High-resolution population density estimates (persons/km²); used to map New Delhi’s extreme population concentrations. **[View on EO dashboard](https://eodashboard.org/explore/?x=0.0000&y=0.0000&z=2.4939&datetime=2020-05-01&template=expert&indicator=NASAPopulation)**                         |
| **[GCOM-C (SGLI Land Surface Temperature)](https://eolp.jaxa.jp/GCOM-C_SGLI_L3M_LST_1month_1-24deg.html)**              | Satellite/Mission   | JAXA                                      | Provides land surface temperature (LST); used to analyze Delhi’s record-breaking June 2024 heatwave.                                           |
| **[Sentinel-5P (TROPOMI)](https://sentinels.copernicus.eu/missions/sentinel-5)**                               | Satellite/Mission   | ESA                                       | Measures atmospheric pollution, including NO₂; used to monitor Delhi and Gurugram’s severe air quality in late 2024. **[View on EO Dashboard](https://eodashboard.org/explore/?x=-0.0917&y=39.4096&z=2.4939&datetime=2025-06-23&template=expert&indicator=N1_NO2)**                          |
| **[Sentinel-2](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2)**                                          | Satellite/Mission   | ESA / Copernicus                          | Optical true-color imagery (RGB bands); used to observe smoke plumes from crop burning near Delhi.                                             |
| **[SUOMI-NPP (VIIRS Nighttime Lights)](https://www.nature.com/articles/s41597-024-04228-6)**                  | Satellite/Mission   | NASA / NOAA                               | Captures nighttime light intensity; used to assess urban activity changes during the COVID-19 lockdown in Delhi. **[View on EO Dashboard](https://eodashboard.org/explore/?x=-87.5000&y=41.8288&z=5.7522&datetime=2019-01-01&template=expert&indicator=NTLU)**                              |
| **[Global Gridded Relative Deprivation Index (GRDI v1)](https://earth.gov/data-catalog/grdi-v1)** | Dataset             | World Bank & partners (hosted on VEDA)    | Multidimensional poverty index (0–100); integrates health, demographics, urbanization, and economic proxies; used to map deprivation in Delhi. **[View on EO dashboard](https://eodashboard.org/explore/?x=-0.0917&y=39.4096&z=2.4939&datetime=2010-01-01&template=expert&indicator=GRDI2)**  |
| **OpenStreetMap (OSM)**                                 | Dataset/Tool        | Open-source                               | Used for base map overlays in urban visualization.                                                                                             |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)**                         | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Provides base layers and visualization tools for interactive storytelling of urban health indicators.                                          |



## Jupyter notebook used:
<iframe width="100%" height="600" src="https://esa-eodashboards.github.io/eodashboard-notebooks/notebooks/nightlights-notebook/night-lights-blending" frameborder="0"></iframe>
Access the notebook to analyze trends, and uncover patterns of human activity on a location of your choice.

