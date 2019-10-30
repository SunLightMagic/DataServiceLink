
from configparser import ConfigParser
cfg = ConfigParser()
configfileName = "../config/configration.cfg"
cfg.read(configfileName)
section=cfg.sections()[0]
host = cfg.get(section,"host")
port = cfg.get(section,"port")
print(host);