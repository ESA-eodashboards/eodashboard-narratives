---
cover-image: https://placehold.co/600x400/png
date: 2026-03-25
theme: atmosphere
tags: GHG, CH4
official: true
collections: collectionIdentifier1, collectionIdentifier2

---

# Monitoring the Greenhouse Gases from Space: the Carbon Budget <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
How satellites track CO₂, CH₄ and N₂O and what they tell us about the planet <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## <!--{ nav="false" }-->
<div align="center">

*This trilateral story, produced in collaboration by the [European Space Agency (ESA)](https://www.esa.int), the [National Aeronautics and Space Administration (NASA)](https://www.nasa.gov/), and the [Japan Aerospace Exploration Agency (JAXA)](https://global.jaxa.jp/), is part of the joint narratives featured on [EO Dashboard](https://eodashboard.org/), showcasing the power of open Earth observation data.*

</div>


  ## <!--{ nav="false" }-->
<p align="center">
  <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/logos/esa.jpg" alt="ESA" height="80" style="margin: 0 15px;"/>
  <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/logos/nasa.jpeg" alt="NASA" height="80" style="margin: 0 15px;"/>
  <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/refs/heads/main/logos/jaxa.jpeg" alt="JAXA" height="80" style="margin: 0 15px;"/>
</p>

## Greenhouse gases (GHG) and carbon budget


Human activities have fundamentally altered the composition of Earth's atmosphere. Since the Industrial Revolution, concentrations of the three most important long-lived greenhouse gases — carbon dioxide (CO₂), methane (CH₄), and nitrous oxide (N₂O) — have risen sharply, driving global warming and threatening the stability of the Earth's climate system.
From their vantage point in orbit, satellites offer a unique and powerful tool: the ability to observe these gases across the entire globe, continuously, and with growing precision. The ESA Climate Change Initiative (CCI) has been generating long-term, satellite-derived records of these Essential Climate Variables (ECVs) since 2010. Together with the RECCAP-2 project, these datasets are being used to constrain regional carbon budgets, identify emission hotspots, and support international climate policy.
This story takes you through each of the three gases in turn, what satellites measure, what the science tells us, and why it matters for the planet's future.

## Earth observation of GHG

# Part 1: CO₂ — The Dominant Driver <!--{ as="img" mode="hero" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Mauna_Loa_Observatory_-_Flickr_-_NOAA_Photo_Library.jpg/1280px-Mauna_Loa_Observatory_-_Flickr_-_NOAA_Photo_Library.jpg" }-->
### Carbon dioxide: measuring the pulse of the carbon cycle <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->
 
#
Carbon dioxide is the **single largest contributor to human-caused global warming**, responsible for around two-thirds of the increase in radiative forcing since pre-industrial times. Despite decades of international climate agreements, atmospheric CO₂ continues to rise at approximately **2 ppm per year**, driven primarily by fossil fuel combustion and deforestation.
 
Yet our understanding of exactly *where* CO₂ is being emitted and absorbed remains incomplete. Satellites offer a critical complement to ground-based monitoring networks — measuring the column-averaged concentration of CO₂ from space across regions where in-situ observations are sparse or absent.
 
## Global CO₂ from Space <!--{ as="eox-map" mode="tour" }-->
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="2.5" center=[0,20] projection="" animationOptions={duration:500}}-->
 
#### Measuring XCO₂ from Orbit
The key variable retrieved by satellites is **XCO₂** — the column-averaged dry-air mole fraction of CO₂, expressed in parts per million (ppm). This represents the average concentration of CO₂ through the entire atmospheric column, from the surface to the top of the atmosphere.
 
The ESA GHG-CCI programme has produced XCO₂ records from multiple satellite sensors:
- **SCIAMACHY/ENVISAT** (2002–2012)
- **TANSO-FTS/GOSAT** (2009–present)
- **OCO-2** (2014–present), retrieved using the FOCAL algorithm
 
The latest **CRDP9** data package provides XCO₂ from OCO-2 (v11) covering September 2014 to December 2023, and from GOSAT-2 (v2.0.3) covering February 2019 to December 2023.
 
<center>
<img src="https://climate.esa.int/media/images/GHG-CCI_XCO2_global_2019.width-1200.jpg" width="500">
<span style="font-size:15px;">Global XCO₂ distribution from ESA GHG-CCI. Credit: ESA CCI</span>
</center>
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="3.5" center=[0,50] projection="" animationOptions={duration:500}}-->
 
#### The Breathing Planet: Seasonal Cycle
One of the most striking features visible in XCO₂ data is the **seasonal cycle** of the Northern Hemisphere. Every summer, as land vegetation draws down CO₂ through photosynthesis, concentrations dip. Every winter, as respiration and decomposition dominate, they rise again. This is the planet breathing.
 
Satellites have extended our ability to observe this cycle in **unprecedented spatial detail**, revealing how different ecosystems — boreal forests, tropical rainforests, agricultural lands — contribute to the global carbon balance.
 
<center>
<img src="https://climate.esa.int/media/images/GHG_seasonal.width-1200.jpg" width="500">
<span style="font-size:15px;">The seasonal cycle of XCO₂ as seen from space. Credit: ESA CCI</span>
</center>
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="3.0" center=[10,48] projection="" animationOptions={duration:500}}-->
 
#### CO₂ and the Global Stocktake
The **RECCAP-2** project used CCI XCO₂ data within atmospheric inversion frameworks to produce top-down estimates of regional CO₂ fluxes — and compared them with countries' official UNFCCC reports.
 
A key finding: the **global land carbon sink**, estimated by absorbing around 1.4 billion tonnes of carbon per year through observations, was found to be **several times larger** than the sum obtained by adding up individual countries' nationally reported figures. This discrepancy highlights the critical role of satellite data in independently verifying carbon budgets and informing the Paris Agreement's global stocktake process.
 
<center>
<img src="https://climate.esa.int/media/images/RECCAP2_CO2_flux.width-1200.jpg" width="500">
<span style="font-size:15px;">Regional CO₂ flux estimates from RECCAP-2. Credit: ESA CCI / RECCAP-2</span>
</center>
 
---
 
# Part 2: CH₄ — The Potent Intruder <!--{ as="img" mode="hero" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Methane_emissions.jpg/1280px-Methane_emissions.jpg" }-->
### Methane: a shorter lifetime, but a far greater warming punch <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->
 
#
Methane is the **second most important anthropogenic greenhouse gas** after CO₂. Over a 20-year timescale, it is more than **80 times more potent** as a warming agent. Atmospheric CH₄ remained relatively stable between roughly 2000 and 2006, but has been rising steeply again since then — a trend that continues to puzzle scientists and concern policymakers.
 
Methane's sources are diverse: wetlands, rice cultivation, livestock, landfills, and — critically — fossil fuel extraction and distribution. Because CH₄ has a relatively short atmospheric lifetime of around 12 years (compared to centuries for CO₂), rapid reductions in emissions could have a **near-term climate benefit**, making it a priority target for the Global Methane Pledge.
 
## Global CH₄ from Space <!--{ as="eox-map" mode="tour" }-->
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="2.5" center=[40,20] projection="" animationOptions={duration:500}}-->
 
#### Measuring XCH₄ from Orbit
Like CO₂, the primary satellite-derived variable is **XCH₄** — the column-averaged dry-air mole fraction of methane, expressed in parts per billion (ppb).
 
The ESA GHG-CCI+ programme currently provides XCH₄ from:
- **Sentinel-5P / TROPOMI**, retrieved using the WFMD algorithm (v1.8), covering November 2017 to December 2023 — the highest spatial resolution XCH₄ product to date (~5.5 × 3.5 km)
- **GOSAT-2**, retrieved using SRON's RemoTeC Full Physics (SRFP) and Proxy (SRPR) algorithms, covering February 2019 to December 2023
 
The combination of these records with earlier SCIAMACHY and GOSAT data creates a time series extending back to **2002**, enabling trend analysis spanning more than two decades.
 
<center>
<img src="https://climate.esa.int/media/images/GHG-CCI_XCH4_TROPOMI.width-1200.jpg" width="500">
<span style="font-size:15px;">Global XCH₄ from Sentinel-5P/TROPOMI (ESA GHG-CCI+). Credit: ESA CCI</span>
</center>
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="4.0" center=[55,40] projection="" animationOptions={duration:500}}-->
 
#### Hotspot Detection: Where is Methane Coming From?
One of the most compelling applications of high-resolution XCH₄ data is the detection of **emission hotspots** — localised areas of intense methane release that are often invisible to surface monitoring networks.
 
TROPOMI data has enabled the identification of large point sources from oil and gas infrastructure, coal mines, and agricultural operations across Central Asia, the Middle East, and beyond. A fast data-driven method developed within the GHG-CCI framework allows these hotspot emissions to be **quantified from the satellite signal alone**.
 
<center>
<img src="https://climate.esa.int/media/images/CH4_hotspot.width-1200.jpg" width="500">
<span style="font-size:15px;">CH₄ emission hotspot detected by TROPOMI. Credit: ESA CCI</span>
</center>
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="3.5" center=[55,30] projection="" animationOptions={duration:500}}-->
 
#### Underreported: What RECCAP-2 Found
A striking finding from the RECCAP-2 project concerns the **gap between satellite-derived methane estimates and countries' official reports**. Atmospheric inversion modelling using CCI XCH₄ data found that methane emissions from oil- and gas-extracting states in Central Asia and the Gulf region were **several times higher** than officially reported to the UNFCCC.
 
This is not merely an accounting discrepancy — it has direct implications for climate mitigation policy and the credibility of the Global Methane Pledge, which aims to reduce methane emissions by 30% by 2030. Independent satellite monitoring provides an essential cross-check on national inventory data.
 
<center>
<img src="https://climate.esa.int/media/images/RECCAP2_CH4_Gulf.width-1200.jpg" width="500">
<span style="font-size:15px;">Observed vs. reported CH₄ emissions from the fossil fuel sector. Credit: ESA CCI / RECCAP-2</span>
</center>
 
---
 
# Part 3: N₂O — The Overlooked Gas <!--{ as="img" mode="hero" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Agriculture_day.jpg/1280px-Agriculture_day.jpg" }-->
### Nitrous oxide: the third greenhouse gas, and the most undermonitored <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->
 
#
Nitrous oxide is often overshadowed by CO₂ and CH₄ in public and policy discussions — yet it is the **third most important long-lived greenhouse gas**, and it plays a dual role: it is both a powerful warming agent (approximately 265 times more potent than CO₂ over 100 years) and the dominant source of **ozone-depleting substances** in the stratosphere today.
 
N₂O emissions are closely tied to agriculture — particularly the use of nitrogen-based fertilizers — as well as to livestock, biomass burning, and certain industrial processes. Together with other "other long-lived greenhouse gases" (OLLGHGs) such as SF₆ and CFCs, N₂O accounts for **nearly 20% of the total increase in radiative forcing** since pre-industrial times.
 
Despite its significance, satellite-based monitoring of N₂O remains less mature than for CO₂ and CH₄. This is the frontier that ESA's newest CCI activities — including the **LOLIPOP project** — are now working to advance.
 
## Global N₂O from Space <!--{ as="eox-map" mode="tour" }-->
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="2.5" center=[0,20] projection="" animationOptions={duration:500}}-->
 
#### Measuring N₂O from Orbit
Unlike CO₂ and CH₄, N₂O does not yet have a dedicated near-surface-sensitive column retrieval product within the GHG-CCI mainstream suite. Current satellite-based N₂O observations focus primarily on **stratospheric and upper tropospheric profiles**, retrieved from instruments such as:
 
- **MIPAS/ENVISAT** — mid-infrared limb emission sounder (2002–2012)
- **IASI/MetOp** — thermal infrared nadir sounder, providing tropospheric and stratospheric N₂O profiles (2006–present)
- **SCIAMACHY/ENVISAT** — also provided N₂O column information in solar occultation mode
 
The ESA CCI **LOLIPOP project** (LOng-LIved greenhouse gas PrOducts Performances), led by CNR-ISAC in Italy, is currently assessing the quality and usability of these datasets for climate modelling and inventory support.
 
<center>
<img src="https://climate.esa.int/media/images/N2O_global.width-1200.jpg" width="500">
<span style="font-size:15px;">N₂O distribution from satellite observations. Credit: ESA CCI / LOLIPOP</span>
</center>
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="3.5" center=[10,48] projection="" animationOptions={duration:500}}-->
 
#### Agriculture: The Dominant Source
Globally, **agriculture accounts for approximately 70% of anthropogenic N₂O emissions**, predominantly through the application of synthetic and organic nitrogen fertilizers to soils. Europe provides a well-studied case: a comprehensive synthesis study within RECCAP-2 found that agricultural activities represented the largest single source of N₂O across EU27 + UK, with rivers, lakes, and inland waters adding a further contribution through nitrogen leaching and runoff.
 
Satellite observations, while not yet providing the same near-surface sensitivity for N₂O as for CO₂ and CH₄, are being used in combination with atmospheric inversion models to **constrain regional N₂O budgets** and identify areas where emissions may be larger than inventories suggest.
 
<center>
<img src="https://images.pexels.com/photos/2132180/pexels-photo-2132180.jpeg" width="500">
<span style="font-size:15px;">Agricultural fields — the dominant source of N₂O emissions. Photo: Pexels (CC0)</span>
</center>
 
### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain Light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857"}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857"}}]}]' zoom="2.5" center=[0,20] projection="" animationOptions={duration:500}}-->
 
#### The Road Ahead: LOLIPOP and Future Products
The LOLIPOP project held its first major user workshop in Bologna, Italy in November 2025, bringing together instrument teams, modellers, and inventory compilers to chart the path forward for N₂O satellite products.
 
Key priorities identified include: evaluating user requirements for N₂O data accuracy; assessing how well current IASI and MIPAS products meet application needs; and exploring the potential of **future sensors** — including instruments on the upcoming Metop-SG satellite — to deliver improved near-surface N₂O observations.
 
The ambition is clear: to bring N₂O monitoring to the same level of maturity as CO₂ and CH₄, enabling a truly **three-gas satellite constraint** on the global greenhouse gas budget in support of the Paris Agreement.
 
<center>
<img src="https://climate.esa.int/media/images/LOLIPOP_workshop.width-1200.jpg" width="500">
<span style="font-size:15px;">LOLIPOP user workshop, Bologna, November 2025. Credit: ESA CCI / LOLIPOP</span>
</center>
 
---
 
## <!--{ as="div" }-->
 
Together, CO₂, CH₄ and N₂O are responsible for the overwhelming majority of human-caused climate change. Monitoring all three from space — accurately, continuously, and with global coverage — is one of the central scientific and operational challenges of our time.
 
The ESA CCI, through its GHG-CCI+, RECCAP-2, and LOLIPOP projects, is meeting this challenge by delivering increasingly robust, validated, and policy-relevant data records. These datasets are not only advancing scientific understanding of the global carbon cycle — they are becoming an indispensable tool for verifying progress towards the goals of the Paris Agreement.
 
As satellite technology continues to evolve — with new missions, improved algorithms, and higher spatial resolution — the coming decade promises to bring the three-gas budget closer to the level of certainty that international climate policy urgently requires.
 
> *"Achieving net-zero by the second half of the century is considered vital if global temperatures are to remain well below the two degrees rise prescribed by the Paris Agreement. From their vantage point in space, satellites provide a unique means of tracking progress towards achieving this balance between GHG emissions from sources and removal by sinks."*
> — ESA Climate Change Initiative
 
**Explore the data:**
- [ESA GHG-CCI Project](https://climate.esa.int/en/projects/ghgs/)
- [RECCAP-2 Project](https://climate.esa.int/en/supporting-the-paris-agreement/reccap-2-climate-space/)
- [LOLIPOP Project](https://climate.esa.int/en/projects/long-lived-greenhouse-gas-products-performances-lolipop/)
- [CCI Open Data Portal](https://climate.esa.int/en/odp/)
 
## <!--{ as="div" }--> Open Science
 
All datasets referenced in this story are freely and openly available. The ESA CCI is committed to open science — data products, documentation, and validation reports are published through the CCI Open Data Portal and partner archives.
 
| **Name** | **Type** | **Agency / Provider** | **Description** |
|---|---|---|---|
| **[GHG-CCI XCO₂ (OCO-2 FOCAL v11)](https://climate.esa.int/en/projects/ghgs/)** | Dataset | ESA CCI GHG-CCI+ | Column-averaged CO₂ from OCO-2; Sept 2014 – Dec 2023; global |
| **[GHG-CCI XCO₂ (GOSAT-2 SRFP v2.0.3)](https://climate.esa.int/en/projects/ghgs/)** | Dataset | ESA CCI GHG-CCI+ | Column-averaged CO₂ from GOSAT-2; Feb 2019 – Dec 2023; global |
| **[GHG-CCI XCH₄ (S5P/TROPOMI WFMD v1.8)](https://climate.esa.int/en/projects/ghgs/)** | Dataset | ESA CCI GHG-CCI+ | Column-averaged CH₄ from Sentinel-5P; Nov 2017 – Dec 2023; global |
| **[GHG-CCI XCH₄ (GOSAT-2 SRFP/SRPR v2.0.3)](https://climate.esa.int/en/projects/ghgs/)** | Dataset | ESA CCI GHG-CCI+ | Column-averaged CH₄ from GOSAT-2; Feb 2019 – Dec 2023; global |
| **[LOLIPOP N₂O / OLLGHG Products](https://climate.esa.int/en/projects/long-lived-greenhouse-gas-products-performances-lolipop/)** | Dataset | ESA CCI LOLIPOP | N₂O, SF₆, CFCs from IASI and MIPAS; profiles and columns |
| **[RECCAP-2 Regional Carbon Budgets](https://cci.esa.int/reccap2)** | Dataset | ESA CCI RECCAP-2 | Top-down CO₂, CH₄, N₂O flux estimates; global and regional |
| **[Global Carbon Atlas](https://globalcarbonatlas.org/)** | Platform | Global Carbon Project | Interactive visualisation of carbon fluxes from RECCAP-2 datasets |
| **[CCI Open Data Portal](https://climate.esa.int/en/odp/)** | Platform | ESA CCI | Access to all CCI ECV data records |
 
---
 
## Contributors
### Closing: The 3-GHG Challenge
 
