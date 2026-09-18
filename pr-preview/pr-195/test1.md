# Unsupervised Mapping of Urban Thermal Environments in the Milan and Monza-Brianza area <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2022/07/land-surface_temperature_in_milan_on_18_june_2022/24345700-1-eng-GB/Land-surface_temperature_in_Milan_on_18_June_2022_pillars.jpg" }-->
#### <small>Authors: Thomas Martinoli¹ , Yiyi Cen¹ , Sara Reffinetti¹ <br><sub style='font-size:0.7em'>¹ Politecnico of Milan</sub></small>

## 
*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in September 2026. It was developed by a team from the Politecnico of Milan.*

## 
<p align="center" style="margin-top:-20px; margin-bottom:-20px;">
  <img src="https://cdn.freebiesupply.com/logos/large/2x/politecnico-di-milano-1-logo-png-transparent.png" alt="Politecnico di Milano" height="250"/>
</p>

## Challenge
Urban environments are not spatially uniform. Vegetation, buildings, impervious surfaces, bare soil and water often occur within short distances and influence surface temperature in different ways. As a result, different parts of the same city can exhibit clearly different thermal conditions.

Urban environments are often described using predefined land-cover classes, such as built-up areas, vegetation or water. While these classifications are useful, real urban surfaces tend to vary continuously and often overlap or mix with one another. Fixed classes may therefore not fully capture this complexity.

This leads to our main research question:

**Can distinct urban thermal environments be identified directly from multi-variable Earth Observation data without defining the classes in advance?**

## Objective
The objective of this study is to use multi-variable Earth Observation data and unsupervised learning to develop a data-driven characterisation of urban environments in the Milan–Monza area.

By combining information related to temperature, vegetation and built-up characteristics, we use clustering to identify urban areas with similar environmental properties and then interpret their surface and thermal characteristics. Finally, the resulting clusters are compared with existing land-cover products and Local Climate Zones to understand how these data-driven urban types relate to established classification systems.

## Dataset
The analysis focused on the **provinces of Milan and Monza-Brianza**, leveraging Earth Observation data from **June to August 2021** to capture thermal variations.
| Data source | Product | Variables | Spatial Resolution |
| :---: | :---: | :---: | :---: ||
| **Landsat 8** | Collection 2 Level-2 | Land Surface Temperature (LST) | 30 m |
| **Sentinel-2** | MSI – Level-2A (L2A) | NDVI, NDRE, NDBI, BSI, mNDWI, Albedo | 20 m |
| **Copernicus CLMS*** | Tree Cover Density | Vegetation cover | 10 m |
| **Copernicus CLMS*** | Imperviousness | Impervious surfaces | 10 m |

*CLMS: Copernicus Land Monitoring Service

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=11.5 center=[9.02,45.5268] layers='[{"type":"Tile","properties":{"id":"terrain-light","title":"Terrain Light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"study-area","title":"Study Area"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/AOI_Milan_Monza%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":"rgba(255,255,255,0.03)","stroke-color":"#d7191c","stroke-width":3}}]' animationOptions='{"duration":500}' }-->
#### Milan and Monza-Brianza Area
The study focuses on the Milan and Monza-Brianza area in northern Italy. The region includes highly urbanised city centres, residential areas, industrial and commercial zones, green spaces and peri-urban areas.

These different urban environments are closely interwoven within a relatively compact area, providing rich spatial variation for comparing different urban surface characteristics.

### <!--{ zoom=11.5 center=[9.02,45.5268] layers='[{"type":"Tile","properties":{"id":"terrain-light","title":"Terrain Light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"tree-cover","title":"Tree Cover Density 2021"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/TCD_2021_100m_classes%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":["match",["get","class_id"],1,"rgba(198,233,192,0.60)",2,"rgba(77,175,74,0.70)",3,"rgba(0,100,0,0.85)","rgba(0,0,0,0)"]}},{"type":"Vector","properties":{"id":"study-area","title":"Study Area"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/AOI_Milan_Monza%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":"rgba(255,255,255,0)","stroke-color":"#d7191c","stroke-width":2}}]' animationOptions='{"duration":500}' }-->
#### Tree Cover Density
Tree Cover Density is one of the variables used to describe urban vegetation structure. The map shows clear spatial differences in tree canopy cover across the study area, ranging from areas with very limited tree cover to much greener zones.

This map is presented as one example of the input variables used in the analysis. The full analysis also includes multiple Sentinel-2 spectral indices and other surface characteristics.

### <!--{ zoom=11.5 center=[9.02,45.5268] layers='[{"type":"Tile","properties":{"id":"terrain-light","title":"Terrain Light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Vector","properties":{"id":"imperviousness","title":"Imperviousness Density 2021"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/Imperviousness_2021_100m_classes%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":["match",["get","class_id"],1,"rgba(245,220,180,0.60)",2,"rgba(230,130,80,0.72)",3,"rgba(170,30,30,0.85)","rgba(0,0,0,0)"]}},{"type":"Vector","properties":{"id":"study-area","title":"Study Area"},"source":{"type":"Vector","url":"https://pub-fa7ad61ab36e4bc19f50a87a8cd497d4.r2.dev/AOI_Milan_Monza%20%281%29.geojson","format":"GeoJSON"},"style":{"fill-color":"rgba(255,255,255,0)","stroke-color":"#d7191c","stroke-width":2}}]' animationOptions='{"duration":500}' }-->
#### Imperviousness Density
Imperviousness Density describes the proportion of buildings, roads and other artificial sealed surfaces, providing an indication of urban built-up intensity.

Spatially, high imperviousness is mainly concentrated in the urban core of Milan and other continuously urbanised areas. Towards the urban fringe, imperviousness generally decreases, revealing a gradual transition from densely built-up areas to lower-density and more open environments.

## Methodology workflow
The analysis followed a systematic processing pipeline:

- **1- Select and composite data:** The study focused on the Milan and Monza-Brianza area during summer 2021 (June–August). Sentinel-2 Level-2A images were selected based on acquisition date and cloud cover. Six surface indicators—NDVI, NDRE, NDBI, BSI, MNDWI and Albedo—were derived, and a pixel-wise temporal median was calculated using valid observations. Tree Cover Density and Imperviousness Density were taken from the corresponding 2021 annual products, while LST was represented by the summer composite.

| Variable | Formula / derivation | Environmental information |
| :---: | :--- | :--- |
| **NDVI** | (B8A − B04) / (B8A + B04) | Vegetation greenness |
| **NDRE** | (B8A − B05) / (B8A + B05) | Red-edge vegetation condition |
| **NDBI** | (B11 − B8A) / (B11 + B8A) | Built-up characteristics |
| **BSI** | ((B11 + B04) − (B8A + B02)) / ((B11 + B04) + (B8A + B02)) | Bare soil and built-up surfaces |
| **MNDWI** | (B03 − B11) / (B03 + B11) | Water detection and masking |
| **Albedo** | Derived from six Sentinel-2 spectral bands | Surface reflectivity |

- **2- Aggregate and align datasets:** All variables were aligned to a common **100 m spatial grid** using the Sentinel-2 100 m grid as the reference (EPSG:32632). The original 10 m Tree Cover Density and Imperviousness Density products were aggregated to 100 m using area-weighted averaging, while LST was aligned to the same grid. The resulting feature raster contained nine variables.

- **3- Mask invalid and water cells:** Only grid cells with valid values for all input variables were retained, with no missing-value imputation applied. Water cells were identified using MNDWI and cells with **MNDWI > 0.2** were excluded from the analysis.

- **4- Assess correlations and normalize:** Correlations between variables were examined to identify potential redundancy. Each variable was then clipped to its 1st–99th percentile range and rescaled to **0–1** to reduce the influence of extreme values and differences in scale.

- **5- PCA:** Principal Component Analysis (PCA) was applied to the normalized variables. MNDWI was excluded because it had already been used for water masking. The minimum number of principal components explaining at least **90% of the total variance** was retained; the first three components reached this threshold.

- **6- K-means clustering:** K-means clustering was applied in the PCA-reduced feature space for **k = 4–15**. Different evaluation criteria suggested different optimal solutions: **k = 4, 6 and 9**. These three clustering configurations were therefore retained for further comparison and interpretation.


<p align="center">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/307316d228fa0050e18127b7c0f9c93e3b65c077/assets/yiyilv/IMG2006-1789684437359.png" width="900">
</p>

<p align="center">
  <em>Figure X. Evaluation of different numbers of K-means clusters using Inertia, Silhouette Score and the Calinski–Harabasz Index. The different criteria highlighted k = 4, 6 and 9 as candidate solutions for further analysis.</em>
</p>

- **7- Cluster interpretation:** Each cluster was characterised using the mean normalized values of the input variables. The cluster labels were then mapped back onto the original 100 m grid to examine their spatial distribution and environmental differences.
- **8- Comparison:** The **k = 4, 6 and 9** clustering solutions were compared in terms of their spatial patterns, cluster profiles and correspondence with **Local Climate Zones (LCZ)**. LCZ was used as an external reference to assess how the data-driven clusters relate to established urban climate types.

## Results
Different clustering evaluation metrics suggested different numbers of clusters, so we further compared three solutions: **k = 4, 6 and 9**. These can be interpreted as different levels of detail within the same urban environmental structure: k = 4 captures broader environmental types, k = 6 provides an intermediate level of subdivision, and k = 9 describes finer-scale environmental differences. Cluster labels are independent across different values of k, so the comparison is based mainly on their characteristics and spatial patterns.

#### Clustering structure in PCA space

We first compared the three solutions in PCA feature space. The first two principal components capture most of the dominant variation in the data, with PC1 explaining **76.8%** of the total variance and PC2 explaining **8.1%**. Based on the PCA loadings, the negative direction of PC1 is mainly associated with vegetation-related variables such as NDVI and NDRE, while the positive direction is more strongly related to NDBI, BSI, Imperviousness and LST. PC2 is largely influenced by Tree Cover Density.

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/fb5278e891629cc2a381df21d1ef8ffd4368513f/assets/yiyilv/pcaclustersk4-1789687251614.png" style="width: 90%;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/59ef6ffd718502d8644fb992bbd2f762095f42da/assets/yiyilv/pcaclustersk6-1789687261059.png" style="width: 90%;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/9c2e21e9395e7d7df171813647b68d62481e777c/assets/martinolithomas-ui/pcaclustersk9-1789689006480.png" style="width: 90%;">
</div>


*Figure 1. K-means clustering results for k = 4, 6 and 9 projected onto the first two principal components. Colours represent different clusters and crosses indicate cluster centroids.*

All three solutions show a similar overall structure. Rather than forming several completely separated groups, the data follow a relatively continuous environmental gradient. Moving from the left to the right side of the PCA space broadly corresponds to a transition from more vegetated and less built-up surfaces towards more built-up and warmer urban environments.

With **k = 4**, this continuous gradient is divided into four broad regions, producing the simplest clustering structure. With **k = 6**, some of these broader regions are further subdivided, particularly within intermediate built-up and transitional environments. With **k = 9**, the same gradient is divided into finer groups, revealing more local differences.

Overall, increasing k does not substantially change the underlying structure of the data, but progressively provides a finer subdivision of the same environmental gradient.
#### Cluster profiles and environmental characteristics

Each profile shows the mean normalised value (0–1) of the eight variables entering the PCA, computed for each cluster. Values are relative within the study area, not physical units, and are used to interpret each cluster in terms of vegetation, built-up intensity, tree cover and relative surface temperature.

![profili_B0_k4.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/9c2f2331019fcc9120c0e9a520d8b54e7e1712c7/assets/yiyilv/profiliB0k4-1789687647016.png)
<p align="center">
  <em>Figure X. Cluster profiles for k = 4: mean normalised value (0–1) of each variable per cluster.</em>
</p>

C2 (grey) represents the built-up type and covers 27% of the analysed cells. It is characterised by the lowest NDVI/NDRE (~0.25), the highest NDBI/BSI (~0.8), high imperviousness (0.71) and the highest LST (0.77). C3 (dark green) covers 8% of the area and corresponds to tree cover. It shows high NDVI (0.90) and Tree Cover Density (0.73), the lowest albedo and the lowest LST (0.25). C1 (light green) covers 31% of the area and represents non-woody vegetation, with NDVI comparable to C3 (0.87) but near-zero tree cover. C0 (ochre) covers 34% of the area and is intermediate: moderate NDVI (0.57) and relatively high NDBI/BSI (~0.6) combined with low imperviousness (0.17), indicating bare or sparsely vegetated, largely unsealed surfaces rather than built-up areas.

With k = 6, the same overall structure as k = 4 is preserved. Tree cover (C1, dark green, 7%) and non-woody vegetation (C4, green, 23%) remain essentially unchanged. 
![profili_B0_k6 1.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/b189c5764ed92432c0457fcef60a2eea7c1117af/assets/yiyilv/profiliB0k6-1-1789687654701.png)
<p align="center">
  <em>Figure X. Cluster profiles for k = 6: mean normalised value (0–1) of each variable per cluster.</em>
</p>

The remaining clusters can be interpreted as a finer subdivision of the built-up and intermediate types of k = 4. The built-up domain appears as a dense type (C5, dark grey, 15%; imperviousness 0.83, LST 0.81) and an intermediate type (C2, light grey, 18%; imperviousness 0.52, LST 0.69). Unsealed surfaces appear as bare/sparsely vegetated (C0, brown, 16%; LST 0.56) and partially vegetated (C3, ochre, 21%; LST 0.43).

With k = 9, the same behaviour is observed, and the additional clusters can be interpreted as further detail at both ends of the gradient. 
![profili_B0_k9.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/a96a09713bd649adc3c98e1a9ddbe2f105634e01/assets/martinolithomas-ui/profiliB0k9-1789688732488.png)
<p align="center">
  <em>Figure X. Cluster profiles for k = 9: mean normalised value (0–1) of each variable per cluster.</em>
</p>

The built-up domain is resolved into three levels of imperviousness (0.39 → 0.61 → 0.87), with LST increasing accordingly (0.62 → 0.72 → 0.83). The vegetated domain includes dense tree cover (C3, dark green, 5%; lowest LST 0.18), mixed tree–open vegetation (C8, olive, 6%), and two non-woody vegetation types of different density (C7 and C1). Partial tree cover (C8, LST 0.38) is not cooler than dense non-woody vegetation (C7, LST 0.21).

Across all three solutions, the same pattern emerges: surface temperature rises as the landscape becomes more built-up and falls as vegetation increases. Vegetated areas are consistently the coolest, whether or not they are tree-covered. At k = 4, tree cover and non-woody vegetation reach almost the same LST (0.25 vs 0.28), and at k = 9 areas with partial tree cover are even warmer than dense grassland or cropland. At 100 m resolution, what keeps a surface cool is how densely it is vegetated, not whether that vegetation is trees. Albedo, by contrast, changes little between clusters (0.37–0.48) and plays only a minor role.


#### Spatial distribution
The clusters follow a clear spatial pattern. At k = 4, the built-up cluster covers Milan's urban core and extends north into the Monza-Brianza conurbation and along the main radial roads. The south is mostly non-woody vegetation, corresponding to the agricultural plain. Tree cover is concentrated in narrow corridors along the western and eastern edges, in line with the Ticino and Adda river valleys, plus a few patches in the north. The intermediate cluster is scattered across farmland and the urban fringe, where bare, cultivated and built surfaces are mixed at fine scale.
![map_b0_k4.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/eca453f839766d09967f956ae7d05e4baa445b04/assets/martinolithomas-ui/mapb0k4-1789689699736.png)

At k = 6 and k = 9 the pattern does not change. 

![map_b0_k6.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/b32fa2c0b2e2420a7a78c5b212d1b8909b424c9e/assets/yiyilv/mapb0k6-1789687722581.png)
![map_b0_k9.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e654446fd8d4b84c9b04b55db7aa398dd77d59ef/assets/martinolithomas-ui/mapb0k9-1789688920085.png)The extra clusters mainly subdivide the built-up area into a dense core and less sealed surrounding zones and towns, while the agricultural south and the river corridors stay largely the same. Gaps within the study area are masked water bodies.

!


#### Preliminary comparison of clustering resolutions

## Conclusions


## Open Science


## Contributors
Authors, contibutors, reviewers




