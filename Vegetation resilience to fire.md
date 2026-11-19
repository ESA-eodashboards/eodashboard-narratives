---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
official: false

---

# Raging Fires and Back to Baseline? Tracking vegetation resilience from space <!--{ as="img" mode="hero" src="https://climate.esa.int/media/images/Fire-CCI-banner_1920.min-1280x200.format-jpeg.jpg" }-->
## Authors: <img src="https://media.licdn.com/dms/image/v2/D5603AQFXeYHSklrkgg/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1702715854161?e=1796256000&v=beta&t=MjEEqQmy-rfCDJr3s6Dobuhz5UQlQdq6mJU9iz--EcI" alt="Jakob Everke" width="48" height="48" style="border-radius:50%;object-fit:cover;vertical-align:middle;margin:0 6px 0 12px;"/>Jakob Everke ¹ <a href="https://www.linkedin.com/in/jakob-everke-7671432a5/?locale=en-US" target="_blank" rel="noopener" style="margin-left:4px;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="18" height="18" style="vertical-align:middle;"/></a>, <img src="https://media.licdn.com/dms/image/v2/C5603AQHxqA4EF8NRxA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1654228641493?e=1796256000&v=beta&t=_OPEjCvG9NiITbC16eXDTQrEhyajlT2SH7VmfR5w9gs" alt="Kyzer Gerez" width="48" height="48" style="border-radius:50%;object-fit:cover;vertical-align:middle;margin:0 6px 0 12px;"/>Kyzer Gerez ¹ <a href="https://www.linkedin.com/in/kyzer-gerez/" target="_blank" rel="noopener" style="margin-left:4px;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="18" height="18" style="vertical-align:middle;"/></a>, <img src="https://media.licdn.com/dms/image/v2/D4E03AQGWybSn5yfMdA/profile-displayphoto-shrink_400_400/B4EZSI5GbUHgAo-/0/1737463457921?e=1796256000&v=beta&t=LClhiuKJF2DqCQ3bNUsxUyFOPS-ZIDrBrqFfZEJPcgc" alt="Jonas Siethoff" width="48" height="48" style="border-radius:50%;object-fit:cover;vertical-align:middle;margin:0 6px 0 12px;"/>Jonas Siethoff ² <a href="https://www.linkedin.com/in/jonas-siethoff/" target="_blank" rel="noopener" style="margin-left:4px;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="18" height="18" style="vertical-align:middle;"/></a><!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
> ¹ TU Wien ² Ruhr University Bochum

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in **November 2026**. It was developed by a team from **TU Wien** and **Ruhr University Bochum**.*

##  <!--{ nav="false"}-->
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/TU_Wien-Logo.svg/960px-TU_Wien-Logo.svg.png" alt="TU Wien" height="80" style="margin: 0 15px;"/>
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/cb063564046a2aa8df8d315372a12bc6a7fedad9/assets/JSiethoff/Ruhr-Universitaet-BochumLogoBlauscreenrgb-1795096537261.png" alt="Ruhr University Bochum" height="80" style="margin: 0 15px;"/>
</p>


## Challenge
Forests cover about **a third of the Earth's land surface** ([Forzieri et al., 2022](https://doi.org/10.1038/s41586-022-04959-9)), yet their importance reaches far beyond that footprint. They support **biodiversity**, store **carbon** and benefit **human health** ([Watson et al., 2018](https://doi.org/10.1038/s41559-018-0490-x)). As major **carbon sinks** that also regulate regional **temperature and hydrology**, they are central to **climate mitigation and adaptation** ([Reek et al., 2026](https://doi.org/10.1126/science.ads4361)).

Over long timescales, forests have adapted to specific **disturbance regimes**, defined by the type, severity and frequency of fire, and these regimes have shaped their **resilience** ([Johnstone et al., 2016](https://doi.org/10.1002/fee.1311)). **Climate change** is now making disturbances **more frequent and more severe**, which can fundamentally alter forest **structure and function** ([Seidl et al., 2016](https://doi.org/10.1111/1365-2664.12511)).

This raises a central question: **how well can forests absorb these shocks and return to their prior state?** The answer decides whether forests stay functional and stable in the long term. The capacity to **resist** disruption, **recover** structure and function, and **persist** under changing conditions is called ***resilience***, and it is the focus of this story.

## Objective
The objective of this study was to measure how vegetation responds to and recovers from wildfire across **Europe** between **2003 and 2022**. For every burned grid cell, we asked three questions:

1. **Did the fire cause a significant drop in vegetation?**
2. **How large was that drop?**
3. **Did the vegetation recover, and how long did it take?**

Finally, we compared the results between **land-cover types** to see which vegetation recovers fastest.


## Where did it burn?
<p align="center">
  <img src="https://raw.githubusercontent.com/JSiethoff/eodashboard-narratives/JSiethoff/burn-severity-wip/assets/annual_burn_area.gif" alt="Animation of burned areas per year, [YEAR]–[YEAR]" width="100%"/>
</p>

*Total burned area across Europe per year, 2003–2022, from the ESA CCI Fire Burned Area product.*

**[1–2 sentences: how much burned in total, which years or regions stand out.]**


## Vegetation in motion <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-06-06T00:00:00Z;:;Normalized Difference Vegetation Index (NDVI) (Weekly Average) ;:;EPSG:3857","title":"Normalized Difference Vegetation Index (NDVI) (Weekly Average) "},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG%3A3857&time=2021-06-06T00%3A00%3A00Z&vmin=-0.5&vmax=1&cbar=RdYlGn","projection":"EPSG:3857","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="3.8" center=[15,52] projection="" animationOptions={duration:1500}}-->
#### Europe in summer
June 2021. **Green** means dense, active vegetation; **red** means sparse or dormant vegetation. This is **NDVI**, one of the five vegetation indices we use to track fire impact and recovery.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-12-31T00:00:00Z;:;Normalized Difference Vegetation Index (NDVI) (Weekly Average) ;:;EPSG:3857","title":"Normalized Difference Vegetation Index (NDVI) (Weekly Average) "},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG%3A3857&time=2021-12-31T00%3A00%3A00Z&vmin=-0.5&vmax=1&cbar=RdYlGn","projection":"EPSG:3857","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="3.8" center=[15,52] projection="" animationOptions={duration:1500}}-->
#### Europe in winter
Six months later, December 2021. Much of Europe has turned red: vegetation follows the **seasons**. To find the fire signal, we first remove this seasonal cycle from every time series.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-06-06T00:00:00Z;:;Normalized Difference Vegetation Index (NDVI) (Weekly Average) ;:;EPSG:3857","title":"Normalized Difference Vegetation Index (NDVI) (Weekly Average) "},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG%3A3857&time=2021-06-06T00%3A00%3A00Z&vmin=-0.5&vmax=1&cbar=RdYlGn","projection":"EPSG:3857","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="6" center=[-4.0,40.0] projection="" animationOptions={duration:1500}}-->
#### Spain
**[1 sentence: typical land cover, e.g. Mediterranean shrubland, pine and oak forest, and why it is fire-prone.]**
<img src="LINK_TO_IMAGE_SPAIN_VEGETATION" alt="Typical vegetation in Spain" width="100%" style="border-radius:8px;margin-top:0.5rem;"/>

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"ndvi_deepESDL;:;2021-06-06T00:00:00Z;:;Normalized Difference Vegetation Index (NDVI) (Weekly Average) ;:;EPSG:3857","title":"Normalized Difference Vegetation Index (NDVI) (Weekly Average) "},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/ndvi/{z}/{y}/{x}?crs=EPSG%3A3857&time=2021-06-06T00%3A00%3A00Z&vmin=-0.5&vmax=1&cbar=RdYlGn","projection":"EPSG:3857","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }","tileGrid":{"tileSize":[256,256],"origin":[-20037508.342789244,20037508.342789244],"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063,9.554628535647032,4.777314267823516,2.388657133911758,1.194328566955879,0.5971642834779395,0.29858214173896974,0.14929107086948487,0.07464553543474244,0.03732276771737122,0.01866138385868561,0.009330691929342804],"matrixIds":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"extent":[-20037508.342789244,-20037508.342789244,20037508.342789244,20037508.342789244]}}}]' zoom="5" center=[67.0,48.0] projection="" animationOptions={duration:1500}}-->
#### Kazakhstan
**[1 sentence: typical land cover, e.g. steppe grassland, and how it differs from Spain.]**
<img src="LINK_TO_IMAGE_KAZAKHSTAN_VEGETATION" alt="Typical vegetation in Kazakhstan" width="100%" style="border-radius:8px;margin-top:0.5rem;"/>


## Results
#### How hard did the fire hit?
<p align="center">
  <img src="LINK_TO_SEVERITY_MAP" alt="Map of burn severity across Europe" width="100%"/>
</p>

*Fire severity: share of the burnable area in each 0.25° cell that burned (maximum over 2003–2022).*

**[1–2 sentences: where the drop was largest or smallest.]**

#### Back to baseline?
<p align="center">
  <img src="LINK_TO_TIMESERIES_1" alt="Vegetation trend of a burned cell" width="48%" style="margin: 0 1%;"/>
  <img src="LINK_TO_TIMESERIES_2" alt="Vegetation trend of a burned cell" width="48%" style="margin: 0 1%;"/>
</p>

***[Vegetation index]** trend (seasonal cycle removed) of burned cells. Grey: the three years before the fire (baseline). Red: the fire year. Dashed lines: baseline level (grey), threshold for a significant drop (red), 80 % recovery line (green).*

**[1–2 sentences: what the curves show, e.g. one recovers within X months, the other does not return to baseline.]**

#### Who bounces back fastest?
<p align="center">
  <img src="LINK_TO_CHART_1" alt="Recovery compared between vegetation types" width="48%" style="margin: 0 1%;"/>
  <img src="LINK_TO_CHART_2" alt="Recovery compared between vegetation types" width="48%" style="margin: 0 1%;"/>
</p>

*Left: **[what chart 1 shows, e.g. recovery time per vegetation type]**. Right: **[what chart 2 shows, e.g. share of recovered cells per vegetation type]**.*

<p align="center">
  <img src="LINK_TO_CHART_3" alt="Recovery compared between vegetation types" width="48%" style="margin: 0 1%;"/>
  <img src="LINK_TO_CHART_4" alt="Recovery compared between vegetation types" width="48%" style="margin: 0 1%;"/>
</p>

*Left: **[chart 3]**. Right: **[chart 4]**. **[Delete this row if not needed.]***

**[1–2 sentences: which vegetation types recover fastest or slowest.]**

## Data and Methods
#### The satellite behind the data
<p align="center">
  <img src="https://terra.nasa.gov/wp-content/uploads/2024/01/Terra-Year-In-Review-Background-Padlet_v25.png" alt="NASA Terra satellite" width="60%"/>
</p>

*NASA's Terra satellite. Its **MODIS** instrument, together with its twin on Aqua, provides the burned-area data and the reflectance behind the vegetation indices used in this story. Image: NASA.*

MODIS has been observing the whole Earth every one to two days since 2000. This **long, consistent record** is what makes it possible to follow vegetation before, during and for years after a fire.

#### Datasets
Burned areas come from the **ESA CCI Fire** gridded burned-area product. Vegetation dynamics were analysed with **five vegetation indicators** from the **Earth System Data Cube (ESDC) v3.0.1**, provided through DeepESDL. Both datasets share the same **0.25° grid (about 25 km)**, so every burned grid cell can be matched directly to its vegetation time series.

| **Dataset** | **What it measures** | **Source** | **Resolution** | **Period used** | **Used for** |
| --- | --- | --- | --- | --- | --- |
| **ESA CCI Fire Burned Area** (gridded, v5.1) | Burned area per grid cell, also split by vegetation class | MODIS Terra | 0.25°, monthly | 2003–2022 | Burned cells, fire year, fire severity and dominant vegetation type |
| **NDVI** | Vegetation greenness and photosynthetic activity | MODIS Terra/Aqua (MCD43C4, C6.1) | 0.25°, 8 days | 2000–2021 | Vegetation indicator: baseline, fire impact, recovery |
| **kNDVI** | Non-linear NDVI, less prone to saturation in dense vegetation | MODIS Terra/Aqua (MCD43C4, C6.1) | 0.25°, 8 days | 2000–2021 | Vegetation indicator: baseline, fire impact, recovery |
| **NIRv** | Near-infrared reflectance of vegetation, linked to canopy structure and productivity | MODIS Terra/Aqua (MCD43C4, C6.1) | 0.25°, 8 days | 2000–2021 | Vegetation indicator: baseline, fire impact, recovery |
| **SIF (GOSIF)** | Sun-induced chlorophyll fluorescence, a direct signal of photosynthesis | GOSIF (OCO-2, MODIS, reanalysis) | 0.25°, 8 days | 2000–2021 | Vegetation indicator: baseline, fire impact, recovery |
| **GPP** | Gross primary productivity: carbon taken up by photosynthesis | FLUXCOM | 0.25°, 8 days | 2001–2020 | Vegetation indicator: baseline, fire impact, recovery |

The vegetation types come directly from the Fire CCI product, which reports for each cell how much of the burned area fell into each land-cover class. Each burned cell is assigned the class with the **largest burned area**.

#### Methodology workflow
<div style="display:flex;flex-wrap:wrap;align-items:stretch;justify-content:center;gap:6px;margin:1.5rem 0;font-family:inherit;">
  <div style="flex:1 1 130px;max-width:170px;background:#fdecea;border-top:5px solid #c0392b;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">🔥</div>
    <div style="font-weight:700;margin:4px 0;">1. Burned cells</div>
    <div style="font-size:0.85rem;">ESA CCI Fire<br/>+ quality filters</div>
  </div>
  <div style="align-self:center;font-size:1.6rem;color:#888;">➜</div>
  <div style="flex:1 1 130px;max-width:170px;background:#fdf0e3;border-top:5px solid #e67e22;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">📈</div>
    <div style="font-weight:700;margin:4px 0;">2. Vegetation indices</div>
    <div style="font-size:0.85rem;">5 ESDC indicators<br/>STL → trend</div>
  </div>
  <div style="align-self:center;font-size:1.6rem;color:#888;">➜</div>
  <div style="flex:1 1 130px;max-width:170px;background:#fdf7dc;border-top:5px solid #d4a017;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">📏</div>
    <div style="font-weight:700;margin:4px 0;">3. Pre-fire baseline</div>
    <div style="font-size:0.85rem;">mean ± SD<br/>3 years before fire</div>
  </div>
  <div style="align-self:center;font-size:1.6rem;color:#888;">➜</div>
  <div style="flex:1 1 130px;max-width:170px;background:#eef6e2;border-top:5px solid #8bb93a;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">⚡</div>
    <div style="font-weight:700;margin:4px 0;">4. Fire impact</div>
    <div style="font-size:0.85rem;">drop below<br/>mean − 2 SD?</div>
  </div>
  <div style="align-self:center;font-size:1.6rem;color:#888;">➜</div>
  <div style="flex:1 1 130px;max-width:170px;background:#e3f3e6;border-top:5px solid #27ae60;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">🌱</div>
    <div style="font-weight:700;margin:4px 0;">5. Recovery</div>
    <div style="font-size:0.85rem;">80 % of loss regained?<br/>months to recovery</div>
  </div>
  <div style="align-self:center;font-size:1.6rem;color:#888;">➜</div>
  <div style="flex:1 1 130px;max-width:170px;background:#e3eef6;border-top:5px solid #2e86c1;border-radius:10px;padding:12px;color:#222;text-align:center;">
    <div style="font-size:1.8rem;">🌳</div>
    <div style="font-weight:700;margin:4px 0;">6. Land-cover comparison</div>
    <div style="font-size:0.85rem;">recovery times<br/>by land-cover class</div>
  </div>
</div>

1. **Burned cells:** select all 0.25° cells in Europe that burned between 2003 and 2022 in the ESA CCI Fire product. To keep only reliable, clearly burned cells, a cell must have at least **90 % observed area**, at least **70 % burnable area** and at least **1 km² burned area**, and its dominant burned vegetation class must be **forest or natural vegetation mosaic** (croplands, grasslands, shrublands, urban and other classes are excluded). **Fire severity** is the share of the burnable area in a cell that burned.
2. **Time series and preprocessing:** extract the 8-day time series of the five vegetation indicators for each burned cell and decompose them with **STL** (Seasonal-Trend decomposition using Loess). All further steps use the **trend** component, i.e. the signal with the seasonal cycle removed. Cells with more than 20 % missing values are skipped.
3. **Pre-fire baseline:** the mean and standard deviation of the trend over the **three years before the fire year**.
4. **Fire impact:** the impact is **significant** if the lowest trend value within **24 months** after the start of the fire year falls more than **two standard deviations** below the baseline mean.
5. **Recovery:** a cell counts as **recovered** once its trend has regained **80 % of the fire-induced loss**. Recovery time is counted in months from the start of the fire year. This follows the 80 % benchmark of [White et al. (2017)](https://doi.org/10.1016/j.rse.2017.03.035), scaled by the size of the disturbance as in the Recovery Indicator ([Kennedy et al., 2012](https://doi.org/10.1016/j.rse.2011.09.024)), because vegetation-index drops are much smaller than the NBR drops that the original metric was designed for.
6. **Land-cover comparison:** recovery times are compared between the dominant **land-cover classes** of the burned cells.

## Conclusions
#### Key findings
- **[Finding 1, e.g. share of burned cells with a significant drop.]**
- **[Finding 2, e.g. how many recovered and how fast.]**
- **[Finding 3, e.g. which land-cover classes recover fastest or slowest.]**

#### Limitations
- Vegetation indices such as NDVI react quickly to new green growth, so they can show recovery before the forest structure has actually returned: **spectral recovery is not the same as ecological recovery**.
- Only the fire year is known, not the exact fire date, so impact windows and recovery times are counted from 1 January of the fire year.
- One grid cell covers about 25 × 25 km (0.25°), so a burned cell usually also contains unburned land, which dampens the measured drop.
- Results are per grid cell, not per fire event.

#### Outlook
The next step is to explain *why* recovery differs between burned areas. We plan to relate the recovery metrics to post-fire climate conditions such as precipitation (ERA5).


## Open Science
| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| --- | --- | --- | --- |
| **[ESA CCI Fire Burned Area (gridded, v5.1)](https://climate.esa.int/en/projects/fire/)** | Dataset | ESA Climate Change Initiative | Monthly burned area on a 0.25° grid (`ESACCI-L4_FIRE-BA-MODIS-2001-2022-fv5.1.zarr`), used for burned cells, fire year, fire severity and dominant vegetation type. |
| **[Earth System Data Cube v3.0.1](https://www.earthsystemdatalab.net/)** | Dataset | DeepESDL / ESDC | Vegetation indicators NDVI, kNDVI, NIRv, SIF-GOSIF and GPP at 0.25° and 8 days (`esdc-8d-0.25deg-1x720x1440-3.0.1.zarr`), used to derive the pre-fire baseline, fire impact and recovery. |
| **[DeepESDL](https://www.earthsystemdatalab.net/)** | Platform | ESA / Brockmann Consult | Cloud-based Jupyter environment used for data access, time-series extraction and the full analysis workflow. |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)** | Platform | EO Dashboard Consortium (ESA, NASA, JAXA) | Base layers, NDVI map layer and the narrative editor used to present this story. |
| **[statsmodels](https://www.statsmodels.org/)** | Tool | Open source | STL decomposition of the vegetation time series. |
| **[xcube](https://xcube.readthedocs.io/)** | Tool | Open source | Access to the Earth System Data Cube on DeepESDL. |
| **[ESA Climate Toolbox](https://climate.esa.int/en/data/toolbox/)** | Tool | ESA Climate Change Initiative | Access to the ESA CCI Fire product. |
| **xarray, pandas, matplotlib, seaborn, cartopy** | Tool | Open source | Data handling, plots and maps. |

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