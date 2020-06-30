import utils, config, discord
from discord.ext import commands

# Startup
utils.log("STARTUP BEGIN...")
client = commands.Bot(command_prefix = "!")

# Removing the standard "help" command
client.remove_command("help")

# Loading cogs:
client.load_extension("cogs.custom_messages")
client.load_extension("cogs.on_ready")
# Development tools
client.load_extension("cogs.dev_dev")

# Starting the Bot
utils.log("STARTUP CLEAR, RUNNING BOT")
client.run(config.BOT_TOKEN)
