"""modulo com todas as transformações nencessárias para consolidar os dados de entrada."""

import pandas as pd


def transforma_em_um_unico(all_data):
    """
    funcao para consolidar os dados de arquivo EXCEL

    type: all_data: list
    """

    if not all_data:
        raise ValueError('No data to transform')
    consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)

    return consolidated_df
