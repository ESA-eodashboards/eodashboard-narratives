---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: some,tags
official: false

# When Heat Meets Pollution: Mapping Madrid's Urban Heat–Air Quality Connection from Space <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/f1f46716f8557709bf58b1e43426428d124d661f/assets/vittorez/prova-1789676182440.png" }-->
####

## Authors: Gianluca Flaminio¹, Nikolina Zallemi¹, Vittoria Rezzuto¹ and Thomas Xolias²
> ¹ Politecnico di Milano  ² Aristotle University of Thessaloniki

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub on 14–18 September 2026. It was developed by a team from Politecnico di Milano and Aristotle University of Thessaloniki.*

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/it/archive/b/be/20260803144359%21Logo_Politecnico_Milano.png" alt="Politecnico di Milano" height="80" style="margin: 0 15px;"/>
  <img src="https://thumb.wikimedia.org/wikipedia/en/thumb/c/c8/ESA_Patch_2026.svg/1280px-ESA_Patch_2026.svg.png?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=thumbnail" alt="ESA" height="80" style="margin: 0 15px;"/>
  <img src="https://www.auth.gr/wp-content/uploads/banner-horizontal-black-en.png" alt="Aristotle University of Thessaloniki" height="80" style="margin: 0 15px;"/>
</p>

## Challenge
### Can the same urban fabric that stores heat also shape the air we breathe?

Cities transform both the surface energy balance and atmospheric composition. Asphalt, roofs and other impervious surfaces absorb and store solar energy, vegetation is unevenly distributed, traffic and heating emit nitrogen oxides, and urban geometry alters ventilation and heat release. These processes do not operate independently: heat, boundary-layer dynamics, emissions and atmospheric chemistry can reinforce or oppose one another depending on season and time of day.

Madrid provides a compelling case study. An Arup international urban-heat survey reported an extreme Madrid urban heat-island hot spot of **8.5°C relative to rural surroundings** on the hottest day analysed in 2022, and found the built-up centre to be nearly **8°C hotter than El Retiro Park** in its modelled air-temperature comparison. The study also highlighted the importance of evening and night-time heat exposure. These figures are background context rather than a direct benchmark for our 2026 satellite analysis because the methodology, dates and temperature variables differ.

The relevance of Madrid was reinforced again in June 2026, when ESA reported that an exceptional western-European heatwave produced **land-surface temperatures of about 48°C in Madrid** in a late-morning Copernicus Sentinel-3 observation. This illustrates an important distinction at the heart of our analysis: satellite land-surface temperature can become much hotter than the near-surface air temperature experienced by people.

Against this background, we ask whether Madrid's spatial heat patterns coincide with atmospheric-pollution patterns, and whether those relationships change between winter and summer and between day and night.

## Objective

The objective is to investigate the spatial and temporal relationship between **land-surface temperature (LST)**, **near-surface air temperature**, **nitrogen dioxide (NO₂)**, **ozone (O₃)**, **vegetation (NDVI)** and **elevation** across Madrid during **January and July 2026**.

Rather than asking only whether two maps look similar, the analysis quantifies how much of the observed spatial variability in LST is associated with meteorology, vegetation, topography and air-pollution fields. A second objective is to test whether adding NO₂ and O₃ provides additional explanatory information once air temperature, NDVI and elevation are already accounted for.

The study is exploratory and associative. Regression coefficients and R² values describe relationships in the analysed data; they do **not** establish that a pollutant directly causes surface warming or cooling.

## Analysed phenomena

### Urban heat island and land-surface temperature

The **Urban Heat Island (UHI)** describes the tendency of urban areas to be warmer than their rural surroundings. It can be observed in different parts of the urban climate system. A **surface UHI** is expressed through differences in land-surface temperature, while the **canopy-layer UHI** concerns near-surface air temperature. The two are physically related but are not interchangeable and may peak at different times of day.

Satellite thermal infrared observations are particularly useful for mapping the surface expression of urban heat. They show how strongly roofs, roads, bare soil, vegetation and other surfaces heat and cool. Air temperature, by contrast, describes the state of the lower atmosphere and is generally smoother in space.

### Nitrogen dioxide

**NO₂** is a short-lived reactive trace gas associated with combustion sources such as road traffic, industry and residential heating. Its spatial distribution is controlled not only by emissions but also by atmospheric mixing, wind, boundary-layer depth and chemistry. Stable conditions can allow pollutants to accumulate near the surface, whereas stronger daytime mixing can dilute them.

### Ozone

**O₃** behaves differently from a directly emitted pollutant. Tropospheric ozone is produced through photochemical reactions involving nitrogen oxides and volatile organic compounds in the presence of sunlight. As a result, NO₂ and O₃ can show contrasting diurnal behaviour. In urban environments, fresh nitric oxide emissions can also remove ozone locally through titration. Their statistical relationship therefore depends on time of day, season, transport and meteorological conditions.

### Vegetation and topography

**NDVI** is used as an indicator of vegetation greenness and abundance. Vegetated surfaces can modify surface temperature through shading, evapotranspiration and different radiative properties relative to built surfaces. **Elevation** is included as a topographic control because temperature patterns across the Madrid region may also reflect altitude rather than urbanisation alone.

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=3 center=[0,20] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### From Space
Earth observation allows heat, vegetation and atmospheric composition to be examined consistently across large areas. In this study, satellite observations are combined with Copernicus atmospheric and meteorological datasets to move from a regional view to the scale of Madrid.

### <!--{ zoom=6 center=[-3.7,40.4] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### Zooming into Spain
In late June 2026, western Europe experienced an exceptional heatwave. ESA's Sentinel-3 land-surface-temperature image showed some surfaces in central Spain reaching around 55°C and measured about 48°C over Madrid. Because rock, asphalt and other surfaces can store large amounts of heat, land-surface temperature can be substantially higher than air temperature.

### <!--{ zoom=11 center=[-3.7038,40.4168] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Tile","properties":{"id":"osm-borders","opacity":0.8},"source":{"type":"XYZ","url":"https://tile.openstreetmap.org/{z}/{x}/{y}.png"}}]' animationOptions='{"duration":500}' }-->
#### Focusing on Madrid
Madrid combines a dense built-up core, large transport corridors, major green spaces and a pronounced elevation gradient. This makes it possible to investigate whether the spatial footprint of heat overlaps with atmospheric-composition patterns and whether vegetation and topography help explain those contrasts.

## Methods

### Study design

Two contrasting months were selected: **January 2026** to represent winter conditions and **July 2026** to represent summer conditions. To capture diurnal differences, observations were separated into two local-time windows:

- **DAY:** 11:00–13:00 Europe/Madrid local time
- **NIGHT:** 22:00–24:00 Europe/Madrid local time

Within each date and time window, valid observations were summarised using the **median**. Cloud-contaminated or unavailable LST pixels were retained as missing values rather than filled artificially.

All layers were co-registered to a common **1 km grid in ETRS89 / UTM zone 30N (EPSG:25830)** and clipped to the Madrid study boundary. The common grid contained **2,279 analysis cells** inside the study mask. Resampling to 1 km provides spatial alignment between datasets; it does not increase the intrinsic spatial resolution of coarser atmospheric products.

### Data

| Variable | Source | Role in the analysis | Native / original scale | Harmonised representation |
|---|---|---|---|---|
| Land-surface temperature | Copernicus Sentinel-3 SLSTR | Response variable | ~1 km LST product | 1 km Madrid grid, day/night |
| Air temperature | ERA5 | Meteorological control | Coarse atmospheric reanalysis | Interpolated/aligned to 1 km grid |
| NO₂ | CAMS European air-quality fields for quantitative analysis | Pollution predictor | ~0.1° / ~10 km | Interpolated/aligned to 1 km grid |
| O₃ | CAMS European air-quality fields for quantitative analysis | Pollution predictor | ~0.1° / ~10 km | Interpolated/aligned to 1 km grid |
| NDVI | Copernicus Sentinel-2 | Vegetation indicator | High-resolution optical imagery | Monthly value aggregated/aligned to 1 km |
| Elevation | CNIG/IGN MDT25 | Topographic control | 25 m DEM | Aggregated/aligned to 1 km |

**Sentinel-3 LST.** The Copernicus Sentinel-3 Sea and Land Surface Temperature Radiometer (SLSTR) provides the operational `SL_2_LST` product at approximately 1 km resolution. LST represents the radiometric temperature of the land surface rather than 2 m air temperature. Quality filtering is essential because thermal infrared retrievals are affected by cloud; invalid/cloud-contaminated observations were excluded from the statistical analysis.

**Atmospheric composition.** The quantitative regression dataset uses **CAMS** gridded NO₂ and O₃ fields. CAMS European products are available at approximately 0.1° (~10 km), so the 1 km interpolation used here is for co-registration only. Neighbouring 1 km cells derived from the same coarse atmospheric field should not be interpreted as independent kilometre-scale pollution measurements.

**Sentinel-5P context.** Sentinel-5P/TROPOMI provides Level-2 products for NO₂ and ozone and is an important Earth-observation source for atmospheric-composition mapping. If the NO₂/O₃ animations shown in this narrative are based on TROPOMI, they should be presented as satellite observational context, while the regression results below should remain explicitly labelled as using the CAMS harmonised pollution fields. This distinction avoids mixing visualisation products and quantitative model inputs.

**ERA5 air temperature.** ERA5 is the ECMWF/Copernicus global atmospheric reanalysis, combining observations with a numerical weather-prediction model through data assimilation. Near-surface air temperature provides the meteorological background against which satellite LST is interpreted.

**NDVI.** NDVI was derived from Sentinel-2 imagery and used as a monthly vegetation indicator for January and July. Because the NDVI layer is monthly rather than day/night specific, it was not interpreted as a separate diurnal variable.

**Elevation.** Elevation was obtained from Spain's CNIG/IGN MDT25 digital terrain model, which has a native grid spacing of 25 m and is referenced to ETRS89/UTM in mainland Spain. Elevation was aggregated to the common 1 km analysis grid.

<div style="display: flex; gap: 10px; flex-wrap: wrap;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/f5846d22d1d8e72d52c5e1c12bda88eaf61fb31e/assets/vittorez/January2026DAYERA5points-1789664866675.png" style="width: 48%;"/>
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/ddc783ae88471643856a243fb22fb58fad9e77bd/assets/vittorez/January2026NIGHTERA5points-1789664698044.png" style="width: 48%;"/>
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/5ee7ca898d90bca05ae3b1bfd58ec020467d8747/assets/vittorez/July2026DAYERA5points-1789664734518.png" style="width: 48%;"/>
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/d166097551ceb3144b21b1136853b44a2ef3e9c5/assets/vittorez/July2026NIGHTERA5points-1789664798000.png" style="width: 48%;"/>
</div>

#### NDVI
<div style="display: flex; gap: 0px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/2d1c2767f70007ad2d25be452ce624631721eb74/assets/vittorez/ndvijanuary-1789657144484.png" style="width: 100%; object-fit: contain; aspect-ratio: 1/1;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/cfbf6ab1b282b802591491bf645fa2afcd336a25/assets/vittorez/ndvijuly-1789656529381.png" style="width: 130%; object-fit: contain; aspect-ratio: 1/1;" />
</div>

#### Elevation
![DEM.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/d2fd45aac11c10b636ef956b5767d87df4ec0934/assets/vittorez/DEM-1789656842797.png)

### Methodology workflow

The workflow was designed to keep the physical meaning of each variable while placing all datasets on a common analytical framework.

**1. Spatial harmonisation.** All layers were clipped to the Madrid study boundary, projected to EPSG:25830 and aligned to the same 1 km grid. Sentinel-3 LST was already close to the target analysis scale. Finer-resolution NDVI and elevation data were aggregated, whereas coarser ERA5 and CAMS fields were interpolated for alignment only.

**2. Temporal harmonisation.** Dynamic variables were organised by date and separated into DAY and NIGHT windows. Daily medians were calculated within the selected time windows. January and July were analysed separately to avoid mixing contrasting seasonal regimes.

**3. Exploratory mapping and correlation.** Monthly and daily maps were used to inspect heat, pollutant and air-temperature patterns. Pearson correlations and simple regressions were used to quantify bivariate spatial relationships. The magnitude of `r` and `R²` was emphasised over p-values because the large number of grid cells and spatial autocorrelation can make very small effects appear statistically significant.

**4. Vegetation and elevation analysis.** NDVI and elevation do not vary between day and night in the same way as atmospheric variables. For these predictors, a representative monthly LST was calculated for each grid cell as the equal-weight mean of the monthly daytime and monthly nighttime LST summaries:

`Representative monthly LST = (mean daytime LST + mean nighttime LST) / 2`

This uses all available daytime observations and all available nighttime observations without requiring day and night retrievals to occur on the same date. It should be interpreted as a representative combination of the selected day/night windows, **not** as a true 24-hour daily mean.

**5. Multiple regression.** To evaluate the added information associated with pollution, two nested models were compared for each month and time period:

`Baseline: LST ~ Tair + NDVI + Elevation`

`Full: LST ~ Tair + NDVI + Elevation + NO₂ + O₃`

For this step, LST, air temperature, NO₂ and O₃ were first matched on the **same cell and the same valid dates** before monthly spatial medians were calculated. This prevents a predictor from being summarised over dates when LST was missing. Heteroskedasticity-consistent **HC3 robust standard errors** were used. Standardised coefficients were computed to compare relative effect sizes across predictors, and variance-inflation factors (VIF) were inspected for multicollinearity.

The key multiple-regression quantity is:

`ΔR² = R²(full model) − R²(baseline model)`

It measures how much additional spatial LST variance is associated with adding NO₂ and O₃ after air temperature, NDVI and elevation are already included.

## Results

### Land Surface Temperature: Madrid changes character between winter and summer

The Sentinel-3 maps show the expected seasonal contrast: July surfaces are substantially warmer than January surfaces, and daytime LST is higher and more spatially heterogeneous than nighttime LST. The night maps are particularly useful because they show where stored daytime heat persists after sunset, when urban materials continue releasing energy to the atmosphere.

<div style="display: flex; gap: 0px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/42843771e87e66c404bde5357140eed52e75edf1/assets/vittorez/January2026DAYLST-1789678227552.png" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c07c14130a7d689f23ec2735d89249a0d18ef49b/assets/vittorez/January2026NIGHTLST-1789678253754.png" />
</div>

<div style="display: flex; gap: 0px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/773bab750cd18172c33674ea83c4367ecff7aea8/assets/vittorez/July2026DAYLST-1789678287867.png" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c0fa57c306d500e1297f023f705224734828c03d/assets/vittorez/July2026NIGHTLST-1789678318314.png" />
</div>

### Nitrogen dioxide: an urban signal shaped by emissions and mixing

NO₂ patterns change between season and time of day because emissions, atmospheric mixing and chemistry all vary. The animations help reveal that pollution does not simply follow the temperature field. A high-LST surface and a high-NO₂ atmosphere can coincide because both are linked to dense urban areas, but their relationship can also weaken or reverse when boundary-layer mixing and photochemistry change.

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e75cffa4e129c6611205f50637e88eeda8aab387/assets/vittorez/January2026NO2DAYESRI-1789655589787.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/516f4965e19cbc50cb353c5b548e59aa7a344e21/assets/vittorez/January2026NO2NIGHTESRI-1789655678870.gif" style="width: 48%;" />
</div>

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e8d59e29b342c013cbe967e990b9c538246f36b4/assets/vittorez/July2026NO2DAYESRI-1789655733388.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e9f4dacbb2e9ac5069bfe3b75f535e04825b9f6c/assets/vittorez/July2026NO2NIGHTESRI-1789656066047.gif" style="width: 48%;" />
</div>

<p align="center"><em>Seasonal and diurnal shifts in NO₂ over Madrid.</em></p>

### Ozone: a contrasting photochemical pattern

O₃ adds a complementary view of Madrid's atmospheric chemistry. Unlike NO₂, ozone is not emitted directly by traffic. Its distribution reflects photochemical production, transport and chemical loss. The relationship between NO₂ and O₃ therefore changes with sunlight, emissions and atmospheric stability, which is one reason the pollutant–temperature relationship cannot be reduced to a single correlation coefficient.

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/788bce10551db1393e418ee9e227e55207834387/assets/vittorez/January2026O3DAYESRI-1789674050098.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/4baf52f1123b4d21e0fd80f379cf8c9eb19b2c44/assets/vittorez/January2026O3NIGHTESRI-1789674110930.gif" style="width: 48%;" />
</div>

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/92083e76bf511d013515694d41d894666c32f74f/assets/vittorez/July2026O3DAYESRI-1789674453031.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/25ad7c43057f88d27f331bbf235b63431b6b2959/assets/vittorez/July2026O3NIGHTESRI-1789674407166.gif" style="width: 48%;" />
</div>

<p align="center"><em>Seasonal and diurnal shifts in O₃ over Madrid.</em></p>

### Air temperature: the atmospheric background to surface heating

ERA5 air temperature provides the atmospheric context for interpreting Sentinel-3 LST. Although air and surface temperatures are related, they are not equivalent: surface temperature responds directly to solar radiation, material properties, moisture and shading, while near-surface air temperature is mixed through the lower atmosphere.

![January_2026_DAY_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/42b773597b70145ea3940828d26e4f286935757d/assets/vittorez/January2026DAYtemperaturetimeseries-1789665925063.png)

![January_2026_NIGHT_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/0ed1e6201a90d8dd0fd50eba66fbb287b5b9a0eb/assets/vittorez/January2026NIGHTtemperaturetimeseries-1789665960480.png)

![July_2026_DAY_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/fb8a6d73f45ae30a58240f68fdedf0f85c44c677/assets/vittorez/July2026DAYtemperaturetimeseries-1789665978602.png)

![July_2026_NIGHT_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/2160595e7ef4c116aa6725291f1c3e77f51fe2ca/assets/vittorez/July2026NIGHTtemperaturetimeseries-1789666002145.png)

### Air temperature, NO₂ and O₃ correlation

The correlation plots illustrate why season and time of day must be treated separately. The three atmospheric variables do not move in lockstep: atmospheric stability, mixing, emissions and photochemistry alter their relationships. In particular, NO₂ and O₃ can contain overlapping or opposing spatial information, so their individual simple-regression slopes should not be interpreted as independent physical effects.

![January_2026_DAY_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/b92dcccfedc5f5bd8294c312db9346590d8afb8e/assets/vittorez/January2026DAYtemperatureNO2O3-1789665595806.png)

![January_2026_NIGHT_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/5f4a3180dda80702316cd740d213ee7a5612a19b/assets/vittorez/January2026NIGHTtemperatureNO2O3-1789665623159.png)

![July_2026_DAY_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c62611a1d7f80f0483996e0a6888a2a06ee7be77/assets/vittorez/July2026DAYtemperatureNO2O3-1789665645694.png)

![July_2026_NIGHT_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/a364361583f954148f83f25bd6d0e2e19f31f984/assets/vittorez/July2026NIGHTtemperatureNO2O3-1789665686005.png)

### Simple spatial relationships with LST

The simple regressions reveal strong seasonal and diurnal contrasts. Air temperature is the strongest single atmospheric predictor in January daytime (`R² ≈ 0.17`) and January nighttime (`R² ≈ 0.19`). In July daytime, however, the spatial air-temperature field alone explains only about `5%` of LST variability, while at night the relationship becomes much stronger (`R² ≈ 0.32`).

For pollution variables, simple relationships are generally weaker during the day. July-nighttime patterns are more pronounced: NO₂ alone explains about `17%` of the spatial LST variability and O₃ about `18%`. These values are **not additive**, because the predictors share spatial information and are influenced by common meteorological and urban factors.

### Vegetation and elevation: summer surface structure matters

To avoid treating monthly NDVI and static elevation as if they had distinct day/night values, both were compared with representative monthly LST.

In **January**, NDVI is negatively correlated with LST (`r = -0.271`, `R² = 0.073`). A 0.1 increase in NDVI corresponds to approximately **0.29°C lower representative LST** in the fitted relationship. In **July**, the relationship strengthens markedly (`r = -0.481`, `R² = 0.231`), corresponding to approximately **0.91°C lower LST per 0.1 increase in NDVI**. The result points to a much stronger vegetation–surface-temperature relationship during summer.

Elevation also shows a negative bivariate relationship with representative LST. The fitted gradient is approximately **-0.42°C per 100 m in January** (`R² = 0.050`) and **-0.61°C per 100 m in July** (`R² = 0.123`). Thus, both vegetation and topography are more strongly associated with the spatial temperature pattern in July than in January.

### Multiple regression: when does pollution add information beyond meteorology and surface controls?

The multiple regression compares a baseline model containing air temperature, NDVI and elevation with a full model that also includes NO₂ and O₃. Dynamic variables were matched by date before spatial aggregation, so the model compares like with like.

| Period | Baseline R² | Full R² | Additional R² from NO₂ + O₃ |
|---|---:|---:|---:|
| January DAY | 0.275 | 0.299 | **+0.024** |
| January NIGHT | 0.307 | 0.320 | **+0.013** |
| July DAY | 0.291 | 0.305 | **+0.014** |
| July NIGHT | 0.361 | 0.455 | **+0.094** |

For three of the four cases, adding pollution increases explained spatial LST variance by only about **1–2 percentage points**. The clearest exception is **July nighttime**, when the full model increases R² from **0.361 to 0.455**. In other words, NO₂ and O₃ together add about **9.4 percentage points** of explained spatial LST variance after air temperature, NDVI and elevation are already included.

The standardised coefficients help identify which variables carry the strongest independent association within each full model. In **July daytime**, NDVI is dominant (`β* ≈ -0.51`), while air temperature has a much smaller standardised coefficient (`β* ≈ +0.13`). In **July nighttime**, air temperature becomes the strongest predictor (`β* ≈ +0.52`), followed by NO₂ (`β* ≈ +0.27`) and elevation (`β* ≈ +0.26`), while O₃ is negatively associated with LST (`β* ≈ -0.16`).

This day–night contrast is one of the central results of the study: **summer daytime LST is most strongly structured by vegetation, whereas summer nighttime LST contains a stronger atmospheric and pollution-related signal.**

## Discussion

### Madrid's heat story is also a time-of-day story

External studies already show why Madrid deserves close attention. Arup's 2022 urban-heat comparison identified Madrid as the most extreme hot spot among the six cities examined and noted substantial evening heat exposure. ESA's June 2026 Sentinel-3 observation independently illustrates the intensity of the surface heat environment immediately before our July study period. Our results do not reproduce either study directly, but they place the January–July analysis in a broader context of documented heat vulnerability.

The July results reinforce the importance of vegetation. The much stronger negative NDVI–LST relationship in summer is consistent with the idea that green surfaces can moderate daytime surface heating through shading and evapotranspiration. The analysis does not isolate individual parks or interventions, but the spatial pattern is compatible with the broader observation that vegetated urban areas tend to be cooler than densely built surfaces.

### Why does the pollution signal become clearer at night in July?

At night, solar forcing disappears and differences in stored heat release, atmospheric stability and urban ventilation become more important. A shallower nocturnal boundary layer can reduce pollutant dispersion, while heat stored in buildings and paved surfaces continues to be released. These processes can make heat and pollution patterns more spatially aligned even if pollution itself is not the cause of the heat.

The July-night multiple regression is therefore best interpreted as evidence of **shared spatial structure**: after controlling for air temperature, vegetation and elevation, NO₂ and O₃ still contain information associated with where LST remains high at night. The analysis cannot determine whether this arises from emissions, urban density, atmospheric stability, land cover not explicitly included in the model, or other covarying processes.

### NO₂ and O₃ should be interpreted together, not as isolated causal effects

NO₂ and O₃ are chemically and meteorologically linked. In January nighttime, their VIF values are around 6, indicating notable collinearity and making the individual coefficients less stable. The combined added value of the pollution block is therefore more robust for the narrative than treating each pollutant coefficient as a separate causal effect.

### Limitations

This is an exploratory two-month case study, not a climatology. January and July capture contrasting seasonal conditions but cannot represent interannual variability, heatwave-to-heatwave variability or the full annual cycle. A stronger follow-up study should analyse several years and multiple heat events.

The input datasets also operate at different physical scales. Sentinel-3 LST is close to the 1 km analysis grid, whereas ERA5 and especially CAMS atmospheric fields are much coarser. Interpolating them to 1 km improves co-registration but does not create independent 1 km atmospheric observations. This spatial smoothing, together with spatial autocorrelation among neighbouring grid cells, means that formal significance levels may overstate the effective amount of independent information.

Cloud cover creates another limitation because thermal-infrared LST is unavailable beneath clouds. The number of valid LST dates therefore varies by grid cell and by period. July nighttime, for example, has fewer valid observations per cell than July daytime. Finally, the study is observational: regression and correlation identify associations, not causal mechanisms.

## Conclusions

Madrid's heat–air-quality relationship is strongly dependent on **season and time of day**. The clearest summer daytime signal is vegetation: NDVI explains about **23%** of the spatial variability in representative July LST in the simple regression, and it remains the strongest standardised predictor in the July daytime multiple model.

At night, the balance changes. Air temperature becomes more important, and in **July nighttime** the addition of NO₂ and O₃ increases the explained spatial LST variance from **36.1% to 45.5%**, an increase of **9.4 percentage points**. This does not demonstrate that pollution causes higher LST; rather, it shows that summer nocturnal pollution fields contain meaningful spatial information about the areas where heat persists after controlling for major meteorological, vegetation and topographic factors.

The combined Earth-observation perspective is therefore more informative than any single layer. Sentinel-3 shows where surfaces are hot, ERA5 describes the atmospheric thermal background, atmospheric-composition products show how pollutants are distributed, Sentinel-2 reveals vegetation patterns, and the DEM separates part of the topographic signal. Together, they provide a framework for identifying locations where heat and poor air-quality conditions may overlap and for motivating more detailed urban-scale studies.

## Open Science

This workflow is built around openly accessible Earth-observation and Copernicus data and can be reproduced for other cities. The analysis can be extended by publishing the preprocessing and statistical scripts together with the harmonised grid definition, quality-control rules and metadata describing each derived product.

For future work, the workflow could be strengthened by adding more years, additional summer heat events, higher-resolution urban-form information, in-situ air-quality stations and meteorological observations, and spatial statistical models that explicitly account for autocorrelation. Comparing satellite/reanalysis results with neighbourhood-scale measurements would also help determine how much of the apparent 1 km variability is physically resolved rather than inherited from coarse atmospheric products.

## References

1. Weng, Q., Yang, S. *Urban Air Pollution Patterns, Land Use, and Thermal Landscape: An Examination of the Linkage Using GIS.* Environmental Monitoring and Assessment 117, 463–489 (2006). https://doi.org/10.1007/s10661-006-0888-9
2. Fuladlu, K., Altan, H. *Examining land surface temperature and relations with the major air pollutants: A remote sensing research in case of Tehran.* Urban Climate 39, 100958 (2021). https://doi.org/10.1016/j.uclim.2021.100958
3. Goldberg, D. L. et al. *TROPOMI NO₂ in the United States: A detailed look at the annual averages, weekly cycles, effects of temperature, and correlation with surface NO₂ concentrations.* Earth's Future 9, e2020EF001665 (2021). https://doi.org/10.1029/2020EF001665
4. Guo, Y. et al. *Modeling urban air temperature using satellite-derived surface temperature, meteorological data, and local climate zone pattern—a case study in Szeged, Hungary.* Theoretical and Applied Climatology 155, 3841–3859 (2024). https://doi.org/10.1007/s00704-024-04852-7
5. Shen, P., Wang, M., Ma, H. et al. *On the two-way interactions of urban thermal environment and air pollution: A review of synergies for identifying climate-resilient mitigation strategies.* Building Simulation 18, 259–279 (2025). https://doi.org/10.1007/s12273-024-1210-x
6. European Space Agency. *Europe feels the heat beneath our feet.* 25 June 2026. https://www.esa.int/ESA_Multimedia/Images/2026/06/Europe_feels_the_heat_beneath_our_feet
7. Arup. *Madrid suffers most extreme urban heat island “hot spot” – new international survey shows.* Updated 16 August 2023. https://www.arup.com/news/madrid-suffers-most-extreme-urban-heat-island-hot-spot--new-international-survey-shows/
8. Copernicus Sentinel-3 SLSTR Land User Handbook. *Land Surface Temperature product (SL_2_LST).* https://sentinels.copernicus.eu/documents/247904/4598082/Sentinel-3-SLSTR-Land-Handbook.pdf
9. Copernicus Atmosphere Monitoring Service. *CAMS European air quality forecasts / analyses.* https://www.copernicus.eu/en/access-data/copernicus-services-catalogue/cams-european-air-quality-forecasts
10. Copernicus Climate Change Service / ECMWF. *ERA5 hourly data on single levels from 1940 to present.* https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels
11. European Space Agency. *Sentinel-5P data products.* https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-5P/Data_products
12. Centro Nacional de Información Geográfica / Instituto Geográfico Nacional. *MDT25 – 1ª cobertura.* https://centrodedescargas.cnig.es/CentroDescargas/modelo-digital-terreno-mdt25-primera-cobertura

## Contributors

**Authors:** Gianluca Flaminio, Nikolina Zallemi, Vittoria Rezzuto and Thomas Xolias  
**Institutions:** Politecnico di Milano and Aristotle University of Thessaloniki  
**Context:** ESA ESRIN Science Hub Challenge, September 2026


