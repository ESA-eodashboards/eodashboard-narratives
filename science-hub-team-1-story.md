---
cover-image: https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2023/10/earthcare_for_a_better_understanding_of_earth_s_radiation_balance/25154725-1-eng-GB/EarthCARE_for_a_better_understanding_of_Earth_s_radiation_balance_pillars.png
date: 2025-01-01
theme: theme_name
tags: some,tags

---

# Exploring our atmosphere with EarthCARE <!--{ as="img" mode="hero" src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2023/10/earthcare_for_a_better_understanding_of_earth_s_radiation_balance/25154725-1-eng-GB/EarthCARE_for_a_better_understanding_of_Earth_s_radiation_balance_pillars.png" }-->
### Authors: Paula Romero Jure¹ and Giacomo Roversi²³ <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->
> ¹ University of Leeds ² Ca’ Foscari University of Venice  ³ CNR-ISAC Rome

# 
*This story is based on results from the [Science Hub Challenges in September 2025](https://sciencehub.esa.int/2025/09/29/science-hub-challenges-september-2025/) organised and hosted by ESA's ESRIN, using data from [EarthCARE satellite](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/EarthCARE),  an ESA-JAXA joint mission, which was processed via the [MAAP platform](https://portal.maap.eo.esa.int/biomass/), by students from the following organizations:*



<p align="center">
  <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/images.png?raw=true" alt="Ca' Foscari" height="80" style="margin: 0 15px;"/>
  <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-2/cafoscari.png?raw=true" alt="NOC" height="80" style="margin: 0 15px;"/>
  <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/logo-isac-CNR-nuovo.png?raw=true" alt="BAS" height="80" style="margin: 0 15px;"/>
</p>



## Aerosols and clouds belong together

Some clouds would not exist without aerosols, tiny particles that act as nuclei for cloud droplet formation. As air parcels rise through the troposphere, they cool, carrying water vapor that condenses around hygroscopic aerosol particles once temperatures drop enough. These particles, called Cloud Condensation Nuclei (CCN), enable liquid cloud droplets to form.

<div style="text-align: center;">
    <img src="
https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/clouds_ccns.png?raw=true " width="500"/>
    <p><b>Figure 1: CCNs </b> Schematic representation of how liquid cloud droplets form with the help of aerosol particles.</p>
</div>

Some aerosols help form ice crystals instead, acting as Ice **Nucleating Particles (INPs)**, common at higher, colder altitudes. Depending on whether droplets are liquid, ice, or both, clouds are classified as liquid, ice, or mixed-phase. Natural aerosols include sea salt, volcanic sulfates, and desert dust, while anthropogenic aerosols arise from pollution and biomass burning. 

<img src="https://upload.wikimedia.org/wikipedia/commons/3/39/Ice_Nucleation_Mechanisms.png?20141019054030" width="600" style="display:block; margin:auto;"/> <p style="text-align:center;"><b>Figure 2: INPs</b> Various ice nucleation mechanisms in the atmosphere or modes of ice formation in clouds.</p>

Because aerosols influence droplet formation, they also affect cloud structure and behavior. For instance, more CCNs create numerous smaller droplets, increasing cloud reflectivity: **the Twomey effect**. By altering droplet number, phase, and thickness, aerosols modify how clouds reflect sunlight and trap heat, playing a key role in how clouds either amplify or mitigate global warming.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Representation_of_the_direct_and_first_indirect_effect_of_aerosols_on_the_albedo_of_clouds.png/1200px-Representation_of_the_direct_and_first_indirect_effect_of_aerosols_on_the_albedo_of_clouds.png?20191119202505" width="600" style="display:block; margin:auto;"/> <p style="text-align:center;"><b>Figure 3: Aerosols radiative effects.</b>  Aerosols particles can change the way the radiation is reflected and reemited themselves, this is called a direct effect. They can also modify the size and amount of particles that a cloud is made of, consecuently changing how much cradiation is reflected by the cloud. This is an indirect effect from the aerosols.</p>

<img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2024/05/clouds_in_the_climate_system/26088977-1-eng-GB/Clouds_in_the_climate_system_article.png" width="600" style="display:block; margin:auto;"/> <p style="text-align:center;"><b>Figure 4: Cloud radiative effects.</b>  The amount of clouds, their height in the atmosphere and their thickness are fundamental variables that determine how they interact with the incomming and outgoing radiation. </p>

## Challenge
We cannot continuously sample cloud droplets and aerosols directly within clouds, so researchers use several remote methods to study them. You might wonder: how did we understand clouds before satellites, and how can satellites detect such tiny particles?

Our first tool was and remains theory. Physics helps predict how clouds behave and interact with aerosols. Over time, scientists developed equations to describe these processes, later enhanced by computational models that simulate thousands of atmospheric equations. Though simplified, these models reveal valuable insights into cloud–aerosol interactions. To verify models, we rely on observations. In the lab, scientists study ice crystal growth or simulate clouds in controlled conditions. Aircraft equipped with specialized instruments can collect samples and measure properties in real time, but these missions are costly and limited. Satellites, on the other hand, provide continuous, global coverage that complements models, lab work, and field campaigns. Together, these tools offer a more complete picture of this complex system, helping us improve weather and climate predictions in a warming world.
## Objective

The objective of this study is to explore whether and how aerosols influence cloud characteristics: specifically the distribution of liquid water and ice content, at various altitudes using EarthCare’s vertical profiling capabilities. To this end, **EarthCare**,  a mission realised through a joint venture between the [European Space Agency (ESA)](esa.int) and the [Japan Aerospace Exploration Agency (JAXA)](https://global.jaxa.jp/), was used to identifying patterns in cloud-aerosol interactions across different regions and conditions (e.g. land vs. ocean, tropical vs. polar environments), and determining whether increased CCN or INP concentrations correlate with observable changes in cloud composition.


<div style="text-align: center;"> <img src="https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2024/01/earthcare_over_desert_dust/25391626-1-eng-GB/EarthCARE_over_desert_dust_pillars.png" width="800"/> <p><b>Figure 5.</b> EarthCare Satellite (source: ESA).</p> </div>

#### Why EarthCare? 

EarthCARE is a first-of-its-kind mission that offers an unlikely opportunity to understand the complexity of cloud changes using a single satellite. What makes EarthCARE special is its four instruments working together to study clouds, aerosols, and radiation in detail.


* **ATLID (Atmospheric Lidar)** uses laser pulses to detect aerosols and thin cloud layers by measuring how light scatters back from particles, providing high-resolution profiles that improve on previous lidar missions like CALIPSO.
* **CPR (Cloud Profiling Radar)** can "see" across the clouds with radar signals to measure their vertical structure and water content, adding the capability to  capture cloud motion and the speed of precipitation. This imporves the previous mission called CloudSat .
* **MSI (Multi-Spectral Imager)** delivers multi-wavelength images in 7 different bands that reveal cloud structure and aerosol distribution over large areas, complementing [MODIS](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/modis/) with higher spatial resolution. The product resolution of MODIS is 250m/500/1km, while the MSI is 500m. 
* **BBR (Broadband Radiometer)** measures solar and thermal radiation reflected and emitted by Earth, enabling direct estimates of top-of-atmosphere radiative effects and energy balance. 

<div style="text-align: center;"> <img src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/team1-earthcare-sensors-image.png?raw=true" width="800"/> <p><b>Figure 6.</b> EarthCare Satellite (source: ESA).</p> </div>

Together, these instruments provide comprehensive and blended data that will help us explore interactions and uncover new insights into how clouds and aerosols influence climate.

## Use cases
In the latest ESA challenge workshop, we set out to explore the clouds and aerosols at three different locations with quite special characteristics. 
The first region lies just north of the Equator and stretches West to East across the Pacific Ocean. It's called the call the Inter-Tropical Convergence Zone (ITCZ) and it is characterized by persistent clouds with high and icy tops. The second region is in Antartica, the Southern Ocean. Here the conditions are quite different and clouds are lower, but because of the temperature these are mostly made of ice. 

<div style="text-align: center;">
    <img src="
https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/Globe1_pacific.png?raw=true  " width="500"/>
    <p><b>Figure 7: Locations to study. </b> The three locations of our study for the ESA challenge.</p>
</div>

1. **West Pacific**
The western ITCZ is very interesting because air raises in very strong updrafts (air moving upwards), mostly because the sea serface temperature is usually high. These updrafts and the clouds can form storms that can stir the ocean, lifting sea salt aerosols into the atmosphere. These are natural aerosols (non-anthropogenic). However, nearby regions such as Southeast Asia and China may contribute with anthropogenic aerosols derived from human activities, like pollution or industrial activity.

2.  **Eastern Pacific**  
This region typically experiences downdrafts, where air sinks rather than rises, as the sea temperature is usually lower than in the West. Yet, high clouds still form here. Being far from major population centers, we expect fewer aerosol sources. 

3.   **Southern Ocean** 
The atmospheric dynamics are quite particular in this region. Ice clouds form at much lower altitudes given the extremely low temperature of the atmosphere. However, there can also be some supercooled clouds at low altitudes. Aerosols might potentially be carried from far away, and influence cloud formation here. We mostly expect sea salt aerosols, but there could also be stratospheric aerosols, especially from volcanic eruptions.

Comparing these three very interesting regions with quite distinctive characteristics could give us a hint on whether the aerosols are influencing changes in the clouds. 
<div style="text-align: center;">
    <img src="
https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/Screenshot%20from%202025-11-06%2012-12-20.png?raw=true" width="500"/>
    <p><b>Figure 8:  The Walker circulation. </b> Normal Pacific conditions (Walker circulation) feature warm western waters with rising air and convection, and cool eastern waters with sinking air, producing east-to-west trade winds. Credit: [David Babb @ Penn State is licensed under CC-BY-NC-4.0](https://www.e-education.psu.edu/meteo3/node/2273).</p>
</div>



## Data and Methods
Two instruments (out of of the four) on-board of EarthCare, we used, which can provide a vertical profiliing of the atmosphere:
- **Cloud Profiling Radar (CPR)**: 94 GHz nadir-viewing radar with ~750m horizontal resolution and 500m vertical resolution, providing cloud structure and water content.
- **Atmospheric Lidar (ATLID)**: 354.8 nm nadir-viewing lidar with <30m horizontal resolution. The vertical resolution is 103m (below 20.2km altitude) and 500 m (above 20.2km altitude), detecting aerosols and thin clouds.

#### Dataset
The analysis used three primary EarthCARE data products:
- **CPR_CLD_2A**: Cloud variables including Liquid Water Path (LWP) and Ice Water Path (IWP), plus land/ocean flags
- **ATL_ALD_2A**: Aerosol Optical Thickness (AOT) at 355nm from lidar measurements
- **AC_TC_2A**: Synergistic radar-lidar target classification distinguishing cloud types and aerosol layers

Data coverage: Approximately 600-700 scenes from June-July and September 2025 (limited by early mission data availability). Analysis was conducted using the Multi-Mission Algorithm and Analysis Platform (MAAP).

#### Methodology workflow

The analysis followed a systematic processing pipeline:
* **1- Extract** all the data available for the areas we're interested in (600~700 scenes)
* **2- Resample** data by time at 1s temporal resolution
* **3- Merge** datasets(radar+lidar+synergetic) at 1 m temporal definition (AOT, L/IWP, Target classification)
* **4- Resample** at 1 minute temporal
* **5- Select** only the months for which all data is available: June-July, September 2025
* **5- Normalize** variables (x-min/max-min)
* **6 - Clustering** approach using simple **K-means** to understand centroids distance and relations between variables

The elbow metric was used to quantify the ideal amount of clusters for the data, which is 5 (where the "elbow" is).  Finally, the synergetic product provided insights on the types of clouds or aerosols that are grouped on each cluster.

The code was run at MAAP portal.

**Limitations**: Not all EarthCARE data products are yet available, and merging different instruments (particularly MSI with CPR and ATLID) remains challenging in early mission phases.

## Results
Although this was only an exploratory analysis, we can see some insights. 
The following plots show the clusters obtained in 2 dimensions, where each dimension is one of the variables we worked with. Each colour represents the cluster to which each data point has been classified to. The red crosses show the clusters' centroids. 
	
The first thing to notice is that, ovearall, the West Pacific classification is different than the East one. Taking a closer look at the IWP vs AOD plots, many of the points and especially the ones with higher value lie either in IWP=0 or AOT=0. This is expected as the Aerosols are measured with the lidar and, as stated previously, the thick clouds made of ice, therefore wtih high IWP, will make the lidar extinguished. However, there are some points that have a value different to 0 in both axis.

<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;">
    <img 
        src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/results1_team1.png?raw=true" 
        style="max-width: 100%; width: 800px; height: auto;"
        alt="Pacific region clusters"
    />
    <p style="text-align: center; font-size: 1.2em; margin-top: 10px;">
        <b>Figure 9: Clustering results in ITCZ</b> K-means clustering results for West Pacific (upper row) and East Pacific (bottom row).
    </p>
</div>

Taking a closer look at the West Pacific, there are some values in the space where the IWP>0.2 kgm-3, which is considerered a thick ice clouds, and AOT!= 0. Many of these points are classified as cluster 5 (brown dots) and 1 (blue dots). If we take a look at the LWP vs AOT plot, we see that most of the data points in cluster 5 have a lower LWP values compared to their IWP values. In cluster 1 instead, for the same AOD values, they have higher values of LWP. Finally, lookig at the LWP vs IWP plot, we confirm that cluster 5 data points are mostly thick clouds made of ice and cluster 1 points are mostly made of liquid water. 
In the East Pacific, we see similar distributions, although there are many more points and clusters where the LWP is higher than in the west. This means that there might be more liquid or mixed phase clouds, that can interact with aerosols, especially the sea salt. 

In Antartica, we clearly see a much more pristine environment. 
The first plot shows that there don't seem to be many links between the aerosols and the ice clouds, exept perhaps for one outlier that would need further research. 
The second and third plot show that there are not many liquid clouds. 

<div style="display: flex; flex-direction: column; align-items: center; margin: 40px 0;">
    <img 
        src="https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/results3_team1.png?raw=true" 
        style="max-width: 100%; width: 800px; height: auto;"
        alt="Spatial cluster distribution"
    />
    <p style="text-align: center; font-size: 1.2em; margin-top: 10px;">
        <b>Figure 10: Clustering results in Antartica. </b> Compared to the ITCZ results, we didn't find many aerosols.
    </p>
</div>


## Conclusions

This study demonstrates the capability of EarthCARE's integrated sensor suite to reveal relationships between aerosol properties and cloud microphysics across different climate regions.

We have tested the potential of EarthCARE to unveal the interactions between clouds and aerosols. 
Focusing on different areas were we know the clouds but where we are still exploring the distributions of aerosols was challenging, but thanks to EarthCare we were able to get insights on the links. 

The synergetic products makes it easier to interpret the possible links between differet types of clouds and different species of aerosols. We took a limited time period of data this time, but with the upcomming data and more statistical analysis, we'll be able to push the boundaries of this problem. 


## <!--{ as="div" }--> Open Science

| **Name**                                                                                                                                       | **Type**            | **Agency / Provider**                     | **Description / Usage**                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[EarthCARE Mission](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/EarthCARE)**                                        | Mission/Platform             | ESA/JAXA               | Earth Cloud, Aerosol and Radiation Explorer satellite providing integrated observations from Cloud Profiling Radar, Atmospheric Lidar, Multi-Spectral Imager, and Broad Band Radiometer.                            |
| **[CPR_CLD_2A Product](https://www.eoportal.org/satellite-missions/earthcare#sensor-complement)**                                                                                       | Dataset | ESA/JAXA                        | Cloud Profiling Radar Level 2A product providing cloud variables, Liquid Water Path (LWP), Ice Water Path (IWP), and land/ocean flags.                                     |
| **[ATL_ALD_2A Product](https://amt.copernicus.org/preprints/amt-2023-252/)**                                          | Dataset     | ESA/JAXA               | Atmospheric Lidar Level 2A product providing Aerosol Optical Thickness (AOT) at 355nm and aerosol layer properties.                                                     |
| **[AC_TC_2A Product](https://www.eoportal.org/satellite-missions/earthcare#sensor-complement)**                          | Dataset | ESA/JAXA | Synergistic radar-lidar target classification product distinguishing cloud types and aerosol layers.                                               |
| **[MAAP - Multi-Mission Algorithm and Analysis Platform](https://maap-project.org/)**                          | Platform | ESA/NASA | Cloud-based platform for processing and analyzing Earth observation data, used for EarthCARE data processing and clustering analysis.                                               |

#### Code Repository
Access the complete analysis code and notebooks on GitHub.
<iframe width="100%" height="600" src="https://github.com/giacom0rovers1/earthcare_aerosol_cloud_interactions" frameborder="0"></iframe>

#### References
- [Finney, D. L., et al. (2025). Microphysical fingerprints in anvil cloud albedo. *Journal of the Atmospheric Sciences*](https://egusphere.copernicus.org/preprints/2025/egusphere-2025-1227/)

- [Lorian, A., et al. (2023). Aerosol effects on deep convection: A review. *Atmospheric Research*.](https://doi.org/10.5194/acp-19-2601-2019)

- [Grabowski, W. W., and Morrison, H. (2016). Untangling microphysical impacts on deep convection applying a novel modeling methodology. *Journal of the Atmospheric Sciences*, 73(6), 2503-2524.](https://doi.org/10.1175/JAS-D-14-0307.1)

- [Heikenfeld, M., et al. (2019). Aerosol effects on deep convection: The propagation of aerosol perturbations through convective cloud microphysics. *Atmospheric Chemistry and Physics*, 19(4), 2601-2627.](https://doi.org/10.5194/acp-19-2601-2019)

- [Igel, A. L., and van den Heever, S. C. (2021). The relative influence of environmental characteristics on tropical deep convective morphology as observed by CloudSat. *Journal of Geophysical Research: Atmospheres*, 126(6).]( https://doi.org/10.1002/2014JD022690)

- [Mi, Jiaqin & Yang, Yuanjian & Zhou, Shuxue & Ma, Xiaoyan & Wei, Siying. (2024). Exploring impacts of aerosol on convective clouds using satellite remote sensing and machine learning. Journal of Applied Remote Sensing. 18. 10.1117/1.JRS.18.012007.](https://www.researchgate.net/publication/377380698_Exploring_impacts_of_aerosol_on_convective_clouds_using_satellite_remote_sensing_and_machine_learning)

- [AMT - Cloud top heights and aerosol layer properties from EarthCARE lidar observations](https://amt.copernicus.org/preprints/amt-2023-252/)

- [GMD - Estimation of aerosol and cloud radiative heating rate in the tropical stratosphere using a radiative kernel method](https://gmd.copernicus.org/)

- [Wildfires in Southeast Asia pollute the atmosphere in the northern South China Sea](https://www.sciencedirect.com/)

- [Copernicus - Wildfires 2025 review: ASEAN reduces emissions, but haze persists](https://atmosphere.copernicus.eu/)

####  Contributors
Filippo Calì Quaglia (Ca' Foscari University, Venice)


