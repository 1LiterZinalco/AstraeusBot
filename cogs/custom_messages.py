import utils, discord
from discord.ext import commands

class custom_messages(commands.Cog):
    def __init__(self, client):
        self.client = client

#============================================================================================================#

    @commands.command(pass_context = True, aliases=['info', 'about', 'github'])
    async def help(self, ctx):
        embed=discord.Embed(title="Available commands", description="""``!twitch`` - Astraeus' Twitch channel\n``!socialmedia`` - ...and other social media profiles\n``!designs``- Astraeus' banner & emoji designers\n``!wallpapers`` - Titanfall2 themed wallpapers by Astraeus\n``!catalog`` - Personal astrophotography by Astraeus\n\n[*MRVN is open-source on GitHub*](https://github.com/1LiterZinalco/MRVN)""", color=0x9c5eb3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/727242138840203374/2ffc86022ecb17bf52b38781be358488.png?size=512")
        await ctx.send(embed=embed)

    @commands.command(pass_context = True, aliases=['design', 'designer', 'designers'])
    async def designs(self, ctx):
        await ctx.send("Please check out my amazing designers and consider following them! <3\nBanner: <https://www.instagram.com/assassinwoof/>\nEmote 1: <https://www.instagram.com/2verycool/>\nEmote: 2: <https://www.instagram.com/jamess_cz/>")

    @commands.command(pass_context = True, aliases=['live', 'stream', 'livestream'])
    async def twitch(self, ctx):
        await ctx.send("Follow Astraeus on Twitch: <https://www.twitch.tv/astraeustf>")

    @commands.command(pass_context = True, aliases=['wallpaper', 'background', 'pictures'])
    async def wallpapers(self, ctx):
        await ctx.send("Some good looking Titanfall2 themed wallpapers, made by Astraeus.\n<https://drive.google.com/drive/folders/1nYG6BqxqU4rH5DTTZGrc0vyMAqidcSVi>")

    @commands.command(pass_context = True, aliases=['astrophotography', 'astro'])
    async def catalog(self, ctx):
        await ctx.send("Here's a download link to Astraeus' catalog 🪐\n<https://drive.google.com/drive/folders/10ZTT9gGjRNw0HQHJmD9OQCYn19D3w91n?usp=sharing>")

    @commands.command()
    async def socialmedia(self, ctx):
        await ctx.send("""
**Astraeus' socal media links :)**
Donations: <https://streamlabs.com/astraeustf/tip>
Instagram: <https://www.instagram.com/titanfall2memes/>
Twitter: <https://twitter.com/AstraeusTF>
Youtube: <https://www.youtube.com/channel/UCvoS-_azvqxz5YZ10w92Uxw>
""")

    @commands.command()
    async def helpmod(self, ctx):
        await ctx.send("""
**Moderation Commands**
``!ban [member] (optional reason)``
_Bans a member from the server_

``!tempban [member] [duration] (optional reason)``
_Temporarily bans a member from the server_

``!clear (optional member) (optional count)``
_Clears messages in a particular channel_

``!clear-all-infractions``
_Remove all the infractions of everyone in the server_

``!infractions [member]``
_Displays how many infractions this member has_

``!kick [member] (optional reason)``
_Kicks a member from the server_

``!mute [member] (optional reason)``
_Mutes a member in the whole server_

``!tempmute [member] [duration] (optional reason)``
Temporarily mutes a member in the server

``!role-info [role]``
_Gets information about a role_

``!server-info``
_Gets information about your server_

``!slowmode (optional timeout) (optional off)``
_Enables/Disables slowmode in a channel_

``!unban [member]``
_Unbans a member_

``!unmute [member]``
_Unmutes a member_

``!user-info (optional member)``
_Gets information about a user_

``!warn [member] (optional reason)``
_Warns a member_
""")

#============================================================================================================#

def setup(client):
    client.add_cog(custom_messages(client))
    utils.log("Initialized cogs.custom_messages")

#============================================================================================================#
