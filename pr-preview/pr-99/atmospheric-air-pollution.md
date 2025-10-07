---
cover-image: https://live.staticflickr.com/67/352250460_ee2f9e5565_b.jpg
date: 2025-01-01 
theme: theme_name
tags: some,tags

---

# Monitoring Atmospheric Aerosol in Asia-Pacific <!--{ as="img" mode="hero" src="https://live.staticflickr.com/67/352250460_ee2f9e5565_b.jpg" }-->
### Operational Aerosol Observation Using Himawari-AHI and Multi-Platform Integration <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Atmospheric Aerosols

Atmospheric aerosols, suspended particles including dust, smoke, and pollution, affect air quality, visibility, and public health over vast distances. Desert dust from the Gobi and Taklamakan can travel thousands of kilometers to reach populated areas in China, Korea, and Japan. Wildfire emissions from Siberia and Southeast Asia create regional smoke episodes. Urban pollution from industrial centers impacts multiple countries, with concentrations changing in response to economic development and regulatory policies.

Satellite remote sensing now provides the observational capability needed to track these phenomena across regional scales. Japan's Himawari-8/9 Advanced Himawari Imager (AHI) delivers observations over the Asia-Pacific region at 10-minute intervals, while complementary instruments including MODIS, GCOM-C/SGLI, Korea's GEMS, and ESA's EarthCARE provide additional temporal coverage, spectral information, and vertical profiling capabilities.


## Earth Observations <!--{ as="eox-map" mode="tour" }-->


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;10a0b9e3-6c77-408f-a200-a7fcf2a637b1;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2025-06-23T00:00:00Z/2025-06-23T23:59:59Z"}},"opacity":0}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false}]}]' zoom="7.073885363053369" center=[81.26858135898271,38.099545486981754] projection="" animationOptions={duration:500}}-->
#### Dust storms
 Dust storms, Yellow sand from Gobi and Taklamakan Desert, travels for a long distance from central to eastern Asia and the Pacific Ocean.
 
 <center>

<img src="https://eoimages.gsfc.nasa.gov/images/imagerecords/1000/1925/Taklimakan.jpg" width="600">
<span style="font-size:15px;">Caption.Source:</span>
</center>

<center>

<img src=" https://eoimages.gsfc.nasa.gov/images/imagerecords/1000/1925/Taklimakan.jpg" width="600">
<span style="font-size:15px;">Taklimakan Desert.Seen in this true-color Moderate-resolution Imaging Spectroradiometer (MODIS) image from October 27, 2001.</span>
</center>


 (imagery: AHI RGB (or dust index) images for broad areas e.g., from 80E-150E 15N-60N in Yellow dust events). It affects public health and visibility in China, Korea and Japan when they reach the surface (EarthCARE ATLID profile in dust event in Spring 2025, e.g., around 25 March 2025). If there were long-distance transport events from the Saharan Desert after 2025, we can connect MTG/FCI and AHI images. (In different aspects, when it reaches the ocean, it can give nutrients for the phytoplankton and may influence the carbon cycle in the ocean.)
 
 
 ### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;10a0b9e3-6c77-408f-a200-a7fcf2a637b1;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2025-06-23T00:00:00Z/2025-06-23T23:59:59Z"}},"opacity":0}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false}]}]' zoom="5.809520483392844" center=[122.62510333899236,28.72158738444547] projection="" animationOptions={duration:500}}-->
#### Urban pollution
Urban pollution over Asian big cities. It affects public health and visibility in cities of India, Thailand, Vietnam, Indonesia, China, Korea, Japan, and so on (imagery: AHI AOT image over South Asia or East Asia). It was decreased in some cities by political regulations; however, it is still increasing in some cities with rising industry. For example, aerosols have decreased in China, recent decades, but are still large especially over other cities (imagery: AOT time series from 2000 to 2025 around cities (MODIS+AHI+SGLI+..), and figures or a movie of NO2 over east Asia by Korean GEMS?).


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"NO2_daily;:;10a0b9e3-6c77-408f-a200-a7fcf2a637b1;:;NO2_daily;:;EPSG:3857","title":"NO2_daily"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["AWS_NO2-VISUALISATION"],"TILED":true,"TIME":"2025-06-23T00:00:00Z/2025-06-23T23:59:59Z"}},"opacity":0}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false}]}]' zoom="5.572157740011712" center=[134.990105633207,-1.1761414742908727] projection="" animationOptions={duration:500}}-->
#### Wildfires
Wildfires in east Siberia and southeast Asia cause dense smoke sometimes. It also affects public health and visibility for the residents around the area (imagery: AHI AOT of wild fire events in east Siberia (e.g., Jul-Aug 2021) and Thailand (e.g., April 2023) for example). It is said that wildfires may increase under the coming climate change, cause land cover and surface albedo (imagery: an example of burned area images by GCOM-C) which influence the radiation budget, and the emitted smoke can make negative feedback shading solar light, on the other emitted GHG enhance the global warming. 


