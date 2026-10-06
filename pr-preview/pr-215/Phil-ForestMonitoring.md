---
cover-image: https://www.philchm.ph/wp-content/uploads/DSC_3796-1024x683.jpg
date: 2026-09-28
theme: Forest
tags: Forest Monitoring,Philippines,ALOS-2,Illegal Encroachment
official: true
collections: collectionIdentifier1, collectionIdentifier2
---

# Bantay Kagubatan: Seeing Settlements Before the Forest Falls <!--{ as="img" mode="hero" src="YOUR_PHILIPPINES_COVER_IMAGE_URL" style="width: 100%; height:800px;" }-->

### Authors: Romer Kristi D. Aranas<sup>1</sup>, Pocholo Miguel De Lara<sup>2</sup>, Elmar Sobrevega<sup>3</sup>, Mariel Juanillo<sup>1</sup>, Karina Amit<sup>4</sup><!--{ style="font-size:1.0rem;opacity:0.7;margin-top:1rem; color:Yellow" }-->

<div style="text-align:left; font-size:0.95rem; opacity:0.85; margin-top:1rem; color:Yellow;">

1. Philippine Space Agency (PhilSA)  
2. Department of Science and Technology – Advanced Science and Technology Institute (DOST-ASTI)  
3. Department of Environment and Natural Resources – Forest Management Bureau (DENR-FMB)  
4. University of the Philippines Diliman (UP Diliman)

</div>

#

This story is based on results from the **ALOS-2 Ideathon: Bridging Space Data and Societal Needs**, conducted in February 2025 and organized by the Japan Aerospace Exploration Agency (JAXA) together with project partners.  
<!-- TODO: Replace "project partners" with the confirmed organizing institutions. -->

<p align="center">
  <img src="YOUR_JAXA_LOGO_URL" height="50" style="margin: 0 5px;"/>
  <img src="YOUR_IDEATHON_PARTNER_LOGO_URL" height="50" style="margin: 0 5px;"/>
  <img src="YOUR_RESTEC_LOGO_URL" height="70" style="margin: 0 5px;"/>
</p>

The study, **Bantay Kagubatan: Seeing Settlements Before the Forest Falls**, was developed by participants from the following organizations:

<p align="center">
  <img src="YOUR_PHILSA_LOGO_URL" height="65" style="margin: 0 8px;"/>
  <img src="YOUR_DOST_ASTI_LOGO_URL" height="65" style="margin: 0 8px;"/>
  <img src="YOUR_DENR_FMB_LOGO_URL" height="65" style="margin: 0 8px;"/>
  <img src="YOUR_UP_DILIMAN_LOGO_URL" height="65" style="margin: 0 8px;"/>
</p>


## Challenge <!--{ style="font-size:2.00rem;opacity:1;margin-top:1rem; color:Navy" }-->

The Philippines faces substantial and continuing pressure on its forest resources. Over roughly a century, national forest cover has declined from about **70% to approximately 24%**, while an estimated **47,000 hectares of forest continue to be lost annually**. Around **6.8 million hectares of watershed areas** are considered to be at critical risk.

This loss affects far more than forest extent alone. Forested watersheds are essential for **water supply, irrigation, biodiversity conservation, disaster-risk reduction, and climate commitments**. Approximately **14.2 million hectares** are considered important for irrigation, while many cities and communities depend directly on forested watersheds for their water supply. Between 2001 and 2022, an estimated **1.42 million hectares of tree cover were lost**, representing roughly a **7.6% decline** and approximately **848 million tons of associated CO₂ emissions**.

One particularly difficult challenge is **illegal encroachment into forest and watershed areas**. In 2023, 26 new structures were reportedly detected across only three watersheds, while the Buyog Watershed experienced a decline in forest area from approximately 19 ha to 7 ha. An estimated **55% of critical watersheds remain unprotected**.

The key operational problem is that **structures can be established beneath an apparently intact forest canopy before large-scale clearing becomes visible**. Conventional monitoring frequently detects the disturbance only after substantial forest loss has already occurred.

The people and institutions affected include forest-dependent communities, downstream cities and farms relying on watershed services, local government units (LGUs), DENR-FMB enforcement teams, and national agencies responsible for environmental reporting and forest protection.

### Why Existing Monitoring Can Miss the Earliest Stage

Current forest monitoring still depends heavily on **field surveys and satellite observations of visible canopy disturbance**:

- **Field surveys** are expensive, time-consuming, and difficult to conduct repeatedly across remote and mountainous terrain.
- **Optical sensors**, including Landsat and Sentinel-2, can be affected by persistent cloud cover and primarily observe the upper canopy.
- **C-band SAR**, such as Sentinel-1, is especially useful for monitoring surface and canopy changes but has more limited interaction with deeper forest structure than longer-wavelength L-band SAR.
- By the time conventional observations clearly register forest clearing, an encroachment may already be established.

This creates a critical monitoring gap: **the period between the establishment of a structure beneath the canopy and the later appearance of visible forest clearing**.


#### Problem Statement <!--{ style="font-size:2.0rem;opacity:1;margin-top:1rem; color:Navy" }-->

Traditional monitoring is often **reactive rather than preventive**. Illegal structures may be discovered months or years after they first appear, when surrounding forest disturbance is already visible and enforcement becomes more difficult.

The central question of this project is therefore:

**Can ALOS-2 L-band SAR identify an anomalous backscatter signal associated with a sub-canopy settlement before forest clearing becomes visible to optical or C-band sensors?**

If such a signal can be demonstrated reliably, L-band observations could provide an **earlier warning window for targeted field verification and preventive enforcement**, rather than serving only as documentation after clearing has occurred.


## Objectives <!--{ style="font-size:1.5rem;opacity:1;margin-top:1rem; color:Navy" }-->

**Primary Objective:**  
Demonstrate whether **ALOS-2 L-band SAR can detect anomalous signals associated with documented settlements beneath forest canopy before forest clearing becomes visible in optical or C-band observations**, establishing the evidence base for a potential early-warning approach.

**Specific Objectives:**

1. Characterize the **ALOS-2 HH, HV, and HH/HV backscatter signatures** of documented sub-canopy settlement sites during the period before visible forest clearing.
2. Compare, site by site, the timing of the first ALOS-2 anomaly with the first detectable change in **Sentinel-2, Sentinel-1, and CopPhil Forest Cover Change products**.
3. Determine where the L-band early signal is **detectable, ambiguous, or absent**, rather than assuming that all settlement sites produce the same response.
4. Establish a technical foundation for a future **preventive monitoring layer for DENR-FMB and LGUs**.


## Case Study <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Tile","properties":{"id":"s2-cloudless-2025","title":"Sentinel-2 Cloudless 2025"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2025_3857/default/g/{z}/{y}/{x}.jpg"]}},{"type":"Tile","properties":{"id":"labels","title":"Labels"},"source":{"type":"XYZ","urls":["https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.jpg"]}}]' center=[125.95,7.62] zoom="9" animationOptions="{duration:500}" }-->

##### Davao de Oro, Mindanao

**Davao de Oro** (formerly Compostela Valley) in Mindanao serves as the pilot area for the study. It was selected because it represents a documented hotspot for forest loss and illegal logging, while DENR-FMB maintains field presence and case records that can be used to anchor the satellite analysis to documented encroachment locations.

The source material identifies several reasons for selecting the province:

- Approximately **43,000 hectares of forest loss between 2010 and 2023**.
- Around **80% of the province is classified as geohazard area**.
- The province was severely affected by **Typhoon Pablo in 2012**, highlighting the importance of watershed and forest protection.
- DENR-FMB field records provide the opportunity to compare remote-sensing signals against **documented, ground-verified encroachment sites**.

<!-- The center above is an approximate province-level center for visualization. Replace it with the exact anchor-site coordinates once the 2–3 final sites are confirmed. -->

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
  <img src="YOUR_DAVAO_DE_ORO_STUDY_AREA_MAP_URL" style="max-width: 100%; width: 1200px; height: auto;" alt="Davao de Oro study area"/>
  <p style="text-align: center; font-size: 0.9em; font-style: italic; margin-top: 5px; margin-bottom: 1px;">
    <b>Figure [1].</b> Pilot study area in Davao de Oro, Mindanao.
  </p>
</div>


## Why ALOS-2? <!--{ style="font-size:1.5rem;opacity:1;margin-top:1rem; color:Navy" }-->

The **Advanced Land Observing Satellite-2 (ALOS-2)**, operated by JAXA, carries the **PALSAR-2 L-band Synthetic Aperture Radar (SAR)** sensor. Unlike optical imagery, SAR can acquire observations **day or night and through cloud cover**. Its longer L-band wavelength also interacts more deeply with vegetation structure than shorter-wavelength radar such as C-band, making it particularly relevant for investigating changes that may occur **beneath or within a forest canopy**.

For *Bantay Kagubatan*, the importance of ALOS-2 is not simply forest-cover mapping. The study asks whether **changes in HH and HV backscatter can reveal an anomalous signal at a documented settlement site while the upper canopy still appears intact**.

This does **not** mean that every structure beneath forest can automatically be detected. The Ideathon study is designed specifically to test under which site conditions such a signal is present, ambiguous, or absent.


### ALOS-2 Annual Mosaic — Anchor Site Template <!--{ style="font-size:1.2rem;opacity:1;margin-top:1rem; color:Navy" }-->

The final story should visualize the selected anchor sites through a multi-year ALOS-2 time series. Once the exact sites, years, and GeoTIFF URLs are finalized, the following map blocks can be duplicated for each relevant year.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"YOUR_ALOS2_GEOTIFF_URL_YEAR_1"}]},"properties":{"id":"alos2-anchor-site-year-1","title":"ALOS-2 PALSAR-2 Annual Mosaic - YEAR 1"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],8000],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]' zoom="14" center=[YOUR_LONGITUDE,YOUR_LATITUDE] projection="" animationOptions={duration:500}}-->

#### PALSAR-2 L-band — HH Polarization (YEAR 1)

This view should show the **ALOS-2 PALSAR-2 annual mosaic** for the selected anchor site using HH polarization. The HH signal will be examined together with HV and the HH/HV ratio to establish the site's pre-encroachment backscatter behavior and identify any departure from that baseline.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"YOUR_ALOS2_GEOTIFF_URL_YEAR_2"}]},"properties":{"id":"alos2-anchor-site-year-2","title":"ALOS-2 PALSAR-2 Annual Mosaic - YEAR 2"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],8000],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]' zoom="14" center=[YOUR_LONGITUDE,YOUR_LATITUDE] projection="" animationOptions={duration:500}}-->

#### PALSAR-2 L-band — HH Polarization (YEAR 2)

The same location should be shown for the next relevant year. A change in backscatter relative to the established forest baseline would be treated as a **candidate anomaly**, not automatically as proof of settlement. The signal must be interpreted together with field records and the comparison datasets.

### <!--{ layers='[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"YOUR_ALOS2_GEOTIFF_URL_YEAR_3"}]},"properties":{"id":"alos2-anchor-site-year-3","title":"ALOS-2 PALSAR-2 Annual Mosaic - YEAR 3"},"style":{"variables":{"band":1},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["band",1],8000],0,[0,0,0,1],1,[255,255,255,1]],["color",0,0,0,0]]}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels","visible":true},"source":{"type":"XYZ","url":"https://{a-e}.s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]' zoom="14" center=[YOUR_LONGITUDE,YOUR_LATITUDE] projection="" animationOptions={duration:500}}-->

#### PALSAR-2 L-band — HH Polarization (YEAR 3)

This later observation should be compared against both the pre-encroachment baseline and the year in which visible canopy disturbance is first recorded by Sentinel-2, Sentinel-1, CopPhil, or DENR field documentation.


## Methodology Workflow & Data

The study combines **L-band SAR, C-band SAR, optical imagery, CopPhil thematic products, and DENR-FMB field information**. The multi-sensor approach is intended to reconstruct when each documented encroachment site first becomes detectable by different observation systems.

| Name | Provider | Resolution | Temporal Coverage | Polarization | Purpose |
|---|---|---|---|---|---|
| Landsat | USGS / NASA | 15–30 m (optical) | 2020–present | N/A | Forest-cover mapping and supporting optical change interpretation |
| Sentinel-1 | ESA / Copernicus | 5–40 m (C-band SAR, IW/EW) | 2020–present | VV, VH | Surface clearing and structure/disturbance comparison |
| Sentinel-2 | ESA / Copernicus | 10–60 m (optical) | 2020–present | N/A | Optical change timeline and canopy-disruption interpretation |
| ALOS-2 PALSAR-2 | JAXA | ~25 m (L-band SAR, annual mosaic) | Annual time series | HH, HV | Primary dataset for testing sub-canopy backscatter anomalies |
| CopPhil Forest & Area Type | Copernicus Philippines (CopPhil) | 10–30 m | Annual | N/A | Reference mapping of forest areas |
| CopPhil Forest Cover Change | Copernicus Philippines (CopPhil) | 20 m | Annual | N/A | Reference for the timing of mapped forest disturbance/change |


### Proposed Operational Processing Chain

The broader monitoring concept consists of four steps:

1. **Satellite data acquisition** — integrate observations from JAXA, NASA/USGS, ESA/Copernicus, and CopPhil.
2. **Processing and analysis** — use optical data for forest characterization and SAR data to investigate structure- and disturbance-related signals.
3. **Validation** — compare candidate detections with DENR-FMB field information and expert review.
4. **Platform integration** — ultimately provide results through a web-based interface with regional/provincial search and downloadable outputs.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
  <img src="YOUR_METHODOLOGY_WORKFLOW_URL" style="max-width: 100%; width: 1000px; height: auto;" alt="Methodology and processing workflow"/>
  <p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 10px;">
    <b>Figure [2].</b> Methodology and processing steps for the proposed monitoring system.
  </p>
</div>


### Current Approach: Retrospective Case Study

The present Ideathon effort is **not yet an automated operational monitoring system**. Instead, it is a focused retrospective case study designed to answer one testable question:

**Did ALOS-2 register an anomalous backscatter signal at a documented settlement site before the surrounding forest clearing became visible to CopPhil, optical imagery, or C-band SAR?**

The retrospective workflow proceeds in six stages:

1. **Baseline characterization** — extract ALOS-2 HH, HV, and HH/HV ratio for approximately 2–3 years before documented encroachment to establish a site-specific forest backscatter baseline.
2. **Temporal backscatter profiling** — plot the annual HH/HV time series from the first available mosaic to 2025 and identify departures from the pre-encroachment baseline.
3. **Optical timeline reconstruction** — assemble Sentinel-2 annual best-available composites and identify the first year in which canopy disruption becomes visible in true-colour imagery or NDVI.
4. **CopPhil cross-reference** — determine the first year in which each site appears as a change pixel in the CopPhil Forest Cover Change product.
5. **Timeline comparison** — compare the ALOS-2 anomaly year, first optical visibility, first CopPhil registration, and DENR documented date.
6. **Signal characterization** — classify each case as detectable, ambiguous, or inconclusive, avoiding over-interpretation where the evidence is insufficient.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
  <img src="YOUR_RETROSPECTIVE_CASE_STUDY_FIGURE_URL" style="max-width: 100%; width: 1000px; height: auto;" alt="Retrospective case-study approach"/>
  <p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 10px;">
    <b>Figure [3].</b> Pilot area and retrospective case-study approach.
  </p>
</div>


## Results

### Proof-of-Concept Status

This project is currently at the **proof-of-concept stage**, and final operational results are not yet available. The statements below therefore represent the **hypotheses being tested**, rather than confirmed findings.

The analysis is designed to determine whether:

- **ALOS-2 HH/HV backscatter exhibits a detectable anomaly** at documented settlement sites while the forest canopy still appears intact.
- The first ALOS-2 anomaly occurs **before** a corresponding disturbance becomes visible in Sentinel-2, Sentinel-1, or CopPhil Forest Cover Change.
- Any resulting lead time can be quantified site by site and interpreted as a potential **early-warning window**.
- The signal is sufficiently repeatable to justify development of a future L-band monitoring layer, while explicitly documenting sites where the response is ambiguous or absent.


### Four-Phase Detection Concept

The clearest way to communicate the concept is as a four-phase progression of forest encroachment:

| Phase | Site Condition | Optical / Sentinel-2 | C-band / Sentinel-1 | L-band / ALOS-2 |
|---|---|---|---|---|
| **Phase 1** | Undisturbed forest | Forest canopy visible | Stable canopy/surface response | Stable forest backscatter baseline |
| **Phase 2** | Early encroachment; structure may exist beneath largely intact canopy | Little or no visible canopy change | Limited surface/canopy indication | **Potential anomalous sub-canopy/structural signal to be tested** |
| **Phase 3** | Initial clearing around settlement | Canopy disruption begins to appear | Disturbance becomes increasingly detectable | Backscatter response may strengthen or change |
| **Phase 4** | Established clearing / settlement | Clear visible change | Clear surface disturbance | Clear departure from original forest baseline |

The project is centered on **Phase 2**. If a repeatable L-band anomaly can be demonstrated during this stage, it could create an earlier opportunity for field verification before extensive canopy loss occurs.

<div style="display: flex; flex-direction: column; align-items: center; margin: 10px 0;">
  <img src="YOUR_SENSOR_PHASE_MODEL_FIGURE_URL" style="max-width: 100%; width: 1000px; height: auto;" alt="Sensor detection phases"/>
  <p style="text-align: center; font-style: italic; font-size: 0.9em; margin-top: 10px;">
    <b>Figure [4].</b> Conceptual comparison of what different sensors may detect as forest encroachment progresses. Phase 2 is the critical period being tested for a potential L-band early-warning signal.
  </p>
</div>


### Per-Site Timeline Output

For each finalized anchor site, the most important result should be summarized as a common timeline:

| Observation | Year / Date | Evidence |
|---|---|---|
| Pre-encroachment ALOS-2 baseline | TBD | HH, HV, HH/HV |
| First candidate ALOS-2 anomaly | TBD | L-band backscatter departure |
| First visible Sentinel-2 canopy disturbance | TBD | True-colour / NDVI |
| First Sentinel-1 disturbance | TBD | VV / VH response |
| First CopPhil Forest Cover Change registration | TBD | CopPhil change product |
| DENR-FMB documented encroachment date | TBD | Field / administrative record |

<!-- Duplicate this table for Anchor Site 1, Anchor Site 2, and Anchor Site 3 once the final sites and analysis results are available. -->


## Limitations

The current work has several important limitations:

1. **Proof-of-concept scale:** The retrospective study is anchored to only **2–3 documented sites** and should not yet be interpreted as a general operational capability.
2. **Detection is not guaranteed:** A sub-canopy structure may not always produce a distinct or separable L-band backscatter anomaly. Some sites may remain ambiguous or inconclusive.
3. **Annual temporal resolution:** ALOS-2 yearly mosaics provide relatively coarse temporal resolution, so the onset of an anomaly may only be localized to a particular year rather than an exact date.
4. **Sensor differences:** Optical, C-band, and L-band observations respond to different physical characteristics and have different spatial resolutions and acquisition conditions, complicating direct comparison.
5. **Cloud limitations for optical data:** Sentinel-2 and Landsat observations may be unavailable or difficult to interpret during persistently cloudy periods.
6. **Site-specific effects:** Topography, vegetation density, moisture, radar geometry, settlement size, and construction materials may influence the observed backscatter response.
7. **Data availability:** Additional ALOS-2/ALOS-4 acquisitions over the final anchor sites may be required where suitable observations are not already available through existing archives or public sources.


## Future Development

If the retrospective analysis demonstrates a reproducible L-band early-warning signal, the next stage is to develop a **dual-frequency SAR monitoring pipeline** and an **Early Encroachment Alert system**.

The proposed development path is:

- **Finalize anchor sites:** Confirm 2–3 documented encroachment sites with DENR-FMB.
- **Complete multi-year analysis:** Generate ALOS-2 HH, HV, and HH/HV profiles and compare them with Sentinel-1, Sentinel-2, CopPhil, and field records.
- **Request additional observations where required:** Identify gaps and consider ALOS-2/ALOS-4 acquisitions over priority sites.
- **Define detection criteria:** Determine how large and persistent an L-band anomaly must be before it becomes a candidate field-verification alert.
- **Expand validation:** Test the method across additional watersheds, forest types, terrain conditions, and settlement characteristics.
- **Develop the dual-frequency workflow:** Use L-band for the potential early/sub-canopy signal and C-band/optical data for subsequent confirmation of surface disturbance.
- **Integrate with CopPhil:** Explore an operational L-band monitoring layer and alert interface for DENR-FMB and LGU users.

The long-term goal is not to replace field enforcement, but to provide **earlier and more targeted information for field verification**, helping agencies prioritize where limited monitoring resources should be deployed.


## References

- European Space Agency. (n.d.). *Copernicus Sentinel-1 and Sentinel-2* [Satellite imagery]. Copernicus Data Space Ecosystem. https://dataspace.copernicus.eu
- Global Forest Watch. (2024). *Philippines: Tree cover loss, 2001–2022* [Data set]. World Resources Institute. https://www.globalforestwatch.org
- Hansen, M. C., Potapov, P. V., Moore, R., Hancher, M., Turubanova, S. A., Tyukavina, A., Thau, D., Stehman, S. V., Goetz, S. J., Loveland, T. R., Kommareddy, A., Egorov, A., Chini, L., Justice, C. O., & Townshend, J. R. G. (2013). High-resolution global maps of 21st-century forest cover change. *Science, 342*(6160), 850–853. https://doi.org/10.1126/science.1244693
- Intergovernmental Panel on Climate Change. (2006). *2006 IPCC guidelines for national greenhouse gas inventories*. Institute for Global Environmental Strategies.
- Japan Aerospace Exploration Agency. (n.d.). *Global PALSAR-2/PALSAR yearly mosaic* [Data set]. Earth Observation Research Center. https://www.eorc.jaxa.jp/ALOS/en/
- Philippines. (2023). *First biennial transparency report of the Philippines*. United Nations Framework Convention on Climate Change.
- Shimada, M., Itoh, T., Motooka, T., Watanabe, M., Shiraishi, T., Thapa, R., & Lucas, R. (2014). New global forest/non-forest maps from ALOS PALSAR data (2007–2010). *Remote Sensing of Environment, 155*, 13–31. https://doi.org/10.1016/j.rse.2014.04.014
- United Nations. (2015). *Paris Agreement*.
- United Nations Framework Convention on Climate Change. (2022). *Philippine forest reference level*.
- U.S. Geological Survey. (n.d.). *Landsat 8–9 OLI/TIRS* [Satellite imagery]. Earth Resources Observation and Science Center. https://www.usgs.gov/landsat-missions

