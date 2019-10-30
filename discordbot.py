from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')
        
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
