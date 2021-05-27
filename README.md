# What
Due to the COVID pandemic access to boulderbar locations is limited.
This script parses available slots at all viennese boulderbar locations.

https://boulderbar.net

# Example Visualization
![example visualization](https://github.com/manuelnagele/boulderbar-checker/blob/master/img/example_visualization.png?raw=true)

# Example Telegraf Config
```
[[inputs.exec]]
  commands = ['/opt/boulderbar-checker/main.py'] 
  timeout = "10s"
  name_override = "boulderbar_checker"
  data_format = "json"
  interval = "60s"
```
