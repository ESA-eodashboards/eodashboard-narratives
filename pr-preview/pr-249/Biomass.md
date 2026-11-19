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



## Data and Methods
#### Dataset
- **Source**: SAR Data
- **Temporal coverage**: Measurements are available every 3 days, from 07/25/2026 to 08/12/2026 resulting in 7 SAR measurements.
- **Spatial resolution**: The raw data has an inital resolution of 39m azimuth and 6m range. After applying the "multilooking method" a resolution of about 40m per pixel is achieved.
- **Area**: The inital datafile has a width of 1363 pixels
and a height of 3425 pixels.
#### Methodology workflow


Our methodology consists of seven main steps, starting with the reconstruction of the polarimetric SAR data and ending with the development of a potential wetness indicator.

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


 The Freeman-Durden method is applied to separate the signal into odd-bounce, double-bounce and volume scattering contributions.


This methods helps to distinguish the radar responses associated with vegetation, water and the underlying surface.

##### 4. Temporal Coherence Analysis

Temporal coherence is calculated for the seven SAR acquisitions (25 July–12 August 2026) using two approaches:

- **Consecutive comparison:** Each acquisition is compared with the following one to identify short-term changes.
- **Reference comparison:** All acquisitions are compared against the first timestamp to investigate changes relative to a common reference.

The resulting coherence maps reveal areas of different temporal stability.

##### 5. Selected Areas
Three approaches are considered to find specific areas of interest: 
<ul>
  <li><strong>First:</strong> Mean of all pairs relative to the first image (t0→t1, t0→t2, …).</li>
  <li><strong>Consecutive:</strong> Mean of all image-to-image pairs (t0→t1, t1→t2, …).</li>
  <li><strong>All:</strong> Mean of every pair from both groups.</li>
</ul>
 A square is slid over the mean coherence (forest only). The 3 squares with the lowest coherence and 1 with the highest (a stable reference) is picked, without overlapping. A square is only allowed if at least MIN_VALID of it is forest. Only the AOIs of the consecutive approach is saved as shapefiles and considered in the following steps.
 Within these chosen areas, the temporal evolution of the polarimetric scattering powers and decomposition parameters is analysed.

The objective is to identify which scattering contributions change most significantly throughout the observation period and how these changes relate to the underlying water conditions.
##### 6. Temporal Pixel-wise Decomposition of Signal Power Pixel-wise comparison of signal power composition


<p>
To investigate tidal movement and its influence on radar backscatter, a pixel-wise decomposition of signal power was generated across the entire time series. This allows temporal changes in the individual scattering contributions to be tracked at each pixel, helping to identify areas where variations in water levels affect the radar response.
</p>

<p>
By examining the evolution of signal power over time, potential tidal-driven changes in scattering behaviour can be identified and compared with observed sea-level variations. This provides a basis for assessing the sensitivity of different scattering mechanisms to underlying water dynamics.
</p>

##### 7. Copernicus Sea-Level Comparison and Wetness Indicator

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