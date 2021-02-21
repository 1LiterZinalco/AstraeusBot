import utils, os, discord
from discord.ext import commands

class developer(commands.Cog):
    def __init__(self, client):
        self.client = client

#============================================================================================================#

    @commands.command()
    async def tell(self, ctx, channel, message):
        if(utils.check_permission(ctx.author.id) == True):
            try:
                await ctx.message.delete()
            except:
                pass
            channel = self.client.get_channel(int(channel))
            await channel.send(message)
        else:
            await channel.send(":fingers_crossed:")

    @commands.command()
    async def ping(self, ctx):
        if(utils.check_permission(ctx.author.id) == True):
            try:
                await ctx.message.delete()
            except:
                pass
            embed=discord.Embed(title="Ping", description="```{}```".format(ctx.message))
            embed.add_field(name="Latency", value=str(self.client.latency), inline=False)
            embed.add_field(name="ClientUser", value=str(self.client.user), inline=False)
            embed.add_field(name="Websocket Gateway", value=str(self.client.ws), inline=False)
            embed.set_footer(text=str(os.uname()))
            await ctx.send(embed=embed)

#============================================================================================================#

def setup(client):
    client.add_cog(developer(client))
    utils.log("Initialized cogs.developer")
