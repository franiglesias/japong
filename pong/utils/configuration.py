import configparser


def read_configuration(key):
    """
    Reads the configuration data for match
    """
    cfg = configparser.ConfigParser()
    cfg.read('./config.toml')
    return cfg[key]
