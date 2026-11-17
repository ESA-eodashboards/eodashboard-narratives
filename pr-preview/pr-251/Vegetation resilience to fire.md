---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
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
The objective of this study was to measure how quickly vegetation recovers after wildfire in **[STUDY AREA]**. Using satellite data from **[YEAR]** to **[YEAR]**, we:

- identified burned areas from the ESA CCI Fire Burned Area product,
- extracted vegetation-index time series for each burned area, and
- derived recovery metrics (recovery time and recovery rate) relative to each area's pre-fire baseline.


## Earth observations <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="" animationOptions={duration:500}}-->
#### Study area
**[1–2 sentences: where the study area is, why it was chosen (e.g. fire-prone Mediterranean ecosystems), and the study period.]**

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="" animationOptions={duration:500}}-->
#### Where did it burn?
The ESA CCI Fire Burned Area product flags every pixel that burned in a given month. This layer shows all burned pixels in the study area between **[YEAR]** and **[YEAR]**.

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="" animationOptions={duration:500}}-->
#### From pixels to fire events
Neighbouring burned pixels were grouped into burned areas, so each polygon roughly represents one fire event. These polygons are the units for which we extract vegetation time series. **[n burned areas, size range]**

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="" animationOptions={duration:500}}-->
#### Before the fire
kNDVI shortly before **[FIRE NAME / DATE]**. This is the pre-fire baseline that recovery is measured against.

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="" animationOptions={duration:500}}-->
#### Right after the fire
kNDVI shortly after the fire. The drop compared with the baseline shows how strongly the vegetation was hit.

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ESDC_kndvi;:;2021-12-23T00:00:00Z;:;xcube tiles;:;EPSG:3857","title":"xcube tiles"},"source":{"type":"XYZ","url":"https://api.earthsystemdatalab.net/api/tiles/esdc/kndvi/{z}/{y}/{x}?crs=EPSG:3857&time=2021-12-23T00:00:00Z&vmin=0&vmax=1&cbar=RdYlGn","projection":"EPSG:3857"}},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]}]}]' zoom="2.6456584324087107" center=[-10.569682342641302,7.8903138332408105] projection="" animationOptions={duration:500}}-->
#### How fast does vegetation recover?
Recovery time per burned area: the number of **[months]** until kNDVI returned to **[X %]** of its pre-fire baseline. **[1–2 sentences on the pattern: where recovery was fast or slow.]**


## Data and Methods
#### Dataset
- **Burned area**: ESA CCI Fire Burned Area **[product version, resolution]**
- **Vegetation**: ESDC **[kNDVI / NDVI / ...]** via DeepESDL
- **Temporal coverage**: **[YEAR–YEAR]**

#### Methodology workflow
1. **Burned pixels:** extract all pixels flagged as burned in the ESA CCI Fire product for the study area and period.
2. **Burned areas:** group adjacent burned pixels into burned-area polygons, each representing roughly one fire event. **[aggregation rule, e.g. spatial connectivity + same/neighbouring month; minimum size]**
3. **Time-series extraction:** extract the vegetation-index time series for each burned area. **[spatial mean/median per polygon?]**
4. **Preprocessing:** **[gap filling, smoothing, removing seasonality]**
5. **Recovery metrics:** compute each burned area's pre-fire baseline (**[definition]**), then:
   - *recovery time*: the time until the index returns to **[X %]** of the baseline
   - *recovery rate*: **[e.g. slope of the index over the first N months after the fire]**



## Results


## Conclusions
**[Main findings in 2–3 sentences.]**

#### Outlook
The next step is to explain *why* recovery differs between burned areas. We plan to relate the recovery metrics to land cover (ESA CCI Land Cover) and post-fire climate conditions such as precipitation (ERA5). Building on that, these variables could be used to predict how strongly future fires would affect a given area and how well it would recover.



## <!--{ as="div" }--> Open Science
| **Name**                                                                                                                                                 | **Type**            | **Agency / Provider**                     | **Description / Usage**                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[DATASET NAME](LINK)** | Dataset             | DeepESDL / ESDC                           | Description how this dataset was used in this story |
| **[EO Dashboard](https://eodashboard.org/explore/?x=15.0000&y=48.0000&z=4.0000&datetime=2025-09-19&template=expert)**                                    | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Provides base layers and visualization tools for interactive exploration of NDVI and other Earth observation indicators.                                                                                                                |

#### Notebook
Access the notebook to reproduce the study workflow.
<iframe width="100%" height="600" src="LINK TO NOTEBOOK" frameborder="0"></iframe>


#### References
- Forzieri, G., Dakos, V., McDowell, N. G., Ramdane, A., & Cescatti, A. (2022). Emerging signals of declining forest resilience under climate change. *Nature*, 608, 534–539. https://doi.org/10.1038/s41586-022-04959-9

- Johnstone, J. F., Allen, C. D., Franklin, J. F., Frelich, L. E., Harvey, B. J., Higuera, P. E., Mack, M. C., Meentemeyer, R. K., Metz, M. R., Perry, G. L. W., Schoennagel, T., & Turner, M. G. (2016). Changing disturbance regimes, ecological memory, and forest resilience. *Frontiers in Ecology and the Environment*, 14, 369–378. https://doi.org/10.1002/fee.1311

- Reek, J. E., Zohner, C. M., Smith, G. R., Cook-Patton, S. C., De Frenne, P., D'Odorico, P., Floriancic, M. G., Jackson, R. B., Jones, J. A., Kirchner, J. W., et al. (2026). More than mitigation: The role of forests in climate adaptation. *Science*, 391(6786), 669–678. https://doi.org/10.1126/science.ads4361

- Seidl, R., Spies, T. A., Peterson, D. L., Stephens, S. L., & Hicke, J. A. (2016). Searching for resilience: addressing the impacts of changing disturbance regimes on forest ecosystem services. *Journal of Applied Ecology*, 53(1), 120–129. https://doi.org/10.1111/1365-2664.12511

- Watson, J. E. M., Evans, T., Venter, O., Williams, B., Tulloch, A., Stewart, C., Thompson, I., Ray, J. C., Murray, K., Salazar, A., McAlpine, C., Potapov, P., Walston, J., Robinson, J. G., Painter, M., Wilkie, D., Filardi, C., Laurance, W. F., Houghton, R. A., … Lindenmayer, D. (2018). The exceptional value of intact forest ecosystems. *Nature Ecology & Evolution*, 2, 599–610. https://doi.org/10.1038/s41559-018-0490-x



## Contributors
Authors, contibutors, reviewers