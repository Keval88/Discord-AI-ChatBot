import discord
from discord.ext import commands

class Autoresponses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    allowed_channel_ids = [1205435434839052318, 1201776251615051878, 704131804323512373, 1193010471620587542, 791554672367763488, 1175260007080669197]

    keyword_responses = {
        'kev': 'Has a bigger brain',
        'bot': 'I am a bot',
        'hello': 'My world',
        'thanks': 'Always here to help!',
        'goodbye': 'Farewell and take care!',
        'help': 'How can I assist you today?',
        'funny': 'I’m glad you enjoyed that!',
        'weather': 'Looking up the weather for you!',
        'music': 'Let’s talk about music!',
        'news': 'Here’s what’s happening around the world:',
        'sports': 'Which sport are you interested in?',
        'food': 'What type of cuisine are you craving today?',
        'halil': 'Hello Halil! What can I do for you today?',
        'curse words': 'Watch your language!'
    }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user or message.channel.id not in self.allowed_channel_ids:
            return
        
        for keyword, response in self.keyword_responses.items():
            if keyword in message.content.lower():
                reply = await message.channel.send(response)
                await message.add_reaction("👀")
                break



async def setup(bot):
    await bot.add_cog(Autoresponses(bot))