from channels.generic.websocket import AsyncWebsocketConsumer

class DiaryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    async def disconnect(self,close_code):
        pass
    async def recieve(self, text_data):
        await self.send(text_data-"Запись обновлена")

