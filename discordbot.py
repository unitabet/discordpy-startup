from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
        
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@bot.event
async def on_ready():
    CHANNEL_ID = 635047342546092085
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')

@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if message.content == '/ping':
        await message.channel.send('pong')
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
