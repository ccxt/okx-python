# okx-python
Python SDK (sync and async) for Okx with Rest and WS capabilities.

You can check Okx's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/okx)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install okx-exchange
```

## Usage

### Async

```Python
from okx_exchange import OkxAsync

async def main():
    instance = OkxAsync({})
    order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)
```

### Sync

```Python
from okx_exchange import OkxSync

def main():
    instance = OkxSync({})
    order =  instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)
```

### Websockets

```Python
from okx_exchange import OkxWs

async def main():
    instance = OkxWs({})
    while True:
        orders = await instance.watch_orders("BTC/USDC")
```

