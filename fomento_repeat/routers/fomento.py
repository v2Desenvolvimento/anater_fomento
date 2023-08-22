import json

import certifi
import urllib3
from fastapi import APIRouter
from loguru import logger


router = APIRouter()


@router.post('/fomento')
async def get_fomento(
        nome: str | None = None,
        cpf: str | None = None,
        nis: str | None = None,
        dia: int | None = None,
        mes: int | None = None,
        ano: int | None = None,
        uf: int | None = None
):
    http = urllib3.PoolManager(ca_certs=certifi.where())

    logger.info('Chegando em fomento.cidadania.gov.br!')
    url = 'https://fomento.cidadania.gov.br/webservice/WS3/consulta_cu.php?'
    entrada = {'nome': nome, 'cpf': cpf, 'nis': nis, 'dia': dia, 'mes': mes, 'ano': ano, 'uf': uf}
    saida = {
        key: value for key, value in entrada.items()
        if value is not None
    }
    req = http.request('POST', url, fields=saida)
    logger.info('Fechando conexão em fomento.cidadania.gov.br!')
    return json.loads(req.data)
