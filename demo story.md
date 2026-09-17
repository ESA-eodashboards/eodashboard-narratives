# AI for air quality monitoring using Earth <!--{as="img" mode="hero" src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/f1f46716f8557709bf58b1e43426428d124d661f/assets/vittorez/prova-1789676182440.png" }-->
#### 

## Authors: Gianluca Flaminio¹, Nikolina Zallemi¹, Vittoria Rezzuto¹, and Thomas Xolias²
> ¹ Politecnico di Milano ² Aristotle University of Thessaloniki

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in 14-18 September 2026. It was developed by a team from Politecnico di Milano and Aristotle University of Thessaloniki.*

## 
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/it/archive/b/be/20260803144359%21Logo_Politecnico_Milano.png" alt="Politecnico di Milano" height="80" style="margin: 0 15px;"/>
  <img src="https://thumb.wikimedia.org/wikipedia/en/thumb/c/c8/ESA_Patch_2026.svg/1280px-ESA_Patch_2026.svg.png?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=thumbnail" alt="ESA" height="80" style="margin: 0 15px;"/>
  <img src="https://www.auth.gr/wp-content/uploads/banner-horizontal-black-en.png" alt="Aristotle University of Thessaloniki" height="80" style="margin: 0 15px;"/>
</p>

## Challenge
Exploring the Synergy Between Air Pollution and Urban Heat: Linking NO2, Land Surface Temperature, and Air Temperature

## Objective
Investigation of the spatial and temporal relationship between air pollution, LST from satellite, and near surface air temperature from ERA5. Quantify whether pollution hotspots systematically coincide with elevated LST/UHI patterns and assess how meteorology mediates this relationship.

## Analysed phenomena
The **Urban Heat Island** is the tendency of urban and suburban areas to sustain higher air and surface temperatures than the surrounding rural landscape. This effect results from the modification of the natural surface energy balance by urbanization rather than by regional climate. This phenomenon is always defined relative to a rural reference, with both a surface form (LST) and a canopy/air form (T air), which do not necessarily peak at the same time of day. The UHI is defined by the difference between the temperature in the countryside and the urban temperature.

**NO2** is a reactive trace gas produced mainly by combustion, vehicle traffic, industry, and heating.
Since NO2's lifetime is on the order of hours, its diurnal cycle is tightly linked to both traffic timing and boundary-layer dynamics.
Therefore the peaks of NO2 concentration are typically in the morning and in the late afternoon during traffic hours, and with shallow, stable boundary layer limiting dilution, and drop in the early afternoon, when higher solar radiation and a deeper boundary layer both dilute NO2 and accelerate its photochemical conversion to O3. This produces an inverse relationship between NO2 and O3 on short timescales and an opposite response to the same thermal driver.

## Earth observations <!--{ as="eox-map" mode="tour" position="left" }-->

### <!--{ zoom=3 center=[0,20] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### From Space
Looking at the Earth from a global perspective to observe atmospheric dynamics.

### <!--{ zoom=6 center=[-3.7,40.4] layers='[{"type":"Tile","properties":{"id":"s2cloudless"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2025_3857"}}]' animationOptions='{"duration":500}' }-->
#### Zooming into Spain
*"An exceptional heatwave is affecting countries across western Europe, with cities and regions of France, Spain and southern Italy experiencing unseasonal temperatures."*

"Europe feels the heat beneath our feet" - ESA, 25/06/2026

### <!--{ zoom=11 center=[-3.7038,40.4168] layers='[{"type":"Tile","properties":{"id":"terrain-light"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"terrain-light_3857"}},{"type":"Tile","properties":{"id":"osm-borders","opacity":0.8},"source":{"type":"XYZ","url":"https://tile.openstreetmap.org/{z}/{x}/{y}.png"}}]' animationOptions='{"duration":500}' }-->
#### Focusing on Madrid
*"Madrid’s urban centre has the most extreme urban heat island (UHI) “hot spot” of six major cities around the world, with temperatures 8.5°C hotter than rural surroundings, according to new research by global sustainable development consultancy, Arup."*

*"Within the survey area in Madrid, severe UHI hot spots meant researchers found 500,000 children and elderly people living with evening UHI heat spikes of 7°C or more."*

"Madrid suffers most extreme urban heat island "hot spot" – new international survey shows" - Arup, 16/08/2023

## Methods
### Data
**Temporal coverage:** January and July 2026

**Land Surface Temperature:** Sentinel-3

**NO2:** Sentinel-5P TROPOMI

**O3:** Sentinel-5P TROPOMI

**Air temperature:** ERA5
<div style="display: flex; gap: 10px; flex-wrap: wrap;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/f5846d22d1d8e72d52c5e1c12bda88eaf61fb31e/assets/vittorez/January2026DAYERA5points-1789664866675.png" style="width: 48%;"/>
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/ddc783ae88471643856a243fb22fb58fad9e77bd/assets/vittorez/January2026NIGHTERA5points-1789664698044.png" style="width: 48%;"/>
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/5ee7ca898d90bca05ae3b1bfd58ec020467d8747/assets/vittorez/July2026DAYERA5points-1789664734518.png" style="width: 48%;"/>
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/d166097551ceb3144b21b1136853b44a2ef3e9c5/assets/vittorez/July2026NIGHTERA5points-1789664798000.png" style="width: 48%;"/>
</div>

**NDVI:** 
<div style="display: flex; gap: 0px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/2d1c2767f70007ad2d25be452ce624631721eb74/assets/vittorez/ndvijanuary-1789657144484.png" style="width: 100%; object-fit: contain; aspect-ratio: 1/1;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/cfbf6ab1b282b802591491bf645fa2afcd336a25/assets/vittorez/ndvijuly-1789656529381.png" style="width: 130%; object-fit: contain; aspect-ratio: 1/1;" />
</div>

**DEM:**
![DEM.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/d2fd45aac11c10b636ef956b5767d87df4ec0934/assets/vittorez/DEM-1789656842797.png)


#### Methodology workflow
Description

## Results
#### Land Surface Temperature
<div style="display: flex; gap: 0px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/42843771e87e66c404bde5357140eed52e75edf1/assets/vittorez/January2026DAYLST-1789678227552.png" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c07c14130a7d689f23ec2735d89249a0d18ef49b/assets/vittorez/January2026NIGHTLST-1789678253754.png" />
</div>

<div style="display: flex; gap: 0px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/773bab750cd18172c33674ea83c4367ecff7aea8/assets/vittorez/July2026DAYLST-1789678287867.png" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c0fa57c306d500e1297f023f705224734828c03d/assets/vittorez/July2026NIGHTLST-1789678318314.png" />
</div>

#####
#### Nitrogen dioxide 
<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e75cffa4e129c6611205f50637e88eeda8aab387/assets/vittorez/January2026NO2DAYESRI-1789655589787.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/516f4965e19cbc50cb353c5b548e59aa7a344e21/assets/vittorez/January2026NO2NIGHTESRI-1789655678870.gif" style="width: 48%;" />
</div>

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e8d59e29b342c013cbe967e990b9c538246f36b4/assets/vittorez/July2026NO2DAYESRI-1789655733388.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/e9f4dacbb2e9ac5069bfe3b75f535e04825b9f6c/assets/vittorez/July2026NO2NIGHTESRI-1789656066047.gif" style="width: 48%;" />
</div>

<p align="center"><em>Visualizing the seasonal and diurnal shifts in NO2 concentrations for January and July.</em></p>

#### Ozone
<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/788bce10551db1393e418ee9e227e55207834387/assets/vittorez/January2026O3DAYESRI-1789674050098.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/4baf52f1123b4d21e0fd80f379cf8c9eb19b2c44/assets/vittorez/January2026O3NIGHTESRI-1789674110930.gif" style="width: 48%;" />
</div>

<div style="display: flex; gap: 10px;">
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/92083e76bf511d013515694d41d894666c32f74f/assets/vittorez/July2026O3DAYESRI-1789674453031.gif" style="width: 48%;" />
  <img src="https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/25ad7c43057f88d27f331bbf235b63431b6b2959/assets/vittorez/July2026O3NIGHTESRI-1789674407166.gif" style="width: 48%;" />
</div>

<p align="center"><em>Visualizing the seasonal and diurnal shifts in O3 concentrations for January and July.</em></p>


#### Air temperature
![January_2026_DAY_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/42b773597b70145ea3940828d26e4f286935757d/assets/vittorez/January2026DAYtemperaturetimeseries-1789665925063.png)

![January_2026_NIGHT_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/0ed1e6201a90d8dd0fd50eba66fbb287b5b9a0eb/assets/vittorez/January2026NIGHTtemperaturetimeseries-1789665960480.png)

![July_2026_DAY_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/fb8a6d73f45ae30a58240f68fdedf0f85c44c677/assets/vittorez/July2026DAYtemperaturetimeseries-1789665978602.png)

![July_2026_NIGHT_temperature_timeseries.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/2160595e7ef4c116aa6725291f1c3e77f51fe2ca/assets/vittorez/July2026NIGHTtemperaturetimeseries-1789666002145.png)


#### Air temperature, NO2, and O3 correlation
![January_2026_DAY_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/b92dcccfedc5f5bd8294c312db9346590d8afb8e/assets/vittorez/January2026DAYtemperatureNO2O3-1789665595806.png)

![January_2026_NIGHT_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/5f4a3180dda80702316cd740d213ee7a5612a19b/assets/vittorez/January2026NIGHTtemperatureNO2O3-1789665623159.png)

![July_2026_DAY_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/c62611a1d7f80f0483996e0a6888a2a06ee7be77/assets/vittorez/July2026DAYtemperatureNO2O3-1789665645694.png)

![July_2026_NIGHT_temperature_NO2_O3.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/a364361583f954148f83f25bd6d0e2e19f31f984/assets/vittorez/July2026NIGHTtemperatureNO2O3-1789665686005.png)

### 



#### Discussion 

**THE FOLLOWING PART COULD BE USED TO INTERPRETE OUR RESULTS :)**

Winter: stronger temperature inversions and shallower, more stable boundary layers trap NO2 near the surface, while UHI intensity (especially in its air/canopy form) is comparatively weaker. 

Summer: UHI is strongest, particularly at night, while NO2's photochemical consumption is fastest, partly offsetting emission-driven increases, but LST-NO2 spatial correlation is empirically stronger in summer than in winter, since both fields are driven by the same underlying urban density even as their diurnal magnitudes diverge.

RICORDIAMOCI CHE è UN'ANALISI CON LE SUE FRAGILITÀ NON ESAUSTIVA, QUINDI ANDREBBERO CONSIDERATI PIÙ ANNI, PIÙ DATI E BLABLA

## Conclusions


## Future steps
![NO2_monthly_mean_January_Madrid_basemap.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/69b2e365e0a428dc44bc6bf15925979d461d5d3b/assets/vittorez/NO2monthlymeanJanuaryMadridbasemap-1789681325763.png)

![NO2_monthly_mean_July_Madrid_basemap.png](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/37836ecd478826b07659615a1d502ab8e7795ee5/assets/vittorez/NO2monthlymeanJulyMadridbasemap-1789681342550.png)

## Open Science


## References
1. Weng, Q., Yang, S. Urban Air Pollution Patterns, Land Use, and Thermal Landscape: An Examination of the Linkage Using GIS. Environ Monit Assess 117, 463–489 (2006). https://doi.org/10.1007/s10661-006-0888-9
2. Kamyar Fuladlu, Haşim Altan, Examining land surface temperature and relations with the major air pollutants: A remote sensing research in case of Tehran, Urban Climate, Volume 39, 2021, 100958, ISSN 2212-0955. https://doi.org/10.1016/j.uclim.2021.100958.
3. Goldberg, D. L., Anenberg, S. C., Kerr, G. H., Mohegh, A., Lu, Z., & Streets, D. G. (2021). TROPOMI NO2 in the United States: A detailed look at the annual averages, weekly cycles, effects of temperature, and correlation with surface NO2 concentrations. Earth's Future, 9, e2020EF001665. https://doi.org/10.1029/2020EF001665
4. Guo, Y., Unger, J., Khabibolla, A. et al. Modeling urban air temperature using satellite-derived surface temperature, meteorological data, and local climate zone pattern—a case study in Szeged, Hungary. Theor Appl Climatol 155, 3841–3859 (2024). https://doi.org/10.1007/s00704-024-04852-7
5. Shen, P., Wang, M., Ma, H. et al. On the two-way interactions of urban thermal environment and air pollution: A review of synergies for identifying climate-resilient mitigation strategies. Build. Simul. 18, 259–279 (2025). https://doi.org/10.1007/s12273-024-1210-x
6. "Europe feels the heat beneath our feet". https://www.esa.int/ESA_Multimedia/Images/2026/06/Europe_feels_the_heat_beneath_our_feet 
7. "Madrid suffers most extreme urban heat island "hot spot" – new international survey shows". https://www.arup.com/news/madrid-suffers-most-extreme-urban-heat-island-hot-spot--new-international-survey-shows/

## Contributors
Authors, contibutors, reviewers