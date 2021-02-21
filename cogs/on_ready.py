import utils, discord
from discord.ext import commands

class on_ready(commands.Cog):
    def __init__(self, client):
        self.client = client

#============================================================================================================#

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name="Titanfall 2"))
        print("ready")

#============================================================================================================#

def setup(client):
    client.add_cog(on_ready(client))
    print("Initialized cogs.on_ready")
