---
cover-image: https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/13-nightlights.jpg
date: 2025-01-01
theme: economy
tags: light,night,lockdown
official: true
---

# During COVID-19 lockdowns night lights in central business districts decreased <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/13-nightlights.jpg" }-->
### Read more about how researchers are using night lights to track variations in energy use, migration, and transportation <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Nightlights in the Port of Dunkirk (France)
 
The High Definition Nightlights dataset is processed to eliminate light sources like moonlight reflectance and other interferences. The darker shades are places with less light while the lighter shades of yellow are areas with more light.

The Port of Dunkirk is the third-largest maritime port in northern France. Located on the busy North Sea, the port is well known for the comings and goings of heavy cargo barges. In early March, following French government guidance, the port began to limit activity in response to the novel coronavirus.

Researchers are using night lights to track variations in energy use, migration, and transportation at the port in response to social distancing and lockdown measures.

They are able to visualize the extent social distancing measures impacted various economic activities based on whether light pollution increased or decreased, which highways were shut down, and which cities stayed the same.

    MISSING IMAGE OF THE PORT OF DUNKIRK

*Port of Dunkirk. Image source: <https://www.cruisemapper.com/ports/dunkirk-port-9901>*

## Map Example <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"nightlights-2022-03-01T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap_name=inferno&rescale=0,255&url=s3://veda-data-store/nightlights-hd-monthly/finalBMHD_ScaledDunkirk_202203.tif"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="11.18238776778081" center=[2.3125063121984724,51.015780452383126] }-->

## Nightlights in Tokyo, Japan

In the vibrant city of Tokyo, while some areas seemingly remain unchanged, others revealed a decrease in lights at night. Japan’s virus state of emergency is significantly looser than lockdowns elsewhere in the world. It largely calls for more people to work from home and for bars and restaurants to shut from 8 p.m. In December, amid COVID-19 surge, the city has urged restaurants and bars to shut early, and a new state of emergency putting the upcoming Olympics at stake.

Dimmer lights during December’s state of emergency were most noticeable in the surroundings of the central Tokyo. As example, Shibuya City a major commercial and finance center, housing the two busiest railway stations in the world, shown in some areas decreasing light due to the imposed closing hours. However, overall change in lights are not so obvious in most parts, as bars for instance are too small and difficult to detect using monthly averaged data.

Read the full story in this tutorial: [Lockdown is also changing our Planet at night](https://medium.com/euro-data-cube/lockdown-is-also-changing-our-planet-at-night-520deffec252).

High-resolution nighttime images from space, referred to by NASA as the Black Marble HD dataset, provide data on how coronavirus-containment strategies have affected local businesses and neighborhoods. The nightlights sensor can decipher changes in urban business, industry, and transportation activity patterns associated with closures, event cancellations, and reduced vehicle traffic.

## Map Example <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"nightlights-2022-03-01T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap_name=inferno&rescale=0,255&url=s3://veda-data-store/nightlights-hd-monthly/finalBMHD_ScaledTokyo-23Wards_202203.tif"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="13.925400344493246" center=[139.74557556451532,35.68584873272013] }-->

## The Suomi-NPP Visible Infrared Imaging Radiometer Suite (VIIRS)

 Suomi pioneered the generation of satellite products providing global measurement of nocturnal visible and near-infrared light. The high-resolution nighttime images from space, referred to by NASA as the Black Marble HD dataset, is processed to eliminate light sources like moonlight reflectance and other interferences. Furthermore, before assuming the direct link between decrease of lights and COVID-19-related restrictions it is always important to discard other potential factors for change. Nevertheless, this data can shed a light (pun intended) on how coronavirus-containment strategies have affected local businesses and neighborhoods, deciphering changes in urban business, industry, and transportation activity patterns associated with closures, event cancellations, and reduced vehicle traffic by night.
 
 ### Explore Datasets
 
 This **EO Dashboard** provides access to interactive nightlight maps on a large number of cities, worldwide. Access these datasets by clicking on the [**Dashboard**](https://eodashboard.org/explore) tab at the top of the page or directly from the links below:

### NASA Nightlights datasets are available for the following cities:

*   [Dhaka, Bangladesh](https://eodashboard.org/explore?indicator=N5&poi=BD01)
    
*   [Ghent, Belgium](https://eodashboard.org/explore?indicator=N5&poi=BE01)
    
*   [Beijing, China](https://eodashboard.org/explore?indicator=N5&poi=CN01)
    
*   [Hamburg, Germany](https://eodashboard.org/explore?indicator=N5&poi=DE01)
    
*   [Barcelona, Spain](https://eodashboard.org/explore?indicator=N5&poi=ES02)
    
*   [Madrid, Spain](https://eodashboard.org/explore?indicator=N5&poi=ES01)
    
*   [Dunkirk, France](https://eodashboard.org/explore?indicator=N5&poi=FR03)
    
*   [Marseille, France](https://eodashboard.org/explore?indicator=N5&poi=FR02)
    
*   [Paris, France](https://eodashboard.org/explore?indicator=N5&poi=FR01)
    
*   [London, Great Britain](https://eodashboard.org/explore?indicator=N5&poi=GB01)
    
*   [Genoa, Italy](https://eodashboard.org/explore?indicator=N5&poi=IT03)
    
*   [Milan, Italy](https://eodashboard.org/explore?indicator=N5&poi=IT02)
    
*   [Rome, Italy](https://eodashboard.org/explore?indicator=N5&poi=IT02)
    
*   [Venice, Italy](https://eodashboard.org/explore?indicator=N5&poi=IT01)
    
*   [Aichi Nagoya, Japan](https://eodashboard.org/explore?indicator=N5&poi=JP06)
    
*   [Fukuoka, Japan](https://eodashboard.org/explore?indicator=N5&poi=JP05)
    
*   [Hokkaido Sapporo, Japan](https://eodashboard.org/explore?indicator=N5&poi=JP04)
    
*   [Kyoto, Japan](https://eodashboard.org/explore?indicator=N5&poi=JP03)
    
*   [Osaka, Japan](https://eodashboard.org/explore?indicator=N5&poi=JP02)
    
*   [Tokyo, Japan](https://eodashboard.org/explore?indicator=N5&poi=JP01)
    
*   [Colombo, Sri Lanka](https://eodashboard.org/explore?indicator=N5&poi=LK01)
    
*   [Amsterdam, The Netherlands](https://eodashboard.org/explore?indicator=N5&poi=NL01)
    
*   [Auckland, Australia](https://eodashboard.org/explore?indicator=N5&poi=NZ01)
    
*   [Lima, Peru](https://eodashboard.org/explore?indicator=N5&poi=PE01)
    
*   [Gdynia, Poland](https://eodashboard.org/explore?indicator=N5&poi=PL01)
    
*   [Puerto Rico, Commonwealth of Puerto Rico](https://eodashboard.org/explore?indicator=N5&poi=PR01)
    
*   [Singapore, Republic of Singapore](https://eodashboard.org/explore?indicator=N5&poi=SG01)
    
*   [New Orleans, USA](https://eodashboard.org/explore?indicator=N5&poi=US02)


*Suomi-NPP. NASA Black Marble data courtesy of Universities Space Research Association (USRA), Earth from Space Institute (EfSI) and NASA Goddard Space Flight Center’s Terrestrial Information Systems Laboratory using VIIRS day-night band data from the Suomi National Polar-orbiting Partnership and Landsat-8 Operational Land Imager (OLI) data from the U.S. Geological Survey.*
