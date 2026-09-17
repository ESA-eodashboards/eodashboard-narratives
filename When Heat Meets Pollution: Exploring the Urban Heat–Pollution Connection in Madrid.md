---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
official: false

# When Heat Meets Pollution: Mapping Madrid’s Urban Heat–Air Quality Connection from Space <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/7a9015e727bdd1b39edfc85fc116f6b7f4a9c91d/assets/vittorez/WhatsApp-Image-2026-09-18-at-00.09.00-1789683136373.jpeg" }--> 


####

## Authors: Gianluca Flaminio¹, Nikolina Zallemi¹, Vittoria Rezzuto¹, and Thomas Xolias²
> ¹ Politecnico di Milano  ² Aristotle University of Thessaloniki

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub on 14-18 September 2026. It was developed by a team from Politecnico di Milano and Aristotle University of Thessaloniki.*

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/it/archive/b/be/20260803144359%21Logo_Politecnico_Milano.png" alt="Politecnico di Milano" height="80" style="margin: 0 15px;"/>
  <img src="https://thumb.wikimedia.org/wikipedia/en/thumb/c/c8/ESA_Patch_2026.svg/1280px-ESA_Patch_2026.svg.png?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=thumbnail" alt="ESA" height="80" style="margin: 0 15px;"/>
  <img src="https://www.auth.gr/wp-content/uploads/banner-horizontal-black-en.png" alt="Aristotle University of Thessaloniki" height="80" style="margin: 0 15px;"/>
</p>

## Challenge
### Can the same urban fabric that stores heat also shape the air we breathe?

Cities transform both the surface energy balance and atmospheric composition. Asphalt, roofs and other impervious materials absorb and store solar energy, vegetation is unevenly distributed, traffic and heating emit nitrogen oxides, and urban geometry changes ventilation and heat release. These processes do not operate independently: heat, atmospheric mixing, emissions and chemistry can reinforce or oppose one another depending on season and time of day.

Madrid provides a particularly relevant case study. [Arup](https://www.arup.com/news/madrid-suffers-most-extreme-urban-heat-island-hot-spot--new-international-survey-shows/ ) reported that Madrid showed the most extreme Urban Heat-Island hot spot among the six major cities included in its international survey, with a modelled urban-rural contrast of **8.5°C** on the day analysed. The same study highlighted strong evening exposure among vulnerable population groups. These values provide context rather than a direct benchmark for our analysis because they refer to a different year, methodology and temperature variable.

Madrid's heat exposure was again visible from space in June 2026. During an exceptional western-European heatwave, [ESA](https://www.esa.int/ESA_Multimedia/Images/2026/06/Europe_feels_the_heat_beneath_our_feet?) highlighted Sentinel-3 observations showing very high land-surface temperatures across Spain, including Madrid. 
![Screenshot 2026-09-18 010510.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/3d3adaf4b0f174cb85bec43d1e101aa5b6f49eec/assets/NikolinaZallemi/Screenshot-2026-09-18-010510-1789686475564.png)
<p align="center" style="color: #888; font-size: 0.85em;">
  Source: ESA.
</p>
This underlines a key distinction in our study: **Land Surface Temperature (LST)** describes the temperature of the surface and can become substantially hotter than the near-surface air temperature experienced by people.

We ask a simple question with a complex answer: **Where heat persists across Madrid, do air-pollution patterns follow the same geography, and does that relationship change between winter and summer and between day and night?**

## Objective

The objective is to investigate the spatial and temporal relationship between **LST**, **near-surface air temperature**, **nitrogen dioxide (NO₂)**, **ozone (O₃)**, **vegetation (NDVI)** and **elevation** across Madrid during **January and July 2026**.

Rather than asking only whether two maps look similar, the analysis quantifies how much of the observed spatial variability in LST is associated with meteorology, vegetation, topography and air-pollution.

A second objective is to test whether NO₂ and O₃ provide additional explanatory information once air temperature, NDVI and elevation are already accounted for.

## Analysed phenomena

### Urban heat island and land-surface temperature

The **Urban Heat Island (UHI)** describes the tendency of urban areas to be warmer than their rural surroundings. It can be observed in different parts of the urban climate system. A **surface UHI** is expressed through differences in land-surface temperature, while the **canopy-layer UHI** concerns near-surface air temperature. The two are physically related but are not interchangeable and may peak at different times of day.

Satellite thermal infrared observations are particularly useful for mapping the surface expression of urban heat. They show how strongly roofs, roads, bare soil, vegetation and other surfaces heat and cool. Air temperature, by contrast, describes the state of the lower atmosphere and is generally smoother in space.

### Nitrogen dioxide

**NO₂** is a reactive trace gas associated mainly with combustion sources such as road traffic, industry and residential heating. Its spatial distribution depends not only on emissions but also on wind, atmospheric mixing, boundary-layer depth and chemistry. Stable conditions can allow pollutants to accumulate near the surface, while stronger daytime mixing can dilute them.

NO₂ also has a marked diurnal cycle. Concentrations can increase during traffic periods or under shallow, stable boundary layers and decrease when stronger mixing and photochemical transformation become important. This means that a high-NO₂ pattern cannot be interpreted independently of meteorological conditions.

### Ozone

**O₃** behaves differently from a directly emitted pollutant. Tropospheric ozone is formed through photochemical reactions involving nitrogen oxides and volatile organic compounds in the presence of sunlight. In urban environments, fresh nitric oxide emissions can also remove ozone locally through titration. NO₂ and O₃ may therefore show contrasting spatial and temporal behaviour, and their statistical relationship depends on sunlight, emissions, transport and boundary-layer conditions.

### Vegetation and topography

**NDVI** is used as an indicator of vegetation greenness and abundance. Vegetated surfaces can modify surface temperature through shading, evapotranspiration and different radiative properties relative to built surfaces. **Elevation** is included as a topographic control because temperature patterns across the Madrid region may also reflect altitude rather than urbanisation alone.

#### NDVI
<div style="display: flex; gap: 0px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/2d1c2767f70007ad2d25be452ce624631721eb74/assets/vittorez/ndvijanuary-1789657144484.png" style="width: 100%; object-fit: contain; aspect-ratio: 1/1;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/cfbf6ab1b282b802591491bf645fa2afcd336a25/assets/vittorez/ndvijuly-1789656529381.png" style="width: 130%; object-fit: contain; aspect-ratio: 1/1;" />
</div>
<p align="center" style="color: #777; font-size: 0.85em;">
  Spatial distribution of NDVI across Madrid in January and July 2026.
</p>

#### Elevation

<p align="center">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/d2fd45aac11c10b636ef956b5767d87df4ec0934/assets/vittorez/DEM-1789656842797.png"
       style="width: 60%; max-width: 750px;" />
</p>

<p align="center" style="color: #777; font-size: 0.85em;">
  Digital Elevation Model of the Madrid study area. The bounding box indicates the area analysed in this study.
</p>

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=3 center=[0,20] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### From Space
Heat leaves a footprint. Pollution does too.
From hundreds of kilometres above Earth, satellites allow us to observe both. They capture the temperature of the land surface, the greenness of vegetation, and the atmospheric signatures of pollutants across entire cities.

### <!--{ zoom=6 center=[-3.7,40.4] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### Zooming into Spain

*"An exceptional heatwave is affecting countries across western Europe, with cities and regions of France, Spain and southern Italy experiencing unseasonal temperatures."*

**"Europe feels the heat beneath our feet" - ESA, 25/06/2026**

The event provides the large-scale thermal context for our July analysis: intense solar heating can produce very high surface temperatures over central Spain, while urban materials can retain part of that heat after sunset.

### <!--{ zoom=11 center=[-3.7038,40.4168] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Tile","properties":{"id":"osm-borders","opacity":0.8},"source":{"type":"XYZ","url":"https://tile.openstreetmap.org/{z}/{x}/{y}.png"}}]' animationOptions='{"duration":500}' }-->
#### Focusing on Madrid

*"Madrid's urban centre has the most extreme urban heat island (UHI) 'hot spot' of six major cities around the world, with temperatures 8.5°C hotter than rural surroundings, according to new research by global sustainable development consultancy, Arup."*

*"Within the survey area in Madrid, severe UHI hot spots meant researchers found 500,000 children and elderly people living with evening UHI heat spikes of 7°C or more."*

**"Madrid suffers most extreme urban heat island 'hot spot' - new international survey shows" - Arup, 16/08/2023**

Madrid combines a dense built-up core, major transport corridors, large green spaces and a pronounced elevation gradient. This makes it possible to investigate whether the spatial footprint of heat overlaps with atmospheric-composition patterns and whether vegetation and topography help explain those contrasts.

## Methods

### Study design

Two contrasting months were selected: **January 2026** to represent winter conditions and **July 2026** to represent summer conditions. For the main LST regression workflow, dynamic observations were separated into two local-time windows:

- **DAY:** 11:00-13:00 Europe/Madrid local time
- **NIGHT:** 22:00-24:00 Europe/Madrid local time

Within each date and time window, valid observations were summarised using the **median**. Cloud-contaminated or unavailable LST pixels were retained as missing values rather than filled artificially.

All layers were co-registered to a common **1 km grid in ETRS89 / UTM zone 30N (EPSG:25830)** and clipped to the Madrid study boundary. The common mask contained **2,279 analysis cells**. Resampling provides spatial alignment between datasets.

### Data

| Variable | Source | Role in the analysis | Harmonised representation |
|---|---|---|---|
| Land-surface temperature | Copernicus Sentinel-3 SLSTR | Main response variable | 1 km Madrid grid, DAY/NIGHT |
| Air temperature | ERA5 | Meteorological control | Interpolated/aligned to the common 1 km grid |
| NO₂ | Sentinel-5P TROPOMI for EO visualisation; CAMS gridded fields for the quantitative harmonised analysis | Pollution indicator/predictor | Aligned to the common 1 km grid |
| O₃ | Sentinel-5P TROPOMI for EO visualisation; CAMS gridded fields for the quantitative harmonised analysis | Pollution indicator/predictor | Aligned to the common 1 km grid |
| NDVI | Copernicus Sentinel-2 | Vegetation indicator | Monthly January/July value aligned to 1 km |
| Elevation | CNIG/IGN MDT25 | Topographic control | Aggregated/aligned to 1 km |


### Methodology workflow

The workflow was designed to preserve the physical meaning of each variable while placing all datasets on a common analytical framework.

**1. Spatial harmonisation.** All layers were clipped to the Madrid study boundary, projected to EPSG:25830 and aligned to the same 1 km grid. Finer-resolution NDVI and elevation data were aggregated, whereas coarser atmospheric fields were interpolated for alignment only.

**2. Temporal harmonisation.** Dynamic variables were organised by date and separated into the selected DAY and NIGHT windows. Daily medians were calculated within each time window. January and July were analysed separately to avoid mixing contrasting seasonal regimes.

**3. Exploratory mapping and correlation.** Monthly and daily maps were used to inspect heat, pollutant and air-temperature patterns. Pearson correlation measures linear spatial association, while Spearman correlation is based on ranks and captures monotonic relationships that may not be perfectly linear. Both were used to compare temperature and pollution fields while also reporting the fraction of cells with valid matched data.

**4. Simple spatial regression.** For each month and period, valid cell-date observations were collapsed to one representative value per 1 km cell and simple OLS regressions were used to quantify the relationship between LST and individual predictors. R² is interpreted as the fraction of observed spatial LST variability described by that one-predictor linear model, not as a causal contribution.

**5. Vegetation and elevation analysis.** NDVI is monthly and elevation is static, so separate DAY/NIGHT values would not add physical meaning. For these predictors, a representative monthly LST was calculated for each grid cell as the equal-weight mean of the monthly daytime and nighttime LST summaries:

`Representative monthly LST = (mean daytime LST + mean nighttime LST) / 2`

This uses all available daytime observations and all available nighttime observations without requiring day and night retrievals to occur on the same date. It should be interpreted as a representative combination of the selected day/night windows, **not** as a true 24-hour daily mean.

**6. Multiple regression.** To evaluate whether pollution adds information beyond meteorology and surface controls, two model specifications were compared for each month and period:

`Baseline: LST ~ Tair + NDVI + Elevation`

`Full: LST ~ Tair + NDVI + Elevation + NO₂ + O₃`

For this step, LST, air temperature, NO₂ and O₃ were first matched on the **same cell and the same valid dates** before monthly spatial medians were calculated. This prevents a predictor from being summarised over dates when LST was missing. Heteroskedasticity-consistent **HC3 robust standard errors** were used. Standardised coefficients were calculated to compare relative effect sizes across predictors, and variance-inflation factors (VIF) were inspected for multicollinearity.

The main multiple-regression quantity is:

`ΔR² = R²(full model) - R²(baseline model)`

It measures how much additional spatial LST variance is associated with adding NO₂ and O₃ after air temperature, NDVI and elevation are already included.

## Results

### Land Surface Temperature: Madrid changes character between winter and summer

The Sentinel-3 maps show the expected seasonal contrast: July surfaces are substantially warmer than January surfaces, while daytime LST is generally higher and more spatially heterogeneous than nighttime LST. The night maps are particularly informative because they show where stored daytime heat persists after sunset, when urban materials continue releasing energy.

<div style="display: flex; gap: 0px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/42843771e87e66c404bde5357140eed52e75edf1/assets/vittorez/January2026DAYLST-1789678227552.png" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c07c14130a7d689f23ec2735d89249a0d18ef49b/assets/vittorez/January2026NIGHTLST-1789678253754.png" />
</div>

<div style="display: flex; gap: 0px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/773bab750cd18172c33674ea83c4367ecff7aea8/assets/vittorez/July2026DAYLST-1789678287867.png" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c0fa57c306d500e1297f023f705224734828c03d/assets/vittorez/July2026NIGHTLST-1789678318314.png" />
</div>

<p align="center"><em>Sentinel-3 land-surface-temperature patterns for January and July 2026, separated into the selected daytime and nighttime windows.</em></p>

#### Air temperature
ERA5 provides the meteorological background for the analysis.
<div style="display: flex; gap: 10px; flex-wrap: wrap;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/f5846d22d1d8e72d52c5e1c12bda88eaf61fb31e/assets/vittorez/January2026DAYERA5points-1789664866675.png" style="width: 48%;"/>
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/ddc783ae88471643856a243fb22fb58fad9e77bd/assets/vittorez/January2026NIGHTERA5points-1789664698044.png" style="width: 48%;"/>
</div>
<p align="center" style="color: #777; font-size: 0.85em;">
  Monthly median ERA5 2-m air temperature across Madrid for the selected daytime and nighttime windows in January 2026.
</p>
Winter air temperatures show a clear day–night contrast across Madrid. During the 11:00–13:00 window, the spatial mean is about 5.2 °C, decreasing to 4.3 °C during the 22:00–24:00 window. The maps also reveal a persistent spatial gradient across the region, with warmer conditions generally concentrated toward the southern and central parts of the study area and cooler temperatures toward the north and northwest.

<div style="display: flex; gap: 10px; flex-wrap: wrap;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/5ee7ca898d90bca05ae3b1bfd58ec020467d8747/assets/vittorez/July2026DAYERA5points-1789664734518.png" style="width: 48%;"/>
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/d166097551ceb3144b21b1136853b44a2ef3e9c5/assets/vittorez/July2026NIGHTERA5points-1789664798000.png" style="width: 48%;"/>
</div>
<p align="center" style="color: #777; font-size: 0.85em;">
  Monthly median ERA5 2-m air temperature across Madrid for the selected daytime and nighttime windows in July 2026.
</p>
Summer temperatures are much higher and spatially more uniform across Madrid. The spatial mean reaches about 29.1 °C during the daytime window and 29.5 °C at night. The slightly higher nighttime monthly median reflects the specific selected time windows and the monthly aggregation of ERA5 data, rather than implying that nights are generally warmer than days. The maps nevertheless show that high near-surface air temperatures persist well into the evening, highlighting the limited nighttime thermal relief during summer.

### Nitrogen dioxide: An urban signal shaped by emissions

NO₂ patterns change between season and time of day because emissions, atmospheric mixing and chemistry all vary. The animations show that pollution does not simply follow the temperature field. A high-LST surface and a high-NO₂ atmosphere can coincide because both are linked to dense urban areas, but their relationship can weaken or reverse when boundary-layer mixing and photochemistry change.

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e75cffa4e129c6611205f50637e88eeda8aab387/assets/vittorez/January2026NO2DAYESRI-1789655589787.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/516f4965e19cbc50cb353c5b548e59aa7a344e21/assets/vittorez/January2026NO2NIGHTESRI-1789655678870.gif" style="width: 48%;" />
</div>

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e8d59e29b342c013cbe967e990b9c538246f36b4/assets/vittorez/July2026NO2DAYESRI-1789655733388.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e9f4dacbb2e9ac5069bfe3b75f535e04825b9f6c/assets/vittorez/July2026NO2NIGHTESRI-1789656066047.gif" style="width: 48%;" />
</div>

<p align="center"><em>Seasonal and diurnal shifts in NO₂ over Madrid.</em></p>

### Ozone: A contrasting photochemical pattern

O₃ adds a complementary view of Madrid's atmospheric chemistry. Unlike NO₂, ozone is not emitted directly by traffic. Its distribution reflects photochemical production, transport and chemical loss. The relationship between NO₂ and O₃ therefore changes with sunlight, emissions and atmospheric stability, which is one reason the pollutant-temperature relationship cannot be reduced to a single correlation coefficient.

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/788bce10551db1393e418ee9e227e55207834387/assets/vittorez/January2026O3DAYESRI-1789674050098.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/4baf52f1123b4d21e0fd80f379cf8c9eb19b2c44/assets/vittorez/January2026O3NIGHTESRI-1789674110930.gif" style="width: 48%;" />
</div>

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/92083e76bf511d013515694d41d894666c32f74f/assets/vittorez/July2026O3DAYESRI-1789674453031.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/25ad7c43057f88d27f331bbf235b63431b6b2959/assets/vittorez/July2026O3NIGHTESRI-1789674407166.gif" style="width: 48%;" />
</div>

<p align="center"><em>Seasonal and diurnal shifts in O₃ over Madrid.</em></p>

### Air temperature: The atmospheric background to surface heating

 Although air and surface temperatures are related, they are not equivalent: surface temperature responds directly to solar radiation, material properties, moisture and shading, while near-surface air temperature is mixed through the lower atmosphere.

![January_2026_DAY_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/42b773597b70145ea3940828d26e4f286935757d/assets/vittorez/January2026DAYtemperaturetimeseries-1789665925063.png)

![January_2026_NIGHT_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/0ed1e6201a90d8dd0fd50eba66fbb287b5b9a0eb/assets/vittorez/January2026NIGHTtemperaturetimeseries-1789665960480.png)

In January, the mean temperature over the selected period was approximately 5.33 °C during the daytime window (11:00–13:00) and 4.45 °C during the nighttime window (22:00–24:00). Several short warm and cold episodes are visible during the month. Temperatures dropped markedly around 5–7 January, particularly at night, when the spatial mean approached or fell slightly below 0 °C, whereas warmer episodes occurred around 3 January, 13 January and toward the end of the month, with spatial means approaching 8–10 °C. The close agreement between the spatial mean and median indicates that the overall regional temperature signal is relatively coherent, while the wider separation between spatial minima and maxima shows that meaningful temperature differences remain across the Madrid study area.

Interestingly, the July late-evening mean is slightly higher than the late-morning mean. This should not be interpreted as a general night-versus-day temperature inversion, but rather as a feature of the selected observation windows and the persistence of summer heat into the evening.

![July_2026_DAY_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/fb8a6d73f45ae30a58240f68fdedf0f85c44c677/assets/vittorez/July2026DAYtemperaturetimeseries-1789665978602.png)

![July_2026_NIGHT_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/2160595e7ef4c116aa6725291f1c3e77f51fe2ca/assets/vittorez/July2026NIGHTtemperaturetimeseries-1789666002145.png)

July presents a very different thermal regime, characterized by persistently high temperatures and relatively limited nighttime cooling. Mean air temperature was about 28.96 °C during the daytime window and 29.66 °C during the late-evening/nighttime window. The warmest periods occurred during the first third of the month and again around 21–23 July and at the end of July, when spatial mean temperatures exceeded 31–32 °C. In contrast, a pronounced cooler episode occurred around 25–26 July, when the spatial mean temporarily dropped to approximately 23–24 °C before rapidly increasing again. The relatively high nighttime values indicate that warm atmospheric conditions often persisted well into the evening during July.

### Air temperature, NO₂ and O₃ correlation

The atmospheric correlation plots illustrate why season and time of day must be treated separately. Air temperature, NO₂ and O₃ do not move in lockstep: atmospheric stability, mixing, emissions and photochemistry alter their relationships. In particular, NO₂ and O₃ can carry overlapping or opposing information, so their individual simple-regression slopes should not be interpreted as isolated physical effects.

![January_2026_DAY_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/b92dcccfedc5f5bd8294c312db9346590d8afb8e/assets/vittorez/January2026DAYtemperatureNO2O3-1789665595806.png)

![January_2026_NIGHT_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/5f4a3180dda80702316cd740d213ee7a5612a19b/assets/vittorez/January2026NIGHTtemperatureNO2O3-1789665623159.png)

![July_2026_DAY_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c62611a1d7f80f0483996e0a6888a2a06ee7be77/assets/vittorez/July2026DAYtemperatureNO2O3-1789665645694.png)

![July_2026_NIGHT_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/a364361583f954148f83f25bd6d0e2e19f31f984/assets/vittorez/July2026NIGHTtemperatureNO2O3-1789665686005.png)

### Spatial correlations: Where do heat and pollution overlap?

The spatial-correlation analysis indicates that warmer parts of Madrid generally tend to coincide with higher NO₂ concentrations, but the strength of the relationship depends strongly on season and time window.

For **ERA5 air temperature versus NO₂**, the strongest spatial association in the correlation product occurs in the **July evening window (21:00-23:00)**, with **Pearson r = 0.69** and **Spearman ρ = 0.67**, based on about **94% of valid cells**. A similarly strong relationship is seen in January evening (**r = 0.64, ρ = 0.67**). During the morning/daytime comparison, the relationship is weaker but remains positive, particularly in July (**r = 0.40, ρ = 0.41**).

For **LST versus NO₂**, the clearest result again appears in the **July evening** case, with **r = 0.48** and **ρ = 0.49**, although valid-cell coverage is lower at about **73%**. January daytime/morning shows a moderate positive relationship (**r = 0.41, ρ = 0.45**), while the January evening relationship is weak and slightly negative.

Overall, these results indicate that urban heat and NO₂ hotspots **partially overlap spatially**, particularly under summer evening conditions. This overlap is more plausibly interpreted as the imprint of common urban controls - dense built-up areas, traffic activity, heat storage and reduced ventilation - than as evidence that temperature directly causes higher NO₂.

The **NO₂-O₃ relationship is strongly negative** across the spatial cases, reaching values close to -0.9 to -1.0 in the correlation product. This is consistent with the coupled chemistry of NOx and ozone and reinforces the need to interpret the two pollutants together rather than independently.

![Spatial correlations - January and July](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/eda403b0143816867713b5a5cd7d33ac4dce016b/assets/vittorez/spatialcorrelationsjanuaryjulycombined-1-1789682024434.png)

<p align="center"><em>Spatial correlation summary for January and July. Pearson describes linear association, while Spearman describes rank-based monotonic association.</em></p>

### Simple spatial relationships with LST

The simple regressions provide another view of how the controls on Madrid's surface temperature change with season and time of day. Air temperature is the strongest single atmospheric predictor in January daytime (`R² ≈ 0.17`) and January nighttime (`R² ≈ 0.19`). In July daytime, the spatial air-temperature field alone explains only about `5%` of LST variability, whereas at night the relationship becomes much stronger (`R² ≈ 0.32`).

For the pollution variables, the simple relationships are generally weaker during the day. The clearest bivariate pollution signal occurs in **July nighttime**, when NO₂ alone explains about `17%` of spatial LST variability and O₃ about `18%`. These percentages must not be added: NO₂ and O₃ share spatial information and are influenced by common meteorological and urban processes. The simple regressions are therefore a descriptive step before the multivariable analysis.

### Vegetation and elevation: summer surface structure matters

NDVI is a monthly surface descriptor and elevation is static, so it is more meaningful to relate them to a representative monthly LST than to interpret them as separate DAY/NIGHT variables. For each 1 km cell, all valid daytime LST observations were averaged across the month, all valid nighttime observations were averaged separately, and the two monthly summaries were then given equal weight.

The simple spatial regressions show a clear seasonal strengthening of both relationships:

| Predictor | January 2026 | July 2026 | Interpretation |
|---|---:|---:|---|
| **NDVI - Pearson r** | -0.271 | -0.481 | Greener cells tend to be cooler, especially in summer |
| **NDVI - R²** | 0.073 | **0.231** | Vegetation explains much more of the summer spatial pattern |
| **LST difference per +0.1 NDVI** | -0.29°C | **-0.91°C** | The fitted summer vegetation gradient is much stronger |
| **Elevation - Pearson r** | -0.223 | -0.350 | Higher terrain tends to be cooler |
| **Elevation - R²** | 0.050 | **0.123** | Topographic association also strengthens in July |
| **LST difference per +100 m** | -0.42°C | **-0.61°C** | Negative elevation gradient in both months |

The strongest surface result is the **July NDVI relationship**. NDVI alone explains about **23.1% of the spatial variability** in representative monthly LST, compared with only **7.3% in January**. A +0.1 difference in NDVI is associated with approximately **0.91°C lower LST in July**, versus about **0.29°C in January**. The stronger July relationship is compatible with a greater role for shading and evapotranspiration during intense summer solar heating.

Elevation shows the same seasonal tendency, although its relationship is weaker than NDVI. A 100 m increase in elevation is associated with about **0.42°C lower LST in January** and **0.61°C lower LST in July**. Elevation alone explains about **12.3%** of the July spatial LST variation, compared with **5.0%** in January.

#### Simple-regression figures

<div style="display: flex; gap: 10px; flex-wrap: wrap;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/4397d81ad780cc21c1f91227eadcb68a00c0068f/assets/vittorez/WhatsApp-Image-2026-09-18-at-00.19.03-1789684358349.jpeg" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/133bf34e033fa16d2d6e55e69d3876b752ddc48b/assets/vittorez/WhatsApp-Image-2026-09-18-at-00.19.06-1789684402666.jpeg" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/60b88ad1116638560fe5ada150aa0ba6032f9b7f/assets/vittorez/WhatsApp-Image-2026-09-18-at-00.20.54-1789684433079.jpeg" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/8b456053801a162507ab018e3da49ee50b631916/assets/vittorez/WhatsApp-Image-2026-09-18-at-00.21.46-1789684480025.jpeg" style="width: 48%;" />
</div>

<p align="center"><em>Simple-regression figures summarising the seasonal relationships between representative LST, vegetation and topographic controls.</em></p>

### Multiple regression: does pollution add information beyond meteorology and surface controls?

Simple regressions cannot distinguish independent information from shared urban structure. A pollutant may correlate with LST because both are related to the same built-up areas, traffic corridors, elevation or atmospheric conditions. The multiple regression therefore compares a baseline model with a model that adds the two pollution variables.

- **Baseline:** `LST ~ air temperature + NDVI + elevation`
- **Full:** `LST ~ air temperature + NDVI + elevation + NO₂ + O₃`

The dynamic variables were matched by **exact cell and date** before monthly spatial aggregation, ensuring that LST, air temperature, NO₂ and O₃ were summarised from the same valid observation dates.

| Period | Cells | Baseline R² | Full R² | ΔR² from NO₂ + O₃ |
|---|---:|---:|---:|---:|
| January DAY | 2242 | 0.275 | 0.299 | **+0.024 (2.4 pp)** |
| January NIGHT | 2268 | 0.307 | 0.320 | **+0.013 (1.3 pp)** |
| July DAY | 2279 | 0.291 | 0.305 | **+0.014 (1.4 pp)** |
| July NIGHT | 1766 | 0.361 | **0.455** | **+0.094 (9.4 pp)** |

For **January daytime, January nighttime and July daytime**, adding NO₂ and O₃ increases explained variance by only about **1-2.4 percentage points**. The clear exception is **July nighttime**: the model rises from `R² = 0.361` to `R² = 0.455`. After accounting for air temperature, vegetation and elevation, the pollution fields therefore contain an additional **9.4 percentage points of spatial information** about where LST remains high at night.

This is an **association**, not evidence that NO₂ or O₃ causes the additional warming. The added explanatory value may reflect common spatial patterns linked to urban density, retained heat, emissions, ventilation and nocturnal boundary-layer structure.

### Which variables matter after adjustment?

Because the predictors use different physical units, **standardised regression coefficients (β*)** are more useful than raw slopes for comparing their relative strength within the same model.

| Predictor | January DAY | January NIGHT | July DAY | July NIGHT |
|---|---:|---:|---:|---:|
| Air temperature | **+0.381** | **+0.502** | +0.132 | **+0.522** |
| NDVI | -0.270 | -0.098 | **-0.512** | +0.103 |
| Elevation | -0.109 | +0.333 | -0.061 | +0.260 |
| NO₂ | +0.063 | +0.265 | -0.153 | +0.271 |
| O₃ | -0.117 | +0.206 | -0.043* | -0.163 |

`*` The 95% confidence interval for O₃ in July daytime crosses zero, so its adjusted coefficient is not clearly different from zero in that model.

The contrast between **July day and July night** is especially informative. During the day, NDVI is the dominant adjusted predictor (`β* = -0.512`), indicating lower LST in greener cells after the other variables are controlled. At night, the structure changes: air temperature becomes dominant (`β* = +0.522`), while NO₂ retains a positive adjusted association (`β* = +0.271`) and O₃ a negative one (`β* = -0.163`).

January is more moderate. Air temperature remains the strongest positive predictor in both periods. January nighttime also shows moderate NO₂/O₃ multicollinearity, so the individual pollutant coefficients should be interpreted more cautiously than the combined contribution of the pollution block to model fit.

#### Multiple-regression figures

<div style="display: flex; gap: 10px; flex-wrap: wrap;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/7cce28ec8659fbe30f9237070976b1ceaa6d857f/assets/vittorez/WhatsApp-Image-2026-09-18-at-00.23.20-1789684514508.jpeg" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/5b9b0d7e978f125f27a2184ed380a028ff5f413d/assets/vittorez/WhatsApp-Image-2026-09-18-at-00.23.46-1789684533985.jpeg" style="width: 48%;" />
</div>

<p align="center"><em>Matched-date multiple-regression summaries. The key comparison is the added explanatory value of NO₂ and O₃ and the shift in dominant standardised predictors between July daytime and nighttime.</em></p>

### What the combined results tell us

Taken together, the results describe two different summer regimes. During **July daytime**, the strongest spatial contrast is a surface one: vegetation is closely associated with lower LST, and pollution adds relatively little once vegetation, elevation and air temperature are considered. During **July nighttime**, the explanatory structure becomes more atmospheric: air temperature is the dominant predictor, and the pollution block adds substantially more information than in any other analysed period.

The spatial-correlation analysis points in the same direction. The strongest positive temperature-NO₂ and LST-NO₂ overlap occurs in the summer evening case, while the multiple regression shows that the pollution block retains the largest added explanatory value in July NIGHT. These are related but not identical analyses because the time windows and matching rules differ; together they indicate that the **summer evening/night period is the clearest part of the dataset for joint heat-pollution spatial structure**.

## Discussion

### Madrid's heat story is also a time-of-day story

External studies already show why Madrid deserves close attention. Arup's urban-heat comparison identified Madrid as an extreme heat-island case and highlighted evening exposure, while ESA's June 2026 Sentinel-3 observation illustrates the intensity of the surface heat environment immediately before the July study period. Our analysis does not reproduce those studies directly, but it places the January-July comparison in a broader context of documented heat vulnerability.

The July results reinforce the importance of vegetation. The much stronger negative NDVI-LST relationship in summer is consistent with the physical role of green surfaces in moderating daytime heating through shading and evapotranspiration. The analysis does not isolate individual parks or interventions, but the spatial pattern is compatible with the broader expectation that greener surfaces are often cooler than densely built ones under strong solar forcing.

### Why does the pollution signal become clearer in summer evening/night conditions?

At night, solar forcing disappears and differences in stored heat release, atmospheric stability and urban ventilation become more important. A shallower nocturnal boundary layer can reduce pollutant dispersion while heat stored in buildings and paved surfaces continues to be released. These processes can make heat and pollution patterns more spatially aligned even if pollution itself is not the cause of the heat.

The July-night multiple regression is therefore best interpreted as evidence of **shared spatial structure**. After controlling for air temperature, vegetation and elevation, NO₂ and O₃ still contain information associated with where LST remains high at night. The analysis cannot determine whether this arises from emissions, urban density, atmospheric stability, urban form not explicitly represented in the model, or other covarying processes.

### NO₂ and O₃ should be interpreted together

NO₂ and O₃ are chemically and meteorologically linked. Their strong negative correlations in the exploratory spatial analysis and the moderate multicollinearity seen in the January-night regression show that they are not independent urban tracers. For this reason, the **combined change in model R² after adding both pollutants** is more robust for the narrative than treating each individual coefficient as a separate causal effect.

### Limitations

This is an exploratory **two-month case study**, not a climatology. January and July capture contrasting seasonal conditions but cannot represent interannual variability, the full annual cycle, or the diversity of individual heatwave and pollution episodes. A stronger follow-up study should include multiple years and several warm-season events.

The datasets also operate at different physical scales. Sentinel-3 LST is close to the 1 km analysis grid, whereas ERA5 and especially CAMS atmospheric fields are much coarser. Interpolating them to 1 km improves co-registration but does not create independent 1 km atmospheric observations. Spatial smoothing and spatial autocorrelation among neighbouring cells mean that formal statistical significance can overstate the effective amount of independent information.

Cloud cover is another limitation because thermal-infrared LST is unavailable beneath clouds. The number of valid LST observations therefore varies by grid cell and period. **July nighttime is the sparsest multiple-regression case, with a median of only three matched LST dates per cell**, so its strong result should be interpreted together with that sampling limitation.

The exploratory spatial-correlation figure and the regression workflow also use slightly different time-window definitions. Their agreement in identifying stronger summer evening/night relationships is informative, but the exact correlation coefficients should not be directly substituted into the regression interpretation.

Finally, the study is observational. Correlation and regression identify associations and shared spatial structure, not causal mechanisms.

## Conclusions

Madrid's heat-air-quality relationship is strongly dependent on **season and time of day**. The clearest daytime summer signal is vegetation: NDVI explains about **23%** of the spatial variability in representative July LST in the simple regression, and it remains the strongest standardised predictor in the July daytime multiple model.

The atmospheric picture becomes more important after sunset. In **July nighttime**, adding NO₂ and O₃ to a model already containing air temperature, NDVI and elevation raises the explained spatial LST variance from **36.1% to 45.5%**, an increase of **9.4 percentage points**. The complementary spatial-correlation analysis also shows its strongest temperature-NO₂ and LST-NO₂ overlap in the summer evening case.

These findings do not imply that pollution causes urban surface warming. Instead, they show that **heat retention and atmospheric-composition patterns can share the same urban geography**, particularly under summer evening/night conditions. Dense built-up structure, traffic activity, reduced ventilation, atmospheric stability and stored heat may all contribute to that overlap.

The combined Earth-observation perspective is therefore more informative than any single layer. Sentinel-3 shows where surfaces are hot, ERA5 describes the atmospheric thermal background, Sentinel-5P and CAMS provide complementary views of atmospheric composition, Sentinel-2 reveals vegetation patterns, and the DEM separates part of the topographic signal. Together, they offer a reproducible framework for identifying places where heat and poor-air-quality conditions may coincide and for motivating more detailed neighbourhood-scale studies.

## Open Science

This workflow is built around openly accessible Earth-observation and Copernicus data and can be reproduced for other cities. Reproducibility would be strengthened by publishing the preprocessing and statistical scripts together with the common-grid definition, quality-control rules and metadata for each derived product.

Future work should extend the analysis to more years and heat events, incorporate higher-resolution urban-form information and in-situ air-quality and meteorological stations, and use spatial statistical models that explicitly account for autocorrelation. Comparing satellite/reanalysis results with neighbourhood-scale measurements would also help distinguish physically resolved local variability from patterns inherited from coarser atmospheric products.

## References

1. Weng, Q., Yang, S. *Urban Air Pollution Patterns, Land Use, and Thermal Landscape: An Examination of the Linkage Using GIS.* Environmental Monitoring and Assessment 117, 463-489 (2006). https://doi.org/10.1007/s10661-006-0888-9
2. Fuladlu, K., Altan, H. *Examining land surface temperature and relations with the major air pollutants: A remote sensing research in case of Tehran.* Urban Climate 39, 100958 (2021). https://doi.org/10.1016/j.uclim.2021.100958
3. Goldberg, D. L. et al. *TROPOMI NO₂ in the United States: A detailed look at the annual averages, weekly cycles, effects of temperature, and correlation with surface NO₂ concentrations.* Earth's Future 9, e2020EF001665 (2021). https://doi.org/10.1029/2020EF001665
4. Guo, Y. et al. *Modeling urban air temperature using satellite-derived surface temperature, meteorological data, and local climate zone pattern - a case study in Szeged, Hungary.* Theoretical and Applied Climatology 155, 3841-3859 (2024). https://doi.org/10.1007/s00704-024-04852-7
5. Shen, P., Wang, M., Ma, H. et al. *On the two-way interactions of urban thermal environment and air pollution: A review of synergies for identifying climate-resilient mitigation strategies.* Building Simulation 18, 259-279 (2025). https://doi.org/10.1007/s12273-024-1210-x
6. European Space Agency. *Europe feels the heat beneath our feet.* 25 June 2026. https://www.esa.int/ESA_Multimedia/Images/2026/06/Europe_feels_the_heat_beneath_our_feet
7. Arup. *Madrid suffers most extreme urban heat island "hot spot" - new international survey shows.* 16 August 2023. https://www.arup.com/news/madrid-suffers-most-extreme-urban-heat-island-hot-spot--new-international-survey-shows/
8. Copernicus Sentinel-3 SLSTR Land User Handbook. *Land Surface Temperature product (SL_2_LST).* https://sentinels.copernicus.eu/documents/247904/4598082/Sentinel-3-SLSTR-Land-Handbook.pdf
9. Copernicus Atmosphere Monitoring Service. *CAMS European air quality forecasts / analyses.* https://www.copernicus.eu/en/access-data/copernicus-services-catalogue/cams-european-air-quality-forecasts
10. Copernicus Climate Change Service / ECMWF. *ERA5 hourly data on single levels from 1940 to present.* https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels
11. European Space Agency. *Sentinel-5P data products.* https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-5P/Data_products
12. Centro Nacional de Información Geográfica / Instituto Geográfico Nacional. *MDT25 - 1ª cobertura.* https://centrodedescargas.cnig.es/CentroDescargas/modelo-digital-terreno-mdt25-primera-cobertura

## Contributors

**Authors:** Gianluca Flaminio, Nikolina Zallemi, Vittoria Rezzuto and Thomas Xolias  
**Institutions:** Politecnico di Milano and Aristotle University of Thessaloniki  
**Context:** ESA ESRIN Science Hub Challenge, September 2026



