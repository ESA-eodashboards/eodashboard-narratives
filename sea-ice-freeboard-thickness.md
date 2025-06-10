---
cover-image: https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/CryoSat.jpeg
date: 2025-01-01
theme: cryosphere
tags: climate,ice,polar,warming
official: true
---

#   Measuring Thickness of Sea Ice in the Polar Oceans<!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/CryoSat.jpeg" }-->
### Read more about monitoring Sea Ice Freeboard & Thickness from Satellite Altimetry. <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Sea Ice Freeboard and Thickness from Satellite Altimetry

NASA provides data collected over the Arctic Ocean by the Ice, Cloud and land Elevation Satellite-2 (ICESat-2) that show monthly sea ice freeboard from 2018 to the present. Sea ice freeboard is the amount of sea ice and snow cover that is visible above the surface of the ocean and, along with snow depth, is a critical measurement for accurately measuring the thickness of sea ice in the polar oceans. Click [here](https://icesat-2.gsfc.nasa.gov/science) to learn more about this research.

NASA’s ICESat-2 mission has been measuring the height of the Earth’s features from space with a laser ever since its launch in September 2018. The Advanced Topographic Laser Altimeter System (ATLAS) onboard ICESat-2 shoots pulses of light towards the Earth’s surface. ATLAS counts the particles of light (i.e., photons) that bounce off the Earth’s surface and return to the instrument’s sensors, measuring the round-trip time of each photon with extreme accuracy. Scientists can then take the total elapsed time to generate a height measurement of the particular surface that each photon bounced from. When enough photon measurements have been collected, scientists clump these measurements together to form a “photon cloud” that produces continuous surface elevation measurements as the satellite collects more and more data along its orbit. ICESat-2 collects data over the same location every 91 days, and this allows scientists to develop a picture of how the heights at certain spots around the globe are changing over time.

Collecting repeated height measurements of the Earth’s ice from space is an important way to view changes happening over the course of seasons and years. While ICESat-2 can only measure the height of Earth’s ice, scientists utilize special formulas (based on Archimedes' principle) to take those height measurements and turn them into measurements of sea ice freeboard that includes the ice above and below the waterline.

## Map Example <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"SITI_IS2SITMOGR4-cog-2021-04-01T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap_name=plasma&rescale=0.0,4.0&url=s3://veda-data-store/IS2SITMOGR4-cog/IS2SITMOGR4_01_202104_005_002.tif"]}},{"type":"Tile","properties":{"id":"Terrain Light Stereographic North"},"source":{"type":"TileWMS","urls":["https://sxcat-demo.eox.at/sxcat_maps/wms"],"params":{"layers":"sx-cat_ortho680500","format":"image/png"}}}]' zoom="1.4076931936914734" center=[-65.82427470346784,81.0891663077961] }-->

## ESA's CryoSat-2 and Envisat

While measurements from ICESat-2 can be used to determine the height and freeboard of polar sea ice, scientists also rely on ESA and the CryoSat-2 mission to measure sea ice thickness. Researchers at ESA provide monthly measurements of sea ice thickness from the CryoSat-2 and Envisat radar altimeters and other supporting missions.

Watch this video to learn how ESA measures sea ice thickness from space.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9einyMSOmHE?si=Sj-70Ym8hiDPkpi_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Globe Map

    Globe Map (Cesium)
		
## Explore Datasets

This **EO Dashboard** provides access to interactive maps of Sea Ice Thickness and Sea Ice Concentration. Access these datasets directly from the links below:

- [Sea Ice Thickness from Cryosat](https://www.eodashboard.org/explore?poi=World-SIC)
- [Sea Ice Thickness from Envisat](https://www.eodashboard.org/explore?poi=World-SIE)
- [Sea Ice Thickness from IceSAT-2](https://www.eodashboard.org/explore?poi=World-SITI)
- [Sea Ice Concentration Antarctic from GCOM-W](https://www.eodashboard.org/explore?poi=World-N12_1_sea_ice_concentration_arctic)

## Map Example <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"sea_ice_thickness_envisat-2012-03-01T00:00:00Z"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"ESA-CCI-V2-ENVISAT","styles":"","format":"image/png","time":"2012-03-01"}}},{"type":"Tile","properties":{"id":"Terrain Light Stereographic North"},"source":{"type":"TileWMS","urls":["https://sxcat-demo.eox.at/sxcat_maps/wms"],"params":{"layers":"sx-cat_ortho680500","format":"image/png"}}}]' zoom="2.0680307352535534" center=[-153.8783520795357,87.25976768229664] }-->





