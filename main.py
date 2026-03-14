import os 
import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run ():
    intents = discord.Intents.default()
    intents.message_content=True

    bot = commands.Bot(command_prefix="!", intents = intents)

    @bot.event
    async def on_ready():
        #logging in as bot
        logger.info(f"user: {bot.user}  (id: {bot.user.id})")

        #load extensions
        await bot.load_extension("cogs.autoresponse")
        print("autoresponses extension loaded")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send(f'Error: {error}')

    # bot Secret Security Code
    bot.run(settings.DISCORD_API_SECRET, root_logger = True)

if __name__ == "__main__":
    run()