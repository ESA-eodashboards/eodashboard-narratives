---
cover-image: https://climate.esa.int/media/images/Fire-CCI-banner_1920.min-1280x200.format-jpeg.jpg
date: 2025-01-01
theme: theme_name
tags: wildfire,resilience,vegetation,NDVI,recovery,ESA CCI,DeepESDL
official: false

---

# Raging Fires and Back to Baseline? Tracking vegetation resilience from space <!--{ as="img" mode="hero" src="https://climate.esa.int/media/images/Fire-CCI-banner_1920.min-1280x200.format-jpeg.jpg" }-->
## Authors: <img src="https://media.licdn.com/dms/image/v2/D5603AQFXeYHSklrkgg/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1702715854161?e=1796256000&v=beta&t=MjEEqQmy-rfCDJr3s6Dobuhz5UQlQdq6mJU9iz--EcI" alt="Jakob Everke" width="48" height="48" style="border-radius:50%;object-fit:cover;vertical-align:middle;margin:0 6px 0 12px;"/>Jakob Everke ¹ <a href="https://www.linkedin.com/in/jakob-everke-7671432a5/?locale=en-US" target="_blank" rel="noopener" style="margin-left:4px;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="18" height="18" style="vertical-align:middle;"/></a>, <img src="https://media.licdn.com/dms/image/v2/C5603AQHxqA4EF8NRxA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1654228641493?e=1796256000&v=beta&t=_OPEjCvG9NiITbC16eXDTQrEhyajlT2SH7VmfR5w9gs" alt="Kyzer Gerez" width="48" height="48" style="border-radius:50%;object-fit:cover;vertical-align:middle;margin:0 6px 0 12px;"/>Kyzer Gerez ¹ <a href="https://www.linkedin.com/in/kyzer-gerez/" target="_blank" rel="noopener" style="margin-left:4px;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="18" height="18" style="vertical-align:middle;"/></a>, <img src="https://media.licdn.com/dms/image/v2/D4E03AQGWybSn5yfMdA/profile-displayphoto-shrink_400_400/B4EZSI5GbUHgAo-/0/1737463457921?e=1796256000&v=beta&t=LClhiuKJF2DqCQ3bNUsxUyFOPS-ZIDrBrqFfZEJPcgc" alt="Jonas Siethoff" width="48" height="48" style="border-radius:50%;object-fit:cover;vertical-align:middle;margin:0 6px 0 12px;"/>Jonas Siethoff ² <a href="https://www.linkedin.com/in/jonas-siethoff/" target="_blank" rel="noopener" style="margin-left:4px;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="18" height="18" style="vertical-align:middle;"/></a><!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
> ¹ Technische Universität Wien ² Ruhr-University Bochum

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in **November 2026**. It was developed by a team from the **Vienna University of Technology** and **Ruhr University Bochum**.*

##  <!--{ nav="false"}-->
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/TU_Wien-Logo.svg/960px-TU_Wien-Logo.svg.png" alt="TU Wien" height="80" style="margin: 0 15px;"/>
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyTL97S8-CF2SFUzfZfvT5Lq-xG_tWv8Kp2ZvFegOf83EpvQUkF5PmUTQ&s=10" alt="RUB" height="80" style="margin: 0 15px;"/>
</p>


## Challenge
Forests cover about a third of the Earth's land surface ([Forzieri et al., 2022](https://doi.org/10.1038/s41586-022-04959-9)), and their importance goes far beyond their spatial footprint. They support biodiversity, store carbon and benefit human health ([Watson et al., 2018](https://doi.org/10.1038/s41559-018-0490-x)). As major carbon sinks that also regulate regional temperature and hydrology, they are central to both climate mitigation and adaptation ([Reek et al., 2026](https://doi.org/10.1126/science.ads4361)).

Over long timescales, forests have adapted to specific disturbance regimes, defined by the type, severity and frequency of fire, and these regimes have shaped their resilience ([Johnstone et al., 2016](https://doi.org/10.1002/fee.1311)). Climate change is now altering these regimes by making disturbances more frequent and more severe. This is a concern because changed disturbance regimes can fundamentally alter how forest ecosystems are structured and how they function ([Seidl et al., 2016](https://doi.org/10.1111/1365-2664.12511)).

Forests matter, and fire pressure on them is rising. This raises a central question: **how well can forests absorb these shocks and return to their prior state?** Answering it is essential for judging whether forests will remain functional and stable in the long term. The capacity to resist disruption, recover structure and function, and persist under changing conditions is called *resilience*, and it is the focus of this story.


## Objective
The objective of this study was to measure how vegetation responds to and recovers from wildfire in **[STUDY AREA]** between **[YEAR]** and **[YEAR]**. For every burned pixel, we asked three questions:

1. **Did the fire cause a significant drop in vegetation?**
2. **How large was that drop?**
3. **Did the vegetation recover, and how long did it take?**


## Where did it burn?
<p align="center">
  <img src="https://raw.githubusercontent.com/JSiethoff/eodashboard-narratives/JSiethoff/burn-severity-wip/assets/annual_burn_area.gif" alt="Animation of burned areas per year, [YEAR]–[YEAR]" width="100%"/>
</p>

*Burned areas per year from the ESA CCI Fire Burned Area product, **[YEAR]–[YEAR]**.*

**[1–2 sentences: how much burned in total, which years or regions stand out.]**


## Back to baseline? A journey through time <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2018-06-20T00:00:00Z;:;Normalized Difference Vegetation Index (NDVI) (Weekly Average) ;:;EPSG:3857","title":"Normalized Difference Vegetation Index (NDVI) (Weekly Average) "},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG%3A3857&time=2018-06-20T00%3A00%3A00Z&vmin=0&vmax=0.9&cbar=RdYlGn","projection":"EPSG:3857","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}},"visible":true}]' zoom="4.5" center=[16.39,47.19] projection="" animationOptions={duration:1500}}-->
#### Europe's vegetation from space
NDVI across Europe (8-day composite): green means dense, healthy vegetation, red means sparse or stressed vegetation. We now zoom into a burned area in Spain and compare it before and after the fire. **[1 sentence on why this area.]**

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2018-12-19T00:00:00Z;:;Normalized Difference Vegetation Index (NDVI) (Weekly Average) ;:;EPSG:3857","title":"Normalized Difference Vegetation Index (NDVI) (Weekly Average) "},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG%3A3857&time=2018-12-19T00%3A00%3A00Z&vmin=0&vmax=0.9&cbar=RdYlGn","projection":"EPSG:3857","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}},"visible":true}]' zoom="6" center=[-5.125,40.375] projection="" animationOptions={duration:1500}}-->
#### Spain: before the fire  **[DATE]**
**[Place name, ecosystem type, e.g. Mediterranean pine forest.]** This is the vegetation during the two years before the fire, the baseline we measure recovery against.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2019-06-19T00:00:00Z;:;Normalized Difference Vegetation Index (NDVI) (Weekly Average) ;:;EPSG:3857","title":"Normalized Difference Vegetation Index (NDVI) (Weekly Average) "},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG%3A3857&time=2019-06-19T00%3A00%3A00Z&vmin=0&vmax=0.9&cbar=RdYlGn","projection":"EPSG:3857","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}},"visible":true}]' zoom="6" center=[-5.125,40.375] projection="" animationOptions={duration:1500}}-->
#### Spain: right after the fire  **[DATE]**
**[Fire year.]** NDVI dropped by **[X %]** compared with the baseline, a significant impact.


## Results
#### Two places, two stories
The curves below show the vegetation trend (NDVI with the seasonal cycle removed) for the two areas from the map tour. The grey band is the pre-fire baseline, the red band is the fire year. The dashed lines show the baseline mean (grey), the threshold for a significant drop (red) and the 80 % recovery line (green).

<p align="center">
  <img src="LINK_TO_TREND_PLOT_SPAIN" alt="NDVI trend, Spain" width="48%" style="margin: 0 1%;"/>
  <img src="LINK_TO_TREND_PLOT_UKRAINE" alt="NDVI trend, Ukraine" width="48%" style="margin: 0 1%;"/>
</p>

*Left: **[place]**, Spain. Right: **[place]**, Ukraine.*

**[2–3 sentences comparing the two curves: size of the drop, speed of recovery, whether the baseline was reached.]**

#### The big picture
| | **Spain** | **Ukraine** | **All burned pixels** |
| --- | --- | --- | --- |
| Burned pixels analysed | [n] | [n] | [n] |
| Significant drop after fire | [X %] | [X %] | [X %] |
| Median drop (in % of baseline NDVI) | [X %] | [X %] | [X %] |
| Recovered (80 % of loss regained) | [X %] | [X %] | [X %] |
| Median time to recovery | [X months] | [X months] | [X months] |
| False alarms in placebo test | – | – | [X %] |

**[Optional: more trend plots for other areas. Copy the image block above.]**


## Data and Methods
#### The satellite behind the data
<p align="center">
  <img src="LINK_TO_SATELLITE_IMAGE" alt="[Satellite name]" width="60%"/>
</p>

*NASA's Terra satellite. Its MODIS instrument (together with its twin on Aqua) provides both the burned-area data and the vegetation indices used in this story. Image: [credit].*

MODIS has been observing the whole Earth every one to two days since 2000. This long, consistent record is what makes it possible to follow vegetation before, during and for years after a fire. **[Optional: 1 more sentence.]**

#### Datasets
Vegetation dynamics were analysed with five vegetation indicators from the **Earth System Data Cube (ESDC) v3.0.1**, provided through DeepESDL. The ESDC combines satellite-derived and model-based environmental datasets into one consistent data cube at **0.25° spatial resolution (about 25 km)** and **8-day temporal resolution**. Burned areas come from the ESA CCI Fire product.

| **Dataset** | **What it measures** | **Source** | **Resolution** | **Period** | **Used for** |
| --- | --- | --- | --- | --- | --- |
| **ESA CCI Fire Burned Area** (FireCCI51, v5.1) | Burned area | MODIS Terra | 250 m, monthly | 2001–[YEAR] | Burned pixels and fire year |
| **NDVI** | Vegetation greenness and photosynthetic activity | MODIS Terra/Aqua (MCD43C4, C6.1) | 0.25°, 8 days | 2000–2021 | Main indicator: baseline, fire impact, recovery |
| **kNDVI** | Non-linear NDVI, less prone to saturation in dense vegetation | MODIS Terra/Aqua (MCD43C4, C6.1) | 0.25°, 8 days | 2000–2021 | **[e.g. comparison with NDVI]** |
| **NIRv** | Near-infrared reflectance of vegetation, linked to canopy structure and productivity | MODIS Terra/Aqua (MCD43C4, C6.1) | 0.25°, 8 days | 2000–2021 | **[…]** |
| **SIF (GOSIF)** | Sun-induced chlorophyll fluorescence, a direct signal of photosynthesis | GOSIF (OCO-2, MODIS, reanalysis) | 0.25°, 8 days | 2000–2021 | **[…]** |
| **GPP** | Gross primary productivity: carbon taken up by photosynthesis | FLUXCOM | 0.25°, 8 days | 2001–2020 | **[…]** |

DeepESDL dataset ID of the burned-area product: `esacci.FIRE.mon.L3S.BA.MODIS.Terra.MODIS_TERRA.v5-1.pixel`

#### Methodology workflow
<div style="display:flex;flex-wrap:wrap;align-items:stretch;justify-content:center;gap:6px;margin:1.5rem 0;font-family:inherit;">
  <div style="flex:1 1 150px;max-width:190px;background:#fdecea;border-top:5px solid #c0392b;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">🔥</div>
    <div style="font-weight:700;margin:4px 0;">1. Burned pixels</div>
    <div style="font-size:0.85rem;">ESA CCI Fire<br/>pixels + fire year</div>
  </div>
  <div style="align-self:center;font-size:1.6rem;color:#888;">➜</div>
  <div style="flex:1 1 150px;max-width:190px;background:#fdf0e3;border-top:5px solid #e67e22;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">📈</div>
    <div style="font-weight:700;margin:4px 0;">2. NDVI time series</div>
    <div style="font-size:0.85rem;">ESDC NDVI<br/>STL → trend</div>
  </div>
  <div style="align-self:center;font-size:1.6rem;color:#888;">➜</div>
  <div style="flex:1 1 150px;max-width:190px;background:#fdf7dc;border-top:5px solid #d4a017;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">📏</div>
    <div style="font-weight:700;margin:4px 0;">3. Pre-fire baseline</div>
    <div style="font-size:0.85rem;">mean ± SD<br/>2 years before fire</div>
  </div>
  <div style="align-self:center;font-size:1.6rem;color:#888;">➜</div>
  <div style="flex:1 1 150px;max-width:190px;background:#eef6e2;border-top:5px solid #8bb93a;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">⚡</div>
    <div style="font-weight:700;margin:4px 0;">4. Fire impact</div>
    <div style="font-size:0.85rem;">drop below mean − 2 SD?<br/>+ placebo test</div>
  </div>
  <div style="align-self:center;font-size:1.6rem;color:#888;">➜</div>
  <div style="flex:1 1 150px;max-width:190px;background:#e3f3e6;border-top:5px solid #27ae60;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">🌱</div>
    <div style="font-weight:700;margin:4px 0;">5. Recovery</div>
    <div style="font-size:0.85rem;">80 % of loss regained?<br/>months to recovery</div>
  </div>
</div>

1. **Burned pixels:** identify all pixels that burned in a given year from the ESA CCI Fire product. The fire year is the unit of time, since no exact fire date is used.
2. **Time series and preprocessing:** extract the 8-day NDVI time series of each burned pixel and decompose it with STL (Seasonal-Trend decomposition using Loess). All further steps use the **trend** component, i.e. NDVI with the seasonal cycle removed.
3. **Pre-fire baseline:** the mean and standard deviation of the trend over the **two years before the fire year** ([White et al., 2017](https://doi.org/10.1016/j.rse.2017.03.035)).
4. **Fire impact:** the impact is **significant** if the lowest trend value within **24 months** after the start of the fire year falls more than **two standard deviations** below the baseline mean. To check how often this rule gives false alarms, we applied it to fire-free years before the actual fire (placebo test).
5. **Recovery:** a pixel counts as **recovered** once its trend has regained **80 % of the fire-induced loss**. Recovery time is counted in months from the start of the fire year. This follows the 80 % benchmark of White et al. (2017), scaled by the size of the disturbance as in the Recovery Indicator ([Kennedy et al., 2012](https://doi.org/10.1016/j.rse.2011.09.024)), because NDVI drops are much smaller than the NBR drops that the original metric was designed for.

#### Key parameters
| **Parameter** | **Value** | **Why** |
| --- | --- | --- |
| Baseline period | 2 years before the fire year | Following White et al. (2017) |
| Impact window | 0–24 months after 1 Jan of the fire year | Exact fire date unknown, so the whole fire year plus one year is covered |
| Significance threshold | Baseline mean − 2 SD | Drop clearly outside normal pre-fire variability |
| Recovery threshold | 80 % of the fire-induced loss regained | 80 % benchmark of White et al. (2017), scaled by disturbance size (Kennedy et al., 2012) |


## Conclusions
#### Key findings
- **[Finding 1, e.g. share of burned pixels with a significant drop.]**
- **[Finding 2, e.g. how many recovered and how fast.]**
- **[Finding 3, e.g. the difference between Spain and Ukraine.]**

#### Limitations
- NDVI reacts quickly to new green growth, so it can show recovery before the forest structure has actually returned: **spectral recovery is not the same as ecological recovery**.
- Only the fire year is known, not the exact fire date, so impact windows and recovery times are counted from 1 January of the fire year.
- One NDVI pixel covers about 25 × 25 km (0.25°), so a burned pixel usually also contains unburned land, which dampens the measured drop.
- Results are per pixel, not per fire event.

#### Outlook
The next step is to explain *why* recovery differs between burned areas. We plan to relate the recovery metrics to land cover (ESA CCI Land Cover) and post-fire climate conditions such as precipitation (ERA5). Building on that, these variables could be used to predict how strongly future fires would affect a given area and how well it would recover.


## Open Science
| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| --- | --- | --- | --- |
| **[ESA CCI Fire Burned Area – FireCCI51 (MODIS Terra, pixel)](https://climate.esa.int/en/projects/fire/)** | Dataset | ESA Climate Change Initiative | Monthly burned-area product at 250 m (v5.1, dataset ID `esacci.FIRE.mon.L3S.BA.MODIS.Terra.MODIS_TERRA.v5-1.pixel`), used to identify burned pixels and the fire year. |
| **[Earth System Data Cube v3.0.1](https://www.earthsystemdatalab.net/)** | Dataset | DeepESDL / ESDC | Vegetation indicators (NDVI, kNDVI, NIRv, SIF-GOSIF, GPP) at 0.25° and 8 days. NDVI time series of each burned pixel were decomposed with STL and used to derive the pre-fire baseline, fire impact and recovery. |
| **[DeepESDL](https://www.earthsystemdatalab.net/)** | Platform | ESA / Brockmann Consult | Cloud-based Jupyter environment used for data access, time-series extraction and the full analysis workflow. |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)** | Platform | EO Dashboard Consortium (ESA, NASA, JAXA) | Base layers, NDVI map layer and the narrative editor used to present this story. |
| **[statsmodels (STL)](https://www.statsmodels.org/)** | Tool | Open source | Seasonal-trend decomposition of the NDVI time series. **[Check that this is the STL implementation you used.]** |
| **[TOOL / LIBRARY](LINK)** | Tool | **[Provider]** | **[e.g. xarray, pandas, matplotlib: what it was used for]** |

#### Notebook
Access the notebook to reproduce the study workflow.
<iframe width="100%" height="600" src="LINK_TO_NOTEBOOK" frameborder="0"></iframe>

#### References
- Forzieri, G., Dakos, V., McDowell, N. G., Ramdane, A., & Cescatti, A. (2022). Emerging signals of declining forest resilience under climate change. *Nature*, 608, 534–539. https://doi.org/10.1038/s41586-022-04959-9

- Johnstone, J. F., Allen, C. D., Franklin, J. F., Frelich, L. E., Harvey, B. J., Higuera, P. E., Mack, M. C., Meentemeyer, R. K., Metz, M. R., Perry, G. L. W., Schoennagel, T., & Turner, M. G. (2016). Changing disturbance regimes, ecological memory, and forest resilience. *Frontiers in Ecology and the Environment*, 14, 369–378. https://doi.org/10.1002/fee.1311

- Kennedy, R. E., Yang, Z., Cohen, W. B., Pfaff, E., Braaten, J., & Nelson, P. (2012). Spatial and temporal patterns of forest disturbance and regrowth within the area of the Northwest Forest Plan. *Remote Sensing of Environment*, 122, 117–133. https://doi.org/10.1016/j.rse.2011.09.024

- Reek, J. E., Zohner, C. M., Smith, G. R., Cook-Patton, S. C., De Frenne, P., D'Odorico, P., Floriancic, M. G., Jackson, R. B., Jones, J. A., Kirchner, J. W., et al. (2026). More than mitigation: The role of forests in climate adaptation. *Science*, 391(6786), 669–678. https://doi.org/10.1126/science.ads4361

- Seidl, R., Spies, T. A., Peterson, D. L., Stephens, S. L., & Hicke, J. A. (2016). Searching for resilience: addressing the impacts of changing disturbance regimes on forest ecosystem services. *Journal of Applied Ecology*, 53(1), 120–129. https://doi.org/10.1111/1365-2664.12511

- Watson, J. E. M., Evans, T., Venter, O., Williams, B., Tulloch, A., Stewart, C., Thompson, I., Ray, J. C., Murray, K., Salazar, A., McAlpine, C., Potapov, P., Walston, J., Robinson, J. G., Painter, M., Wilkie, D., Filardi, C., Laurance, W. F., Houghton, R. A., … Lindenmayer, D. (2018). The exceptional value of intact forest ecosystems. *Nature Ecology & Evolution*, 2, 599–610. https://doi.org/10.1038/s41559-018-0490-x

- White, J. C., Wulder, M. A., Hermosilla, T., Coops, N. C., & Hobart, G. W. (2017). A nationwide annual characterization of 25 years of forest disturbance and recovery for Canada using Landsat time series. *Remote Sensing of Environment*, 194, 303–321. https://doi.org/10.1016/j.rse.2017.03.035


## Contributors
| **Role** | **Name** |
| --- | --- |
| Authors | Jakob Everke, Kyzer Gerez, Jonas Siethoff |
| Contributors | [Names] |
| Reviewers | [Names] |