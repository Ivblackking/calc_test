import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from .helpers import calculate_pension


class PensionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        task = asyncio.create_task(calculate_pension(data))
        pension = await asyncio.gather(task)

        await self.send(text_data=json.dumps({"pension": pension}))