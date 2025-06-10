---
cover-image: https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/trilateral/Esa_Nasa_jaxa_covid19_cover_V3.jpg
date: 2025-01-01
theme: covid-19
tags: travel,airplane,lockdown
official: true
---

#  During COVID-19 related lockdowns, air travel decreased<!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/trilateral/Esa_Nasa_jaxa_covid19_cover_V3.jpg" }-->
### Read more about COVID-19 impacts on air travel with EO and AI <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Grounded airplanes during the novel coronavirus pandemic

During COVID-19 related lockdowns, activities like air travel decreased to prevent the spread of the novel coronavirus. To help quantify these changes, scientists are combining two kinds of space-based remote sensing data – synthetic aperture radar (SAR) data from JAXA’s ALOS-2 and [ESA’s Copernicus Sentinel-1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1) satellites with NASA-processed high-resolution optical remote sensing data from Planet Inc. and [ESA's Copernicus Sentinel-2 multispectral satellite data](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) – to observe and quantify the changes in grounded airplanes and air traffic around the world.

SAR is a high-resolution, space-based radar that makes 2D images out of 3D objects. By comparing SAR images of airports before, during, and after lockdowns, scientists can determine how air traffic may have changed during the pandemic. In general, manmade targets such as buildings, cars, and airplanes appear brighter in SAR imagery than natural targets like bare land, forested areas, or the ocean.

Figure 1. shows a color composited SAR image of Tokyo International Airport, Haneda from the PALSAR-2 instrument aboard the ALOS-2 satellite. The different colors in the image correspond to the different dates the images were captured: red images were captured before lockdowns on November 28, 2019, green images were captured as lockdowns began on March 19, 2020, and blue images were captured during lockdowns on May 14, 2020. White colored areas, such as buildings, indicate no changes during the time period, whereas individual red, green, or blue colored pixels in the parking areas of the airport indicate airplanes at that time. Cyan colored areas show airplanes on March and May 2020.

Figure 2 shows a time series animation of SAR images taken from [Sentinel-1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1) at Tokyo International Airport, Haneda from January 10 to June 2, 2020. Brighter pixels in parking areas of the airport may correspond with airplanes at each acquisition date.

![](https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/trilateral/JP01-E8_Fig1.png)

*Figure 1. A multi-temporal, color-composite PALSAR-2 image at Tokyo International Airport, Haneda acquired on November 2019 (red), March 2020 (green), and May 2020 (blue).*

![](https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/trilateral/JP01-E13b_Animation.gif)

*Figure 2. Sentinel-1 animation at Tokyo International Airport, Haneda from January to June 2020. Brighter pixels in parking areas of the airport may correspond with airplanes at each acquisition date.*

In addition to the SAR imagery, NASA and ESA scientists also used artificial intelligence technology and high-resolution optical imagery from Planet and [Copernicus Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) to detect and count aircraft on the ground at airports.

Combining high-resolution optical remote sensing data from Planet and Sentinel-2 with SAR imagery from ALOS-2 and [Sentinel-1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1) is a powerful method to provide reliable time series data on the number of aircrafts grounded at airports over time. While imagery from optical satellites like Planet or [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) is powerful to monitor changes in grounded aircrafts around the world systematically, their sensors cannot penetrate clouds, limiting the detection capability on cloudy or rainy days. Alternatively, SAR data, while lower resolution, can penetrate clouds. Therefore, scientists are combining these datasets to get the most comprehensive images of changes at aircraft counts at airports during the COVID-19 pandemic.

The following interactive maps show:

- Aircraft detection on the San Francisco airport in the U.S. and Narita airport in Japan, using Planet imagery
    
- Aircraft detection over the CDG airport in Paris (France) using Sentinel-2 imagery and AI
    

More airports can be explored on this dashboard. Click the [**EXPLORE**](https://eodashboard.org/explore) on top of this page to explore all locations.

San Francisco airport, US
## San Francisco airport, US <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Vector","properties":{"id":"Plane detections"},"source":{"type":"Vector"}},{"type":"Tile","properties":{"id":"Parked Airplanes-2020-10-26T00:00:00Z"},"source":{"type":"XYZ","urls":["https://8ib71h0627.execute-api.us-east-1.amazonaws.com/v1/planet/{z}/{x}/{y}?date=2020_10_26&site=sf"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="13.792332771953118" center=[-122.37750000000001,37.619361707303256] }-->

Narita airport, Japan 
## Narita airport, Japan <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Vector","properties":{"id":"Plane detections"},"source":{"type":"Vector"}},{"type":"Tile","properties":{"id":"Parked Airplanes-2020-10-25T00:00:00Z"},"source":{"type":"XYZ","urls":["https://8ib71h0627.execute-api.us-east-1.amazonaws.com/v1/planet/{z}/{x}/{y}?date=2020_10_25&site=tk"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="12.982544998850098" center=[140.385,35.768367472164485] }-->

CDG airport in Paris, France
## CDG airport in Paris, France <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Vector","properties":{"id":"Plane detections"},"source":{"type":"Vector"}},{"type":"Tile","properties":{"id":"Parked Airplanes-2022-11-24T11:07:24Z"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"SENTINEL-2-L2A-TRUE-COLOR","format":"image/png","time":"2022-11-24T10:22:24/2022-11-24T11:52:24"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="12.545858516542904" center=[2.5694357161733556,49.000904522387] }-->
