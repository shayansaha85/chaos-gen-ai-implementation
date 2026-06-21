import yaml
import os

def load_config(config_file='config.yaml'):
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file {config_file} not found.")
    
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
        
    return config
