# -*- coding: utf-8 -*-
from itertools import product
from pathlib import Path
import glob

from source.utils import download_url, unzip

REPO_DIR = Path(__file__).resolve().parent.parent
RESOURCES_DIR = REPO_DIR / 'source'
DUMPS_DIR = RESOURCES_DIR / "DUMPS"

WORD_EMBEDDINGS_NAME = "glove.42B.300d"
WORD_FREQUENCY_FILEPATH = DUMPS_DIR / 'enwiki-words-frequency.txt'
COMPLEXITY_MODEL_FILEPATH = DUMPS_DIR / 'lin_reg_we_weight_0.4_0.7.pkl'
GOOGLE_WORD_EMBEDDINGS_FILEPATH = DUMPS_DIR / 'GoogleNews-vectors-negative300.bin'

def download_glove(model_name, dest_dir):
    url = ''
    if model_name == 'glove.6B':
        url = 'http://nlp.stanford.edu/data/glove.6B.zip'
    elif model_name == 'glove.42B.300d':
        url = 'http://nlp.stanford.edu/data/glove.42B.300d.zip'
    elif model_name == 'glove.840B.300d':
        url = 'http://nlp.stanford.edu/data/glove.840B.300d.zip'
    elif model_name == 'glove.twitter.27B':
        url = 'http://nlp.stanford.edu/data/glove.twitter.27B.zip',
    else:
        possible_values = ['glove.6B', 'glove.42B.300d', 'glove.840B.300d', 'glove.twitter.27B']
        raise ValueError('Unknown model_name. Possible values are {}'.format(possible_values))
    file_path = download_url(url, dest_dir)
    out_filepath = Path(file_path)
    out_filepath = out_filepath.parent / f'{out_filepath.stem}.txt'
    if not out_filepath.exists():
        print("Extracting: ", Path(file_path).name)
        unzip(file_path, dest_dir)

if __name__ == '__main__':
    pass