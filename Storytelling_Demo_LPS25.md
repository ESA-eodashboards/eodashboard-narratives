## TITLE ##

At night, on the surface of our planet, multiple sources of illumination, such as streetlights, buildings and ships can be seen from space. 

<figure style="text-align: center;">
    <img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2013/10/night_lights/13355175-1-eng-GB/Night_lights_pillars.jpg" 
         alt=" Photograph taken from onboard the International Space Station showing a nighttime Paris and London. . " 
         style="display: block; margin: 0 auto;"
         width="800								">
    <figcaption>
         Photograph taken from onboard the International Space Station showing a nighttime Paris and London. Credit: 
        <a href="https://www.esa.int/ESA_Multimedia/Search?SearchText=nighttime+lights&result_type=images" target="_blank">
             ESA/NASA
        </a>.
    </figcaption>
</figure>

###  SUBTITTLE ###
One source of nighttime light imagery is the Visible Infrared Imaging Radiometer Suite (VIIRS) aboard the  [Suomi National Polar-orbiting Partnership (Suomi NPP)](https://eospso.nasa.gov/missions/suomi-national-polar-orbiting-partnership), a joint mission of the National Oceanic and Atmospheric Administration ([NOAA](https://www.noaa.gov/)) and [NASA](https://www.nasa.gov/). This satellite makes global daily measurements of nocturnal visible and near-infrared (NIR) light that can be used for Earth system science and applications, allowing to observe signals such as city lights, gas flares, fishing vessels, aurora, gravity waves and wildfires.  

##  EXPLORING THE DATASET (map tour)

##  Visalizig the dataset...<!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"JAXA_Nighttimelevel_Urban"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"JAXA-NIGHTTIMELEVEL-URBAN","styles":"","format":"image/png","time":"2019-01-01T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="7.568167497148919" center=[-81.69190982357188,36.13000317868601] animationOptions={duration:500}}-->
#### TITLE OF THE SIDE PANEL
Adding more information on the dataset being displayed in the map tour.
<figure style="text-align: center;">
    <img src="https://eospso.nasa.gov/sites/default/files/sat/Suomi-NPP.jpg" 
         alt=" Sea ice concentration in May 2023. " 
         style="display: block; margin: 0 auto;"
         width="500">
    <figcaption>
         SUOMI-NPP Satellite. Source:
        <a href="https://eospso.nasa.gov/missions/suomi-national-polar-orbiting-partnership" target="_blank">
             NASA
        </a>.
    </figcaption>
</figure>


### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"JAXA_Nighttimelevel_Urban"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"JAXA-NIGHTTIMELEVEL-URBAN","styles":"","format":"image/png","time":"2019-01-01T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="9.823650315180059" center=[-73.99550312972447,40.83001718614142] animationOptions={duration:500}}-->
#### 
The dataset covers urban areas globally, highlighting nighttime light levels to analyze urbanization, energy use, and economic activities.
<figure style="text-align: center;">
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flive.staticflickr.com%2F8745%2F16384318544_178f2f5482_b.jpg&f=1&nofb=1&ipt=25829b7e1b15806e923ac37a1f3283fca53fcec2090012dc5cd4fa2d91cceaa7&ipo=images" 
         alt=" " 
         style="display: block; margin: 0 auto;"
         width="800
								">
    <figcaption>
        Times Square at night, New York. Credit: 
        <a href="https://www.flickr.com/photos/106447493@N05/16384318544" target="_blank">
             Leon Yaakkov
        </a>
    </figcaption>
</figure>


## Open-sience: Jupyter Notebook
Supporting Open Science, here we reproduce the method developed by Professor Tojo to create the new dataset, in the following [notebook](https://hub.eox.at/services/eoxhub-gateway/eurodatacube/notebook-view/notebooks/contributions/NightLights/Night_Lights_Blending.ipynb). 
The notebok allows to visualize urban expansion and infrastrucutre development using additive color blending - i.e. assigning different years to RGB channels to reveal where artificial areas increased (which could be linked to economic growth) or decreased (suggesting reduced activity).

<figure style="text-align: center;">
    <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/Nightlights/nightime_notebook_image.jpg?raw=true" 
         alt=" . " 
         style="display: block; margin: 0 auto;"
         width="500">
    <figcaption>
         Jupyter Notebook: Nightime Lights with SUOMI NPP.
        <a href="https://hub.eox.at/services/eoxhub-gateway/eurodatacube/notebook-view/notebooks/contributions/NightLights/Night_Lights_Blending.ipynb" target="_blank">
             Access the Notebook
        </a>.
    </figcaption>
</figure>

[Access the notebook](https://hub.eox.at/services/eoxhub-gateway/eurodatacube/notebook-view/notebooks/contributions/NightLights/Night_Lights_Blending.ipynb) to analyze trends, and uncover patterns of human activity on a location of your choice. 
