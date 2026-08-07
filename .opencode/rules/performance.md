# Regras de Performance

- Event loop padrão: uvloop (ou uringcore em Linux).
- Use httptools + orjson/msgspec.
- Nunca chame código síncrono dentro de rotas async.
- Prefira asyncio.TaskGroup.
- Connection pooling rigoroso (banco e HTTP).
- Para CPU-bound: considere free-threaded Python 3.14t.
- Profile antes de otimizar (cProfile, py-spy, Scalene).
- Cache agressivo com Redis quando fizer sentido.
- Workers Uvicorn/Gunicorn: (2 × CPU) + 1 para I/O-bound.
- Preferir bibliotecas nativas async: asyncpg, aioredis, httpx.
- Profile em produção com sampling (OpenTelemetry).
