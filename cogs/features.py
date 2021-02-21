import config, os, utils, time, random, discord, urllib.request
from discord.ext import commands
from PIL import Image

class features(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._timeout_kenobi = 0
        self._timeout_eyeless = 0

#============================================================================================================#

    @commands.command(pass_context = True, aliases=['info', 'about', 'github'])
    async def help(self, ctx):
        embed=discord.Embed(title="Available commands", description="""``!twitch`` - Astraeus' Twitch channel\n``!socialmedia`` - ...and other social media profiles\n``!designs``- Astraeus' banner & emoji designers\n``!wallpapers`` - Titanfall2 themed wallpapers by Astraeus\n``!catalog`` - Personal astrophotography by Astraeus\n``!high5`` - *or ``!superhigh5``, for the cool kids*\n\n[*MRVN is open-source on GitHub*](https://github.com/1LiterZinalco/MRVN)""", color=0x9c5eb3)
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

    @commands.command(pass_context = True, aliases=['shigh5', 'superh5', 'superhigh5', 'shfive', 'superhfive', 'superhighfive', 'shighfive'])
    async def sh5(self, ctx):
        try:
            m = ctx.message.mentions[0]
            try:
                if ctx.message.author == m:
                    await ctx.message.channel.send("That's... kinda sad... But... Here you go...")
                os.system("wget {} -O {}".format(ctx.author.avatar_url_as(format="png", size=64)), config.PATH_HIGH5_SOMEONE_EXECUTER)
                os.system("wget {} -O {}".format(m.avatar_url_as(format="png", size=64)), config.PATH_HIGH5_SOMEONE_TAGGED)
                h5_base = Image.open(config.PATH_HIGH5_SOMEONE_BASE)
                h5_user_1 = Image.open(config.PATH_HIGH5_SOMEONE_EXECUTER)
                h5_user_2 = Image.open(config.PATH_HIGH5_SOMEONE_TAGGED)
                h5_base.paste(h5_user_1, (174, 68))
                h5_base.paste(h5_user_2, (349, 61))
                h5_base.save(config.PATH_HIGH5_SOMEONE_RESULT)
                await ctx.send(file=discord.File(open(config.PATH_HIGH5_SOMEONE_RESULT, "rb")))
                os.system("rm {}".format(config.PATH_HIGH5_SOMEONE_EXECUTER))
                os.system("rm {}".format(config.PATH_HIGH5_SOMEONE_TAGGED))
                os.system("rm {}".format(config.PATH_HIGH5_SOMEONE_RESULT))
            except Exception as e:
                await ctx.send(":warning: "+str(e))
        except:
            try:
                os.system("wget {} -O {}".format(ctx.author.avatar_url_as(format="png", size=64)), config.PATH_HIGH5_BOT_EXECUTER)
                h5_base = Image.open(config.PATH_HIGH5_BOT_BASE)
                h5_user = Image.open(config.PATH_HIGH5_BOT_EXECUTER)
                h5_base.paste(h5_user, (167, 28))
                h5_base.save(config.PATH_HIGH5_BOT_RESULT)
                await ctx.send(file=discord.File(open(config.PATH_HIGH5_BOT_RESULT, "rb")))
                os.system("rm {}".format(config.PATH_HIGH5_BOT_EXECUTER))
                os.system("rm {}".format(config.PATH_HIGH5_BOT_RESULT))
            except Exception as e:
                await ctx.send(":warning: "+str(e))

    @commands.command(pass_context = True, aliases=['high5', 'highfive', 'hfive'])
    async def h5(self, ctx):
        await ctx.send(":hand_splayed:")

    @commands.Cog.listener()
    async def on_message(self, message):
        if "hello there" in message.content.lower():
            if time.time() > self._timeout_kenobi:
                self._timeout_kenobi = time.time()+15
                if message.author.id == 554409891482173460:
                    gifs = ["https://tenor.com/view/grevious-general-kenobi-star-wars-gif-11406339", "https://tenor.com/view/another-one-for-my-collection-grievous-lightsaber-gif-16775319"]
                    await message.channel.send(gifs[random.randint(0,1)])
                else:
                    await message.channel.send("General Kenobi")

    @commands.command()
    async def eyeless(self, ctx):
        i=0
        if time.time() > self._timeout_eyeless:
            self._timeout_eyeless = time.time()+60
            while i<10:
                g = ctx.message.guild
                m = g.get_member(262225307463974914)
                await ctx.send(m.mention)
                time.sleep(1)
                i+=1

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
    client.add_cog(features(client))
    print("Initialized cogs.features")
