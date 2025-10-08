---
cover-image: https://ichef.bbci.co.uk/ace/standard/976/cpsprodpb/10678/production/_92329176_c0157414-lowland_rainforest_danum_valley_sabah-spl.jpg.webp
date: 2025-01-01
theme: theme_name
tags: some,tags

---

# Evaluating time series interpolation techniques for vegetation monitoring using remote sensing data <!--{ as="img" mode="hero" src="https://ichef.bbci.co.uk/ace/standard/976/cpsprodpb/10678/production/_92329176_c0157414-lowland_rainforest_danum_valley_sabah-spl.jpg.webp" }-->
### Authors: Denise Hick, Fran O'Leary and Mae Evan (Univeristy of Leeds) <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

# 
*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2025. It was developed by a team from University of Leeds.*

## Challenge
Vegetation Earth Observation (EO) time series are essential for monitoring ecosystem health, agricultural productivity, and the impacts of climate change. One of the most widely used indicators in this context is the **Normalised Difference Vegetation Index (NDVI)**, which measures vegetation greenness and health based on how plants reflect light in the red and near-infrared parts of the spectrum. Sensors like MODIS (Moderate Resolution Imaging Spectroradiometer), onboard NASA’s Terra and Aqua satellites, collect reflectance in these red and NIR bands, allowing NDVI to capture vegetation health over time.

<img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-7/stories/ScienceHub-Challenge-September-2025/time-series-interpolation/timesSeries_2.png?raw=true"/>
<p style="text-align:center;"><b>NDVI:</b> A proxy for vegetation health.</p>

However, NDVI time series often still contain residual **effects of clouds, even after data pre-processing**. The accuracy of NDVI reconstructions can also vary depending on land cover type, as different landscapes show distinct patterns in seasonality, amplitude, and the rate of vegetation change (Julien and Sobrino, 2019). Ensuring **accurate interpolation** is therefore crucial for producing reliable insights into vegetation dynamics and environmental change.

<div style="text-align: center;">
    <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-7/stories/ScienceHub-Challenge-September-2025/time-series-interpolation/timeSeries_1.png?raw=true" width="500"/>
    <p><b>Missing data:</b> The impacts of cloud coverage on NDVI acquisitions.</p>
</div>


## Objective
The objective of this study was to design and implement a reproducible framework to compare multiple time series interpolation techniques on vegetation EO datasets with multiple, artificially introduced & user-defined temporal gaps.


## Use cases <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-12-31T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-31T00:00:00Z&vmin=-1&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="3.690591246872277" center=[-11.394579610360768,28.506295590162736] projection="" animationOptions={duration:500}}-->
#### Five contrasting ecosystems
Five different types of forests were used as case studies to test and compare interpolation methods. Each site represents different vegetation types, climatic conditions, and seasonal patterns, providing a comprehensive assessment of method performance under real-world variability.

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-12-31T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-31T00:00:00Z&vmin=-1&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="6.254309813092814" center=[-64.55063927299018,-5.039648675050586] projection="" animationOptions={duration:500}}-->
#### The Amazon forest
The Amazon Forest, the world’s largest tropical rainforest, is characterized by a humid, aseasonal climate with persistently high precipitation and serves as a major global carbon reservoir, storing approximately 123 billion tonnes of carbon (NOAA, 2021).
<a href="https://commons.wikimedia.org/wiki/File:Amazon_Manaus_forest.jpg" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Amazon_Manaus_forest.jpg/960px-Amazon_Manaus_forest.jpg?20091220154622" 
       alt="Elmstein Am Möllberg" />
</a>
<p style="text-align:center;">
  <b>Amazon Forest:</b> View of Amazon basin forest north of Manaus, Brazil. <br>
  <small>Image credit: <a href="https://commons.wikimedia.org/wiki/File:Amazon_Manaus_forest.jpg" target="_blank">Phil P Harris</a></small>
</p>

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-12-31T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-31T00:00:00Z&vmin=-1&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="6.021064855421141" center=[-40.72037883145828,-8.190443898666047] projection="" animationOptions={duration:500}}-->
#### Caatinga Forest, Brazil
Encompassing the semi-arid region of northeastern Brazil, the Caatinga is the largest dry forest biome in South America and one of the most biodiverse dry forests globally. This seasonal tropical ecosystem exhibits pronounced climatic seasonality and variable precipitation across its ~100,000 km² extent, characterized by large seasonal fluxes of carbon, water, and other biogeochemical compounds.

<a href="https://www.latinamericareports.com/new-ucla-research-reveals-worrying-land-degradation-in-northeast-brazil/11869/" target="_blank">
  <img src="https://www.latinamericareports.com/wp-content/uploads/2025/07/Estrada_entre_Canudos_e_Jeremoabo_na_Bahia_Road_between_Canudos_and_Jeremoabo_in_Bahia_12182535453-1024x591.jpg" 
       alt="Elmstein Am Möllberg" />
</a>
<p style="text-align:center;">
  <b>Palatinate Forest Nature Park:</b> View to the north at the Möllbachweiher in Elmstein. <br>
  <small>Image credit: <a href="https://commons.wikimedia.org/wiki/File:Estrada_entre_Canudos_e_Jeremoabo_na_Bahia_Road_between_Canudos_and_Jeremoabo_in_Bahia_%2812182535453%29.jpg" target="_blank">A. Duarte</a></small>
</p>

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-12-31T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-31T00:00:00Z&vmin=-1&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="7.153104075250305" center=[8.589631563526611,49.79640091295067] projection="" animationOptions={duration:500}}-->
#### Palatinate Forest, Elmstein, Germany 
As Germany’s largest contiguous forest, the Palatinate Forest, including the Elmstein region, forms a core component of the Palatinate Forest–Vosges du Nord Biosphere Reserve. It is characterized by temperate mixed forests dominated by beech (Fagus sylvatica) and oak (Quercus spp.). This temperate ecosystem exhibits pronounced seasonality and moderate precipitation typical of Central European forest climates.
<a href="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Elmstein_Am_M%C3%B6llberg_001_2017_05_20.jpg/960px-Elmstein_Am_M%C3%B6llberg_001_2017_05_20.jpg?20190519064440" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Elmstein_Am_M%C3%B6llberg_001_2017_05_20.jpg/960px-Elmstein_Am_M%C3%B6llberg_001_2017_05_20.jpg?20190519064440" 
       alt="Elmstein Am Möllberg" />
</a>
<p style="text-align:center;">
  <b>Palatinate Forest Nature Park:</b> View to the north at the Möllbachweiher in Elmstein. <br>
  <small>Image credit: <a href="https://commons.wikimedia.org/wiki/File:Elmstein_Am_M%C3%B6llberg_001_2017_05_20.jpg" target="_blank">Friedrich Haag</a></small>
</p>


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-12-31T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-31T00:00:00Z&vmin=-1&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="7.79555872724114" center=[105.9056537023329,-7.151663183893675] projection="" animationOptions={duration:500}}-->
#### Muara Angke Mangrove Forest, Indonesia
The Muara Angke Mangrove Forest in Indonesia is a protected wildlife sanctuary and nature conservation area located at Kapuk Muara, Penjaringan, along Jakarta’s northern coast. This coastal tropical ecosystem is characterized by high seasonality and monsoonal precipitation typical of moist tropical mangrove forests.

<a href="https://commons.wikimedia.org/wiki/File:Monyet_Ekor_Panjang_Hutan_Mangrove_Angke.jpg" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Monyet_Ekor_Panjang_Hutan_Mangrove_Angke.jpg/960px-Monyet_Ekor_Panjang_Hutan_Mangrove_Angke.jpg?20200529104522" 
       alt="Monyet Ekor Panjang Hutan Mangrove Angke" />
</a>
<p style="text-align:center;">
  <b>Angke Mangrove Forest:</b> Monkey long tails in mangrove forest Angke. <br>
  <small>Image credit: <a href="https://commons.wikimedia.org/wiki/File:Monyet_Ekor_Panjang_Hutan_Mangrove_Angke.jpg" target="_blank">Sigarwengi</a></small>
</p>


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-12-31T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-31T00:00:00Z&vmin=-1&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="6.327652699530251" center=[-116.63503920729454,51.63812480402609] projection="" animationOptions={duration:500}}-->
#### Rockies Forest, Canada-USA
The North Central Rockies Forests, spanning parts of the northwestern United States and southwestern Canada, represent a boreal forest ecosystem dominated by conifers trees. This ecosystem exhibits pronounced seasonality and moderate precipitation and plays a critical role in carbon storage, hydrological regulation, and providing habitat for diverse wildlife, including elk, grizzly bears, and various bird species.

<a href="https://commons.wikimedia.org/wiki/File:Canadian_Rockies_-_Lake_Louise.jpg" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Canadian_Rockies_-_Lake_Louise.jpg/1200px-Canadian_Rockies_-_Lake_Louise.jpg?20090831175516" 
       alt="Monyet Ekor Panjang Hutan Mangrove Angke" />
</a>
<p style="text-align:center;">
  <b>Canadian Rockies:</b> Lake Louise. <br>
  <small>Image credit: <a href="https://commons.wikimedia.org/wiki/File:Canadian_Rockies_-_Lake_Louise.jpg" target="_blank">Harvey Barryson</a></small>
</p>







## Data and Methods
#### Dataset
- **Source**: NDVI (Normalized Difference Vegetation Index) data were obtained from the DeepESDL Earth System Datacube (ESDC) v.3.0.1, which is a curated dataset derived from MODIS Terra and Aqua satellites.
- **Temporal resolution**: 8-day intervals, providing a moderately high temporal sampling of vegetation dynamics.
- **Spatial resolution**: 0.25° (~28 km), which is suitable for large-scale ecosystem analysis.
- **Preprocessing**: NDVI values are derived from BRDF-corrected daily reflectance data, which reduces biases caused by view angle, atmospheric conditions, and illumination.

#### Methodology workflow
**NDVI time series (2017–2022)** were extracted at selected sites. Then, **artificial gaps** of varying lengths (3 weeks, 3 months, 6 months) were introduced to mimic missing data. Four **interpolation methods**, namely Linear, Cubic Spline, Gaussian Process, and Seasonal Cycles, were used to reconstruct the gaps. 
###### Interpolation techniques:
* **Linear**  – connects data points with straight lines.
* **Cubic Spline** – uses piecewise cubic polynomials to create a smooth curve through the points.
* **Gaussian Process Regression** – a Bayesian method that models data as a smooth curve with uncertainty estimates.
* **Climatology Fill (Seasonal)** – fills missing data using averages from the same period in past years.

<div style="text-align: center;">
    <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-7/stories/ScienceHub-Challenge-September-2025/time-series-interpolation/timeSeries_3.png?raw=true" width="500"/>
    <p><b>Interpolation techniques:</b> Examples in Caatinga Forest.</p>
</div>



Finally, these methods were evaluated based on **accuracy (R², RMSE)** and **computational efficiency**. Overall, this approach allows a controlled comparison of interpolation methods under different ecosystem types (high vs. low seasonality) and gap durations, enabling an evaluation of both accuracy and computational performance.





## Results
Best interpolation teechnique depends on land cover being observed and length of missing data gap:
<div style="text-align: center;">
    <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-7/stories/ScienceHub-Challenge-September-2025/time-series-interpolation/timeSeries_4.png?raw=true"/>
    <p><b>Summary of results:</b> Metrics for each forest type and missing data gap.</p>
</div>


* **1)** Interpolation accuracy decreases as gap length increases, with short gaps generally producing better results. 
* **2)** **Gaussian Process Regression (GPR)** provides strong performance but requires roughly twice the processing time compared to other methods. 
* **3)** For seasonal vegetation patterns, the most effective interpolation method **depends on gap length**: Linear and Cubic Spline work best for **short gaps**, while Seasonal and GPR methods are more reliable for **longer gaps**. 
* **4)** For non-seasonal patterns, either **Linear** or **Seasonal** interpolation performs best.

## Conclusions
The current data (~28 km) is suitable for large forests, but finer-resolution data (e.g., Sentinel-2) is needed for smaller or more fragmented areas. The choice of interpolation method depends on the characteristics of the time series and the length of missing data gaps. Future work will focus on testing these methods on high-resolution datasets across diverse ecosystems and incorporating additional environmental variables to improve accuracy.


## <!--{ as="div" }--> Open Science
| **Name**                                                                                                                                                 | **Type**            | **Agency / Provider**                     | **Description / Usage**                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[NDVI](https://eodashboard.org/explore/?x=0&y=0&z=2.5&datetime=2020-01-01&template=expert&indicator=NDVI)** | Dataset             | DeepESDL / ESDC                           | Normalized Difference Vegetation Index (NDVI) time series. |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)**                                    | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Provides base layers and visualization tools for interactive exploration of NDVI and other Earth observation indicators.                                                                                                                |

#### Notebook
Access the notebook to reproduce the study workflow.
<iframe width="100%" height="600" src="https://esa-eodashboards.github.io/eodashboard-notebooks/notebooks/openchallangenotebook-team-5-challenge-3-timeserie//" frameborder="0"></iframe>


#### References
- Julien, Y. and Sobrino, J.A. (2019). Optimizing and comparing gap-filling techniques using simulated NDVI time series
from remotely sensed global data. International Journal of Applied Earth Observation and Geoinformation, 76, pp.93-111

- de Oliveira, M.L.; dos Santos, C.A.C.; Santos, F.A.C.; de Oliveira, G.; Santos, C.A.G.; Bezerra, U.A.; de B. L. Cunha,
J.E.; da Silva, R.M. Evaluation of Water and Carbon Estimation Models in the Caatinga Biome Based on Remote
Sensing. Forests 2023, 14, 828. https://doi.org/10.3390/f14040828.






