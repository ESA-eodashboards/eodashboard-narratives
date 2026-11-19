# Drivers of tree mortality <!--{ as="img" mode="hero" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoQjsfbD7h_AsxjQTRhWyIqKCHuItJhqu-SjN7Rq2NZ492SPlzK3cRgls&s=10" }-->
#### 

## Authors:
> ¹ Anna Bartels ² Daria Ilina  ³ Elias Gmeiner

*This story is based on results from the Science Hub Challenges organised and hosted by ESA's ESRIN Science Hub in november 2026. It was developed by a team from the TU Vienna and Ruhr Universtiy Bochum.

## 
<p align="center">
  <p align="center">
  <img src="https://www.tuwien.at/index.php?eID=dumpFile&t=p&p=2420997&token=03c096e7a1c6df6c14c7e374869b07ce2d99852f" width="200" />
  <img src="https://services.ruhr-uni-bochum.de/sites/services.ruhr-uni-bochum.de/files/styles/991x660px/public/2023-10/logo_rub_blau.png.webp?h=d95abdc4&itok=EIQbKx4O" width="200" />
</p>

## Challenge
Which environmental factors explain observed tree mortality across Europe?

Climate change is reshaping the vegetation structure and dynamics. These transformations are already measurable across the globe (IPCC 2013; Neumann et al. 2017). For the upcoming time, further significant changes are expected regarding the range and distribution of species.

In Central Europe, forests have already experienced an increase in the frequency and intensity of tree mortality. These effects are primarily driven by recurring extreme droughts and compounding biotic stressors, which exceed the adaptive capacities of long-lived species (Seidl et al. 2017).

The increasing mortality rate threatens the resilience of forests in Europe and challenges the sustainable provision of essential ecosystem services to society (Neumann et al. 2017).

Additionally, tree mortality is a crucial factor as it can trigger irreversible changes in forest communities by pushing ecosystems past critical ecological thresholds (Scheffer et al. 2012). Addressing this vulnerability requires a large-scale understanding of the climatic factors causing tree mortality to identify potential changes before critical tipping points are reached.

## Objective
The objective of this study was to


</p>



## Data and Methods

All the data was spacialy matched to 0.25 degrees of cell size.
If a 0.25 cell has more than 30% of forest we keep it as a forest pixel.
#### Dataset
- **Source**: 
- **Temporal coverage**: 


<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="text-align:center; border:1px solid #ccc; padding:6px;">Datacube name</th>
      <th style="text-align:center; border:1px solid #ccc; padding:6px;">Variable name</th>
      <th style="text-align:left; border:1px solid #ccc; padding:6px;">Description</th>
      <th style="text-align:center; border:1px solid #ccc; padding:6px;">Reference*</th>
      <th style="text-align:center; border:1px solid #ccc; padding:6px;">Region</th>
      <th style="text-align:center; border:1px solid #ccc; padding:6px;">Time range</th>
      <th style="text-align:center; border:1px solid #ccc; padding:6px;">Resolution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">deadtrees.earth v5</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">tree_mortality_fraction</td>
      <td style="text-align:left; border:1px solid #ccc; padding:6px;">Ratio of standing deadwood cover to total tree cover. Both layers were aggregated separately using area-averaged resampling (Resampling.average), with invalid pixels masked, before calculating the ratio. Mean mortality fraction calculated over the period.</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;"><a href="https://deadtrees.earth/" target="_blank">deadtrees.earth</a></td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">Study area</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">2019–2022</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">10 m (input); 0.25° (output), EPSG:3035 input, pyramid level 7 (1.28 km)</td>
    </tr>
    <tr>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">air_temperature</td>
      <td style="text-align:left; border:1px solid #ccc; padding:6px;">Mean summer air temperature (June–August), representing heat exposure during the drought period. No resampling required, as the dataset is already available at the target grid resolution.</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">Study area</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">2018–2021</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">0.25°, 8-day</td>
    </tr>
    <tr>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">surface_moisture</td>
      <td style="text-align:left; border:1px solid #ccc; padding:6px;">Mean summer surface moisture (June–August), representing water availability during the drought period.</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">Study area</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">2018–2021</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">0.25°, 8-day</td>
    </tr>
    <tr>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">root_zone_moisture</td>
      <td style="text-align:left; border:1px solid #ccc; padding:6px;">Mean summer root-zone soil moisture (June–August), representing water availability in the soil layer accessible to tree roots.</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">Study area</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">2018–2021</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">0.25°, 8-day</td>
    </tr>
    <tr>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">evaporative_stress</td>
      <td style="text-align:left; border:1px solid #ccc; padding:6px;">Mean summer evaporative stress (June–August), indicating the degree to which water availability limits evapotranspiration and reflects plant water stress.</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">Study area</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">2018–2021</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">0.25°, 8-day</td>
    </tr>
    <tr>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">kNDVI</td>
      <td style="text-align:left; border:1px solid #ccc; padding:6px;">Mean summer kernel Normalized Difference Vegetation Index (June–August), representing vegetation greenness and vigor during the drought period.</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">Study area</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">2018–2021</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">0.25°, 8-day</td>
    </tr>
    <tr>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">gpp_2017</td>
      <td style="text-align:left; border:1px solid #ccc; padding:6px;">Mean summer Gross Primary Productivity (June–August) for 2017, used as a pre-drought productivity baseline to avoid potential circularity associated with reduced productivity following tree mortality.</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESDC</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">Study area</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">2017</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">0.25°, 8-day</td>
    </tr>
    <tr>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESA CCI Land Cover 2018</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">forest_fraction</td>
      <td style="text-align:left; border:1px solid #ccc; padding:6px;">Fraction of each grid cell covered by forest. Forest classes (50–90) were assigned a value of 1 and all other classes 0, followed by area-averaged aggregation to 0.25°. Used both to define the forest mask (≥ 0.3) and as a measure of forest cover.</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;"><a href="https://climate.esa.int/en/projects/land-cover/" target="_blank">ESA Climate Change Initiative – Land Cover</a></td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">Study area</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">2018</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">300 m (input); 0.25° (output)</td>
    </tr>
    <tr>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">ESA CCI Land Cover 2018</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">needleleaf_fraction</td>
      <td style="text-align:left; border:1px solid #ccc; padding:6px;">Fraction of each grid cell covered by needleleaf forest. Needleleaf classes (70–72, 80–82) were assigned a value of 1 and all other classes 0, followed by area-averaged aggregation to 0.25°. Used as a proxy for spruce abundance, the main host of bark beetles.</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;"><a href="https://climate.esa.int/en/projects/land-cover/" target="_blank">ESA Climate Change Initiative – Land Cover</a></td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">Study area</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">2018</td>
      <td style="text-align:center; border:1px solid #ccc; padding:6px;">300 m (input); 0.25° (output)</td>
    </tr>
  </tbody>
</table>

#### Methodology workflow
Description

## Results
## Tree mortality <!--{ as="eox-map" mode="tour" }-->

### Germany <!--{ layers='[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Vector","properties":{"id":"mortality_cells","title":"Tree mortality fraction"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/egmeiner/eodashboard-narratives/egmeiner/tree-mortality/assets/egmeiner/treemortalitycells-1795012656467.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","mortality"],0.05,"rgba(255,255,204,0.75)",0.1,"rgba(254,204,92,0.75)",0.15,"rgba(253,141,60,0.75)",0.2,"rgba(189,0,38,0.75)"],"stroke-width":0}},{"type":"Vector","properties":{"id":"country-borders","title":"Country borders"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson","format":"GeoJSON"},"style":{"stroke-color":"#111111","stroke-width":1.5,"fill-color":"rgba(0,0,0,0)"}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]' zoom=5.5 center=[10.4,51.1] projection="" animationOptions={duration:1500}}-->

Germany

### Austria <!--{ layers='[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Vector","properties":{"id":"mortality_cells","title":"Tree mortality fraction"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/egmeiner/eodashboard-narratives/egmeiner/tree-mortality/assets/egmeiner/treemortalitycells-1795012656467.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","mortality"],0.05,"rgba(255,255,204,0.75)",0.1,"rgba(254,204,92,0.75)",0.15,"rgba(253,141,60,0.75)",0.2,"rgba(189,0,38,0.75)"],"stroke-width":0}},{"type":"Vector","properties":{"id":"country-borders","title":"Country borders"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson","format":"GeoJSON"},"style":{"stroke-color":"#111111","stroke-width":1.5,"fill-color":"rgba(0,0,0,0)"}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]' zoom=7 center=[14.5,47.6] projection="" animationOptions={duration:1500}}-->

![Bark beetle damage over time](https://raw.githubusercontent.com/egmeiner/eodashboard-narratives/egmeiner/tree-mortality/assets/egmeiner/gifprecipitation-1795078503562.gif)

Austria

### Poland <!--{ layers='[{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}},{"type":"Vector","properties":{"id":"mortality_cells","title":"Tree mortality fraction"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/egmeiner/eodashboard-narratives/egmeiner/tree-mortality/assets/egmeiner/treemortalitycells-1795012656467.geojson","format":"GeoJSON"},"style":{"fill-color":["interpolate",["linear"],["get","mortality"],0.05,"rgba(255,255,204,0.75)",0.1,"rgba(254,204,92,0.75)",0.15,"rgba(253,141,60,0.75)",0.2,"rgba(189,0,38,0.75)"],"stroke-width":0}},{"type":"Vector","properties":{"id":"country-borders","title":"Country borders"},"source":{"type":"Vector","url":"https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson","format":"GeoJSON"},"style":{"stroke-color":"#111111","stroke-width":1.5,"fill-color":"rgba(0,0,0,0)"}},{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]' zoom=5.8 center=[19.1,52.1] projection="" animationOptions={duration:1500}}-->

Poland

## Conclusions


## Open Science <!--{ as="div" component="div" }-->

## Contributors
Authors, contibutors, reviewers[tree_mortality_cells.geojson](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/0a170e04d6f36168a9572b25a46c5bf19a9776d7/assets/egmeiner/treemortalitycells-1795012656467.geojson)![gif_precipitation.gif](https://raw.githubusercontent.com/ESA-eodashboards/eodashboard-narratives/f623ecd3ca12aef22b97d680c873877412a66f98/assets/egmeiner/gifprecipitation-1795078503562.gif)