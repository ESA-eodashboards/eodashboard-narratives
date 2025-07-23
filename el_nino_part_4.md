# El Niño 2023–2024: Flooding and Cyclone Impacts in East Africa Tracked from Space

**The 2023–2024 El Niño has peaked as one of the five strongest on record. This story is Part 4 of a series on its global impacts. [Part 1](https://eodashboard.org/story?id=el-nino-extremes) explores rising land surface temperatures, [Part 2](https://eodashboard.org/story?id=sea-surface-temperature-rise) covers sea surface warming and marine heatwaves, and [Part 3](https://eodashboard.org/story/?id=el_nino_part_3_food_security) examines food security disruptions.**
 
Whether you’re a farmer watching the skies, a family navigating flooded roads, or someone checking the weather from thousands of kilometers away, climate extremes affect us all. During the 2023–2024 El Niño, these extremes - heatwaves, storms, floods, and droughts - made headlines around the world.

What we may not see in those headlines is how these events are monitored in near real-time by satellites orbiting high above. Earth Observation (EO) satellites allow us to detect changes in rainfall, monitor floodwaters as they rise, and map storm damage over vast areas. These capabilities are made possible through collaboration among global space agencies - ESA, NASA, JAXA, and others - who make their datasets open for public use.


This story explores the impacts of El Niño in East Africa, one of the regions hardest hit, using the lens of these open EO datasets, which include rainfall maps, flood extents, and river observations.
 
## El Niño 2023
**A Global Climate Driver**

El Niño is a climate phenomenon marked by warming sea surface temperatures in the central and eastern Pacific Ocean. These temperature changes alter global atmospheric circulation, disrupting weather systems across continents. The result is often a rise in extreme events, from heatwaves and marine heatwaves to droughts and food insecurity, floods, and powerful storms.
Earth Observation satellites play a vital role in documenting El Niño impacts. Through their optical, radar, infrared, and microwave sensors, satellites reveal what can’t always be seen from eye level: how fast floodwaters rise, where crops fail, or how rainfall changes in real time.
 
## Horn of Africa: Floods of 2023
**Rainfall Patterns and Climate Drivers**

During the short rains season (October–December) of 2023, East Africa was hit by exceptional rainfall. This was due to the combined effects of El Niño and a positive Indian Ocean Dipole (IOD)—another ocean-atmosphere system that enhances rainfall over the region [[1]](https://www.icpac.net/fsnwg/special-report-el-ni%C3%B1o-and-positive-indian-ocean-dipole-to-have-significant-multi-sectoral-impacts-in-east-africa/).

Signs of anomaly were visible in EO data from multiple satellite missions: precipitation far above average levels, changes in vegetation, and swelling river systems. These observations were crucial in tracking the development of the flood season as it unfolded.

<figure style="text-align: center;"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Horn_of_Africa_%28orthographic_projection%29.svg/800px-Horn_of_Africa_%28orthographic_projection%29.svg.png" alt="Horn of Africa (orthographic projection)" style="display: block; margin: 0 auto;" width="400"> <figcaption> Horn of Africa (orthographic projection). <a href="https://commons.wikimedia.org/w/index.php?curid=8990864" target="_blank">By L'Américain – Own work, CC BY-SA 3.0</a>. </figcaption> </figure> 


## Satellite Observations

By November 2023, heavy rains had triggered deadly flooding across Somalia, Kenya, Ethiopia, and Tanzania, displacing over one million people and resulting in more than 350 deaths [[2]]( https://edition.cnn.com/2023/12/04/africa/east-africa-floods-more-than-300-killed-intl/index.html). The floods came on the heels of years of drought, compounding the region’s food insecurity [[3]](https://earthobservatory.nasa.gov/images/150712/worst-drought-on-record-parches-horn-of-africa).
In some areas of Ethiopia, Somalia, and Kenya, rainfall totals were two to four times the seasonal average. This led to major rivers, such as the Shebelle River, overflowing and flooding towns like Beledweyne, Somalia. Satellite imagery from NASA’s Landsat 8 captured the scale of flooding. The false color image below highlights the contrast between inundated areas and surrounding terrain [[4]](https://earthobservatory.nasa.gov/images/152108/devastating-flooding-in-east-africa).

<figure style="text-align: center;"> <img src="https://eoimages.gsfc.nasa.gov/images/imagerecords/152000/152108/somaliafloodingzm_oli_2023319.jpg" alt="Flooding in Beledweyne" style="display: block; margin: 0 auto;" width="800"> <figcaption> Beledweyne on November 15, 2023. Landsat 8 false-color image highlights floodwaters (blue), vegetation (green) and cumulus clouds (white). <a href="https://earthobservatory.nasa.gov/images/152108/devastating-flooding-in-east-africa" target="_blank">NASA Earth Observatory</a>. </figcaption> </figure>

In western Somalia, the Juba River also overtopped its banks, damaging roads and croplands in towns like Luuq and Baardheere, where a key bridge was swept away [[5]](https://www.faoswalim.org/resources/site_files/Somalia_Flood_Advisory_20_November_2023.pdf).
To monitor such conditions, the University of California–Santa Barbara Climate Hazards Center uses near-real time analyses and forecasts from NASA’s Goddard Earth Observing System Subseasonal to Seasonal prediction system (GEOS-S2S). This system integrates EO data to track and predict rainfall and soil conditions in regions vulnerable to food insecurity [[6]](https://www.chc.ucsb.edu/), [[7]](https://gmao.gsfc.nasa.gov/gmao-products/).

## Map Tour Example <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{ "type": "Group", "properties": { "id": "OverlayGroup", "title": "Overlay Layers" }, "layers": [ { "type": "Tile", "properties": { "id": "overlay_bright;:;EPSG:3857", "title": "Overlay labels" }, "source": { "type": "XYZ", "url": "//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png", "projection": "EPSG:3857" } } ] },{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Balaton;:;2023-06-01T00:00:00Z;:;Lakes_S2L2A;:;EPSG:3857","title":"Lakes_S2L2A"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-2-L2A-TRUE-COLOR"],"TILED":true,"TIME":"2023-11-20T00:00:00Z/2023-11-20T23:59:59Z"}},"visible":true}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"osm","title":"Background"},"source":{"type":"OSM"}}]}]' zoom="11.899126433739314" center=[45.13806578136379,4.696772861425785] projection="" animationOptions={duration:500}}-->
#### 20 November 2023: Flooded Landscapes of Beledweyne 
This Copernicus Sentinel-2 true color image shows a natural-color view of the flooded region of Beledweyne. Areas covered in water appear dark blue or black, while vegetation appears green and urban zones appear gray. The flooding is visible where water has overflowed rivers or coastlines, covering fields, roads, and settlements, offering a realistic snapshot of the affected landscape.  

<center>
<img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2012/02/sentinel-2/9658480-3-eng-GB/Sentinel-2_pillars.jpg" width="400">
	
<span style="font-size:15px;">Copernicus Sentinel-2 </span>
</center>

The Sentinel-2 collects data across 13 spectral bands, ranging from visible to shortwave infrared wavelengths. What you're seeing here is a true color composite, created using the Red (Band 4), Green (Band 3), and Blue (Band 2) bands—similar to how the **human eye perceives color**. This allows us to view the landscape as it would appear in **real life**, allowing to recognize flooded zones and affected areas.


### <!--{ layers='[{ "type": "Group", "properties": { "id": "OverlayGroup", "title": "Overlay Layers" }, "layers": [ { "type": "Tile", "properties": { "id": "overlay_bright;:;EPSG:3857", "title": "Overlay labels" }, "source": { "type": "XYZ", "url": "//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png", "projection": "EPSG:3857" } } ] },{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Balaton;:;2023-06-01T00:00:00Z;:;Lakes_S2L2A;:;EPSG:3857","title":"Lakes_S2L2A"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-2-L2A-NDWI"],"TILED":true,"TIME":"2023-11-20T00:00:00Z/2023-11-20T23:59:59Z"}},"visible":true}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"osm","title":"Background"},"source":{"type":"OSM"}}]}]' zoom="11.899126433739314" center=[45.13806578136379,4.696772861425785] projection="" animationOptions={duration:500}}-->
#### Improving flood detection with band combiation 
This **false color** image uses the Normalized Difference Water Index (NDWI) to highlight water. In this view, water appears bright blue, making it easier to identify flood extent. NDWI enhances water detection by comparing **green and near-infrared light** (Bands 3 and 8, respectively) reflected from the surface. In this image, we can clearly see how floodwaters, which are **highlighted in blue** have spread across land areas, especially in low-lying or agricultural zones.

### <!--{ layers='[{ "type": "Group", "properties": { "id": "OverlayGroup", "title": "Overlay Layers" }, "layers": [ { "type": "Tile", "properties": { "id": "overlay_bright;:;EPSG:3857", "title": "Overlay labels" }, "source": { "type": "XYZ", "url": "//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png", "projection": "EPSG:3857" } } ] },{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Balaton;:;2023-06-01T00:00:00Z;:;Lakes_S2L2A;:;EPSG:3857","title":"Lakes_S2L2A"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["SENTINEL-2-L2A-NDWI"],"TILED":true,"TIME":"2023-09-26T00:00:00Z/2023-09-26T23:59:59Z"}},"visible":true}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"osm","title":"Background"},"source":{"type":"OSM"}}]}]' zoom="11.899126433739314" center=[45.13806578136379,4.696772861425785] projection="" animationOptions={duration:500}}-->
#### 26/09/2023
Check if make sense

## A Growing Toll
In May 2024, new flooding and mudslides struck Burundi, Kenya, Rwanda, Somalia, Ethiopia, and Tanzania after five days of torrential rain. According to the International Organization for Migration (IOM), over 234,000 people were displaced and more than 637,000 were affected [[8]](https://news.un.org/en/story/2024/05/1149461), [[9]](https://wmo.int/media/news/flooding-worsens-east-africa).
<figure style="text-align: center;"> <img src="https://www.copernicus.eu/system/files/styles/image_of_the_day/private/2024-05/image_day/20240503_FloodsKenya.jpg?itok=J7bQdg3N" alt="Floods in Kenya" style="display: block; margin: 0 auto;" width="800"> <figcaption> Copernicus Sentinel-2 image from 29 April shows flooded terrain near Garissa, Kenya. <a href="https://www.copernicus.eu/system/files/styles/image_of_the_day/private/2024-05/image_day/20240503_FloodsKenya.jpg?itok=J7bQdg3N" target="_blank">European Union, Copernicus</a>. </figcaption> </figure> 
Flooding in the region also led to secondary impacts. Standing water, damaged sanita tion systems, and blocked roads contributed to outbreaks of waterborne diseases such as cholera, as well as mosquito- and flea-borne diseases including malaria, plague, and Rift Valley fever [10](https://earthobservatory.nasa.gov/features/disease-vector), [11](https://www.theguardian.com/environment/2023/aug/10/return-of-el-nino-raises-risk-of-hunger-drought-and-malaria-scientists-warn), [12](https://edition.cnn.com/2023/12/04/africa/east-africa-floods-more-than-300-killed-intl).

## Tracking Tropical Cyclone Freddy
**A Record Storm Tracked from Space**

Beyond rainfall, El Niño’s effects were also evident in the storm season. One of the most striking examples was Tropical Cyclone Freddy, which broke records for both longevity and impact [[13]](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2024GL111964).

EO systems captured its full trajectory and impact using satellite-based precipitation, surface water, and vegetation data—demonstrating the crucial role of global monitoring networks in understanding storm behavior over time.

Freddy made landfall in Madagascar on 21 February 2023, then moved across the Mozambique Channel, where it regained strength and hit Mozambique on 24 February near Vilankulos.
<figure style="text-align: center;"> <img src="https://eoimages.gsfc.nasa.gov/images/imagerecords/151000/151065/tcfreddy_vir_2023067.jpg" alt="Cyclone Freddy" style="display: block; margin: 0 auto;"> <figcaption> SUOMI-NPP satellite view of Cyclone Freddy. <a href="https://eospso.nasa.gov/missions/suomi-national-polar-orbiting-partnership" target="_blank">NASA</a>. </figcaption> </figure> 


## Cyclone Observations <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlaylabels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"customId"},"source":{"type":"XYZ","url":"https://sharaku.eorc.jaxa.jp/cgi-bin/trmm/GSMaP/tilemap/tile_rain.py?prod=rain&year=2023&month=2&day=21&hour=8&min=0&x={x}&y={-y}&z={z}"}},{"type":"Tile","properties":{"id":"Terrainlight"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]'zoom="5.036541747131764"center=[35.633378549999996,-18.82747120552102]}-->
#### On 21 February 2023 Cyclone Freddy made landfall in Madagascar

**Map: Global Satellite Mapping of Precipitation (GSMaP) from JAXA**

<figure style="text-align:center;">
    <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/PRCG_precipitation/PRCG_legend.png" 
         alt="GSMaP 21 February 2023. " 
    </figcaption>
</figure>



### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlaylabels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"customId"},"source":{"type":"XYZ","url":"https://sharaku.eorc.jaxa.jp/cgi-bin/trmm/GSMaP/tilemap/tile_rain.py?prod=rain&year=2023&month=2&day=24&hour=8&min=0&x={x}&y={-y}&z={z}"}},{"type":"Tile","properties":{"id":"Terrainlight"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]'zoom="5.036541747131764"center=[35.633378549999996,-18.82747120552102]}-->
#### 24 February 2023: the Cyclone reaches Mozambique

Though Cyclone Freddy weakened while crossing the island of Madagascar, it regained strength over the Mozambique Channel. On 24 February, it made landfall near Vilankulos as a tropical storm, causing further damage. Cyclone Freddy would go on to traverse the southern Indian Ocean for more than five weeks in February and March 2023, making it the longest-lived cyclone on record.

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlaylabels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"customId"},"source":{"type":"XYZ","url":"https://sharaku.eorc.jaxa.jp/cgi-bin/trmm/GSMaP/tilemap/tile_rain.py?prod=rain&year=2023&month=3&day=14&hour=8&min=0&x={x}&y={-y}&z={z}"}},{"type":"Tile","properties":{"id":"Terrainlight"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]'zoom="5.036541747131764"center=[35.633378549999996,-18.82747120552102]}-->
####  Final landfall in Quelimane, Mozambique

Cylone Freddy circled back to the Mozambique Channel and made a final landfall near Quelimane on 11 March- this time with even more severe rain and winds than before. 

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"alos2_floods;:;2023-03-15T00:00:00Z;:;alos2_floods;:;EPSG:3857","title":"alos2_floods"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["JAXA_ALOS2_FLOODMAPS"],"TILED":true,"TIME":"2023-03-15T00:00:00Z"}},"opacity":1}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2023;:;EPSG:3857","title":"EOxCloudless 2023"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2023_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="8.73907793405558" center=[35.93771646002912,-18.278112939983657] projection="" animationOptions={duration:500}}-->
#### The Aftermath 
By 14 March, the storm had dissipated inland after causing widespread damage and flooding across Madagascar, Mozambique, and surrounding regions. 

Its path and multiple landfalls, along with the fact that it persisted through such a lengthy period, made it a standout cyclone in terms of both meteorological history and the human impact it left behind.

<figure style="text-align: center;">
    <img 
        src="https://earthdata.nasa.gov/s3fs-public/styles/hds_large/public/2023-03/Flooding_Moz_Malawi_22Mar2023_Aqua_Terra_wiotw_1.jpg?VersionId=XJs7_Wl4XnQBpYyrTCCgC717H10WNU9p&itok=01aRUJlE" 
        alt="Flooding in Mozambique and Malawi from NASA MODIS Satellites" 
        style="max-width: 100%; height: auto; display: block; margin: 0 auto;"
    >
    <figcaption style="margin-top: 8px;">
        True-color corrected reflectance image of flooding in Mozambique and Malawi, acquired with Moderate Resolution Imaging Spectroradiometer (MODIS) instruments aboard NASA's Terra and Aqua satellites. Credit: 
        <a href="https://www.earthdata.nasa.gov/news/worldview-image-archive/flooding-mozambique-malawi" target="_blank">
            NASA EarthDATA
        </a>
    </figcaption>
</figure>

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"alos2_floods;:;2023-03-15T00:00:00Z;:;alos2_floods;:;EPSG:3857","title":"alos2_floods"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["JAXA_ALOS2_FLOODMAPS"],"TILED":true,"TIME":"2023-03-15T00:00:00Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]'zoom="11.774612669982734" center=[35.88201367268074,-18.75698819454024] projection="" animationOptions={duration:400}}-->
#### Mapping Flooded Areas with JAXA's ALOS-2 
By using GSMaP data with ALOS-2 data for inundation area estimation, JAXA monitored precipitation and inundated area by Cyclone Freddy.  Unlike optical satellites, ALOS-2 uses **radar, which can see independently of clouds and even at night**. This allows it to capture clear images of flooded areas, even when other satellites are blocked by weather. It's a crucial tool for monitoring floods in real-time, even in poor visibility conditions.
<figure style="text-align: center;">
    <img 
        src="https://africanarguments.org/wp-content/uploads/2023/03/mozambique-cyclone-freddy.jpg" 
        alt="Flooding in Mozambique and Malawi from NASA MODIS Satellites" 
        style="max-width: 100%; height: auto; display: block; margin: 0 auto;"
    >
    <figcaption style="margin-top: 8px;">
        The scene from the city of Quelimane in Mozambique after Cyclone Freddy struck on 11 March. Credit:  
        <a href="https://africanarguments.org/2023/03/nobody-imagined-it-would-be-so-intense-mozambique-cyclone-freddy/" target="_blank">
            UNICEF
        </a>
    </figcaption>
</figure>




**Map: Flooded areas, based on ALOS-2 data**.
<figure style="text-align: center;">
    <img 
        src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/alos2_floods/cm_legend.png.png" 
        alt="" 
        style="max-width: 100%; height: auto; display: block; margin: 0 auto;"
    >
    </figcaption>
</figure>


### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"alos2_floods;:;2023-03-15T00:00:00Z;:;alos2_floods;:;EPSG:3857","title":"alos2_floods"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["JAXA_ALOS2_FLOODMAPS"],"TILED":true,"TIME":"2023-03-15T00:00:00Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2023;:;EPSG:3857","title":"EOxCloudless 2023"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2023_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="12.840205295938151" center=[36.92265812343261,-17.874697018316283] projection="" animationOptions={duration:500}}-->
#### Quelimane
Text describing the current step of the tour and why it is interesting what the map shows currently



## Open Science Datasets
**Supporting Climate Monitoring**

The ability to monitor floods and storms from space relies on collaboration among space agencies and open access to satellite data. Missions from ESA, NASA, and JAXA provide global datasets that measure rainfall, water extent, soil moisture, and surface conditions—critical for understanding events like those in East Africa.
### Satellite Missions
- [Copernicus Sentinel-1 mission]() captures radar imagery, allowing the detection of changes in surface water levels, identification of flooded areas, and assessment of flood severity with high spatial resolution. In fact, the Copernicus Emergency Management Service (CEMS) has developed the Global Flood Monitoring (GFM) system that processes all incoming Sentinel-1 data to provide near-real time flood extent maps. 

- [Copernicus Sentinel-2 mission]() can contribute to flood monitoring through its multispectral imaging capabilities at various wavelengths, enabling the detection of floodwater and the assessment of flood extent, land cover changes, and flood-induced damages, and is used also by Copernicus Emergency Management Service (CEMS). 

- [NASA's Earth Observing System (EOS) satellites]() also play a vital role in flood monitoring. Satellites such as Landsat, Terra, Aqua, and SMAP provide microwave, multispectral, and thermal imaging data that can be used to monitor changes in water bodies, identify flooded areas, and assess flood impacts on surrounding landscapes. 

- [NASA’s SWOT mission](), launched in 2022, measures global river water level, slope, width, and area, which supports space-based estimates of river discharge.  

- [NASA/JAXA’s Global Precipitation Measurement (GPM) mission]() provides valuable information on precipitation patterns  and intensity, aiding in flood forecasting and early warning systems.

### Open Datasets

* [JAXA's multi-satellite global precipitation map named “GSMaP]() JAXA operates the “GSMaP” map under the GPM Mission, by using Dual-frequency Precipitation Radar (DPR) onboard GPM core satellites, other GPM constellation satellites, and Geostationary satellites in cooperation with partners. The main feature of the GSMaP algorithm is utilization of various attributes derived from the spaceborne precipitation radar, TRMM/PR and GPM/DPR. Precipitation information by GSMaP has been widely used, not only for scientific purposes, but also for meteorology, disaster prevention, climate monitoring, agricultural monitoring, public health, education and so on. GSMaP website offers the following global precipitation information: 
	* [JAXA REALTIME RAINFALL WATCH](https://sharaku.eorc.jaxa.jp/GSMaP_NOW/index.htm)
Shows global precipitation map, updated every 30 minutes.For users who would like to see precipitation in the past specific date.
	* [JAXA GLOBAL RAINFALL WATCH](https://sharaku.eorc.jaxa.jp/GSMaP/index.htm)
Shows hourly global precipitation map since March 2000. For users who would like to see daily or monthly precipitation.
	* [JAXA CLIMATE RAINFALL WATCH](https://sharaku.eorc.jaxa.jp/GSMaP_CLM/index.htm) Shows indices related to extreme heavy rainfall and drought as well as accumulated precipitation. 

* [NASA's OPERA project's operational 30-m surface water extent product ((https://podaac.jpl.nasa.gov/dataset/OPERA_L3_DSWX-HLS_V1)), available since April 2023, merges NASA Landsat and ESA Sentinel-2 data to ensure that extreme hydrological events are comprehensively observed, enhancing flood detectability.

* [NASA's LANCE project generates MODIS 250-m flood maps and SMAP 36-km soil moisture maps within 2-hours of satellite overpass](https://www.earthdata.nasa.gov/data/instruments/modis/near-real-time-data) (https://www.earthdata.nasa.gov/data/instruments/smap-l-band-radiometer/near-real-time-data) 

* [NASA's SWOT mission](https://podaac.jpl.nasa.gov/SWOT; https://podaac.github.io/tutorials/quarto_text/SWOT.html ) For global river reaches (approximately 10km in length and exceeding 30m in width), up to six estimates of water surface elevation, slope, and width are produced every 21 days. 
																																										
### Contributors						
Sara Aparicio (Solenix c/o ESA),  Shinichi Sobue (JAXA), Nao Yoshida (JAXA),  Karim Douch (ESA), Craig Ferguson (NASA) 

