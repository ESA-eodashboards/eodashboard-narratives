---
cover-image: https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/stories/forest_story/hero.jpg
date: 2025-01-01
theme: biomass
tags: forest
official: true
---

# Forests on the Brink: Satellite Imagery unveiling Loss and Shifting Forest Landscapes <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/stories/forest_story/hero.jpg" }-->
### Forest Loss and Degradation worldwide <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Forest Loss and Shifting Landscapes

Forests cover 31% of the global land area [(1)](https://www.fao.org/3/CA8753EN/CA8753EN.pdf) and are a critical component of the world’s biodiversity. According to the "State of the World’s Forest 2022" report [(2)](https://www.fao.org/publications/home/fao-flagship-publications/the-state-of-the-worlds-forests/2022/en) published by FAO, they host more than 75% of the world’s terrestrial biodiversity, being home to some of the richest ecosystems. Forests are crucial for maintaining ecosystem balance, offering essential ecosystem services. However, deforestation and forest degradation<sup>1</sup> continue to take place at alarming rates [(3)](https://www.fao.org/documents/card/en/c/ca8753en). Deforestation, rising temperature, drier conditions and more frequent and severe fires are pushing different forest types to the verge of irreversible tipping points [(4)](https://www.bbc.com/news/science-environment-60650415), and risk to lose their ability to bounce back from damage, with far-reaching consequences. Deforestation is also the leading cause for 15% of carbon emissions [(5)](https://petpedia.co/deforestation-statistics/), can have a large impact on physical processes in the local climate, it disrupts the carbon cycle and energy balance and has been being associated with heat waves in North America and Eurasia [(6)](https://climate.mit.edu/explainers/forests-and-climate-change).
The UN FAO [(1)](https://www.fao.org/3/CA8753EN/CA8753EN.pdf) estimated an annual rate of deforestation of 10 million in the most recent five-year period (2015-2020). However, even if the world’s forest area is decreasing, the rate of loss has slowed.

At COP26, 100 countries endorsed the "Glasgow Leaders’s Declaration on Forests and Land Use" [(7)](https://webarchive.nationalarchives.gov.uk/ukgwa/20230418175226/https://ukcop26.org/glasgow-leaders-declaration-on-forests-and-land-use/), which aims to halt and reverse forest loss and land degradation by 2030. Satellite technology can play a crucial role in this commitment by providing real-time data on forest cover and land use changes, enabling governments to enforce policies, track progress or hold accountability for forest loss and degradation [(8)](https://www.bbc.com/news/science-environment-59088498). No single method is universally applicable for monitoring forest degradation, largely due to the specific nature and timing of different degradation processes [(9)](https://cbmjournal.biomedcentral.com/articles/10.1186/s13021-017-0078-9). For this reason, multiple and different types of satellites have been used for forest monitoring, working as a tool for conservation management, allowing to track fires and their emissions, detect illegal logging and estimate biomass.

Several ESA, JAXA and NASA satellites such as the [Copernicus Sentinel missions](https://sentinels.copernicus.eu/web/sentinel), [ALOS-2](https://www.eorc.jaxa.jp/ALOS-2/en/about/palsar2.htm), [MODIS](https://modis.gsfc.nasa.gov/) or [GEDI](https://gedi.umd.edu/), equiped with optical, synthetic aperture radar (SAR) and LiDAR sensors can detect and map forest degradation, supporting conservation management, helping to track fires and to detect illegal logging. 

ESA's forest mission, [BIOMASS](https://earth.esa.int/eogateway/missions/biomass), is a P-band SAR satellite with the main objective to determine the global distribution of forest biomass. This satellite is expected to improve the estimates of carbon stocks and fluxes on land associated with land-use change, forest degradation and forest regrowth. 

Data delivered by these missions provides the essential information used in global forest products such as the global Biomass Essential Climate Variable (ECV) of ESA's [Climate Change Initiative](https://climate.esa.int/en/projects/biomass/) (CCI). 

The following animation shows above ground biomass 2020. While deforestation refers to the entire removal of forest, degradation means that the forest still exists but with reduced functions. ESA (Data source: CCI Biomass project) 

## <!--{ as="iframe" src="https://www.esa.int/content/view/embedjw/559869" width="100%" height="500px" frameBorder="0" scroll="no" style="overflow:hidden" }-->

## <!--{as="eox-map" id="palsar" mode="tour" layers='[{"type":"Tile","properties":{"id":"PALSAR-2/PALSAR Forest/Non-Forest Map"},"source":{"type":"WMTS","urls":["https://ogcpreview1.restecmap.com/examind/api/WS/wmts/JAXA_WMTS_Preview?"],"layer":"FNF-PALSAR2-World-2020-Yearly","format":"image/png","matrixSet":"12d1db38-9354-4569-bbb4-efef0359fa54","tileGrid":{"resolutions":[156543.03392804097,78271.51696402048,39135.75848201024,19567.87924100512,9783.93962050256,4891.96981025128,2445.98490512564,1222.99245256282,611.49622628141,305.748113140705,152.8740565703525,76.43702828517625,38.21851414258813,19.109257071294063],"projection":"EPSG:3857","matrixIds":["156543d03392804097x-20,037,508d343x18,807,214d097","78271d51696402048x-20,037,508d343x18,807,214d097","39135d75848201024x-20,037,508d343x18,807,214d097","19567d87924100512x-20,037,508d343x18,807,214d097","9783d93962050256x-20,037,508d343x18,807,214d097","4891d96981025128x-20,037,508d343x18,807,214d097","2445d98490512564x-20,037,508d343x18,807,214d097","1222d99245256282x-20,037,508d343x18,807,214d097","611d49622628141x-20,037,508d343x18,807,214d097","305d748113140705x-20,037,508d343x18,807,214d097","152d8740565703525x-20,037,508d343x18,807,214d097","76d43702828517625x-20,037,508d343x18,807,214d097","38d21851414258813x-20,037,508d343x18,807,214d097","19d109257071294063x-20,037,508d343x18,807,214d097"],"origin":[-20037508.342789244,18807214.09674771]}}},{"type":"Tile","properties":{"id":"cloudless"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts?layer=s2cloudless-2022_3857&style=default&tilematrixset=GoogleMapsCompatible&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image%2Fjpeg&TileMatrix={z}&TileCol={x}&TileRow={y}"}}]'}-->

### JAXA's Global PALSAR-2/PALSAR Forest/Non-Forest Map

This product counts with an annual estimate of global above-ground biomass at 100 m spatial resolution over five years based on ESA’s C-band (Sentinel-1 A and -B) and JAXA’s L-band SAR on board of ALOS-2 PALSAR-2 with additional information from Space borne LIDAR (such as NASA’s Global Ecosystem Dynamics Investigation Lidar GEDI). JAXA also offers global 25m resolution SAR mosaics and forest/non-forest maps, based on ALOS PALSAR, ALOS-2 PALSAR-2 and the JERS-1 SAR. In addition, “[JICA-JAXA Forest Early Warning System in the Tropics](https://www.eorc.jaxa.jp/jjfast/)" (JJ-FAST) is now operating for monitoring early deforestation in tropical forests globally collaboration with the Japan International Cooperation Agency (JICA) and JAXA. 

 [View dataset](https://eodashboard.org/explore?indicator=FNF)
 
## Boreal Forests <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"ndvi-2024-04-16T11:59:30Z"},"source":{"type":"TileWMS","urls":["https://gpwmap.jaxa.jp/wms"],"params":{"layers":"EODASH:NDVI-GCOMC-World-Monthly","styles":"","format":"image/png","time":"2024-04-16T11:59:30Z"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="3.5452614282206953" center=[12.729978307915157,44.02861456759007] animationOptions={duration:500}}-->
#### Boreal forests: from carbon sink to carbon source?

![BorealForest](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/stories/forest_story/BorealForest.png)

Boreal forests comprise 44% of Earth’s remaining intact forest landscapes [(10)](https://intactforests.org/shp/IFL_readme_2021.pdf). The boreal forest biome stretches across including Canada, Scandinavia, Russia, and China. An increase of 1.6 degrees Celsius (associated to climate change) can have significant effects on species growth and survival. The UN’s Intergovernmental Panel on Climate Change (IPCC) expects that the vast areas of the boreal forest could experience warming of up to 6 to 11 degrees Celsius by 2100, with the potential to hit a tipping point [(11)](https://www.sciencedaily.com/releases/2015/08/150820144722.htm). 

### GCOM-C/SGLI L3 Normalized Difference Vegetation Index (NDVI)

#### observation date: 16 April 2024
 
 [View dataset](https://eodashboard.org/explore?indicator=E10e)
 
### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"ndvi-2024-07-16T11:59:30Z"},"source":{"type":"TileWMS","urls":["https://gpwmap.jaxa.jp/wms"],"params":{"layers":"EODASH:NDVI-GCOMC-World-Monthly","styles":"","format":"image/png","time":"2024-07-16T11:59:30Z"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="3.5452614282206953" center=[12.729978307915157,44.02861456759007] animationOptions={duration:500}}-->
#### GCOM-C/SGLI L3 Normalized Difference Vegetation Index (NDVI)

#### observation date: 16 July 2024
 
 [View dataset](https://eodashboard.org/explore?indicator=E10e)

### <!--{ center="[-100,55]" zoom="4" }-->

While in the southern latitudes the boreal tree cover is declining, at northern latitudes it is turning into a tundra, a biome characterised by lower albedo, less vegetation and lower biomass. This phenomenon can have significant impacts on the global carbon cycle, accelerating climate change. 

**Above ground biomass (AGB)** is a key biophysical ecosystem variable describing all living biomass above the soil including stem, stump, branches, bark, seeds and foliage. These shifts of AGB in boreal forests can be measured by radar satellites such as ALOS-PALSAR. 

##
The northern forests of Canada and Alaska are shifting northwards as a result of climate change, with trees expected to grow in areas previously was too cold for them. At the same time, in the southern parts of the boreal forest, where trees were adapted to colder conditions, the climate is expected to become too warm and dry. As the loss of trees in the southern boreal forest is expected to happen at a faster rate than their gain in northern regions [(12)](https://www.nature.com/articles/s41467-023-39092-2), the boreal forest is on the verge of contracting. 

The shift to tundra along with the more frequent wildfires, contribute to a concerning pattern wherein boreal forests are approaching a critical threshold - more carbon is being released from organic soils in boreal forests than the ecosystems can absorb. This is resulting in a transition of boreal forest from being carbon sinks to becoming significant sources of global emission [(13)](https://climate.nasa.gov/news/2905/boreal-forest-fires-could-release-deep-soil-carbon/), [(14)](https://alaskabeacon.com/2023/03/03/extreme-wildfires-are-turning-worlds-largest-forest-ecosystem-from-carbon-sink-into-net-emitter/). In fact, in 2021 boreal fires emissions accounted for nearly one quarter of global carbon emissions, setting a record-high CO2 emissions from boreal fires. 

To better understanding the vulnerability and resilience of the Arctic and boreal ecosystem to environmental change, NASA created the “Arctic Boreal Vulnerability Experiment (ABoVE)” [(15)](https://above.nasa.gov/index.html?), focusing on linking field-based, process-level studies with geospatial data products derived from airborne and satellite sensors, aiming to improve the capacity to understand and predict ecosystem responses and societal implications. 

## Tropical Forests <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"LIS_Global_DA_Evap-2021-12-01T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap_name=viridis&rescale=0,0.0001&url=s3://veda-data-store/lis-global-da-evap/LIS_Evap_202112010000.d01.cog.tif"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="4.088594761554028" center=[-92.28299168545699,-21.97055668964063] animationOptions={duration:500}}-->
#### Amazon rainforest: the next Savanna?

![AmazonForest](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/stories/forest_story/AmazonForest.png)

In the Amazon, deforestation and climate change enhance the risk to reach a tipping point [(16)](https://www.esa.int/Applications/Observing_the_Earth/Space_for_our_climate/Forest_degradation_primary_driver_of_carbon_loss_in_the_Brazilian_Amazon). 

This ecosystem, thanks to its trees, has the ability to generate its own rainfall. However, ongoing deforestation is fundamentally changing how the land and atmosphere interact, leading to higher surface temperatures and reduced evapotranspiration leading to the ‘drying out’ of the forest.’ This alteration is particularly pronounced during dry seasons when rainfall in the southern Amazon diminishes significantly. Simultaneously, climate change, spurred by escalating greenhouse gas concentrations, further curtails evapotranspiration due to CO2 fertilisation and the closing of stomata in response to escalating temperatures. Both mechanisms collectively decrease rainfall recycling across the Amazon, intensifying drought stress and elevating the likelihood of fires [(17)](https://www.nature.com/articles/s41558-022-01287-8).

### NASA Evapotranspiration Dataset
#### observation date: December 2021

[View the LIS 10km Global DA dataset](https://eodashboard.org/explore?indicator=LIS_Global_DA_Evap)

Less trees mean a diminished release of water vapour in the atmosphere, consequently reducing cloud formation and precipitation, which ultimately lead to droughts and wildfires [(18)](https://www.scientificamerican.com/article/amazon-rain-forest-nears-dangerous-tipping-point/). This cycle forms a positive feedback loop, perpetuating reduced evapotranspiration and carbon stocks. Whether stemming from localised deforestation impacts or broader global climate shifts, scientific consensus asserts a future for the Amazon characterised by increased warmth and aridity. 

As a result, the Amazon rainforest is gradually losing its unique ability to ‘bounce back’ after disruptive occurrences, like droughts or other extreme events, leading to a downward spiral where rainforest will shift into a savanna [(19)](https://www.nature.com/articles/s41558-022-01287-8).
Savannas are generally less efficient than tropical forests at sequestering carbon dioxide from the atmosphere, and recent studies indicate that certain areas of the Amazon are now releasing more carbon dioxide than they absorb. 

### <!--{ layers='[{"type":"Tile","properties":{"id":"RECCAP2_6_deforested_biomass-2018-01-01T00:00:00Z"},"source":{"type":"XYZ","urls":["https://reccap2.api.brockmann-consult.de/api/tiles/cop28~reccap2-9x108x139-0.0.1.zarr/deforested_biomass/{z}/{y}/{x}?crs=EPSG:3857&time=2018-01-01T00:00:00Z&vmin=0&vmax=5&cbar=YlOrRd"]}},{"type":"Tile","properties":{"id":"osm"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"osm_3857"}}]' center="[-75,-5]" zoom="5" }--> 

### ESA Deforestation Dataset  
#### observation date: 2018

[View the Biomass CCI RECCAP-2 dataset](https://eodashboard.org/explore?indicator=RECCAP2_6)

There remains no definitive agreement on a tipping point leading to widespread rainforest depletion and the proliferation of savanna species (Cerrado) from the biome. Given the intricate interplay between regional land-use alterations and global climate shifts, scientists are working to gain more understanding about this potential 'point of no return' for the Amazon rainforest. The threshold has been estimated to occur when deforestation reaches 20-25%. Currently, the Amazon has already undergone approximately 17% deforestation, which highlights the urgency of conservation efforts to prevent reaching an ecological tiping point.

## Wildfires 

Wildfires are becoming more destructive due to several factors, which include rising temperatures, land use changes, and drought [(20)](https://www.pbs.org/newshour/science/climate-change-is-causing-more-wildfires-and-governments-are-unprepared-says-u-n), which contribute to considerable alterations in vast forested areas, transforming them into barren lands that struggle to sustain diverse ecosystems. Savannas and boreal forests have opposite trajectories of fire activity. 

Fires are declining in savannas and grasslands. In fact, global burned area has declined by ~25% over the past 18 years, largely in savannas and grasslands because of agriculture expansion and intensification [(21)](https://www.science.org/doi/10.1126/science.aal4108). 

On the other hand, fires are increasing in boreal forest ecosystems, albeit with large interannual variability [(22)](https://www.fao.org/3/xii/0207-b3.htm), making it difficult to attribute recent high fire years to an overall positive trend in burned areas. The ESA CCI programme also delivers Global maps of burned area, based on the NASA's Moderate Resolution Imaging Spectroradiometer (MODIS) on board the Terra satellite. 

## <!--{ id="wildfires-map" as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"N2_CO2_diff-2022-02-13T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap_name=rdbu_r&rescale=-1e-06,1e-06&url=s3://veda-data-store/co2-diff/xco2_16day_diff._2022-02-13.tif"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="3.321928094887362" center=[49.110112218277,42.5045134584679] animationOptions={duration:500}}-->
#### NASA OCO-2 Carbon Dioxide Difference
This map shows the difference in carbon dioxide (CO2) levels on the observation date (28 July 2021) compared to the 2015-2019 baseline. Redder colors indicate increases in CO2. Bluer colors indicate lower levels of CO2.

[View dataset](https://eodashboard.org/explore?search=Global%3A+NDVI&x=9777576.63986&y=6761469.91318&z=4.04859&indicator=N2_diff&area=POLYGON%28%2891.6860897901812+59.16301123078122%2C139.41269053968733+59.16301123078122%2C139.41269053968733+69.43080822422633%2C91.6860897901812+69.43080822422633%2C91.6860897901812+59.16301123078122%29%29)

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"N2_CO2_diff-2021-07-30T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap_name=rdbu_r&rescale=-1e-06,1e-06&url=s3://veda-data-store/co2-diff/xco2_16day_diff._2021-07-30.tif"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="4.048594761554028" center=[87.83346537234536,51.78570157047935] animationOptions={duration:500}}-->


#### Siberian Boreal Forests - 2021 Wildfires 
**NASA OCO-2 Carbon Dioxide Difference, 28 July 2021**

![Siberia](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/stories/forest_story/Siberia.png)

In August 2021, wildfires in Siberia produced 800 megatons of carbon dioxide, nearly double the previous year [(23)](https://www.space.com/siberia-wildfires-greenhouse-gas-emissions-satellite-images). According to estimates by the European Copernicus Atmosphere Monitoring Service (CAMS), more carbon dioxide was released in two and half months than the world’s six most polluting countries emit in a year. Climate change is exacerbating both drier and warmer conditions, fueling more frequent and farther-reaching wildfires that release massive amount of carbon into the atmosphere [(24)](https://www.nrdc.org/stories/climate-tipping-points-are-closer-once-thought). Also, there is consistent evidence that the intervals between fires are shortening, meaning that more carbon is being released from organic soils in boreal forests than the ecosystems can reabsorb, adding up to the trend where boreal forests are leading to a tipping point in that they are becoming a source for global emissions from biomass burning [(25)](https://earthsky.org/earth/wildfires-turn-worlds-largest-forests-carbon-sinks-emitters/) [(26)](https://alaskabeacon.com/2023/03/03/extreme-wildfires-are-turning-worlds-largest-forest-ecosystem-from-carbon-sink-into-net-emitter/) [(27)](https://climate.nasa.gov/news/2905/boreal-forest-fires-could-release-deep-soil-carbon/).

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"N2_CO2_diff-2022-02-13T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap_name=rdbu_r&rescale=-1e-06,1e-06&url=s3://veda-data-store/co2-diff/xco2_16day_diff._2022-02-13.tif"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="4.005261428220694" center=[-71.06956073988155,-21.13234596475597] animationOptions={duration:500}}-->
#### Grasslands and Savannas
**NASA OCO-2 Carbon Dioxide Difference, 13 February 2022**

Some of the world’s most relevant woody biomes, the savannas, might be facing tipping point [(28)](https://www.researchgate.net/publication/257198227_Mega-fires_tipping_points_and_ecosystem_services_Managing_forests_and_woodlands_in_an_uncertain_future). Fires which play a crucial role in the maintenance and stabilisation of savannas in regions where forest is also a viable stable ecosystem state. Across the grasslands of Asia, the tropical forests of South America, and the savannas of Africa, shifting livelihoods are leading to a significant decline in burned area. By using space assets to detect fires and burn scars, researchers found an ongoing transition from nomadic cultures to settled lifestyles and intensifying agriculture, which has led to a steep drop in the use of fire for land clearing and an overall drop in natural and human-caused fires worldwide. In traditional savanna cultures, people often set fires to keep grazing lands productive and free of shrubs and trees. But as many of these communities have shifted to cultivating permanent fields and building more houses, roads, and villages, the use of fire has declined [(29)](https://earthobservatory.nasa.gov/images/90493/researchers-detect-a-global-drop-in-fires).

Conversely, other activities such as fire suppression have allowed fuel loads to accumulate, resulting in a dramatic increase of wildfire intensity. While much of the evidence comes from Australia and the USA,
additional insights can be gained from other regions as well.

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"N2_CO2_diff-2019-04-28T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap_name=rdbu_r&rescale=-1e-06,1e-06&url=s3://veda-data-store/co2-diff/xco2_16day_diff._2019-04-28.tif"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="4.005261428220694" center=[7.2278600853748705,-14.509631285836164] animationOptions={duration:500}}-->
#### Central Africa
**NASA OCO-2 Carbon Dioxide Difference, 28 April 2019**
In Central Africa, the slash-and-burn agriculture practice combined with the seasonal rise in temperature are primarily responsible for wildfires in Central Africa. In 2019, data from NASA's MODIS satellite revealed Central Africa experienced five times the number of wildfires as the Amazon, although the phenomena and impacts in the two regions are not equivalent [(30)](https://www.newsweek.com/nasa-images-show-africa-has-five-times-more-wildfires-burning-amazonheres-why-theyre-1456382) . The changes in savanna, grassland, and tropical forest fire patterns are so large that they have so far offset some of the increased risk of fire caused by global warming. The impact of a warming and drying climate is more obvious at higher latitudes, where fire has increased in Canada and the American West. Regions of China, India, Brazil, and southern Africa also showed increases in burned area.

### <!--{ layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"N2_CO2_diff-2021-09-25T00:00:00Z"},"source":{"type":"XYZ","urls":["https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?resampling_method=nearest&bidx=1&colormap_name=rdbu_r&rescale=-1e-06,1e-06&url=s3://veda-data-store/co2-diff/xco2_16day_diff._2021-09-24.tif"]}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="6.953333333333323" center=[-120.93207191099233,35.63636581719439] animationOptions={duration:500}}-->
#### California, US
#### Central Africa
**NASA OCO-2 Carbon Dioxide Difference, 25 September 2021**
![California](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/stories/forest_story/California.png)

According to the U.S. Forest Service, recent fires have killed from 13 to 19% of the world’s giant sequoias in 2020 and 2021 alone [(31)](https://insideclimatenews.org/news/23092022/california-sequioa-wildfires/). [(32)](https://www.nps.gov/articles/000/2021-fire-season-impacts-to-giant-sequoias.htm), causing concern in the scientific community that California forests may be nearing a tipping point from wildfires. Giant sequoias evolved to survive and thrive under lightning-ignited wildfires. In fact, the giant trees depend on fire to release the seeds inside their cones and to remove competing trees that would otherwise deprive them of the ample sunlight they need to flourish [(33)](https://150.parks.ca.gov/?page_id=27588).

However, the increased severity of fires in recent years, fueled by the racing pace of global warming, is threatening the giant sequoias. In 2021 two very large fires, the Kings Canyon National Park “(KNP) Complex Fire ”and the “Windy Fire”, burned in the southern Sierra Nevada mountains of California in 2021. They had a significant impact on the region's giant sequoia groves, killing thousands of trees. On September 15, 2021 the Operational Land Imager (OLI) on Landsat 8 [(34)](https://landsat.gsfc.nasa.gov/satellites/landsat-8/) acquired an imagery of the “KNP Complex fire” - the largest wildfire in California history at the time. 

The instrument allowed to depict fire fronts beneath the plumes thanks to the thermal signature provided by infrared data [(35)](https://earthobservatory.nasa.gov/images/148840/fire-encroaching-on-giant-sequoias). Satellite images of the KNP Complex and Windy Fire, both within the Sequoia National Park, were captured by the Geostationary Operational Environmental Satellite 17 (GOES-17) [(36)](https://www.goes-r.gov/multimedia/dataAndImageryImagesGoes-17.html), which prompted authorities to issue evacuation orders [(37)](https://earthobservatory.nasa.gov/images/148878/southern-california-under-smoke).

The following year, 4800 acres burned from 7th to 30th of July causing road closures for multiple weeks. These fires were part of a larger pattern of wildfires in the western United States, where wildland fires occur more frequently and over a longer period each year as the fire season extends. NASA Earth has been spatializing and mapping wildfires since 1950 [(38)](https://appliedsciences.nasa.gov/our-impact/news/washburn-fire-fits-pattern-longer-and-more-frequent-wildfires).

## Human proximity and resilience 

### Temperate forests

Due to their moderate climates, fertile soils, and vegetation productivity, temperate forest regions have historically attracted human settlement. Consequently, these forests are often situated in proximity to large human populations and have faced substantial impacts from human activities. These impacts encompass pollution, deforestation for agricultural expansion, and the introduction of invasive pests and diseases, all of which significantly affect the health and sustainability of these ecosystems [(39)](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/temperate-forest).

![temperate](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/stories/forest_story/temperate.png)

Recent studies [(41)](https://www.nature.com/articles/s41586-022-04959-9) indicate that this type of forest is on the verge of reaching a tipping point. This looming risk stems from several factors, including climate change, land-use alterations, the introduction of invasive species, and other disturbances. These factors can result in a notable decline in forest resilience, characterized by two primary aspects: the forest's ability to recover after a disturbance and its capacity to withstand the highest level of disturbance [(42)](https://besjournals.onlinelibrary.wiley.com/doi/pdf/10.1111/1365-2745.12337). Reductions in forest resilience are statistically associated with abrupt declines in forest primary productivity, occurring as a response to gradual movement toward a critical resilience threshold.

The biomass of some temperate forests exceeds that of any tropical forest. They provide critical ecosystem services, and recent evidence indicates the global importance of carbon sinks in the temperate forest zone, especially in eastern North America. While temperate forests generally have lower biodiversity compared to tropical forests, they do feature hotspots with high levels of endemism [(43)](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/temperate-forest). In Europe, the situation is concerning, with less than half of the continent’s original forested areas remaining. Deforestation is accelerating across the developing word, largely driven by human population growth [(44)](https://www.esa.int/Applications/Observing_the_Earth/Space_for_our_climate/Forests). A study published in Nature reported a worrying trend: canopy mortality has doubled in Europe’s temperate forests over the past three decades [(45)](https://www.nature.com/articles/s41467-018-07539-6).

Another article also published in the same journal estimated a global decline in forest resilience over the past two decades, affecting not just temperate forests but also tropical and arid forests. This decline is likely linked to increased water stress and the broader impacts of climate change [(41)](https://www.nature.com/articles/s41586-022-04959-9).


## Restoration and conservation 

![](https://images.pexels.com/photos/142497/pexels-photo-142497.jpeg)


#### Secondary forest growth - ESA CCI RECCAP2

One of the main drives of degradation in sub/tropical countries is unsustainable logging [(46)](https://iopscience.iop.org/article/10.1088/1748-9326/7/4/044009). To counter this, many private companies, public institutions and non-governmental organisations (NGOs) are stepping up their forestry conservation pledges. But given the size and accessibility of many locations on Earth, a crucial component in these efforts is the use of satellite-based forest monitoring systems. For instance, such system have been instrumental in slowing down deforestation in Brazil [(47)](https://earthobservatory.nasa.gov/images/145988/tracking-amazon-deforestation-from-above). [View dataset](https://eodashboard.org/explore?indicator=RECCAP2_5)

## <!--{ as="iframe" src="https://www.youtube.com/embed/wF_td3QRBuM" width="100%" height="500px" frameBorder="0" scroll="no" style="overflow:hidden" }-->

##

<figcaption>A series of USGS Landsat and Copernicus Sentinel-2 images showing secondary forest regrowth near Rio Capim, in the Brazilian Amazon, from 1985 to 2022.Source: https://www.esa.int
</figcaption>


One notable example of these technologies in action is the Global Forest Watch. This online platform leverages satellite data to support monitoring and evaluation of conservation projects, playing a vital role in international efforts to reduce deforestation.

Synthetic aperture radar (SAR), which can observe land surface through clouds, is also useful technology for monitoring deforestation especially in tropical forests. Japan International Cooperation Agency (JICA) and JAXA are operating “the JICA-JAXA Forest Early Warning System in the Tropics” (JJ-FAST), which provides the latest information on deforestation and forest changes in tropical regions globally, on an average of once every 45 days by utilizing ALOS-2 observation data. JJ-FAST is utilized operationally in some countries in the South America and Africa for monitoring deforestation including illegal logging.
