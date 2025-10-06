---
cover-image: https://ichef.bbci.co.uk/ace/standard/976/cpsprodpb/10678/production/_92329176_c0157414-lowland_rainforest_danum_valley_sabah-spl.jpg.webp
date: 2025-01-01
theme: theme_name
tags: some,tags

---

# Evaluating time series interpolation techniques for vegetation monitoring using remote sensing data <!--{ as="img" mode="hero" src="https://ichef.bbci.co.uk/ace/standard/976/cpsprodpb/10678/production/_92329176_c0157414-lowland_rainforest_danum_valley_sabah-spl.jpg.webp" }-->
### Authors: Fran, Denise, Mae <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

#
*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in February 2025. It was developed by a team from University of Leeds, Edinburgh and Venice*

## Challenge
Vegetation Earth Observation (EO) time series are essential for monitoring ecosystem health, agricultural productivity, and the impacts of climate change. One of the most widely used indicators in this context is the **Normalised Difference Vegetation Index (NDVI)**, which measures vegetation greenness and health based on how plants reflect light in the red and near-infrared parts of the spectrum. 

<img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-7/stories/ScienceHub-Challenge-September-2025/time-series-interpolation/timesSeries_2.png?raw=true"/>
<p style="text-align:center;"><b>NDVI:</b> A proxy for vegetation health.</p>

However, NDVI time series often still contain residual **effects of clouds, even after data pre-processing**. The accuracy of NDVI reconstructions can also vary depending on land cover type, as different landscapes show distinct patterns in seasonality, amplitude, and the rate of vegetation change (Julien and Sobrino, 2019). Ensuring **accurate interpolation** is therefore crucial for producing reliable insights into vegetation dynamics and environmental change.

<div style="text-align: center;">
    <img src="https://github.com/eurodatacube/eodash-assets/blob/AparicioSF-patch-7/stories/ScienceHub-Challenge-September-2025/time-series-interpolation/timeSeries_1.png?raw=true" width="500"/>
    <p><b>Missing data:</b> The impacts of cloud coverage on NDVI acquisitions.</p>
</div>


## Objective
The objective of this study was to design and implement a reproducible framework to compare multiple time series interpolation techniques on vegetation EO datasets with multiple, artificially introduced & user-defined temporal gaps.

## Use cases
**Five contrasting ecosystems** were used as case studies to test and compare interpolation methods. Each site represents different vegetation types, climatic conditions, and seasonal patterns, providing a comprehensive assessment of method performance under real-world variability.
- **Amazon** – Moist tropical forest with low seasonality and high precipitation; stores ~123 billion tonnes of carbon (NOAA, 2021).
- **Caatinga** – Seasonal tropical forest with high seasonality and precipitation; ~100,000 km² with large seasonal fluxes of carbon, water, and other compounds.
- **Elmstein** – Temperate forest with high seasonality and medium precipitation.
- **Muara** – Moist tropical forest with monsoonal precipitation and high seasonality.
- **Rockies** – Boreal forest with high seasonality and medium precipitation.


## Data and Methods
#### Data
- **Source**: NDVI (Normalized Difference Vegetation Index) data were obtained from the DeepESDL Earth System Datacube (ESDC) v.3.0.1, which is a curated dataset derived from MODIS Terra and Aqua satellites.
- **Temporal resolution**: 8-day intervals, providing a moderately high temporal sampling of vegetation dynamics.
- **Spatial resolution**: 0.25° (~28 km), which is suitable for large-scale ecosystem analysis.
- **Preprocessing**: NDVI values are derived from BRDF-corrected daily reflectance data, which reduces biases caused by view angle, atmospheric conditions, and illumination.

#### Methods
**NDVI time series (2017–2022)** were extracted at selected sites. Then, **artificial gaps** of varying lengths (3 weeks, 3 months, 6 months) were introduced to mimic missing data. Four **interpolation methods**, namely Linear, Cubic Spline, Gaussian Process, and Seasonal Cycles, were used to reconstruct the gaps. 
Finally, these methods were evaluated based on **accuracy (R², RMSE)** and **computational efficiency**. Overall, this approach allows a controlled comparison of interpolation methods under different ecosystem types (high vs. low seasonality) and gap durations, enabling an evaluation of both accuracy and computational performance.


## Results
Interpolation accuracy decreases as gap length increases, with short gaps generally producing better results. **Gaussian Process Regression (GPR)** provides strong performance but requires roughly twice the processing time compared to other methods. For seasonal vegetation patterns, the most effective interpolation method **depends on gap length**: Linear and Cubic Spline work best for **short gaps**, while Seasonal and GPR methods are more reliable for **longer gaps**. For non-seasonal patterns, either Linear or Seasonal interpolation performs best.
#### Future work
The current data (~28 km) is suitable for large forests, but finer-resolution data (e.g., Sentinel-2) is needed for smaller or more fragmented areas. The choice of interpolation method depends on the characteristics of the time series and the length of missing data gaps. Future work will focus on testing these methods on high-resolution datasets across diverse ecosystems and incorporating additional environmental variables to improve accuracy.


## Open Science
#### Data used


#### Notebook


#### References
- Julien, Y. and Sobrino, J.A. (2019). Optimizing and comparing gap-filling techniques using simulated NDVI time series
from remotely sensed global data. International Journal of Applied Earth Observation and Geoinformation, 76, pp.93-111

- de Oliveira, M.L.; dos Santos, C.A.C.; Santos, F.A.C.; de Oliveira, G.; Santos, C.A.G.; Bezerra, U.A.; de B. L. Cunha,
J.E.; da Silva, R.M. Evaluation of Water and Carbon Estimation Models in the Caatinga Biome Based on Remote
Sensing. Forests 2023, 14, 828. https://doi.org/10.3390/f14040828.


