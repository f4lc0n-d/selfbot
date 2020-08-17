import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', self_bot=True)

token = "----UR TOKEN HERE----"

help_command = False


client.remove_command('help')
@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def spam(ctx, arg):
    while True:

    
        await ctx.send(arg)


        pass



client.run(token, bot=False)