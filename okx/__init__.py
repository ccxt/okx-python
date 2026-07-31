import sys
import okx.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from okx.ccxt import okx as OkxSync
from okx.ccxt.async_support.okx import okx as OkxAsync
from okx.ccxt.pro.okx import okx as OkxWs
