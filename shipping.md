---
cover-image: https://eodashboard.org/data/story-images/12-ship-traffic.jpg
date: 2025-01-01
theme: cryosphere
tags: climate,ice,polar,warming
official: true
---

#  Travel restrictions interrupted Global Supply chains dependent on cargo shipping<!--{ as="img" mode="hero" src="https://eodashboard.org/data/story-images/12-ship-traffic.jpg" }-->
### Read more about Covid-19 Impacts on global shipping <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Shipping Activity at Major Ports

Supply chains around the world dependent on cargo shipping have been interrupted by travel restrictions and quarantines designed to stop the spread of the novel coronavirus. Many ports are closed, shipments have been canceled, and, in some locations, altered shipping routes have prevented the efficient movement of cargo.

NASA and ESA researchers are using cutting-edge artificial intelligence technology and high-resolution satellite imagery from [Planet Labs](https://www.planet.com/) and [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) to track shipping activity at major ports in the U.S. and in Europe during the coronavirus pandemic.

This data will help quantify the level of shipping-related economic activity over time and could eventually contribute to our understanding of the environmental implications of global decreases in shipping on key air pollutants like nitrogen dioxide (NO<sub>2</sub>) and sulphur dioxide (SO<sub>2</sub>).

Detection of ships on PlanetScope images
----------------------------------------

 NASA’s Interagency Implementation and Advanced Concepts Team (IMPACT), based at NASA’s Marshall Space Flight Center in Huntsville, Alabama, trained an algorithm using supervised machine learning technique to detect ships on PlanetScope images. The algorithm detects a ship on the image and geolocates it. The NASA team has also built an Application Programming Interface (API) that allows ship detections to be aggregated across a port area for a given day. Efforts are also underway to conduct a study of ship detections in U.S. ports during the period of pandemic travel restrictions, as compared to the same period of time in previous years.

NASA researchers have access to the high-resolution imagery from Planet Labs, through the Commercial SmallSat Data Acquisition Program (CSDAP), which acquires data from commercial sources that support NASA's Earth science research goals. The PlanetScope image resolution is 3 meters per pixel, which allows researchers to get a detailed look at changes occurring on the ground. Commercial small satellites also provide high temporal resolution, making images available almost every day (depending on cloud cover) for key areas of interest.

Ship detections can be provided daily, except when prevented by significant cloud cover. After the machine learning model detects the ships, a secondary human validation is also performed before the detections are made available for the dashboard.

Click on the links below to explore ship detections on Planet Labs data on various international ports:

- [San Francisco](https://www.eodashboard.org/?indicator=E13c&poi=US03-E13c)
    
- [New York](https://www.eodashboard.org/?indicator=E13c&poi=US01-E13c)
    
- [Los Angeles](https://www.eodashboard.org/?indicator=E13c&poi=US02-E13c)
    
- [Suez Canal](https://www.eodashboard.org/?indicator=E13c&poi=EG01-E13c)

## Map Example <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Vector","properties":{"id":"Ship detections"},"source":{"type":"Vector"}},{"type":"Tile","properties":{"id":"Shipping Activity at Major Ports-2020-05-20T10:57:05Z"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"SENTINEL-2-L2A-TRUE-COLOR","format":"image/png","time":"2020-05-20T10:12:05/2020-05-20T11:42:05"}}},{"type":"Tile","properties":{"id":"EOxCloudless 2021"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2021_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="12.418491147264769" center=[2.2115209289548927,51.0218377121069] }-->

