#  El Niño 2023-2024 (Part 4):  Severe flooding in East Africa
El Niño-induced heavy rains and flooding across East Africa in October-November 2023, claimed over 350 lives and displaced more than one million people across  Somalia, Kenya, Ethiopia and Tanzania. In Kenya alone, 136 people lost their lives and nearly half a million were displaced. President William Ruto declared a state of emergency in response to the widespread devastation [[1]]( https://edition.cnn.com/2023/12/04/africa/east-africa-floods-more-than-300-killed-intl/index.html). The flooding compounded the region’s ongoing food insecurity crisis brought on by drought conditions that have persisted since 2020 [[2]](https://earthobservatory.nasa.gov/images/150712/worst-drought-on-record-parches-horn-of-africa). In the ‘Horn of Africa’, there are typically two rainy seasons: the short rains from October to December and the long rains from March to May. The October-December 2023 rainy period was extreme with precipitation totals double to quadruple the average in southern and western Ethiopia, Somalia and Kenya. The excessive rainfall led to the Shebelle River overflowing its banks and flooding central Somalia, particularly in Beledweyne [[3]](https://earthobservatory.nasa.gov/images/152108/devastating-flooding-in-east-africa). 

<figure style="text-align: center;">
    <img src="https://eoimages.gsfc.nasa.gov/images/imagerecords/152000/152108/somaliafloodingzm_oli_2023319.jpg" 
         alt=" Photograph taken from onboard the International Space Station showing a nighttime Paris and London. . " 
         style="display: block; margin: 0 auto;"
         width="800
								">
    <figcaption>
         Beledweyne on November 15, 2023 acquired by the OLI (Operational Land Imager) on Landsat 8. This is a false color image to emphasize the presence of water (blue), vegetation (green), and cumulus clouds (white).
        <a href="https://earthobservatory.nasa.gov/images/152108/devastating-flooding-in-east-africa" target="_blank">
             NASA Earth Observatory
        </a>.
    </figcaption>
</figure>


##  Urban and Rural NTL <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"JAXA_Nighttimelevel_Urban"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"JAXA-NIGHTTIMELEVEL-URBAN","styles":"","format":"image/png","time":"2019-01-01T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="7.568167497148919" center=[-81.69190982357188,36.13000317868601] animationOptions={duration:500}}-->
#### NTLU (Nighttime Light Urban)
The **NTLU** provides a comprehensive global spatial representation of nighttime light levels in urban areas. It is derived from satellite observations from the Suomi NPP satellite. This dataset is valuable for studying the **distribution of artificial lighting in urban regions**, offering insights into urban growth, infrastructure development, and socio-economic activity. 
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

This dataset metrics, are **'nighttime radiance values'** (measured in nanowatts per square centimeter per steradian, nW/cm²/sr), which represent the **brightness of artificial lighting in urban areas**. From this, the Nighttime Light Intensity (NTLI) can be generated, a composite of observations reflecting the overall intensity of visible nighttime lights in urban landscapes.

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"JAXA_Nighttimelevel_Rural"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"JAXA-NIGHTTIMELEVEL-RURAL","styles":"","format":"image/png","time":"2019-01-01T00:00:00Z"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="9.351542873898163" center=[2.8882348682431447,44.576074219821635] animationOptions={duration:500}}-->
#### Nighttime Light Rural (NTLR)
This dataset, **NTLR (Nighttime Light Rural)**, also derived from Suomi NPPM provides a comprehensive global spatial representation of nighttime light levels in **rural areas**. This dataset is valuable for studying the distribution of artificial lighting in **rural regions**, offering insights into human activity, **infrastructure development**, and **rural electrification**. 
<figure style="text-align: center;">
    <img src=https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flive.staticflickr.com%2F3235%2F2878685617_eeff89373a_z.jpg&f=1&nofb=1&ipt=6f0925220b598c383594d4fe09dd64cf085f3474e27ddb90ccdb727f5d1e627e&ipo=images" 
         alt=" " 
         style="display: block; margin: 0 auto;"
         width="800
								">
    <figcaption>
       Beledweyne is shown in the image above (right) on November 15, 2023. For comparison, the image on the left shows the same area on September 12, 2023. The images, acquired by the OLI (Operational Land Imager) on Landsat 8, are a false color to emphasize the presence of water (blue), vegetation (green), and cumulus clouds (white). 
        <a href="https://www.flickr.com/photos/bcm_photo/2878685617" target="_blank">
             Ben Murray
        </a>
    </figcaption>
</figure>


### References
- 1 - https://edition.cnn.com/2023/12/04/africa/east-africa-floods-more-than-300-killed-intl/index.html
- 2 - https://earthobservatory.nasa.gov/images/150712/worst-drought-on-record-parches-horn-of-africa
- 3 -  https://earthobservatory.nasa.gov/images/152108/devastating-flooding-in-east-africa 

