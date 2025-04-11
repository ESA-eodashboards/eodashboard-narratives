---
cover-image: https://www.eodashboard.org/data/story-images/Cambodian_rivers.jpg
date: 2025-01-01
theme: oceans
tags: algae,lakes,water
official: true
---

#   Algal blooms in lake waters <!--{ as="img" mode="hero" src="https://www.eodashboard.org/data/story-images/Cambodian_rivers.jpg" }-->
### Read more about observing the increases in algal blooms with ESA, NASA and JAXA satellites <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Temperature, ice cover and precipitation changes impacting algae bloom on Lake Vänern

Algal blooms in lake waters are frequently associated with elevated nutrient levels, in particular phosphorus and nitrogen [1]. These nutrients can enter waterways from point sources such as agriculture or industrial and wastewater treatment plants discharge. Runoff from urban and farmland areas from nutrient-enriched rainfall are additional sources. When there is an overabundance of these nutrients in a lake, eutrophication occurs. Excess of nutrients can cause algal blooms, which can lead to a tipping point where the algae consume oxygen and block sunlight for underwater plants.

Excess nitrogen input from agricultural practices is often the main cause of increased algae growth. However, for Lake Vänern, the largest lake in Sweden and the third-largest lake in Europe, changes in water temperature have been identified as the biggest contributor to the growth of algae [2, 3], together with changes in precipitation patterns [4,5] and lake ice cover, particularly during the warm and dry seasons.

![](https://github.com/eurodatacube/eodash/blob/master/app/public/data/story-images/Eodashboard_lakevanern_2307112.png?raw=true)

A study concluded that total phytoplankton biomass has significantly increased since the 1980s at the same time as total phosphorus and inorganic nitrogen concentrations have significantly decreased [4]. These findings showed that decreasing acidity in combination with increasing water temperatures played a bigger role for phytoplankton growth than nutrient concentrations. This suggested that phytoplankton biomass in oligotrophic small and large lakes is strongly associated with climate and atmospheric depositional change, and that temperature change affects not only phytoplankton growth but also its composition [6].

Warmer winters are also causing an earlier break-up of lake ice, which can lead to an earlier occurrence of the spring phytoplankton bloom in Lake Vänern [7]. As winters in Sweden have become warmer since the 1990s, the timing of ice break-up and the growth and decline of spring phytoplankton have shifted to start earlier. This spring-ward shift in phytoplankton population growth resulted in an extension of the growing season by at least one month [7].

Nevertheless, the nutrients are still a contributing factor to the occurrence of algae blooms in this lake. Changes [2] in precipitation patterns have influenced the lake’s water level and nutrient inputs [8] which can affect the growth of algae. As precipitation will generally increase mostly in the west part of Sweden and during the winter season, flooding on the watercourse in west and southwest Sweden can lead to increased nutrient inputs in Lake Vänern [5].

Moreover, the intense algae or cyanobacteria blooms have impacted drinking water production, irrigation and recreation in Vänern [4]. They resulting changes in water quality, including increased turbidity and reduced oxygen levels harm fish populations and other aquatic organisms, and can affect recreational activities such as swimming and fishing.

### Graph

The graph shows the variation in Lake Vänern's extent (in km2) between 2010-2020, based on ESA CCI data:

    Chart / Graph 1
![](https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2022/04/scandinavian_peninsula/24030319-2-eng-GB/Scandinavian_Peninsula_article.jpg)
*Almost cloud-free Scandinavian Peninsula captured by Copernicus Sentinel-3 mission on 20 March, lake Vänern is visible in the south, [CC BY-SA 3.0 IGO](https://www.esa.int/ESA_Multimedia/Terms_and_Conditions)*

## Rising temperatures and algae bloom

The water quality of Lake Biwa, the largest freshwater lake in Japan, northeast of Kyoto, and its related rivers is improving due to the reduction of inflow pollution load. This lake supplies city and industrial water for 13 million residents in the surrounding megalopolis [1,2]. However, despite improvements resulting from inflow pollution, climate change is still affecting Lake Biwa, and ecosystem issues such as the decrease in native fish and shellfish are becoming apparent.

![](https://github.com/eurodatacube/eodash/blob/master/app/public/data/story-images/Eodashboard_lakebiwa_2307112.png?raw=true)

One of the reasons for this is the direct impact of the increase in alien species and the deterioration of their habitats, as well as changes in the nutrient balance and plankton species composition due to various environmental changes, including climate change. It has also been pointed out that changes in the ecosystem balance of Lake Biwa may affect living things through the food chain. In recent years, it has been observed that the ‘overturn’(1) in Lake Biwa has not been completed and that the oxygen-poor state in the deep-water layer of Lake Biwa has been prolonged because of climate change. The water temperature of Lake Biwa (annual surface layer average) is rising as shown in the following figure.

![](https://github.com/eurodatacube/eodash/blob/master/app/public/data/story-images/Inland_lakes_water_temp_Biwa.jpg?raw=true)
*Average water temperature change in Lake Biwa, [CC SEndo Kouta](http://endoh7735.sakura.ne.jp/biwako/warming.htm)*

### Map

The map shows the lake surface temperature for lake Biwa based on ESA CCI data. [9] [10] [Access this Dataset](https://eodashboard.org/explore?search=Lake+Biwa%3A+Surface+Water+Temperature&x=15146872.04727&y=4190727.05511&z=9.7556&indicator=Lakes_SWT&poi=Biwa-Lakes_SWT)

Even in the middle of summer when the surface water temperature is around 30°C, it remains around 10°C at a depth of 20m or deeper below the thermocline. When the thermocline is formed, the water does not mix vertically, and the supply of oxygen to the bottom of the thermocline becomes stagnant. In addition, in the deep-water layer, oxygen dissolved in water is consumed by the decomposition of organic matter such as dead plankton deposited on the bottom of the lake, and respiration of organisms in the water and on the bottom of the lake. In many deep lakes in the temperate zone, including Lake Biwa, Overturn reaches the entire lake once a year, supplying oxygen to the bottom of the lake.

In March 2019, the impact of the warm winter was significant, and for the first time in observational history, the lake water did not sufficiently mix into a part of the deep waters off Imazu (water depth of about 90 m). In March 2020, Overturn was not confirmed in this water area and Overturn was not completed for the second consecutive year. In March 2021, Overturn was confirmed for the first time in three years. However, problems such as persistently high Chemical Oxygen Demand (COD)(2); outbreaks of blue-green algae; massive growth of aquatic plants, and a decline in native fish and shellfish are still occurring.

## Map Example <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Tile","properties":{"id":"Overlay labels"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"Lakes_SWT_surface_water_temperature"},"source":{"type":"TileWMS","urls":["https://services.sentinel-hub.com/ogc/wms/0635c213-17a1-48ee-aef7-9d1731695a54"],"params":{"layers":"LAKES_SURFACE_WATER_TEMPERATURE","styles":"","format":"image/png"}}},{"type":"Tile","properties":{"id":"Terrain light"},"source":{"type":"XYZ","urls":["//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpg"]}}]' zoom="9.755600344264382" center=[136.06666666666666,35.197308803042446] }-->

<small><i>(1) Overturn: From autumn to winter, when the temperature of the surface water drops, the thermocline weakens and gradually descends to the deep-water layers, gradually mixing the lake water from the surface to the deep-water layers. The thermocline reaches the depths and disappears, and the mixing of the lake water progresses to the bottom of the lake, making the water temperature, dissolved oxygen concentration, and water quality uniform from the surface layer to the bottom layer (the layer directly above the lake bottom). This phenomenon is called “Overturn.”</i></small>

<small><i>(2) Chemical Oxygen Demand (COD) is a measure of the amount of oxygen required to chemically oxidise organic and inorganic substances in water or wastewater. It is a common parameter used to assess the pollution level and the organic content of water.</small></i>

A study using the Second Global Imager (SGLI) on board the Global Change Observation Mission - Climate "SHIKISAI" (GCOM-C), compared the concentration distribution of phytoplankton chlorophyll-a (Chl-a) and the surface temperature around Lake Biwa from 2018 to 2021. GCOM-C observes from the ground with 19 channels from the near-ultraviolet region to the infrared region, allowing to observe various physical quantities such as land, atmosphere, ocean, snow and ice by using channels according to purpose [4]. When comparing SGLI data of May and November of 2019 and 2020, which were warmer winters, against the same period in 2018 and in 2021, one noticeable difference was the change in the circulation process throughout the year. It is conjectured that 2021 seems to show a normal chlorophyll-a concentration (when compared to the two prior years) which could be possible linked to the fact that during this year, overturn was confirmed for the first time in three years [5, 6,7].





