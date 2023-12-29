"""moddulo de extract necessário para consolidar os dados de entrada."""

import glob
import os

import pandas as pd

def extract_excel(input_folder):
    """
    funcao para extrair dados de arquivos EXCEL.

    type: input_folder: str
    """

    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        raise ValueError("No Excel files found")
    all_data = [pd.read_excel(file) for file in files]

    return all_data