# Urban heating 

## Rising Heat Waves
#### Recent record-breaking: Southern Europe case
Across the globe, and increasingly in Europe, heat waves are becoming more frequent and intense. June 2025 was the third warmest June on record globally, as reported in the latest Climate Bulletin by the Copernicus Climate Change Service (C3S) [1](https://climate.copernicus.eu/western-europe-and-mediterranean-gripped-major-heatwaves-june#:~:text=Two%20major%20heatwaves%20led%20to,impact%20more%20people%20across%20Europe.%E2%80%9D&text=The%20average%20temperature%20over%20European,air%20circulation%20out%20of%20Antarctica.). Major heatwaves led to very strong heat stress in large parts of western and southern Europe. Cities like Madrid, Rome, and Lyon facing consecutive days above 42°C. This was the hottest June ever recorded in Europe, surpassing long-standing records. Several cities exceeded 44°C, pushing the limits of heat tolerance for both human populations and infrastructure.

<center>
<img src="https://i2.res.24o.it/images2010/S24/Documenti/2025/07/02/Immagini/Ritagli/esa-temp-U52063276275NdV-1440x752@IlSole24Ore-Web.jpg?r=810x425E" width="600">

<span style="font-size:15px;">Land and sea surface temperture by Copernicus Sentinel-3 LSLT sensor.
	</span>
</center>

These prolonged periods of excessive heat have significant implications for public health, infrastructure, and urban planning. The [Paris Agreement](https://www.consilium.europa.eu/en/policies/paris-agreement-climate/) calls for urgent adaptation strategies to protect vulnerable populations from the worsening impacts of a warming climate. The latest European heatwave underscores the urgency of these actions.

#### Heat stress
**Land surface temperature (LST)**, an essential climate variable, plays a critical role in tracking urban heat. Unlike air temperature, LST measures the heat radiating from the ground—crucial for understanding heat retention in cities dominated by asphalt, concrete, and other heat-absorbing materials. In urban areas like Paris, where surface temperatures can reach up to 60°C on asphalt, the risk of **heat stress is compounded by the lack of green spaces and high-density building structures**.
Heat stress doesn’t affect everyone equally. In urban environments, socio-economic factors heavily influence vulnerability. Children, the elderly, people with chronic illnesses, and communities in low-income neighborhoods are disproportionately affected by extreme heat events. The 2025 heatwave brought this inequality into sharp focus, with hospitals in Southern Europe reporting a surge in heatstroke and dehydration cases [[2]](https://www.theguardian.com/world/2023/jul/18/italian-hospitals-report-rise-in-heat-cases-as-rome-hits-41-point-8c)[[3]](https://phys.org/news/2025-06-cold-climate-southern-europe.html), particularly among those in vulnerable communities who had limited access to cooling facilities.

## Understanding Urban Heat Stress
#### Heat and Human Inequality 20-year long study
A recent study [[4]](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GH001079)  explored the **impact of urban growth and climate change on heat stress in Houston**, Texas, focusing on heat inequalities influenced by socioeconomic and geographic factors. Satellite data, including land cover and vegetation measurements from NASA's MODIS sensor, helped analyze the urban heat island effect, revealing how urbanization and increased surface temperatures exacerbate heat-related health risks. 
The research also integrates population vulnerability data from the CDC to better understand the social dimensions of heat stress in urban populations. In Houston, structural inequalities and patterns of urban development intensify these risks. Social vulnerability indices from the CDC highlight communities where race, income, and access to resources intersect with heightened exposure to heat stress. These are often the same areas with limited green space and increased infrastructure development, creating urban heat islands. NASA Earth observations have been instrumental in understanding how Houston’s urban landscape has evolved over the past two decades. 
## Houston <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"grdi-v1-built;:;povmap-grdi-v1_BUILT_2015-01-01_2021-12-31;:;grdi-v1-built;:;EPSG:3857","title":"grdi-v1-built"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/grdi-v1-built/povmap-grdi-v1_BUILT_2015-01-01_2021-12-31.tif&resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0.0,100.0","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="8.232367701972546" center=[-96.08143276085875,29.688495685404078] projection="" animationOptions={duration:500}}-->
#### The case of the growing city of Houston 
Between 2001 and 2019, satellite-derived land cover maps reveal a significant expansion—over 20%—of urban and built-up land. This growth, concentrated in the city’s southwest, directly **correlates with rising LST**.

Leveraging data from NASA’s Moderate Resolution Imaging Spectroradiometer (MODIS)) platform, the study delved into Houston’s changing landscape over two decades by examining multi-decadal changes both LST and the Normalized Difference Vegetation Index (NDVI), offering a technical perspective on this urban phenomenon. 


Terra has been instrumental in capturing this data. This platform, orbiting Earth, scans our planet in multiple spectral bands, allowing for a detailed analysis of LST and NDVI. The decadal periods of 2000-20009 and 2010-2019 were examined specifically to study the growth of Houston's UHI.

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Sentinel-3-SLSTR-L2-LST;:;2023-06-15T00:00:00Z;:;Sentinel-3-SLSTR-L2-LST;:;EPSG:3857","title":"Sentinel-3-SLSTR-L2-LST"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-3-SLSTR-L2-LST"],"TILED":true,"TIME":"2023-06-15T00:00:00Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.116573981748752" center=[-95.66753398613908,29.492609057699] projection="" animationOptions={duration:500}}-->
#### NDVI
To quantify vegetation and its cooling effects, researchers used the normalized difference vegetation index from the MODIS sensor on NASA’s Terra satellite. **As green space decreased, heat intensity rose**. 


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Sentinel-3-SLSTR-L2-LST;:;2023-06-15T00:00:00Z;:;Sentinel-3-SLSTR-L2-LST;:;EPSG:3857","title":"Sentinel-3-SLSTR-L2-LST"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-3-SLSTR-L2-LST"],"TILED":true,"TIME":"2023-06-15T00:00:00Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="9.116573981748752" center=[-95.66753398613908,29.492609057699] projection="" animationOptions={duration:500}}-->
#### LST 
Day and nighttime LST data showed that higher temperatures persist even after the sun sets, exacerbating health risks overnight.  LST is the temperature of the earth’s surface derived from the Terra satellite that houses the MODIS instrumentation, encompassing both natural terrains and man-made infrastructures. Unlike ambient air temperature, which gauges the immediate atmospheric conditions we feel, LST provides a granular temperature profile of surfaces from park greens to asphalt roads. 
(In fact, during the June 2025 European heatwave, similar patterns were observed, with temperatures in urban areas staying up to 10°C higher than in surrounding rural zones well into the night).


Exmaining this in **conjunction with NDVI** gives an idea of the changing access to green space in sprawling urban spaces such as Houston.







## Taking Action: AI applications 
#### Urban Heat Stress Analysis: The Case of Danish Cities   
CLIM4cities is a European Space Agency-funded project led by the Danish Meteorological Institute (DMI) and co-developed with +ATLANTIC CoLAB. The project focuses on a Proof-of-Concept Application in Danish cities, featuring downscaled short-term predictions and climate change scenarios, aimed at supporting local stakeholders in addressing the impacts of extreme heat events (through adaptation and mitigation strategies). To do so, the project is developing advanced Machine Learning (ML) and Artificial Intelligence (AI) models to significantly enhance air and land surface temperature predictions in urban areas for the adoption by local actors. In the first phase of CLIM4cities, the team held a series of user need workshops, engaging citizens, city planners and other local stakeholders in Denmark to understand and evaluate their needs and priorities for the solution. This engagement also provides the foundation for further interactions with users for validation of the solution. On the technical side, we are integrating citizen observations, numerical weather data, and processed Earth Observation (EO) data to create a comprehensive ML Database. This database trains and tests the models, providing cost-effective, integrated urban climate services. Local Climate Zone classifications (LCZ) originated from Copernicus Land Monitoring Service datasets are used to understand the impacts that the urban heat island effect has across a city's land use and land cover characteristics. In the frame of the project, the consortium is developing a set of high-resolution LCZ baselines, categorised using criteria such as dominant built-up densities, impervious surfaces, tree cover densities, and predominant leaf types.

## Open Science <!--{ as="div" }-->

### Open Datasets and Satellite Missions Used in the Story

| **Name**                                      | **Type**          | **Agency / Provider** | **Description / Usage**                                                                                           |
| --------------------------------------------- | ----------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Copernicus Sentinel-3**                     | Satellite/Mission | ESA / Copernicus      | Provided land and sea surface temperature (LST) data during the 2025 European heatwave.                           |
| **MODIS (on Terra)**                          | Satellite/Sensor  | NASA                  | Used to measure land cover, LST, and NDVI over time in Houston to analyze urban heat islands and vegetation loss. |
| **VEDA**                                      | Platform / Tool   | NASA                  | Used for accessing and analyzing multi-decadal MODIS data, including LST and NDVI, to study urban heat trends.    |
| **Copernicus Land Monitoring Service (CLMS)** | Dataset/Tool      | ESA / Copernicus      | Provides Local Climate Zone (LCZ) classifications used in urban climate modeling for the CLIM4cities project.     |
| **EODashboard**                    | Platform / Web Tool      | EO Dashboard Consortium (ESA, NASA, JAXA) | Aggregates and visualizes multisource EO data in near real‑time—including precipitation, flood extents, and land‑surface anomalies. Enabling the interactive map tours and storytelling. |


### References

### Contributors

Sara Aparício (Solenix c/o ESA), Rajat Shinde (NASA), Derek Koehl (NASA), Manil Maskey (NASA), Ryan Pavlick (NASA), Quentin Paletta (ESA), Paul Fisher (ESA)
    