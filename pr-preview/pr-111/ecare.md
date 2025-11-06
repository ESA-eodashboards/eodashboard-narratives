---
cover-image: https://placehold.co/600x400/png
date: 2025-01-01
theme: theme_name
tags: EarthCARE, clouds, aerosols, ITCZ, southern ocean

---

# Exploring our atmosphere with EarthCARE <!--{ as="img" mode="hero" src="https://placehold.co/600x400/png" }-->
### From aerosols to clouds <!--{ style="font-size:1.5rem;opacity:0.7;margin-top:1rem;" }-->

## Aerosols and clouds belong together

Some clouds would struggle to exist without aerosols.
Aerosols are made of small particles that can act as nuclei, helping cloud droplets form.
In a simplified way, this works as follows: as parcels of air rise from the Earth's surface through the troposphere (the part of the atmosphere in contact with the surface), they carry water vapor, which is water in its gaseous state. As the air ascends, it cools because the temperature in the troposphere decreases with height. Along the way, it may encounter aerosol particles. Some of these particles are hygroscopic, meaning they attract and interact well with water molecules. When the temperature drops sufficiently, water vapor begins to condense around these particles, forming liquid droplets. These particles that help activate cloud droplets are known as Cloud Condensation Nuclei (CCN).

Some aerosols are made of particles that will help water molecules form ice crystals, transitioning into a solid state. This typically occurs higher in the troposphere or at colder temperatures. These particles, which are often insoluble, are called Ice Nucleating Particles (INPs). Depending on the state of the majority of droplets, clouds can be classified as liquid, ice, or mixed-phase.

Different types of aerosols are made of different particles. We often distinguish between aerosols derived from human activity (anthropogenic aerosols) and natural aerosols (non-anthropogenic). Examples of natural aerosols include sea salt spray, sulfates from volcanic eruptions, and dust from deserts. Examples of anthropogenic aerosols include those coming from industrial activity, generally pollution, and smoke from biomass burning.

<div style="text-align: center;">
    <img src="
https://github.com/paula-rj/eodashboard-narratives/blob/paula-rj/first-story-narrative/assets/aapopescu/clouds_formation.png " width="500"/>
    <p><b>Figure 1.</b> Schematic representation of how liquiod cloud droplets form with the help of aerosol particles.</p>
</div>

Figure 3: Aerosols radiative effects. Aerosols particles can change the way the radiation is reflected and reemited themselves, this is called a direct effect. They can also modify the size and amount of particles that a cloud is made of, consecuently changing how much cradiation is reflected by the cloud. This is an indirect effect from the aerosols.

Figure 4: Cloud radiative effects. The amount of clouds, their height in the atmosphere and their thickness are fundamental variables that determine how they interact with the incomming and outgoing radiation. 

Because aerosols influence cloud droplets from the moment they form, they can also affect the overall structure and behavior of the cloud. For example, a higher concentration of CCNs leads to the formation of more and smaller droplets. In liquid clouds, this increases their reflectivity to sunlight, a phenomenon known as the Twomey effect.
Changes in droplet number, phase (liquid or ice), and cloud thickness can alter how clouds reflect solar radiation or trap heat emitted from the Earth's surface. Understanding these interactions is crucial, as clouds can either mitigate or amplify the warming of the planet.

## Challenge 

**Delate. **

That's an introduction rather than the challenge. Challenge and objective can be merged. 

How can a satellite help?

We can't continuously sample cloud droplets and aerosols directly from within clouds. However, researchers have developed several methods to study them remotely. You might ask: How did we develop understanding of clouds when we didn't have satellites to watch them from avobe and how can a satellite measure aerosols from space, given their small size? 

Our first tool was and still is the theory. Physics allows us to predict how clouds behave and interact with aerosols. Over time, researchers developed equations to describe these processes under ideal conditions.

As our understanding improved, these equations became more complex, incorporating more realistic features of the atmosphere. The advances in computing led to the development of computational models. These models are simulations that solve thousands of equations to represent atmospheric processes. While still simplified, these models help us explore interactions and uncover new insights.

To understand if the models are representing the real-life processes, we rely on observations.
One approach is laboratory experiments. Scientists study how ice crystals grow with different types of aerosols or simulate clouds in controlled chambers. However, lab conditions are still idelized compared to how complex is real atmosphere.

Fortunately, we also have airborne measurements. Aircraft equipped with specialized instruments, called probes, can collect samples of clouds and aerosols, which are then analyzed in laboratories. These aircraft can also carry sensors to measure cloud and aerosol properties in real time. However, such field campaigns are costly and cannot be conducted everywhere or continuously. This is where satellites become essential.

Satellites provide global, long-term observations that complement lab experiments, aircraft missions, and models. Together, these tools offer a more complete picture of a system that is both complex and rapidly changing. Improving our understanding helps refine weather and climate predictions and is critical in a warming world.

### Why EarthCare? 

EarthCARE is a first-of-its-kind mission that offers an unlikely opportunity to understand the complexity of cloud changes using a single satellite. What makes EarthCARE special is its four instruments working together to study clouds, aerosols, and radiation in detail.

ATLID (Atmospheric Lidar) uses laser pulses to detect aerosols and thin cloud layers by measuring how light scatters back from particles, providing high-resolution profiles that improve on previous lidar missions like CALIPSO.
CPR (Cloud Profiling Radar) can "see" across the clouds with radar signals to measure their vertical structure and water content, adding the capability to  capture cloud motion and the speed of precipitation. This imporves the previous mission called CloudSat .
MSI (Multi-Spectral Imager) delivers multi-wavelength images in 7 different bands that reveal cloud structure and aerosol distribution over large areas, complementing MODIS with higher spatial resolution. 
BBR (Broadband Radiometer) measures solar and thermal radiation reflected and emitted by Earth, enabling direct estimates of top-of-atmosphere radiative effects and energy balance. 

Together, these instruments provide comprehensive and blended data that will help us explore interactions and uncover new insights into how clouds and aerosols influence climate.

## The challenge 

In the latest ESA challenge workshop, we set out to explore the clouds and aerosols at three different locations with quite special characteristics. 
The first region lies just north of the Equator and stretches West to East across the Pacific Ocean. It's called the call the Inter-Tropical Convergence Zone (ITCZ) and it is characterized by persistent clouds with high and icy tops. The second region is in Antartica, the southern ocean. Here the conditions are quite different and clouds are lower, but because of the temperature these are mostly made of ice. 

<div style="text-align: center;">
    <img src="
https://github.com/eurodatacube/eodash-assets/blob/main/stories/ScienceHub-Challenge-September-2025/Team-1/Globe1_pacific.png?raw=true  " width="500"/>
    <p><b>Figure 2.</b> The three locations of our study for ESA challenge.</p>
</div>

1. **West Pacific**
The western ITCZ is very interesting because air raises in very strong updrafts (air moving upwards), mostly because the sea serface temperature is usually high. These updrafts and the clouds can form storms that can stir the ocean, lifting sea salt aerosols into the atmosphere. These are natural aerosols (non-anthropogenic). However, nearby regions such as Southeast Asia and China may contribute with anthropogenic aerosols derived from human activities, like pollution or industrial activity.

2.  **Eastern Pacific**  
This region typically experiences downdrafts, where air sinks rather than rises, as the sea temperature is usually lower than in the West. Yet, high clouds still form here. Being far from major population centers, we expect fewer aerosol sources. 

3.   **Southern Ocean** 
This region presents a completely different scenario. 
The atmospheric dynamics are quite particular. Ice clouds form at much lower altitudes given the extremely low temperature of the atmosphere. However, there can also be some supercooled clouds at low altitudes. Aerosols might potentially be carried from far away, and influence cloud formation here. We mostly expect sea salt aerosols, but there could also be stratospheric aerosols, especially from volcanic eruptions.

Comparing these three very interesting regions with quite distinctive characteristics could give us a hint on whether the aerosols are influencing changes in the clouds. 

## Data and methods

### EarthCARE Instruments

We've used two of the forurth instruments on-board of EarthCare, the ones that can provide a vertical profiliong of the atmosphere:
- Cloud Profiling Radar (CPR): 94 GHz nadir-viewing radar with ~750m horizontal resolution and 100m vertical resolution, providing cloud structure, ice and liquid water content. 
    Atmospheric Lidar (ATLID): 354.8 nm nadir-viewing lidar with <30m horizontal resolution and 100m vertical resolution, detecting aerosols and thin clouds
 
		Remove Earthcare instruments pic from here
		
### Datesets

The analysis used three primary EarthCARE data products:
 - CPR_CLD_2A: Derived from CPR reflectivity measurement, it provides cloud variables including Liquid Water Path (LWP) and Ice Water Path (IWP), plus land/ocean flags. 
 - ATL_ALD_2A: Derived from ATLID backscatter measurement, it provides aerosol variables including Aerosol Optical Thickness (AOT) at 355nm. 
 - AC_TC_2A: This is a synergistic radar-lidar product, that provides target classification distinguishing cloud types and aerosol layers. 

Data coverage: We've used approximately 600-700 scenes from June-July and September 2025 (limited by early mission data availability). Analysis was conducted using the Multi-Mission Algorithm and Analysis Platform (MAAP).

### Methodology workflow

To get some insights in the possible links between clouds and aerosols, we've developed a K-Means clusterring classiffication using the liquid water path, ice water path and aorosols optical thickness variables. This is an unsupervised machine learning algorithm that groups the data points in a given number of groups, according to the characteristics they have in common. This is basically quantified through the distance of the points to the center of the group or centroid. 

The data processing followed a systematic processing pipeline:

    1- Extract all the data available for the areas we're interested in (600~700 scenes)
    2- Resample data by time at 1s temporal resolution for co-location
    3- Merge datasets(radar+lidar) at 1 m temporal definition (AOT, L/IWP, Target classification)
    4- Resample at 1 minute temporal
    5- Select only the months for which all data is available: June-July, September 2025
    5- Normalize variables (X - min/ max-min)
    6 - Clustering approach using simple K-means to understand centroids distance and relations between variables

Finally, the synergetic product will give us insights on the types of clouds or aerosols that are grouped on each cluster.

We used the elbow method to understand the3 ideal amount of clousters for our data, which is 5 (where the "elbow" lies).  
**! Include elbow method plot**
The code was run at MAAP portal.


### Results
Although this was only an exploratory analysis, we can see some insights. 
	The following plots show the clusters obtained in 2 dimensions, where each dimension is one of the variables we worked with. Each colour represents the cluster to which each data point has been classified to. The red crosses show the clusters' centroids. 
	
	The first thing to notice is that, ovearall, the West Pacific classification is different than the East one. Taking a closer look at the IWP vs AOD plots, many of the points and especially the ones with higher value lie either in IWP=0 or AOT=0. This is expected as the Aerosols are measured with the lidar and, as stated previously, the thick clouds made of ice, therefore wtih high IWP, will make the lidar extinguished. However, there are some points that have a value different to 0 in both axis.
	
Taking a closer look at the West Pacific, there are some values in the space where the IWP>0.2 kgm-3, which is considerered a thick ice clouds, and AOT!= 0. Many of these points are classified as cluster 5 (brown dots) and 1 (blue dots). If we take a look at the LWP vs AOT plot, we see that most of the data points in cluster 5 have a lower LWP values compared to their IWP values. In cluster 1 instead, for the same AOD values, they have higher values of LWP. Finally, lookig at the LWP vs IWP plot, we confirm that cluster 5 data points are mostly thick clouds made of ice and cluster 1 points are mostly made of liquid water. 


	
#### Vertical structure analysis 

#### Spatial Paterns

DELATE

#### Antartica

In Antartica, we clearly see a much more pristine environment. 
The first plot shows that there don't seem to be many links between the aerosols and the ice clouds, exept perhaps for one outlier that would need further research. 
The second and third plot show that there are not many liquid clouds. 

### Conclusions 
In this challenge, we have tested the potential of EarthCARE to unveal the interactions between clouds and aerosols. 
Focusing on different areas were we know the clouds but where we are still exploring the distributions of aerosols was challenging, but thanks to EarthCare we were able to get insights on the links. 


