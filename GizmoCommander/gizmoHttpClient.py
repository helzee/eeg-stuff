# coding=utf8
import asyncio
import aiohttp

class GizmoHttpClient():
    #IP = '10.65.65.87'
    IP = '127.0.0.1'
    PORT = 5000
    BASE_URL = 'http://{0}:{1}'.format(IP,PORT)
    session = None

    async def __ainit__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *err):
        await self.session.close()
        self.session = None

    
    
    async def goDirection(self, direction, nSteps=''):
        try:
            async with self.session.get(self.BASE_URL + direction + nSteps) as response:
                print(response.status)
                if (response.status == 200):
                    print(await response.text())
                
        except aiohttp.ClientConnectorError as e:
            print('Connection error', str(e))

    async def goForward(self, nSteps):
        print('move forward')
        await self.goDirection('/v1/moveForward?steps=', str(nSteps))

    async def goBackward(self, nSteps):
        print('move backward')
        await self.goDirection('/v1/moveBackward?steps=', str(nSteps))

    async def stop(self):
        print('stop')
        await self.goDirection('/v1/moveStop')