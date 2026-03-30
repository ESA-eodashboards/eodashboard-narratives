---
cover-image: https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1200
date: 2025-01-01
theme: atmosphere
tags: urban-heat,machine-learning,earth-observation,digital-twins,climate-adaptation
official: false
---

# CLIM4Cities: from Citizen Science, Machine Learning and Earth Observation towards Urban Climate Services <!--{ as="img" mode="hero" src=https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1200" }-->
### Downscaling air and land surface temperature in urban areas using AI and satellite data <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## <!--{ nav="false" }-->
<div align="center">

*CLIM4Cities is an [European Space Agency (ESA)](https://www.esa.int)-funded project under the call for AI Trustworthy Applications for Climate (ESA Contract No. 4000143628/24/I-DT), developed by [CoLAB +ATLANTIC](https://www.colabatlantic.com/) and the [Danish Meteorological Institute (DMI)](https://www.dmi.dk/).*

</div>

## <!--{ nav="false" }-->
<p align="center">
  <img src="https://storage.googleapis.com/eurogoos-files/media/colab.png" alt="ESA" height="80" style="margin: 0 15px;"/>
  <img src="https://cdn-assets.inwink.com/a89460d8-e7a1-4b06-93c9-8eec92940ee6/4abd0cb8-0729-46db-88b2-26ded1caafda" alt="DMI" height="80" style="margin: 0 15px;"/>
</p>

## Urban Climate in a Changing World

As climate change prospects point towards the pressing need for local adaptation strategies, exposure to extreme weather events becomes one of the most important aspects in determining our society's resilience in the future. At the local level, these conditions are strongly influenced by the energy exchanges between the lower atmosphere and our strongly modified urban surfaces.

Three major societal pressures drive the need for better urban climate tools: **climate change**, **energy poverty**, and an **ageing population** — all of which amplify the risks associated with urban heat islands and extreme heat events. Existing Numerical Weather Prediction (NWP) models are too coarse, too slow, and too data-heavy to capture the fine-scale contrasts between urban neighbourhoods that matter most for local adaptation planning.

**CLIM4Cities** aims to pioneer the development of Machine Learning (ML) and Artificial Intelligence (AI) models designed to downscale air and land surface temperature predictions in urban areas — serving as a preliminary step towards cost-effective Integrated Urban Climate and Weather components for local Digital Twin Systems.

## The CLIM4Cities Approach

The methodology is grounded in a well-established framework (Lowry, 1977) which decomposes any near-surface air temperature measurement into three additive components:

**T = R + L + U**

where **R** is the regional or synoptic-scale contribution, **L** is the natural landscape contribution, and **U** is the artificial disturbance introduced by urban land use and land cover. This decomposition guides the selection of input predictors for the machine learning models.

Input data are drawn from three complementary sources: **citizens' weather station observations** (after rigorous quality control), **Earth Observation and GEO datasets** (including Sentinel-3 LST, Landsat 8/9, Local Climate Zones, imperviousness, tree cover density, and digital elevation), and **NWP reanalysis fields** (DANRA reanalysis for the regional background component). Three ML algorithms are benchmarked — a linear mixed-effects model (LMM), a random forest (RF), and a neural network (NN) — with the Random Forest emerging as the best performer.

## Satellite Observations over the Study Areas <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="11" center=[12.5683,55.6761] projection="" animationOptions={duration:500}}-->
#### Copenhagen, Denmark
**Copenhagen** is one of the four Danish metropolitan areas targeted in the CLIM4Cities proof of concept. The city's complex interplay of coastal proximity, dense urban fabric, and green infrastructure makes it an ideal testbed for the downscaling models. CLIM4Cities targets a **200 m resolution grid** — fine enough to resolve neighbourhood-level contrasts in air and land surface temperature.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Copenhagen_-_Aerial_view_%282010%29.jpg/1280px-Copenhagen_-_Aerial_view_%282010%29.jpg" width="400">
<span style="font-size:15px;">Aerial view of Copenhagen, Denmark</span>
</center>

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="11" center=[10.2039,56.1629] projection="" animationOptions={duration:500}}-->
#### Aarhus, Denmark
**Aarhus**, Denmark's second largest city, presents a different urban morphology from Copenhagen — a more compact historic centre surrounded by suburban expansion and significant coastal and forested areas. The CLIM4Cities model captures these spatial contrasts through Local Climate Zone (LCZ) classifications and topographic exposure indices.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Aarhus_aerial_2016.jpg/1280px-Aarhus_aerial_2016.jpg" width="400">
<span style="font-size:15px;">Aerial view of Aarhus, Denmark</span>
</center>

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="11" center=[9.9217,57.0488] projection="" animationOptions={duration:500}}-->
#### Aalborg, Denmark
**Aalborg** is situated in northern Jutland at the Limfjord estuary, introducing strong coastal and wind exposure effects into the urban climate signal. Topographic exposure per octant (TOPEX) is a key predictor in the CLIM4Cities model for this city, capturing how prevailing wind directions modulate local temperature patterns.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/forty/Aalborg_city.jpg/1280px-Aalborg_city.jpg" width="400">
<span style="font-size:15px;">Aalborg, Denmark</span>
</center>

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="11" center=[10.5018,57.7281] projection="" animationOptions={duration:500}}-->
#### Frederikshavn, Denmark
**Frederikshavn** is a smaller coastal city in northern Denmark and represents the more compact, lower-density end of the urban spectrum in the CLIM4Cities study. Its inclusion demonstrates the **scalability** of the approach beyond large metropolitan areas, a key design principle of the project.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Frederikshavn_harbour.jpg/1280px-Frederikshavn_harbour.jpg" width="400">
<span style="font-size:15px;">Frederikshavn, Denmark</span>
</center>

## Results

CLIM4Cities has developed the first version of its coupled ML-based near-surface Air Temperature (T2m) and Land Surface Temperature (LST) downscaling models, targeting the four Danish metropolitan areas described above.

For **LST downscaling**, Sentinel-3 LST and Synergy (NDVI) products trained multiple models, validated against Landsat 8/9. A hybrid Non-Linear DisTrad (NL-DisTrad) approach combined ML with disaggregation algorithms to capture spatial and vegetation-related temperature patterns. Seasonal performance varied, with R² of 0.67 (Summer), 0.51 (Spring), and 0.56 (Autumn).

For **T2m downscaling**, the Random Forest (RF) model performed best, optimised with a maximum depth of 50. Overall R² was 0.98, consistent during heatwaves but slightly lower (0.97) during cold waves. Mean Absolute Error (MAE) was 0.74K overall, 0.63K during heatwaves, and 0.81K during cold waves — confirming robust performance precisely when it matters most, under extreme heat conditions.

Compared to standard NWP outputs, the CLIM4Cities models are:
- **faster** — minutes to run daily or sub-daily, instead of hours
- **lighter** — MB of data per run, instead of GB
- **more detailed** — resolving contrasts between neighbourhoods at 200 m resolution
- **more accurate** — particularly during temperature extremes such as heatwaves

## Conclusions and Future Work

While the model estimates are inherently location-specific, this approach can be efficiently replicated in other locations with similar biogeographic conditions and available data. Future work will involve expanding the training data to a multi-year time series in other cities and testing the models' ability to generalise results through official weather stations available in all locations.

The urban climate response to climate change and urban development will also be addressed, particularly the **sensitivity of air and land surface temperature to green and blue infrastructure adaptation measures** — directly supporting local planners in evaluating the cooling potential of parks, street trees, water bodies, and permeable surfaces.

## <!--{ as="div" }--> Open Science

All datasets referenced in this story are freely and openly available. Sentinel-3 and Landsat data are distributed without charge through their respective open access portals. Citizen weather station data are quality-controlled and processed within the CLIM4Cities project framework.

| Name | Type | Agency / Provider | Description | Access/Source |
|---|---|---|---|---|
| [Copernicus Sentinel-3 LST & Synergy NDVI](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-3) | Dataset | ESA / Copernicus | Land Surface Temperature and NDVI synergy products used to train and validate the LST downscaling model at 200 m resolution | [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) |
| [Landsat 8/9](https://www.usgs.gov/landsat-missions) | Dataset | NASA / USGS | Used as validation reference for the downscaled LST product; 30 m resolution thermal infrared imagery | [USGS Earth Explorer](https://earthexplorer.usgs.gov/) |
| [DANRA Reanalysis](https://www.dmi.dk/danra/) | Dataset | DMI | Danish high-resolution regional reanalysis providing the synoptic background component (R) for the T2m ML model | [DMI Open Data](https://www.dmi.dk/friedata/observationer/) |
| [Copernicus Land Monitoring Service — Tree Cover Density (TCD)](https://land.copernicus.eu/pan-european/high-resolution-layers/forests/tree-cover-density) | Dataset | EEA / Copernicus | Percentage of tree cover used as urban greenness predictor in the ML model | [Copernicus Land Service](https://land.copernicus.eu/) |
| [Copernicus Land Monitoring Service — Imperviousness (IMD)](https://land.copernicus.eu/pan-european/high-resolution-layers/imperviousness) | Dataset | EEA / Copernicus | Degree of soil sealing used as urban land cover predictor in the ML model | [Copernicus Land Service](https://land.copernicus.eu/) |
| [Local Climate Zones (LCZ)](https://lcz-generator.rub.de/) | Dataset | Various / Community | Urban morphology classification used to characterise the local urban contribution (U) to the temperature signal | [LCZ Generator](https://lcz-generator.rub.de/) |
| [Citizen Weather Station Observations](https://wow.metoffice.gov.uk/) | Dataset | Citizens / IoT sensors | Crowdsourced near-surface air temperature observations used as the response variable in the ML model; quality-controlled via spatio-temporal clustering | Project-specific |
| [EOxCloudless Sentinel-2 Mosaic 2024](https://s2maps.eu/) | Dataset | EOX / ESA | Cloud-free Sentinel-2 basemap used for visualisation of the four Danish study areas | [s2maps.eu](https://s2maps.eu/) |