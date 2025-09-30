# urbanhealth
# Urban health  <!--{ as="img" data-fallback-src="" mode="hero" src="https://live.staticflickr.com/3600/3409479660_54cc371386_b.jpg " }-->
### Satellite-based perspective in megacities <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->

## Introduction
New Delhi, in India, is one of the most densely populated urban centers on Earth. Like many megacities, it faces numerous challenges that threaten the health and well-being of its residents. By combining satellite observations with ground-based and socio-economic data, researchers can track these challenges across key dimensions of urban health. This story shows how the combination of free, open data and tools from three space agencies, **ESA, NASA, and JAXA** can be used to measure and monitor the city’s vulnerability to extreme heat, hazardous air, and the cascading risks of life in a megacity under strain.


## Nighttime lights - a proxy for human activity?
The Nighttime Light Urban (NLTU) dataset, derived from Suomi NPP satellite observations operated jointly by NASA and the National Oceanic and Atmospheric Administration (NOAA), captures the intensity of artificial lighting across urban areas—a reliable proxy for economic activity, population density, and energy consumption.In 2020, the city’s nighttime lights dimmed dramatically. Nighttime light levels **decreased & across much of Delhi**, as shown by the shades of **pink and red**, indicating a presumed reduction in social activity during the lockdown period. 

<center> <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-6/stories/DEMO_BiDS25/nightime_legend.png?raw=true" width="400">
<span style="font-size:15px;"> City's activity</span>
</center>


## Map Example 
<!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":true,"interpolate":false,"sources":[{"url":"https://obs.eu-nl.otc.t-systems.com/eodashboardtutorial/Nighttimelevel_Urban_h25v06_2019-2022.tif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=DZPPJ23QUW6DYLDCKEYP%2F20250926%2Feu-nl%2Fs3%2Faws4_request&X-Amz-Date=20250926T091004Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=22944453c07c039627a18a1d0774b0a5cdb68ed1f1efc3f5e9a2899fce030566"}]},"properties":{"id":"Nightlights-test;:;2023-01-01T00:00:00Z;:;0","title":"Nightlights demo"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="10.148925294772047" center=[77.22961239280947,28.51322687714932] projection="" }-->

