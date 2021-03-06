#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from python_script.writer import HugoWriter


def parse_arguments():
    """Define and parse the script arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('notebook', help='Jupyter notebook filename')
    parser.add_argument('--site-dir', required=True, 
                        help='path to hugo site directory')
    parser.add_argument('--section', required=True, 
                        help='content section where to create markdown')
    args = parser.parse_args()
    _, ext = os.path.splitext(os.path.basename(args.notebook))
    if ext != '.ipynb':
        parser.error('Notebook is expected to have a .ipynb extension.')
    return args.notebook, args.site_dir, args.section
    
    
if __name__ == '__main__':
    notebook, site_dir, section = parse_arguments()
    writer = HugoWriter()
    writer.convert(notebook, site_dir, section)
