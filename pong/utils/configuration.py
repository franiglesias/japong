import configparser

from config import BASE_PATH


def read_configuration(key):
    """
    Reads the configuration data for match
    """
    cfg = configparser.ConfigParser()
    cfg.read(BASE_PATH + '/config.toml')
    return cfg[key]
