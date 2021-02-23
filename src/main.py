from apicalls import *
import asyncio
import os
import autodynatrace


os.environ["AUTOWRAPT_BOOTSTRAP"] = "autodynatrace"


async def getcall():
    while True:
        await asyncio.sleep(1)
        getpayload()


async def postcall():
    while True:
        await asyncio.sleep(1.3)
        postpayload()


async def publicall():
    while True:
        await asyncio.sleep(1.9)
        getpublic()


async def externalcall():
    while True:
        await asyncio.sleep(43.1)
        getexternal()


loop = asyncio.get_event_loop()
cors_loop = asyncio.wait([getcall(), postcall(), publicall(), externalcall()])
loop.run_until_complete(cors_loop)
