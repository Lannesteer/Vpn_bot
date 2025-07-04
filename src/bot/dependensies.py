async def gb_limit_converter(key):
    if key.data_limit is not None:
        gb_limit = round(key.data_limit / (1024 ** 3))
        return gb_limit
