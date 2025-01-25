from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DiaryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("diary_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("diary_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        await self.channel_layer.group_send(
            "diary_group",
            {
                "type": "send_update",
                "message": "Запись обновлена"
            }
        )

    async def send_update(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({"message": message}))

