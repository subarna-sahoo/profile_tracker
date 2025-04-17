import aiohttp

geo_cache = {}

async def get_location(ip: str):
    if ip in geo_cache:
        return geo_cache[ip]

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://ipapi.co/{ip}/json/") as res:
                if res.status == 200:
                    data = await res.json()
                    result = {
                        "country": data.get("country_name"),
                        "city": data.get("city")
                    }
                    geo_cache[ip] = result
                    return result
    except Exception:
        pass

    return {"country": None, "city": None}
