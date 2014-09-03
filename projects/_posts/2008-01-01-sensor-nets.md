---
title: Active Inference for Sensor Networks
date: 2008-01-01
collaborators:
- name: Alex Rogers
  url: http://users.ecs.soton.ac.uk/acr/
  institute: University of Southampton
- name: Roman Garnett
  url: http://www-kd.iai.uni-bonn.de/index.php?page=people_details&id=60
  institute: University of Bonn
- name: Steve Reece
  url: http://www.robots.ox.ac.uk/~reece/
  institute: University of Oxford
- name: Stephen J Roberts
  url: http://www.robots.ox.ac.uk/~sjrob/
  institute: University of Oxford
papers:
- osborne_real-time_2012
- osborne_active_2010
- garnett_bayesian_2010
- osborne_towards_2008
- rogers_information_2008
---
Sensors networks are a growing source of complex data, offering insight into many environmental and human phenomena, but demanding novel forms of information processing. 

We have introduced methods that leverage sensor networks to provide real-time estimates of dynamic environmental phenomoma. Our flexible non-parametric algorithms allow effective inference even with minimal domain knowledge, and our probabilistic approach provides uncertainty estimates to support the decision-making of human operators. We validate our approach using data collected from multiple networks of weather sensors, including <a href="http://www.bramblemet.co.uk/(S(lqsjxi55irywytqdtrnjy245))/default.aspx" title="None">Bramblemet,</a> <a href="http://badc.nerc.ac.uk/data/ukmo-midas/" title="None">MIDAS land surface stations</a> and the <a href="http://atom.research.microsoft.com/sensewebv3/sensormap/view/swissex.aspx" title="SwissEx Main Sites">Wannengrat Alpine Observatory.</a>

We have also introduced algorithms that parsimoniously select only the most valuable observations from sensor networks. Real observations are usually associated with some cost, such as the battery energy required to power a sensor or transmit a reading: it is desirable to reduce the number of such observations. We have demonstrated such active data selection on the real sensor network data above. Our algorithms intelligently concentrate sparse observations in the most informative spatio-temporal locations, even in the presence of dynamic, missing and faulty data.
