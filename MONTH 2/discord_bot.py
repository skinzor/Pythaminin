import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'test':
            await message.channel.send('im work ok')

client = MyClient()
client.run('token')
