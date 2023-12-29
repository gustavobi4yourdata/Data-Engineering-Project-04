"""Este modulo contêm funções para o processo de ETL."""

from .extract import extract_excel
from .load import load_em_um_novo_excel
from .transform import transforma_em_um_unico


def pipeline_completa(input_folder, output_folder, output_file_name):
    """
    Função ETL: Extrai, Transforma e Carrega dados de arquivos EXCEL.

    type: input_folder: strs
    """

    data = extract_excel(input_folder)
    consolidated_df = transforma_em_um_unico(data)
    load_em_um_novo_excel(consolidated_df, output_folder, output_file_name)
