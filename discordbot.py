from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
        
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if message.content == 'rand':
        num = random.randint(1,10)
        await message.channel.send('num')
    # メンバーのリストを取得して表示
    if message.content == '/members':
        await message.channel.send(message.guild.members)
    # 役職のリストを取得して表示
    if message.content == '/roles':
        await message.channel.send(message.guild.roles)
    # テキストチャンネルのリストを取得して表示
    if message.content == '/text_channels':
        await message.channel.send(message.guild.text_channels)
    # ボイスチャンネルのリストを取得して表示
    if message.content == '/voice_channels':
        await message.channel.send(message.guild.voice_channels)
    # カテゴリチャンネルのリストを取得して表示
    if message.content == '/category_channels':
        await message.channel.send(message.guild.categories)
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
