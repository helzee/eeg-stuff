# coding=utf8
import asyncio
import aiohttp

class GizmoHttpClient():
    
    _ip = '10.65.65.87'
    _port = 5000
    _base_url = None
    _session = None

    async def __ainit__(self, ip, port):
        self._ip = ip
        self._port = port
        self._base_url = 'http://{0}:{1}'.format(self._ip,self._port)
        self._session = aiohttp.ClientSession()
        return self

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *err):
        await self._session.close()
        self._session = None

    
    
    async def goDirection(self, direction, nSteps=''):
        try:
            async with self.session.get(self._base_url + direction + nSteps) as response:
                print(response.status)
                if (response.status == 200):
                    print(await response.text())
                
        except aiohttp.ClientConnectorError as e:
            print('Connection error', str(e))
        except ConnectionRefusedError as e:
            print('Connection error', str(e))
        except Exception as e:
            print('Connection error', str(e))
        finally:
            return

    async def goForward(self, nSteps):
        print('move forward')
        await self.goDirection('/v1/moveForward?steps=', str(nSteps))

    async def goBackward(self, nSteps):
        print('move backward')
        await self.goDirection('/v1/moveBackward?steps=', str(nSteps))

    async def stop(self):
        print('stop')
        await self.goDirection('/v1/moveStop')