import asyncio
import aiohttp

class GizmoHttpClient(aiohttp.ClientSession):
    #IP = '10.65.65.87'
    IP = '127.0.0.1'
    PORT = 5000
    BASE_URL = 'http://{IP}:{PORT}'
    
    
    async def goDirection(self, direction, nSteps=''):
        async with self.get(self.BASE_URL + direction + nSteps) as response:
            print(response.status)
            print(await response.text())

    async def goForward(self, nSteps):
        await self.goDirection(nSteps, '/v1/moveForward?steps=')

    async def goBackward(self, nSteps):
        await self.goDirection(nSteps, '/v1/moveBackward?steps=')

    async def stop(self):
        await self.goDirection('/v1/moveStop')