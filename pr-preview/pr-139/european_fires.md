---
cover-image: https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/8-wildfires.jpg
date: 2025-01-01
theme: atmosphere
tags: wildfires,forests,co,carbon-monoxide
official: true
collections: N1_CO
---

# Evaluating Fire Impact on Populated Areas in Europe <!--{ as="img" mode="hero" src="https://raw.githubusercontent.com/eurodatacube/eodash/c59adc7d580c6ced1f85a44c5bdd18bf94b3c9ee/app/public/data/story-images/8-wildfires.jpg" }-->
### How the 2022 Gironde wildfire affected urban areas near Bordeaux, France <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

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

## Wildfire Impacts and Carbon Emissions

The wildfire season during the summer of 2022 in Europe was exceptional, marked by a high number of observed fires, a large extent of burned area, and remarkably high atmospheric emissions linked to these fires. According to data from the [European Forest Fire Information System (EFFIS)](https://effis.jrc.ec.europa.eu/), fires were reported in 26 out of the 27 European countries, collectively burning 837,212 hectares. A significant portion of these wildfires happened in July, with Spain, Portugal, France, and Italy experiencing the most damages.

The selected wildfire incident for this analysis occurred in the **Gironde region** of southwestern France, near the city of Bordeaux, in 2022. The significant fire event started on **July 17, 2022**, lasted for two weeks while burning approximately 7,000 hectares of land. Notably, the [Copernicus Atmosphere Monitoring Service (CAMS)](https://atmosphere.copernicus.eu/) recorded exceptionally elevated levels of carbon monoxide emissions throughout the duration of this event.

## Satellite Data for Wildfire Analysis

Earth observation satellites provide a powerful toolset to monitor wildfire events, assess their extent, and measure their impact on air quality in nearby populated areas. This analysis combines three complementary data sources:

**Sentinel-2** optical imagery is used to visualize the fire event and map the burned area at 10–20 metre resolution. The true colour image captured on July 17, 2022 — the day the fire started — clearly shows the fire plume extending westward from the Gironde forest toward the urban areas near Bordeaux.

**The EC-JRC Global Human Settlement (GHS) Layer** provides global data on total built-up surface from 1975 to 2030, derived from Sentinel-2 composite and Landsat imagery. This layer is used to identify and isolate populated areas within the analysis zone, enabling a targeted assessment of where people were most exposed to the fire emissions.

**Copernicus Sentinel-5P TROPOMI** carbon monoxide (CO) data is then queried specifically over those populated areas using the Sentinel Hub Statistical API. The resulting time series reveals a clear and sharp increase in CO concentration on July 17, 2022, coinciding precisely with the start of the fire, with elevated standard deviation values persisting in the following days — consistent with records showing that the highest carbon emissions in France in 2022 were recorded between June and August.

## From Satellite to Impact Assessment

The analysis workflow links these three data sources in a coherent chain: Sentinel-2 imagery defines the geographic extent of the fire event; the GHS layer identifies which parts of that extent are populated; and Sentinel-5P CO data quantifies the atmospheric exposure of those populations during and after the fire. This integrated approach demonstrates how open Earth observation data — freely accessible through platforms such as the [Euro Data Cube (EDC)](https://eurodatacube.com/) and the [EO Dashboard](https://eodashboard.org/) — can be combined to produce actionable insights about the human and environmental impacts of extreme wildfire events.

As climate change drives more frequent and intense fire seasons across Europe and globally, workflows such as this one become increasingly important for early warning, emergency response, and post-event impact assessment.

## Jupyter Notebook

The following Notebook evaluates fire impact on populated areas on a European site.

<iframe width="95%" style="min-height: 70vh" src="https://esa-eodashboards.github.io/eodashboard-notebooks/notebooks/fire-impact-analysis" frameborder="0"></iframe>

## <!--{ as="div" }--> Open Science

All datasets referenced in this story are freely and openly available. Sentinel-2 and Sentinel-5P data are distributed without charge through the Copernicus Open Access Hub and Sentinel Hub. The GHS layer is openly available from the EC-JRC. No registration is required to access the EO Dashboard interactive maps.

| Name | Type | Agency / Provider | Description | Access |
|---|---|---|---|---|
| [Copernicus Sentinel-2 L2A](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2) | Dataset | ESA / Copernicus | Multispectral