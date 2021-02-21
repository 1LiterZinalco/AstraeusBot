import utils, config, discord
from discord.ext import commands

# Startup
print("STARTUP BEGIN...")
client = commands.Bot(command_prefix = "!")

# Removing the standard "help" command
client.remove_command("help")

# Loading cogs:
client.load_extension("cogs.features")
client.load_extension("cogs.on_ready")
client.load_extension("cogs.developer")

# Starting the Bot
print("STARTUP CLEAR, RUNNING BOT")
client.run(config.BOT_TOKEN)
