# Example Telegraf Config
```
[[inputs.exec]]
  commands = ['/opt/boulderbar-checker/main.py'] 
  timeout = "10s"
  name_override = "boulderbar_checker"
  data_format = "json"
  interval = "60s"
```
