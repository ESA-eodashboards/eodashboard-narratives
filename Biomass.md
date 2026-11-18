# Biomass mission for water dynamics under forest <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2023/02/biomass_satellite_over_forest/24725063-1-eng-GB/Biomass_satellite_over_forest_pillars.jpg" }-->
#### 

## Authors: Inga Lammers(1), Emilian Tietze(2) and Niels Dedring(1)
**Affiliations:**
(1) Ruhr University Bochum (RUB)
(2) TU Wien

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in 11/2026. It was developed by a team from the RUB and TU Wien.*

## 
<p align="center">
  <img src="https://services.ruhr-uni-bochum.de/sites/services.ruhr-uni-bochum.de/files/styles/991x660px/public/2023-10/logo_rub_blau.png.webp?h=d95abdc4&itok=EIQbKx4O" alt="Ruhr University Bochum" height="80" style="margin: 0 15px;"/>
  <img src="https://fam.tuwien.ac.at/lehre/arbeiten/logos/Logos_TU/TU-Signet.jpg" alt="TU Wien" height="80" style="margin: 0 15px;"/>
</p>

## Challenge
The challenge involves observing hydrological processes like inundation and soil moisture beneath dense canopy layers. While traditional optical and shorter-wavelength SAR methods often struggle with such thick vegetation, the Biomass mission introduces P-band radar technology, which is specifically optimized for deeper penetration through complex biomass structures.

## Objective
Our objective is to leverage the unique capabilities of the Biomass mission's P-band radar to accurately quantify subsurface water dynamics. To validate these findings, we cross-reference our data with Sentinel-1 observations, allowing us to assess the performance advantages of P-band radar in forest-covered environments.

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=12 center=[89.3667,21.7583] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Harinagar, Bangladesh
The Sundarbans region presents a complex hydrological landscape. SAR data allows us to observe water levels even beneath the dense canopy.

### <!--{ zoom=13 center=[89.38,21.76] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Tidal Dynamics
Monitoring the daily tidal fluctuations is crucial for understanding nutrient transport. Radar signals reveal the inundation patterns in the mangroves.

### <!--{ zoom=14 center=[89.35,21.74] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### River Channel Analysis
Narrow channels often remain obscured by tree branches. Our SAR processing emphasizes these features to calculate flow accumulation.

### <!--{ zoom=12 center=[89.4,21.78] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Soil Moisture Gradients
We analyze the backscatter intensity to map spatial soil moisture gradients across the forest floor.

### <!--{ zoom=10 center=[89.3667,21.7583] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}}]' animationOptions='{"duration":500}' }-->
#### Regional Impact
Synthesizing these observations provides a comprehensive view of how water dynamics influence the biomass growth of this fragile ecosystem.

## Data and Methods
#### Dataset
- **Source**: SAR Data
- **Temporal coverage**: Measurements are available every 3 days, from 07/25/2026 to 08/12/2026 resulting in 7 SAR measurements.
- **Spatial resolution**: The raw data has an inital resolution of 39m azimuth and 6m range. After applying the "multilooking method" a resolution of about 40m per pixel is achieved.
- **Area**: The inital datafile has a width of 1363 pixels
and a height of 3425 pixels.
#### Methodology workflow


Our methodology consists of six main steps, starting with the reconstruction of the polarimetric SAR data and ending with the development of a potential wetness indicator.

##### 1. Scattering Matrix Reconstruction

The amplitude and phase information from the Biomass Level 1C measurement files are combined to reconstruct the complex scattering matrix:

<p align="center">
  <i>S</i><sub>pq</sub> = |<i>S</i><sub>pq</sub>| e<sup>j&phi;<sub>pq</sub></sup>
</p>

This matrix contains the complex scattering coefficients for the four polarimetric channels (HH, HV, VH and VV), preserving both amplitude and phase information.

##### 2. Polarimetric Multilooking

To reduce speckle and better characterize distributed targets such as mangrove forests, spatial averaging is applied to neighbouring pixels.

Two polarimetric matrices are generated:

- **Covariance Matrix (C3):** Calculated using the lexicographic target vector.
- **Coherency Matrix (T3):** Calculated using the Pauli target vector.

These matrices provide complementary representations of the polarimetric information and form the basis for the subsequent decomposition techniques.

##### 3. Polarimetric Visualization and Decomposition


 The Freeman-Durden method was applied to separate the signal into odd-bounce, double-bounce and volume scattering contributions.


This methods helps to distinguish the radar responses associated with vegetation, water and the underlying surface.

##### 4. Temporal Coherence Analysis

Temporal coherence is calculated for the seven SAR acquisitions (25 July–12 August 2026) using two approaches:

- **Consecutive comparison:** Each acquisition is compared with the following one to identify short-term changes.
- **Reference comparison:** All acquisitions are compared against the first timestamp to investigate changes relative to a common reference.

The resulting coherence maps reveal areas of different temporal stability.

##### 5. Analysis of Selected Areas

Areas exhibiting the highest temporal coherence are selected for further investigation. Within these areas, the temporal evolution of the polarimetric scattering powers and decomposition parameters is analysed.

The objective is to identify which scattering contributions change most significantly throughout the observation period and how these changes relate to the underlying water conditions.

##### 6. Copernicus Sea-Level Comparison and Wetness Indicator

Finally, the temporal changes in the SAR-derived parameters are compared with marine sea-level measurements from the Copernicus Marine Service.

By investigating the relationship between sea-level variations and changes in the polarimetric scattering contributions, we aim to identify the radar parameter most sensitive to changing water conditions.

Based on this relationship, we explore the development of an empirical **wetness indicator** to investigate the potential of P-band SAR for monitoring water dynamics beneath mangrove forests.

## Results


## Conclusions


## Open Science


## Contributors
Authors, contributors, and reviewers from [Ruhr University Bochum](https://services.ruhr-uni-bochum.de/en/rub-logo) and [TU Wien](https://fam.tuwien.ac.at/lehre/arbeiten/logos/Logos_TU/TU-Signet.jpg). (https://www.esa.int)

**Reference:**
ESA Science Hub Challenges (2026). Biomass mission for water dynamics under forest study.

**Image references:**
https://www.esa.int [Accessed: 18/11/2026]
https://services.ruhr-uni-bochum.de/en/rub-logo [Accessed: 18/11/2026]
https://fam.tuwien.ac.at/lehre/arbeiten/logos/Logos_TU/TU-Signet.jpg [Accessed: 18/11/2026]