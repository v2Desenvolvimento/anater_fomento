import json

import certifi
import urllib3
from fastapi import APIRouter
from loguru import logger


router = APIRouter()


@router.post('/fomento')
async def get_fomento(nome: str, cpf: str, nis: str, dia: int, mes: int, ano: int, uf: int):
    http = urllib3.PoolManager(ca_certs=certifi.where())

    logger.info('Chegando em fomento.cidadania.gov.br!')
    url = 'https://fomento.cidadania.gov.br/webservice/WS3/consulta_cu.php?'
    req = http.request('POST', url, fields={'nome': nome, 'cpf': cpf, 'nis': nis, 'dia': dia, 'mes': mes, 'ano': ano, 'uf': uf})
    logger.info('Fechando conexão em fomento.cidadania.gov.br!')
    return json.loads(req.data)
