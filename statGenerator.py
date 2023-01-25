import os
import markdown2
from jinja2 import Environment, FileSystemLoader

def generate_site(input_folder, output_folder):
    # Create the Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))
