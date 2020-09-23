import os
import socket
from aiohttp import AsyncResolver, ClientSession, TCPConnector
from datetime import datetime

from discord.ext import commands


# All the cogs that are to be loaded on launch
cogs = ['bot.cogs.base',]


class DTSBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",
                         description='DTS Apprentice Made Bot!')

    async def on_ready(self):
        self.http_session = ClientSession(
            connector=TCPConnector(resolver=AsyncResolver(), family=socket.AF_INET)
        )
        for cog in cogs:
            try:
                self.load_extension(cog)
            except Exception as e:
                logger.error(f'Failed to load extension: {cog}\n{e}')

        print(f'Client Logged in at {datetime.now()}')
        print(f'Logged in as : {self.user.name}')
        print(f'ID : {self.user.id}')

    def run(self):
        super().run(os.environ.get('TOKEN'), reconnect=True)


if __name__ == '__main__':
    bot = DTSBot()
    bot.run()