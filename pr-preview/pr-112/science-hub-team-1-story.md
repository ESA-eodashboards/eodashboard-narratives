---
cover-image: https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2023/10/earthcare_for_a_better_understanding_of_earth_s_radiation_balance/25154725-1-eng-GB/EarthCARE_for_a_better_understanding_of_Earth_s_radiation_balance_pillars.png
date: 2025-01-01
theme: theme_name
tags: some,tags

---

# The power of EarthCare, the new ESA Earth Explorer: From Aerosols to Clouds <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2023/10/earthcare_for_a_better_understanding_of_earth_s_radiation_balance/25154725-1-eng-GB/EarthCARE_for_a_better_understanding_of_Earth_s_radiation_balance_pillars.png" }-->
### Authors: Giacomo, Paula and Fillipo (University of Leeds) <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

# 
*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2025. It was developed by a team from University of Leeds.*

## Challenge
Clouds play a critical role in Earth’s radiation balance and hydrological cycle, and their properties are strongly influenced by atmospheric aerosols. Understanding how aerosols interact with clouds—both macro- and microphysically—is key for improving climate models and predicting weather patterns. Aerosols such as cloud condensation nuclei (CCN) and ice nucleating particles (INP) can affect the formation, structure, and lifetime of clouds by altering the size and phase (liquid or ice) of cloud particles.

<img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2024/05/clouds_in_the_climate_system/26088977-1-eng-GB/Clouds_in_the_climate_system_article.png" width="600"/> <p style="text-align:center;"><b>Figure 1.</b> Clouds in the climate system.</p>

Thanks to ESA’s EarthCare mission, combining lidar and radar instruments, we can now observe cloud vertical structure in great detail. This allows scientists to assess how cloud properties change with altitude and across different climate zones (e.g., tropics, subtropics, polar regions) and surface types (land vs. ocean), especially in relation to known aerosol distributions.

Yet, linking cloud microphysical properties directly to aerosol presence remains a complex task, requiring multi-instrument observations and detailed analysis across many atmospheric layers.

<div style="text-align: center;"> <img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2024/01/earthcare_over_desert_dust/25391626-1-eng-GB/EarthCARE_over_desert_dust_pillars.png" width="500"/> <p><b>Figure 2.</b> EarthCare Satellite (source: ESA).</p> </div>

## Objective

The objective of this study is to explore whether and how aerosols influence cloud characteristics—specifically the distribution of liquid water and ice content—at various altitudes using EarthCare’s vertical profiling capabilities. T his involves identifying patterns in cloud-aerosol interactions across different regions and conditions (e.g. land vs. ocean, tropical vs. polar environments), and determining whether increased CCN or INP concentrations correlate with observable changes in cloud composition.

## Use cases
To capture the diversity of aerosol-cloud interactions, this study focuses on three climatically distinct oceanic regions:
<img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/Globe1_pacific.png?raw=true" width="600"/> <p style="text-align:center;"><b>Figure 3.</b> Location of use cases.</p>

**Tropics: East and West Pacific:**
The tropics are a key region for studying aerosol-cloud interactions due to their mix of natural and human-made aerosols, sensitive convective clouds, and strong links to global climate systems like El Niño. Warm sea surface temperatures not only influence cloud formation and precipitation but also contribute to ocean acidification, making the tropics critical for understanding both atmospheric and oceanic climate impacts.

**Souther ocean:** The polar regions are key for studying aerosol-cloud interactions due to their sensitivity to small atmospheric changes. Aerosols can affect the amount and thickness of low supercooled clouds, altering precipitation and radiative balance. These changes can accelerate ice sheet melt and trigger climate feedback loops, making the poles crucial for understanding long-term impacts on sea level and global climate.

## Earth Observation <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"N2_CO2_diff;:;xco2_16day_diff._2022-02-13;:;N2_CO2_diff;:;EPSG:3857","title":"N2_CO2_diff"},"source":{"type":"XYZ","url":"https://openveda.cloud/api/raster/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=s3://veda-data-store/co2-diff/xco2_16day_diff._2022-02-13.tif&resampling_method=nearest&bidx=1&colormap_name=rdbu_r&rescale=-1e-06,1e-06","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]}]' zoom="4.061424252974107" center=[-25.304569260712004,25.101129389095888] projection="" animationOptions={duration:500}}-->
#### How can EarthCare Helps us?
Five different types of forests were used as case studies to test and compare interpolation methods. Each site represents different forest types, climatic conditions, and seasonal patterns, providing a comprehensive assessment of method performance under real-world variability.

<div style="text-align: center;">
    <img src="
https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/team1-earthcare-sensors-image.png?raw=true" width="500"/>
    <p><b>Figure 3.</b> Use cases/forests locations.</p>
</div>

