"""Este modulo contêm funçoes para o processo de ETL."""

from .extract import extract_excel
from .transform import transforma_em_um_unico
from .load import load_em_um_novo_excel
from .pipeline import pipeline_completa
