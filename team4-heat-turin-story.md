---
cover-image: https://placehold.co/1200x630/png?text=Heat+Risk+Mapping+Turin
date: 2026-09-18
theme: urban-heat
tags: heat,urban,vulnerability,turin,sentinel-3,sentinel-2,copernicus
official: false
---

# Cooling Turin: Mapping Who Faces the Heat <!--{ as="img" mode="hero" src="https://placehold.co/1200x630/png?text=Heat+Risk+Mapping+Turin" }-->


*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in **2026**. It was developed by a team from the **Polytechnic University of Turin, Polytechnic University of Milan, and Aristotle University of Thessaloniki**.*

## <!--{ nav="false"}-->
<p align="center">
<img src="https://placehold.co/250x80/png?text=PoliTO" alt="Politecnico di Torino" height="80" style="margin: 0 15px;"/>
<img src="https://placehold.co/250x80/png?text=PoliMI" alt="Politecnico di Milano" height="80" style="margin: 0 15px;"/>
<img src="https://placehold.co/250x80/png?text=AUTh" alt="Aristotle University of Thessaloniki" height="80" style="margin: 0 15px;"/>
</p>
<!-- PLACEHOLDER: upload your three university logos with the editor's image button and swap these src URLs. -->

## Challenge
In the summer of 2026, as an African anticyclone pushed temperatures across Italy past 40°C, Turin's eight districts did not all suffer equally. A resident of a leafy, low-density neighbourhood and a resident of a paved, high-density one lived through the same heatwave in very different bodies of air. **Challenge 2C — Mapping Urban Heat Exposure and Vulnerability** asked us to find out exactly where that difference is greatest, and why — by combining Earth Observation data with the geospatial and demographic information that shapes who actually feels a heatwave the hardest.

## Objective
This story asks a simple question with real consequences: can satellite Land Surface Temperature, combined with vegetation cover, built-up density and the age of the people living there, tell us which of Turin's 8 *Circoscrizioni* are most exposed to heat stress — and whether the hospitals, schools and elderly-care homes that would need to respond in a crisis are actually located where that exposure is highest?

## The Heatwave

Before mapping anything from orbit, we needed to know the heatwave was real and pin down exactly when it happened. [ThermalTrace](https://thermaltrace.climate.copernicus.eu/) (Copernicus C3S/ECMWF) gave us daily min/max air temperature and UTCI feels-like temperature for Turin at the nearest ERA5 grid cell, for the whole of August 2026.

![ERA5/UTCI daily temperature time series for Turin, August 2026](thermaltrace_era5_utci_aug2026.png)
<!-- PLACEHOLDER: upload thermaltrace_era5_utci_aug2026.png via the editor's image button and swap this path in. -->

Reading it: daily max feels-like temperature stayed in the 33–40°C range from August 1st all the way through August 20th, peaking near 40°C around August 13th, before a sharp cool-down (dropping to roughly 25°C) starting August 20th–21st and only a partial recovery toward month's end. The **August 1–15 window** used throughout this analysis sits entirely inside that sustained hot stretch — not in the cooler tail after the 20th. We treated this purely as *event selection* context, not as an input to the index itself: no air-temperature or anomaly value is used in the scoring below — the index is built entirely from Sentinel-3 surface temperature plus the geospatial vulnerability layers.

Independent corroboration: on August 4th, 2026 — inside our analysis window — Italy's Ministry of Health issued its highest heat-health warning level ("bollino rosso") for 25 of 27 monitored cities, including Turin at roughly 38°C that day, as the same African-anticyclone heatwave gripped the country. That lines up with the ThermalTrace curve above and confirms this wasn't a model artifact — it was an officially recognised public-health emergency.

## Earth observations <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":true},{"type":"Tile","properties":{"id":"OSM;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"},"visible":false}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="10.5" center=[7.6869,45.0703] projection="" animationOptions={duration:500}}-->
#### Turin's core under the August 2026 heatwave
Sentinel-3 traced the city's heat *at night* — the SLSTR overpasses used here fall in the evening (~21:00–22:00 UTC, or shortly after sunset local time), so this is a map of which districts fail to cool down overnight, arguably the more dangerous signal for public health than a daytime hot spot. Sentinel-2 explains why that overnight heat isn't uniform: the central district Centro-Crocetta (C.1) has the lowest vegetation index (NDVI 0.23) and the most built-up surface signature (NDBI 0.10) of any district, while Aurora-Vanchiglia (C.7), which hugs the Po river parkland, has the highest NDVI at 0.57 — nearly triple.

![Sentinel-3 nighttime LST, smoothed contours, Aug 1–15 2026](01_lst_smoothed_map.png)
<!-- PLACEHOLDER: upload 01_lst_smoothed_map.png -->

![Sentinel-2 NDVI (vegetation) and NDBI (built-up) composite, Turin, Aug 1–15 2026](00_sentinel2_ndvi_ndbi_map.png)
<!-- PLACEHOLDER: upload 00_sentinel2_ndvi_ndbi_map.png -->

<!-- Recommended default for your first submission — delete the eox-map tour block above (including the ### layers line) if you don't want the live basemap, and just keep this section as plain headings + the two images above. -->

## Data and Methods
#### Dataset
- **Source**: Sentinel-3 SLSTR Level-2 LST (Copernicus/ESA); Sentinel-2 MSI L2A via Google Earth Engine; Copernicus Imperviousness HRL 2024; Comune di Torino open geodata (district boundaries, green areas, population by age); OpenStreetMap (hospitals, schools, elderly-care facilities); ThermalTrace ERA5/UTCI (Copernicus C3S/ECMWF)
- **Temporal coverage**: 1–15 August 2026, the heatwave window identified above and corroborated by Italy's Ministry of Health "bollino rosso" alert of 4 August 2026

#### Methodology workflow
We built a **Heat Exposure Index**: daily Sentinel-3 LST (clipped 15–42°C) combined with three static vulnerability layers — the percentage of residents aged 65+, the lack of green cover, and soil imperviousness — each contributing an equal 25% weight, normalized and averaged per district. Sentinel-2 NDVI and NDBI added a complementary, descriptive view of vegetation health and built-up intensity across the same window. Finally, we cross-referenced the resulting district rankings against the real locations of hospitals, schools and elderly-care homes pulled from OpenStreetMap, to see whether protection lines up with risk.

The three static input layers, at district level:

![Urban green areas, Turin](03_green_areas_map.png)
<!-- PLACEHOLDER: upload 03_green_areas_map.png -->

![Imperviousness (soil sealing %) 2024, Turin](04_imperviousness_map.png)
<!-- PLACEHOLDER: upload 04_imperviousness_map.png -->

![Age distribution / % population over 65 per district, Turin](05_age_distribution_dashboard.png)
<!-- PLACEHOLDER: upload 05_age_distribution_dashboard.png (or use 05b_pct_over65_map.png for the simpler district-level map version) -->

## Results

&emsp;Averaged across the five sampled dates, **Centro-Crocetta (C.1) ranks highest** in the city at a Total Risk of **64.5%**, with San Paolo-Pozzo Strada (C.3) close behind at **63.3%** — the two central districts sit well clear of the rest of the field, which trails off from Borgo Vittoria-Lucento (C.5, 55.2%) down to Aurora-Vanchiglia (C.7, 38.8%), the city's least exposed district. Interestingly, on the single hottest day by index score — August 4th — the order flips: C.3 briefly overtakes C.1, 71.1% to 69.0%, because C.3's heat component spikes harder on that day than any other district in the dataset.

![Heat Vulnerability Ranking — average, Aug 1–15 2026 (5 sampled dates)](09_ranking_table_average.png)
<!-- PLACEHOLDER: upload 09_ranking_table_average.png -->

![Heat Vulnerability Ranking — 2026-08-04, city-wide peak sampled day](09_ranking_table_peak_day.png)
<!-- PLACEHOLDER: upload 09_ranking_table_peak_day.png -->

&emsp;The two leading districts get there in different ways. C.1's score is driven almost entirely by having the city's least green space (23.6 of 25 possible points) and an above-average elderly population (22.7/25) — surface heat is actually its *smallest* contributor (8.7/25 on average), meaning C.1's vulnerability is structural, not weather-dependent. C.3, by contrast, carries the city's highest imperviousness score (12.3/25) and is the most heat-reactive district in the whole dataset: its heat component more than doubles on the hottest day (from 5.9% average to 13.6% on Aug 4), the single largest heat value recorded anywhere in the study.

![4-Factor Heat Exposure Index by district, 5 sampled dates](06_heat_exposure_index_map.png)
<!-- PLACEHOLDER: upload 06_heat_exposure_index_map.png -->

![Daily Risk Breakdown by component (age, heat, greenery, imperviousness)](07_daily_vulnerability_ranking.png)
<!-- PLACEHOLDER: upload 07_daily_vulnerability_ranking.png -->

&emsp;The critical-facilities overlay surfaced the clearest actionable gap in the whole study: **Centro-Crocetta — the city's highest average-risk district — has zero elderly-care facilities**, only 3 hospitals, and just 26 schools, fewer than six of the other seven districts. Compare that to Santa Rita-Mirafiori (C.2), a lower-risk district (5th, 53.2%) that nonetheless hosts 6 elderly-care homes, the most of any district, and has the city's highest share of over-65 residents (28.6%). The pattern isn't reversed everywhere — Aurora-Vanchiglia (C.7), the lowest-risk district, still has 6 hospitals — but the one district that combines the highest chronic heat-risk score with essentially no dedicated elderly-care infrastructure is exactly the one a city would want to flag first.

![Critical facilities (hospitals, schools, elderly care) over the static vulnerability map](09_critical_facilities_map.png)
<!-- PLACEHOLDER: upload 09_critical_facilities_map.png -->

&emsp;The ranking held up reasonably well across the sampling window, but not perfectly: on **August 10th and 13th**, several districts (notably C.2, C.3 and C.8) show heat scores of 0.0–0.02, near-zero values that don't reflect genuinely mild conditions but cloud-obscured pixels imputed with the city-wide average, per our bitwise cloud-flag QA. Those two dates should be read as lower-confidence snapshots; the pattern that holds across the clearer days — C.1 and C.3 consistently trading the top two spots — is the one we'd trust for planning.

![Bitwise cloud-cover QA, Turin, Aug 1–15 2026](02_cloud_cover_qa.png)
<!-- PLACEHOLDER: upload 02_cloud_cover_qa.png -->

## Conclusions

Turin's heat risk is not evenly spread across its eight districts, and it splits into two distinct problems rather than one. Centro-Crocetta carries a *chronic* risk rooted in its near-total lack of green space and older population — a problem city planners can address with targeted tree planting, pocket parks, or reflective surfacing, independent of any particular heatwave. San Paolo-Pozzo Strada carries an *acute* risk: it is the district that swings hardest and hottest when a heatwave actually peaks, making it the priority target for emergency cooling-center activation and public-health outreach in the 48 hours after a "bollino rosso" alert like the one issued on August 4th. Most urgently, the fact that Centro-Crocetta — the single highest-risk district on average — has no elderly-care facility at all is a concrete, fixable gap: either new elderly services belong there, or existing outreach programs in neighbouring districts need an explicit plan for reaching C.1's older residents during the next heatwave. A single well-targeted intervention informed by this index likely does more for public safety than the same resources spread evenly across all eight districts.

## <!--{ as="div" }--> Open Science
| **Name** | **Type** | **Agency / Provider** | **Description / Usage** |
| --- | --- | --- | --- |
| **[Sentinel-3 SLSTR L2 LST](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-slstr/product-types/level-2-lst)** | Dataset | Copernicus / ESA | Daily (nighttime-pass) Land Surface Temperature, 1–15 Aug 2026 — the core heat-hazard layer of the index |
| **Sentinel-2 MSI L2A (`COPERNICUS/S2_SR_HARMONIZED`)** | Dataset | Copernicus, via [Google Earth Engine](https://earthengine.google.com/) | Cloud-masked median composite used for NDVI/NDBI |
| **[Imperviousness HRL 2024](https://land.copernicus.eu/en/products/high-resolution-layer-imperviousness)** | Dataset | Copernicus Land Monitoring Service | Soil sealing %, one of the 4 index components |
| **[ThermalTrace](https://thermaltrace.climate.copernicus.eu/)** | Dataset / Tool | Copernicus C3S / ECMWF | ERA5 / UTCI daily temperature, used to select and corroborate the heatwave window |
| **[Geoportale Piemonte](https://www.geoportale.piemonte.it/geonetwork/srv/api/records/c_l219:f71649ef-0855-4f16-abc6-9c6c0a4e4658)** | Dataset | Città di Torino open geodata (CC BY 4.0) | District boundaries, urban green areas, population by age and district |
| **OpenStreetMap** | Dataset | OSM contributors, via Overpass API / [osmnx](https://osmnx.readthedocs.io/) | Hospitals, schools, elderly-care facility locations |
| **[EO Dashboard](https://eodashboard.org/explore/?x=7.6869&y=45.0703&z=10.0000&datetime=2026-08-13&template=expert)** | Platform / Web Tool | EO Dashboard Consortium (ESA, NASA, JAXA) | Base layers and visualization tools for interactive exploration |

#### Notebook
Access the notebook to reproduce the study workflow.
<iframe width="100%" height="600" src="PASTE_LINK_TO_YOUR_HOSTED_NOTEBOOK_HERE" frameborder="0"></iframe>
<!-- PLACEHOLDER: host Team4_Challenge2C_HeatVulnerability_Turin.ipynb somewhere reachable (e.g. GitHub raw link) and paste that URL above. -->

#### References
- Beretta, S. ["Meteo oggi 4 agosto: bollino rosso in 25 città su 27, punte di 41°C"](https://www.quotidianomotori.com/automobili/previsioni-meteo-4-agosto-2026-italia/), *Quotidiano Motori*, 4 Aug 2026 — nationwide red-alert heatwave, corroborating the analysis window
- ThermalTrace, [Copernicus Climate Change Service (C3S) / ECMWF](https://thermaltrace.climate.copernicus.eu/) — daily air and UTCI feels-like temperature used for heatwave-period selection
- Comune di Torino, population by age and district ("B1 Pop per età annuale e circoscrizione 2025"), open data portal
- [Geoportale Piemonte catalog record](https://www.geoportale.piemonte.it/geonetwork/srv/api/records/c_l219:f71649ef-0855-4f16-abc6-9c6c0a4e4658), Città di Torino open geodata, licensed CC BY 4.0
- OpenStreetMap contributors, queried via [Overpass API](https://overpass-api.de/) and [osmnx](https://osmnx.readthedocs.io/)

## Contributors  - optional
Francesco Mezza — Coding & data processing
Sona Guliyeva — Project lead
Sophia Dolla — **[FILL IN — role]**
Filippos Kostikiadis — **[FILL IN — role]**
