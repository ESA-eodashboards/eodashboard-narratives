---
cover-image: https://placehold.co/600x400/png
date: 2026-03-25
theme: water
tags: SMOS, salinity, soil moisture
official: true
collections: SMOS_soil_moisture, SMOS_ocean_salinty

---

# SMOS: Tracking Water Cycle from Space <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2009/09/smos_in_orbit3/10259802-2-eng-GB/SMOS_in_orbit_card_medium.jpg" }-->
How one satellite measures two of the most fundamental variables of Earth's water cycle: Ocean Salinity and Soil Moisture <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## <!--{ nav="false" }-->
<div align="center">

*This trilateral story, produced in collaboration by the [European Space Agency (ESA)](https://www.esa.int), the [National Aeronautics and Space Administration (NASA)](https://www.nasa.gov/), and the [Japan Aerospace Exploration Agency (JAXA)](https://global.jaxa.jp/), is part of the joint narratives featured on [EO Dashboard](https://eodashboard.org/), showcasing the power of open Earth observation data.*

</div>


  ## <!--{ nav="false" }-->
<p align="center">
  <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/logos/esa.jpg" alt="ESA" height="80" style="margin: 0 15px;"/>
  <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/logos/nasa.jpeg" alt="NASA" height="80" style="margin: 0 15px;"/>
  <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/logos/jaxa.jpeg" alt="JAXA" height="80" style="margin: 0 15px;"/>
</p>

## Introducting SMOS: the ESA's Water Mission
 Text describing SMOS history, goal and it's evolution.
 <center>
<img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2014/11/global_soil_moisture/14997474-2-eng-GB/Global_soil_moisture_pillars.jpg" width="550">
<span style="font-size:15px;">Image of SMOS and/or variables</span>
</center>
 
## Earth observations of the Water Cycle

Introduction to the water cycle
 
#### Ocean Salinity
 
Description of this variable and its observation via remote sensing.

#### Soil Moisture
 
Description of this variable and its observation via remote sensing.
 
  ## <!--{ nav="false" }-->
Final description explaining how both variables provide a  **global view of the water cycle**.

 
 
## Ocean Salinity from Space <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"smos_ocean_salinity;:;2023-12-27T00:00:00Z;:;SMOS Ocean Salinity;:;EPSG:3857","title":"SMOS Ocean Salinity"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/smos-os/SSS_corr/{z}/{y}/{x}?crs=EPSG:3857&time=2023-12-27T00:00:00Z&vmin=0&vmax=50&cbar=jet","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="2.860311054919482" center=[4.480756603666212,16.62148967513167] projection="" animationOptions={duration:500}}-->


#### Overview of global Sea Surface Salinty
Introduction to global trends and regions (e.g.: tropical regions, easaly depictable fresh water regions). Description of interpreatation of the color/what's been seen.

 
<center>
<img src="https://climate.esa.int/media/images/CCI_SSS_global_map.width-1200.jpg" width="500">
<span style="font-size:15px;">Some image supporting this.</span>
</center>

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"smos_ocean_salinity;:;2023-12-27T00:00:00Z;:;SMOS Ocean Salinity;:;EPSG:3857","title":"SMOS Ocean Salinity"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/smos-os/SSS_corr/{z}/{y}/{x}?crs=EPSG:3857&time=2023-12-27T00:00:00Z&vmin=0&vmax=50&cbar=jet","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="6.021691575679171" center=[15.646761427648777,57.68236553757578] projection="" animationOptions={duration:500}}-->
#### Use case/example 1
Text describing the current step of the tour and why it is interesting what the map shows currently
Examples that could be mentioned:
- Sea surface salinity as indicator of El Nino
- SSS as indicator of mosoon dynamics

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"smos_ocean_salinity;:;2023-01-04T00:00:00Z;:;SMOS Ocean Salinity;:;EPSG:3857","title":"SMOS Ocean Salinity"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/smos-os/SSS_corr/{z}/{y}/{x}?crs=EPSG:3857&time=2023-01-04T00:00:00Z&vmin=0&vmax=50&cbar=jet","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="4.748342412710123" center=[384.25036622532616,77.42302595750823] projection="" animationOptions={duration:500}}-->
#### Use case/example 2
Text describing the current step of the tour and why it is interesting what the map shows currently
Examples that could be mentioned:
- Sea surface salinity as indicator of El Nino
- SSS as indicator of mosoon dynamics
#
 
 
## Soil Moisture from Space <!--{ as="eox-map" mode="tour" }-->
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"smos_soil_moisture;:;2023-12-06T00:00:00Z;:;SMOS Soil Moisture;:;EPSG:3857","title":"SMOS Soil Moisture"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/smos-sm/Soil_Moisture/{z}/{y}/{x}?crs=EPSG:3857&time=2023-12-06T00:00:00Z&vmin=0&vmax=1&cbar=jet","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="2.8603110549194817" center=[0,-5.400124791776761e-13] projection="" animationOptions={duration:500}}-->
#### Measuring Soil Moisture: The Global Picture
Introduction to global trends and regions (e.g.: tropical regions, easaly depictable fresh water regions). Description of interpreatation of the color/what's been seen.

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"smos_soil_moisture;:;2023-01-04T00:00:00Z;:;SMOS Soil Moisture;:;EPSG:3857","title":"SMOS Soil Moisture"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/smos-sm/Soil_Moisture/{z}/{y}/{x}?crs=EPSG:3857&time=2023-01-04T00:00:00Z&vmin=0&vmax=1&cbar=jet","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="5.105026079341846" center=[25.82622600738743,-3.26248072342662] projection="" animationOptions={duration:500}}-->
#### Use case 1/example
Text describing the current step of the tour and why it is interesting what the map shows currently
Examples that could be mentioned:
- persistent dryness vs consistently moist conditions
- seasonal variability
- some anomalous event
- drought monitoring and food security



### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a xmlns:dct=\"http://purl.org/dc/terms/\" href=\"https://s2maps.eu\" target=\"_blank\" property=\"dct:title\">Sentinel-2 cloudless - s2maps.eu</a> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"https://eox.at\" target=\"_blank\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"},"preload":null},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"smos_soil_moisture;:;2023-11-01T00:00:00Z;:;SMOS Soil Moisture;:;EPSG:3857","title":"SMOS Soil Moisture"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/smos-sm/Soil_Moisture/{z}/{y}/{x}?crs=EPSG:3857&time=2023-11-01T00:00:00Z&vmin=0&vmax=1&cbar=jet","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"},"preload":null}]}]' zoom="5.105026079341846" center=[25.82622600738743,-3.26248072342662] projection="" animationOptions={duration:500}}-->
#### Use case 2/example
Text describing the current step of the tour and why it is interesting what the map shows currently
Examples that could be mentioned:
- persistent dryness vs consistently moist conditions
- seasonal variability
- some anomalous event
- drought monitoring and food security

 
## <!--{ as="div" }-->

### Conclusion: Two Variables, One Mission, One Water Cycle
 

 
## <!--{ as="div" }--> Open Science
 
All datasets referenced in this story are freely and openly available. ESA CCI data products are distributed without charge through the CCI Open Data Portal and partner archives. No registration is required for the soil moisture dataset; ocean salinity data are accessible through CATDS and the CCI Open Data Portal.
 
| **Name** | **Type** | **Agency / Provider** | **Description** | **Access** |
|---|---|---|---|---|
| **[ESA CCI Sea Surface Salinity v5.5](https://climate.esa.int/en/projects/sea-surface-salinity/)** | Dataset | ESA CCI / LOCEAN (CNRS) | Merged L-band SSS from SMOS, Aquarius & SMAP; 2010–2023; global 0.25°; weekly & monthly | [CCI Open Data Portal](https://climate.esa.int/en/odp/) |
| **[ESA CCI Soil Moisture v09.2 (COMBINED)](https://climate.esa.int/en/projects/soil-moisture/)** | Dataset | ESA CCI / TU Wien | Merged active-passive microwave SM; 1978–Dec 2024; global 0.25°; daily | [CEDA Archive](https://archive.ceda.ac.uk/) |
| **[ESA CCI Soil Moisture v09.2 (PASSIVE)](https://climate.esa.int/en/projects/soil-moisture/)** | Dataset | ESA CCI / TU Wien | Passive-only SM product (includes SMOS); 1978–Dec 2024 | [CEDA Archive](https://archive.ceda.ac.uk/) |
| **[SMOS Level-3 Daily Soil Moisture](https://earth.esa.int/eogateway/missions/smos)** | Dataset | ESA / CATDS-CESBIO | Native SMOS L3 SM product; daily global | [CATDS](https://www.catds.fr/) |
| **[SMOS Level-3 Ocean Salinity](https://earth.esa.int/eogateway/missions/smos)** | Dataset | ESA / CATDS | Native SMOS L3 SSS product; daily global | [CATDS](https://www.catds.fr/) |
| **[Copernicus Climate Data Store — SM (C3S)](https://cds.climate.copernicus.eu/)** | Dataset | ECMWF / Copernicus | Near-real-time CCI SM product; updated every 10 days | [CDS](https://cds.climate.copernicus.eu/) |
| **[SMOS Mission — Earth Online](https://earth.esa.int/eogateway/missions/smos)** | Mission page | ESA | Full mission description, data products, documentation | [earth.esa.int](https://earth.esa.int/eogateway/missions/smos) |
| **[CCI Open Data Portal](https://climate.esa.int/en/odp/)** | Platform | ESA CCI | Access to all CCI ECV data records | [climate.esa.int](https://climate.esa.int/en/odp/) |
 


 

## References
 

 
## Contributors
 
