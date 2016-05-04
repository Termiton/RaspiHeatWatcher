# RaspiHeatWatcher

##2 scripts :

#### Guardian.py 
Get cpu temperature every 60 seconds<br>
Mail you if cpu temp > 45'C (default)

#### Logger.py
Mail you every hour cpu temperature

## Configuration 
Edit heatconf-modele.py file<br>
Rename heatconf-modele.py > heatconf.py


## Usage
sudo nohup python /path/HeatWatcher/Guardian.py &<br>
sudo nohup python /path/HeatWatcher/Logger.py &
