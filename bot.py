####pylint:disable=E0001
import discord
import asyncio
from discord.ext.commands import bot
from discord.ext import commands
import platform
import time
import random
import aiohttp
import os
import datetime
import json
import time
import sys
import os
import re
import string
import traceback
import io
import inspect
import random
import functools
import textwrap
import youtube_dl
from urllib.parse import urlparse
from contextlib import redirect_stdout
import image
import glob
from io import BytesIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps 
import PIL
from PIL import Image


discord.__version__
'0.16'

bot = commands.Bot(command_prefix='k!')

bot.remove_command('help')


from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))
load_opus_lib()

@bot.event
async def on_ready():
    print("hi")
    await bot.change_presence(game=discord.Game(name='now '+str(len(bot.servers))+' servers and'' '+str(len(set(bot.get_all_members())))+' user! ', type=1))
opts = {
            'default_search': 'auto',
            'quiet': True,
        }    
 


def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()	






@bot.event    
async def on_message(message):
       	await bot.process_commands(message)
        if message.content.startswith('kermit'): 
           author = message.author     	
           await bot.send_message(message.channel, f"Yes "+author.mention+", just say k!help for help.")   
        if message.content.startswith('owu'):	
           author = message.author     	
           await bot.send_message(message.channel, "ْowu uwu what is!?!?") 
        if message.content.startswith('uwu'):	
           author = message.author     	
           await bot.send_message(message.channel, "ْowu uwu what is!?!?")           
        if message.content.startswith('guys'):	
           author = message.author     	
           await bot.send_message(message.channel, "yes")           
        if message.content.startswith('for what?, my prefix k!'):	
           author = message.author     	
           await bot.send_message(message.channel, "ْowu uwu what is!?!?")           
        if message.content.startswith('look'):	
           author = message.author     	
           await bot.send_message(message.channel, "ok")         
        if message.content.startswith('oof'):	
           author = message.author     	
           await bot.send_message(message.channel, "٠oo٠f roblox so goOd")             
        if message.content.startswith('kevin'):	
           author = message.author     	
           await bot.send_message(message.channel, "kevin")    
        if message.content.startswith('xxxtentacion'):	
           author = message.author     	
           await bot.send_message(message.channel, "Rip, and respect from Kermit")
        if message.content.startswith('lil pump'):	
           author = message.author     	
           await bot.send_message(message.channel, "gucci gang gucci gang")              
        if message.content.startswith('good'):	
           author = message.author     	
           await bot.send_message(message.channel, "not good")                          
        if message.content.startswith('yes'):	
           author = message.author     	
           await bot.send_message(message.channel, "no")
        if message.content.startswith('n٠o u'):	
           author = message.author     	
           await bot.send_message(message.channel, "n٠o n٠o u")                      
        if message.content.startswith('talk'):	
           author = message.author     	
           await bot.send_message(message.channel, "ok")           
        if message.content.startswith('my channel'):	
           author = message.author     	
           await bot.send_message(message.channel, "your channel not good")          
        if message.content.startswith('?'):	
           author = message.author     	
           await bot.send_message(message.channel, "i٠٠٥dk") 
        if message.content.startswith('idk'):	
           author = message.author     	
           await bot.send_message(message.channel, "i٠dk")                      
        if message.content.startswith('lol'):	
           author = message.author     	
           await bot.send_message(message.channel, "lm٠ao")   
        if message.content.startswith('lmao'):	
           author = message.author     	
           await bot.send_message(message.channel, "٠l٠ol")                   
        if message.content.startswith('anime'):	
           author = message.author     	
           await bot.send_message(message.channel, "who weeb")           
        if message.content.startswith('gucci'):	
           author = message.author     	
           await bot.send_message(message.channel, "u ricH")           
        if message.content.startswith('turk'):	
           author = message.author     	
           await bot.send_message(message.channel, "kebab good")           
        if message.content.startswith('english'):	
           author = message.author     	
           await bot.send_message(message.channel, "england good language too")          
        if message.content.startswith('xd'):	
           author = message.author     	
           await bot.send_message(message.channel, "funny :joy: :ok_hand: :joy: :ok_hand:")       
        if message.content.startswith('What'):	
           author = message.author     	
           await bot.send_message(message.channel, "Wut??")                
        if message.content.startswith('wut'):	
           author = message.author     	
           await bot.send_message(message.channel, "whaat??")           
        if message.content.startswith('kebab'):	
           author = message.author     	
           await bot.send_message(message.channel, "i like")    
        if message.content.startswith('who created kermit'):	
           author = message.author     	
           await bot.send_message(message.channel, "lilcsz#5890 created me")  
        	        
@bot.command(name='byemom', aliases=['bm'], pass_context=True, no_pm=True)
async def byemom(ctx, *, content):
        if len(content) > 35:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="The text is too long!", inline=True)
            await bot.say(embed=embed)	
            return
        if content is None:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="Please enter argument example: k!byemom hack", inline=True)
            await bot.say(embed=embed)
            return
        if content is not None:
            img = Image.open('byemom.jpeg')
            font = ImageFont.truetype('champagne-limousines.ttf', size=30)
            rfont = ImageFont.truetype('champagne-limousines.ttf', size=10)
            rotate_text = content
            draw = ImageDraw.Draw(img)
            draw.text((770, 1068), rotate_text, (0, 0, 0), font=font)
            draw.text((706, 1362), "Request by {}".format(ctx.message.author.name), (0, 0, 0), font=rfont)
            draw.text((736, 1362), "ByeMom", (0, 0, 0), font=rfont)
            img.save('byemomtext.jpeg')
            await bot.upload("byemomtext.jpeg")        
            os.remove("byemomtext.jpeg") 
   
@bot.command(pass_context=True)
async def idea(ctx, *, ideamsg: str=None):
	if ideamsg is None:
		embed = discord.Embed(title="Idea", description=f"You need enter idea", color=0x8ab9ff)
	else:		
		channel = bot.get_channel('503569869959331840')
		embed = discord.Embed(title="New idea", description=f"Details: {ideamsg}", color=0xff9393)
		embed.add_field(name="User Name:", value=f"{ctx.message.author}", inline=False) 		
		embed.add_field(name="User ID", value=f"{ctx.message.author.id}", inline=False)     
		embed.add_field(name="Server Name:", value=f"{ctx.message.server.name}", inline=False)
		embed.add_field(name="Server ID:", value=f"{ctx.message.server.id}", inline=False) 		
		await bot.send_message(channel, embed=embed)
		embed = discord.Embed(title="Idea", description=f"Your idea has been sent, you will get a return.", color=0xff9393)
		embed.add_field(name="Idea", value=f"Idea : {ideamsg}", inline=False)    
		embed.add_field(name="User ID", value=f"Name: {ctx.message.author.id}", inline=False)    
		embed.add_field(name="Author Name:", value=f"Name: {ctx.message.author}", inline=False)
		embed.add_field(name="Author ID", value=f"Name: {ctx.message.author.id}", inline=False)
		await bot.say(embed=embed) 
		
@bot.command(pass_context=True)
async def report(ctx, *, ideamsg: str=None):
	if ideamsg is None:
		embed = discord.Embed(title="Report", description=f"You need enter report", color=0x8ab9ff)
	else:		
		channel = bot.get_channel('503590357758640139')
		embed = discord.Embed(title="New report", description=f"Details: {ideamsg}", color=0xff9393)
		embed.add_field(name="User Name:", value=f"{ctx.message.author}", inline=False) 		
		embed.add_field(name="User ID", value=f"{ctx.message.author.id}", inline=False)     
		embed.add_field(name="Server Name:", value=f"{ctx.message.server.name}", inline=False)
		embed.add_field(name="Server ID:", value=f"{ctx.message.server.id}", inline=False) 		
		await bot.send_message(channel, embed=embed)
		embed = discord.Embed(title="Report", description=f"Your report has been sent, you will get a return.", color=0xff9393)
		embed.add_field(name="Report", value=f"Report : {ideamsg}", inline=False)    
		embed.add_field(name="User ID", value=f"Name: {ctx.message.author.id}", inline=False)    
		embed.add_field(name="Author Name:", value=f"Name: {ctx.message.author}", inline=False)
		embed.add_field(name="Author ID", value=f"Name: {ctx.message.author.id}", inline=False)
		await bot.say(embed=embed)
            
@bot.command(pass_context=True)
async def sale(ctx, content=None, *, content2=None):
        if len(content) > 35:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="The text is too long!", inline=True)
            await bot.say(embed=embed)	
            return
        if content is None:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="Please enter argument example: k!sale pen free", inline=True)
            await bot.say(embed=embed)
            return
        if content is not None:
            img = Image.open('sale.jpeg')
            font = ImageFont.truetype('champagne-limousines.ttf', size=30)
            rfont = ImageFont.truetype('champagne-limousines.ttf', size=10)
            rotate_text = content
            rotate_text2 = content2
            draw = ImageDraw.Draw(img)
            draw.text((190, 65), rotate_text, (0, 0, 0), font=font)
            draw.text((100, 640), rotate_text2, (0, 0, 0), font=font)            
            img.save('salebob.png')
            await bot.upload("salebob.png")
            os.remove("salebob.png")  
            return 
        if len(content) > 50:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="The text is too long!", inline=True)
            await bot.say(embed=embed)
            
            
@bot.command(pass_context=True)
async def rip(ctx, *, content=None):
        if len(content) > 20:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="The text is too long!", inline=True)
            await bot.say(embed=embed)	
            return
        if content is None:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="Please enter argument example: k!rip gamer000", inline=True)
            await bot.say(embed=embed)
            return
        if content is not None:
            img = Image.open('rip0.jpeg')
            font = ImageFont.truetype('champagne-limousines.ttf', size=30)
            rfont = ImageFont.truetype('champagne-limousines.ttf', size=10)
            rotate_text = content
            draw = ImageDraw.Draw(img)
            draw.text((185, 374), rotate_text, (0, 0, 0), font=font)          
            img.save('rip.png')
            await bot.upload("rip.png")        
            os.remove("rip.png")  

@bot.command(pass_context=True)
async def google(ctx, *, content=None):
        if len(content) > 35:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="The text is too long!", inline=True)
            await bot.say(embed=embed)	
            return
        if content is None:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="Please enter argument example: k!google hack", inline=True)
            await bot.say(embed=embed)
            return
        if content is not None:
            img = Image.open('fbigoogle.jpeg')
            font = ImageFont.truetype('arial.ttf', size=30)
            rfont = ImageFont.truetype('arial.ttf', size=10)
            rotate_text = content
            draw = ImageDraw.Draw(img)
            draw.text((40, 313), rotate_text, (0, 0, 0), font=font)          
            img.save('google.png')
            await bot.upload("google.png")        
            os.remove("google.png")
            
@bot.command(pass_context=True)
async def tweetdt(ctx, *, content=None):
        if len(content) > 50:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="The text is too long!", inline=True)
            await bot.say(embed=embed)	
            return
        if content is None:
            embed = discord.Embed(colour=(0x36393E))
            embed.add_field(name="Error!", value="Please enter argument example: k!tweetdt 00 is best!", inline=True)
            await bot.say(embed=embed)
            return
        if content is not None:
            img = Image.open('tweetdt.jpg')
            font = ImageFont.truetype('arial.ttf', size=30)
            rfont = ImageFont.truetype('arial.ttf', size=10)
            rotate_text = content
            draw = ImageDraw.Draw(img)
            draw.text((65, 105), rotate_text, (0, 0, 0), font=font)          
            img.save('tweet.png')
            await bot.upload("tweet.png")        
            os.remove("tweet.png")          

			
@bot.command(pass_context=True)
async def status(ctx, *,game):	
    author = ctx.message.author
    if ctx.message.author.id == '428298038612590612': 
            await bot.change_presence(game=discord.Game(name=game, type=1))
            embed = discord.Embed(color=0xb5ff29)
            embed.add_field(name="ِGame:", value="Succesfully game name changed with: {}".format(game))
            await bot.say(embed=embed)
    else:
    	    await bot.say("```Only bot owner```")
    	    
@bot.command(pass_context=True)
async def listenst(ctx, *,game):	
    author = ctx.message.author
    if ctx.message.author.id == '428298038612590612': 
            await bot.change_presence(game=discord.Game(name=game, type=2))
            embed = discord.Embed(color=0xb5ff29)
            embed.add_field(name="ِMusic Status:", value="Succesfully music status name changed with: {}".format(game))
            await bot.say(embed=embed)
    else:
    	    await bot.say("```Only bot owner```")    	    
    	    
    	         
@bot.command(pass_context=True)
async def status1(ctx):
    author = ctx.message.author
    if ctx.message.author.id == '428298038612590612':
                await bot.change_presence(game=discord.Game(name='now '+str(len(bot.servers))+' servers and'' '+str(len(set(bot.get_all_members())))+' user! ', type=1))    	
                embed = discord.Embed(color=0xb5ff29)
                embed.add_field(name="ِGame:", value="Succesfully game name changed with: status1")
                await bot.say(embed=embed)
                
    else:
                await bot.say("```Only bot owner```")
                
@bot.command(pass_context=True)
async def hack(ctx, hack: discord.User=None):	
   if hack is None:
     embed = discord.Embed(color=0xb5ff29)   	
     embed.add_field(name="ِLOL", value="You need hack yourself ? start with shut down phone/pc")
     await bot.say(embed=embed)
   else:
     embed = discord.Embed(color=0xb5ff29)
     loc = ['United States','United Kingdom','Turkey','India','Polish']
     resp = embed.add_field(name="Hack", value="Location:  {}".format(random.choice(loc)))
     resp = embed.add_field(name="ِMail:", value="I'm searching mail...")
     resp = await bot.say(embed=embed)   
     await asyncio.sleep(5)       
     embed = discord.Embed(colour=discord.Colour.magenta()) 
     mails = ['gmail.com','hotmail.com','outlook.com','yahoo.com']      
     hack = hack.name         
     embed.add_field(name="Hack " + hack,value=f"Mail: `"+ hack +"****@{}`".format(random.choice(mails)))
     pas = ['8618**92','playe*','937*8*99','123456**']
     embed.add_field(name="-",value="Password: `" + hack +"{}`" .format(random.choice(pas)))     
     await bot.edit_message(resp, embed=embed)  
     embed = discord.Embed(color=0xb5ff29)
     ip = ['931.*61.3*9.**.03','82.4*1.913.**.43','172.9****.352.**.36','71.58*1.81.**','51.8**2.61.9*']
     lmao = embed.add_field(name="Hack", value=hack + " IP Adress: {}".format(random.choice(ip)))
     lmao = embed.add_field(name="Succesfully get Real IP", value="Ping/DDoS Attack: {}".format(random.choice(ip)))
     lmao = await bot.say(embed=embed) 
     await asyncio.sleep(6)        
     embed = discord.Embed(colour=discord.Colour.green()) 
     device = ['Android 4.4.4.4','Android 5.1.1','Android 7.1.1','Iphone 6s','Windows 7','Windows 8','Windows 10','Iphone X']          
     embed.add_field(name="Hack " + hack,value="Device:  {}".format(random.choice(device)))     
     await bot.edit_message(lmao, embed=embed)
    
    
@bot.command(pass_context=True)
async def ping(ctx):	
     embed = discord.Embed(colour=discord.Colour.blue())
     resp = embed.add_field(name="Ping", value="Loading", inline=True)
     resp = await bot.say(embed=embed)  
     diff = resp.timestamp - ctx.message.timestamp
     embed = discord.Embed(colour=discord.Colour.magenta()) 
     embed.add_field(name="Ping",value=f"Bot ping {1000*diff.total_seconds():.1f}ms requested by " +ctx.message.author.mention, inline=True)
     await bot.edit_message(resp, embed=embed) 

def is_owner(ctx):
    return ctx.message.author.id == " 428298038612590612" 

@bot.command(pass_context = True)
async def bans(ctx):
    x = await bot.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Members", description = x, color = 0xFFFFF)
    return await bot.say(embed = embed) 


@bot.command(pass_context=True)
async def createtxtchannel(ctx, channel=None):
     if channel is None:
     	embed = discord.Embed(title="Missing argument".format(ctx.message.author.name), description="Please enter argument. example: k!createtxtchannel fun", color=0xffaa00)
     	await bot.say(embed=embed)
     	return
     if ctx.message.author.server_permissions.manage_channels or ctx.message.author.id == is_owner:
     	server = ctx.message.server
     	await bot.create_channel(server, channel, type=discord.ChannelType.text)
     	embed = discord.Embed(title="Channel".format(ctx.message.author.name), description="Succesfully, channel created channel name: "+channel, color=0xffaa00)
     	embed.add_field(name="Created by :", value=ctx.message.author.mention, inline=True)     	     	
     	embed.set_thumbnail(url=ctx.message.author.avatar_url)    	
     	await bot.say(embed=embed)
     else:     	
     	embed = discord.Embed(title="No permission".format(user.name), description="You need manage channels permission.", color=0xf800)
     	await bot.say(embed=embed)     
     	
     	
     	
@bot.command(pass_context=True)
async def createvcchannel(ctx, channel=None):
     if channel is None:
     	embed = discord.Embed(title="Missing argument".format(ctx.message.author.name), description="Please enter argument. example: k!createvcchannel fun", color=0x000000)
     	await bot.say(embed=embed)
     	return
     if ctx.message.author.server_permissions.manage_channels or ctx.message.author.id == is_owner:
     	server = ctx.message.server
     	await bot.create_channel(server, channel, type=discord.ChannelType.voice)
     	embed = discord.Embed(title="Voice Channel".format(ctx.message.author.name), description="Succesfully, voice channel created channel name: "+channel, color=0x000000)
     	embed.add_field(name="Created by :", value=ctx.message.author.mention, inline=True)     	     	
     	embed.set_thumbnail(url=ctx.message.author.avatar_url)    	
     	await bot.say(embed=embed)
     else:     	
     	embed = discord.Embed(title="No permission".format(user.name), description="You need manage channels permission.", color=0x000000)
     	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    await bot.say(':ok_hand:')	

queues = {"488302047749": "497833617590976514"}
players = {"488302047749": "497833617590976514"}
@bot.command(pass_context=True)
async def play(ctx, *,url):
    server = ctx.message.server
    voice = bot.voice_client_in(server)
    player = await voice.create_ytdl_player(url, after = lambda: check_queue(server.id))
    if server.id in queues or players[server.id].is_done():
        queues[server.id].append(player)
        player.start()    
       
    
    else:
        queues[server.id] = [player]

        await bot.say("**🔎 Research of** `" + player.title + "`** In ...**")
        await bot.say("⏳ **Music added to queue !**")
 
        
@bot.command(pass_context=True)
async def pause(ctx):
    await bot.say(':ok_hand:')	
    player.pause()

@bot.command(pass_context=True)
async def resume(ctx):
    await bot.say(':ok_hand:')	
    player.resume()
          
@bot.command(pass_context=True)
async def volume(ctx, vol):
    await bot.say('I changed volume!')	
    vol = float(vol)
    vol = player.volume

@bot.command(pass_context=True)
async def stop(ctx):
    await bot.say('**Alright, I can stop song and disconnect**')
    server=ctx.message.server
    voice=bot.voice_client_in(server)
    await voice.disconnect()

@bot.command(pass_context=True)
async def rps(context):
        rps = await bot.say("**I choose ** :grey_question: \n\n I'm waiting for you :smirk:")
        reponses = ["✊", "🖐", "✌"]
        bot_response = random.choice(reponses)
        reactions = await bot.add_reaction(rps, '✊'),  await bot.add_reaction(rps, '🖐'), await bot.add_reaction(rps, '✌')

        def check(reaction, user):
                return user != bot.user
    
        reaction = await bot.wait_for_reaction(message=rps, check=check)

        if str(reaction.reaction.emoji) == "✊":
                if bot_response == "✊":
                    await bot.edit_message(rps, "I choose ✊ \n\n**Draw ! :joy:**")
                if bot_response == "✌":
                    await bot.edit_message(rps, "I choose ✌ \n\n**You win ! :angry:**")
                if bot_response == "🖐":
                    await bot.edit_message(rps, "I choose 🖐 \n\n**You loose ! :astonished: **")

        if str(reaction.reaction.emoji) == "🖐":
                if bot_response == "✌":
                    await bot.edit_message(rps, "I choose ✌ \n\n**You loose ! :astonished: **")
                if bot_response == "🖐":
                    await bot.edit_message(rps, "I choose 🖐 \n\n**Draw ! :joy:**")
                if bot_response == "✊":
                    await bot.edit_message(rps, "I choose ✊ \n\n**You win ! :angry:**")

        if str(reaction.reaction.emoji) == "✌":
                if bot_response == "✊":
                    await bot.edit_message(rps, "I choose ✊ \n\n**You loose ! :astonished:**")
                if bot_response == "🖐":
                    await bot.edit_message(rps, "I choose 🖐 \n\n**You win  !  :angry:**")
                if bot_response == "✌":
                    await bot.edit_message(rps, "I choose ✌ \n\n**Draw ! :joy:**")	

@bot.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    if user is ctx.message.author:
        await bot.say(ctx.message.author.mention)
        embed2 = discord.Embed(title="Awww I see you're lonely...")
        embed2.set_image(url='https://cdn.discordapp.com/attachments/485437458817744934/493845789609689089/1496032842_gif7.gif') 
        await bot.say(embed=embed2)    
        return	
    if user is not None:
        await bot.say(user.mention)
        embed = discord.Embed(title="{} You got hugged by {} ! So cute 🖤".format(user.name, ctx.message.author.name), color=0xDEA6D5)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/469160650132815900/494949506530672670/giphy_1.gif")
        embed.set_footer(text='lilcsz#5890 - Kermit Bot')
        choices = [' https://cdn.discordapp.com/attachments/469160650132815900/495247102822318080/tenor_1.gif','https://cdn.discordapp.com/attachments/469160650132815900/501779813917523978/original.gif', 'https://cdn.discordapp.com/attachments/469160650132815900/494940557253017610/unnamed_4.gif', 'https://cdn.discordapp.com/attachments/469160650132815900/494940558230552607/unnamed_3.gif',' https://cdn.discordapp.com/attachments/469160650132815900/495245917306355722/tenor_5.gif',' https://cdn.discordapp.com/attachments/469160650132815900/495246505595109386/tenor_4.gif',' https://cdn.discordapp.com/attachments/469160650132815900/495247036015443979/tenor_2.gif','  https://cdn.discordapp.com/attachments/469160650132815900/494940556707889152/unnamed_1.gif',' https://cdn.discordapp.com/attachments/469160650132815900/495247250901958656/tenor.gif']  
        embed.set_image(url=random.choice(choices))
        await bot.say(embed=embed)
        return   
    else:
        await bot.say(ctx.message.author.mention)
        embed1 = discord.Embed(title="Awww I see you're lonely...")
        embed1.set_image(url='https://cdn.discordapp.com/attachments/485437458817744934/493845789609689089/1496032842_gif7.gif')
        await bot.say(embed=embed1)

players = {"497833617590976514"}
queues = {"497833617590976514"}
def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()	

@bot.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice = bot.voice_client_in(server)
    player = await voice.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if not server.id in players or players[server.id].is_done():
        queues[server.id].append(player)

    else:
        queues[server.id] = [player]
    await bot.say('Video Has Been Queued!')
    
    
@bot.command(pass_context=True)
async def next(ctx, url):
    server = ctx.message.server
    voice = bot.voice_client_in(server)
    player = await voice.create_ytdl_player(url, after = lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]

        await bot.say("**:mag_right: Research of** `" + player.url + "`** In progress...**")
        await bot.say(":hourglass_flowing_sand: **Music added to queue !**") 

@bot.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
  if user is None:
        embed = discord.Embed(colour = discord.Colour.blue())
        author = ctx.message.author
        pfp = author.avatar_url
        embed.set_author(name="Avatar")
        embed.set_image(url=pfp)
        await bot.say(embed = embed)		
        return
  else:		
         embed = discord.Embed(colour = discord.Colour.blue())
         pfp = user.avatar_url
         embed.set_author(name="Avatar")
         embed.set_image(url=pfp)
         await bot.say(embed = embed)

@bot.command()
async def russian():
 	await bot.say('vodka')

@bot.command() 	
async def rage():
    await bot.say('idiots reeeeeeee')


@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def role(ctx, user:discord.User,*,role:discord.Role):
	if role not in user.roles:
            await bot.add_roles(user, role)
            return await bot.say(":white_check_mark: Succesfully added **{}** role to **{}**".format(role, user)) 
	if role in user.roles:
            await bot.remove_roles(user, role)
            return await bot.say(":white_check_mark: Succesfully deleted **{}** role from **{}**".format(role, user))

 
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def delrole(ctx, user:discord.User,*,role:discord.Role):
	await bot.remove_roles(user, role)
	await bot.say(' :white_check_mark: Succesfully deleted **{}** role from {}**'.format(role, user))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
	if ctx.message.author.server_permissions.kick_members or ctx.message.author.id == is_owner:
		embed = discord.Embed(title="Kicked".format(user.name), description="User Info :", color=0xf800)
		embed.add_field(name="Username :", value=user.name, inline=True)
		embed.add_field(name="ID :", value=user.id, inline=True)
		embed.add_field(name="Moderator :", value=ctx.message.author.name, inline=True)
		embed.set_thumbnail(url=user.avatar_url)
		await bot.say(embed=embed)
		await bot.kick(user)		 
	else:
		embed = discord.Embed(title="No permission".format(user.name), description="You need kick members permission.", color=0xf800)
		await bot.say(embed=embed)    
    
@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
     if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == is_owner:	
        embed = discord.Embed(title="Banned".format(user.name), description="User Info :", color=0xf800)
        embed.add_field(name="Username :", value=user.name, inline=True)
        embed.add_field(name="ID :", value=user.id, inline=True)
        embed.add_field(name="Moderator :", value=ctx.message.author.mention, inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        await bot.ban(user)
        await bot.say(embed=embed)
     else:
     	embed = discord.Embed(title="No permission".format(user.name), description="You need kick members permission.", color=0xf800)
     	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def botowner(ctx):
   embed = discord.Embed(name="Cloud Bot", description="Bot Owner is: lilcsz#5890 send DM for help.", color=0xff00f6)
   await bot.say(embed=embed)

@bot.command(pass_context = True)
async def say(ctx, *args):
    message = ' '.join(args)	
    if "@everyone" in ctx.message.content or "@here" in ctx.message.content:     
             await bot.say("I don't know why you mention everyone/here with say command...," +ctx.message.author.mention)  
             return              
    if "discord.gg" in ctx.message.content or "https://discord.gg" in ctx.message.content: 
             await bot.say("Please don't make adversting with say command author:" +ctx.message.author.mention)     
             return
    else:
             await bot.say(message) 
        
@bot.command(pass_context = True)
async def spacefont(ctx, *, args):
    mesg = ' '.join(args)
    if ctx.message.mention_everyone or ctx.message.content == "@everyone" or ctx.message.content == "@here": 
        await bot.say("You may not tag everyone/here in this command, "+ctx.message.author.mention)
    else:
        await bot.say(mesg)
    
@bot.command(pass_context = True)
async def userinfo(ctx, user: discord.Member):
   embed = discord.Embed(name="Users Info!", description="Here's what I could find about the user.", color=0xff00f6)
   embed.set_author(name="{}'s info.".format(user.name))
   embed.add_field(name="Users Name", value=user.name, inline=True)
   embed.add_field(name="Users ID", value=user.id, inline=True)
   embed.add_field(name="Users Status", value=user.status, inline=True)   
   embed.add_field(name="Server Joined at", value=user.joined_at, inline=True) 
   embed.add_field(name="Discord Joined at", value=user.created_at, inline=True)
   await bot.say(embed=embed)                         
@bot.command(pass_context = True, aliases=['Mute','m'])
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_roles or is_owner:
         try:
            author = ctx.message.author
            server = ctx.message.server     
            perms = discord.Permissions(send_messages=False, read_messages=True)
            if author is member:
                lol = discord.Embed(title = 'Oops!', description = "You can't mute yourself", color=0x000000)
                await bot.say(embed=lol)
                return
            elif discord.utils.get(server.roles, name='kermit-mute'):
                pass
            else: 
                 await bot.create_role(server, name='kermit-mute', permissions=perms)
            role = discord.utils.get(server.roles, name='kermit-mute')
            await bot.add_roles(member, role)
            embed=discord.Embed(title="Muted", color=0x000000)
            embed.add_field(name="**__User:__**", value="{}".format(member.mention), inline=False)
            embed.add_field(name="**__Moderator:__**", value="**{}**".format(ctx.message.author.mention), inline=False)

            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/469160650132815900/500993296756375553/Mute_1.png')
            await bot.say(embed=embed)
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            overwrite.read_messages = True
            overwrite.add_reactions = False
            overwrite.send_tts_messages = False
            overwrite.read_message_history = False
            overwrite.create_instant_invite = False
            overwrite.administrator = False
            overwrite.attach_files = False
            overwrite.manage_messages = False
            overwrite.mention_everyone = False
            overwrite.use_external_emojis = False
            overwrite.manage_permissions = False
            await bot.edit_channel_permissions(ctx.message.channel, role, overwrite)
         except discord.errors.Forbidden:
             poop = discord.Embed(title = "❎ No Permission", description= "I don't have the `MANAGE_CHANNEL/MANAGE_ROLES` permission.", color = 0x000000)
             msg = await bot.say(embed=poop)
             return
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x000000)
        await bot.say(embed=embed)        
        
@bot.command(pass_context = True)
async def givemod(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '428298038612590612':
        role = discord.utils.get(member.server.roles, name='Moderator')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Moderator now!", description="**{0}** is get Moderator role from **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)       
        
@bot.command(pass_context=True)
async def delmod(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Moderator')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User Not Moderator Now!", description="**{0}** is not Moderator now!".format(member, ctx.message.author), color=0x6b009c)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await bot.say(embed=embed)        
                
@bot.command(pass_context=True)
async def deletethis(ctx):
    await bot.say('Ok!')
    await bot.delete_message(ctx.message)
    await bot.say('**Message deleted!**')

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)                                                                            
@bot.command(aliases=['server', 'sinfo', 'si'], pass_context=True, invoke_without_command=True)
async def serverinfo(ctx, *, msg=""):
        if ctx.invoked_subcommand is None:
            if msg:
                server = None
                try:
                    float(msg)
                    server = bot.get_guilds(int(msg))
                    if not server:
                        return await ctx.send(
                                              bot.bot_prefix + 'Server not found.')
                except:
                    for i in bot.server:
                        if i.name.lower() == msg.lower():
                            server = i
                            break
                    if not server:
                        return await ctx.send(bot.bot_prefix + 'Could not find server. Note: You must be a member of the server you are trying to search.')
            else:
                server = ctx.message.server

            online = 0
            for i in server.members:
                if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                    online += 1
            all_users = []
            for user in server.members:
                all_users.append('{}#{}'.format(user.name, user.discriminator))
            all_users.sort()
            all = '\n'.join(all_users)



            role_count = len(server.roles)
            emoji_count = len(server.emojis)
            if (ctx.message):
                em = discord.Embed(color=0xea7938)
                em.add_field(name='Name', value=server.name)
                em.add_field(name='Owner', value=server.owner, inline=False)
                em.add_field(name='Members', value=server.member_count)
                em.add_field(name='Currently Online', value=online)
                em.add_field(name='Region', value=server.region)
                em.add_field(name='Verification Level', value=str(server.verification_level))
                em.add_field(name='Highest role', value=server.role_hierarchy[0])
                em.add_field(name='Number of roles', value=str(role_count))
                em.add_field(name='Number of emotes', value=str(emoji_count))
                em.add_field(name='Created At', value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.set_thumbnail(url=server.icon_url)
                em.set_author(name='Server Info', icon_url='https://cdn.discordapp.com/attachments/490854053337759779/499271024278241301/kermit-tea-png-2.png')
                em.set_footer(text='Server ID: %s' % server.id)
                await bot.say(embed=em)
                
                
@bot.command(aliases=['help', 'helps', 'hp'], pass_context=True)
async def h(ctx):
         embed = discord.Embed(colour=discord.Colour.green()) 
         embed.add_field(name='Moderation Commands',value="Reaction: 🔍", inline=True)
         embed.add_field(name='Fun Commands',value="Reaction: 🍹", inline=True)
         embed.add_field(name='Information Commands',value="Reaction: 💾", inline=True)
         embed.add_field(name='Image Commands',value="Reaction: 🎨", inline=True)                  
         message = await bot.say(embed=embed)   
         reaction = await bot.add_reaction(message,'🔍'), await bot.add_reaction(message,'🍹'), await bot.add_reaction(message,'💾'), await bot.add_reaction(message,'🎨')
         reaction = await bot.wait_for_reaction(message=message, user = ctx.message.author)
         if str(reaction.reaction.emoji) == "🔍":
         	em = discord.Embed(color=0xea7938)
         	em.add_field(name='Moderation Commands',value="`k!ban`, `k!kick`, `k!mute`, `k!unmute`, `k!warn`, `k!role`, `k!delrole`, `k!clear`, `k!nickname`, `k!createtxtchannel`, `k!createvcchannel`", inline=True)
         	await bot.say(embed=em)  
         elif str(reaction.reaction.emoji) == "🍹":		
                em = discord.Embed(colour=discord.Colour.purple()) 
                em.add_field(name='Fun Commands',value="`k!dice`, `k!rateidiot`, `k!rate`, `k!anonim_msg`, `k!say`, `k!hug`, `k!spacefont`", inline=True)
                message = await bot.say(embed=em)
         elif str(reaction.reaction.emoji) == "💾":
                emb =  discord.Embed(colour=discord.Colour.magenta()) 
                emb.add_field(name='Information Commands',value="`k!serverinfo`, `k!userinfo`, `k!invitebot`, `k!botowner`, `k!ping`, `k!report`, `k!idea`", inline=True)
                message = await bot.say(embed=emb)
         elif str(reaction.reaction.emoji) == "🎨":                                
                emb =  discord.Embed(colour=discord.Colour.magenta()) 
                emb.add_field(name='Image Commands',value="`k!byemom`, `k!rip`, `k!sale`, `k!google`, `k!tweetdt`", inline=True)         
                message = await bot.say(embed=emb)
 
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await bot.send_message(userName, "You have been warned for: **{}**".format(message))
    await bot.say(":warning: __**{0} Has Been Warned!**__:warning:  **Reason:{1}** ".format(userName,message))   

@bot.command(pass_context=True)
async def nickname(ctx, member: discord.Member=None, *, newnick=None):
        if ctx.message.author.server_permissions.manage_nicknames:
            if member is None:
              embed=discord.Embed(color=0x00ffd9)
              embed.add_field(name="Member None", value="**Please specify a user**")
              await bot.say(embed=embed)            
              return
            elif newnick is None:
            	embed=discord.Embed(color=0x00ffd9)
            	embed.add_field(name="Nickname None", value="**Please specify a nickname**")
            	await bot.say(embed=embed)
            	return
            author = ctx.message.author
            await bot.change_nickname(member, newnick)
            embed=discord.Embed(color=0x00ffd9)
            embed.add_field(name="Nickname changed:", value="** **")
            embed.add_field(name="Author", value=f"{ctx.message.author}")
            embed.add_field(name="User:", value=f"{member}")
            embed.add_field(name="New nickname:", value=f"{newnick}")
            await bot.say(embed=embed)	
	
@bot.command(pass_context=True)
async def invitebot(ctx):
	   embed=discord.Embed(title="Click Here", url="https://goo.gl/eWhCmz", description=" ", color=0xa8ddff)
	   embed.set_author(name="Kermit Bot")
	   embed.set_footer(text="You can add my bot to your server here")
	   embed.set_thumbnail(url="https://image.ibb.co/cw36B9/unnamed-1.jpg")
	   await bot.say(embed=embed)
@bot.command()
async def dice(numbers=None):
	if numbers is None:
		embed = discord.Embed(colour=discord.Colour.green()) 
		embed.add_field(name='Dice',value="🎰 **Please chose number from 0-10**")
		await bot.say(embed=embed)
		return
		numbers = ['1','2','3','4','0','5','6','7','8','9','10']				
	if numbers is not None:		
	          numbers = ['1','2','3','4','0','5','6','7','8','9','10']
	          embed = discord.Embed(colour=discord.Colour.blue()) 
	          embed.add_field(name='Dice',value="🎰 **You chose number: {}**".format(random.choice(numbers)))
	          await bot.say(embed=embed)
@bot.command()
async def rate(target: discord.Member):
           cards = ['-99999999999','10/10','0/9','0/8','0/7','0/6','0/5', '0/4','0/3','0/2','0/1']		
           embed = discord.Embed(colour=discord.Colour.green())                 
           embed.add_field(name='Rate',value=target.mention + " 🤔 **I give it to him** **{}**".format(random.choice(cards)))
           await bot.say(embed=embed)	

@bot.command(pass_context = True)
async def anonim_msg(ctx, userName: discord.User, *, content): 
    await bot.send_message(userName, f"**You get message from unknown user, message:** {content}")
    await asyncio.sleep(0.2)        
    await bot.delete_message(ctx.message)
    await bot.say(f"**I sent it to the user, user name: {userName}**")	
@bot.command(pass_context=True)
async def rateidiot(ctx, target: discord.Member=None):
	if target is None:
              cards = ['%19 idiot','%32 idiot','%48 idiot','%76 idiot','%100 idiot xDD','%16 idiot','%0 idiot','%5 idiot','%68 idiot','%51 idiot','%66 idiot','%34 idiot','%41 idiot','%24 idiot']
              embed = discord.Embed(colour=discord.Colour.green()) 
              embed.add_field(name='Rate Idiot',value="🎰 " + ctx.message.author.mention + " **is {}**".format(random.choice(cards)))
              await bot.say(embed=embed)
              return
	else:
              cards = ['%19 idiot','%32 idiot','%48 idiot','%76 idiot','%100 idiot xDD','%16 idiot','%0 idiot','%5 idiot','%68 idiot','%51 idiot','%66 idiot','%34 idiot','%41 idiot','%24 idiot']
              embed = discord.Embed(colour=discord.Colour.green()) 
              embed.add_field(name='Rate Idiot',value="🎰 " + target.mention + " **is {}**".format(random.choice(cards)))
              await bot.say(embed=embed)

@bot.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members or ctx.message.author.id == '428298038612590612':
        role = discord.utils.get(member.server.roles, name='kermit-mute')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="**{0}** is unmuted!".format(member, ctx.message.author), color=0x6b009c)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await bot.say(embed=embed)   		       


@bot.command(pass_context=True)
async def cancerspam(ctx):
    await bot.say('Sorry... command removed use k!raid')                       

@bot.command(pass_context=True)
async def hello(ctx):                                
	await bot.say('Hello! https://cdn.discordapp.com/attachments/490854053337759779/490859394809200650/text.gif')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def raid(ctx):
    await bot.say('successfully') 
    await asyncio.sleep(1)
    await bot.say('QQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    await asyncio.sleep(1)    
    await bot.say('QQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    await asyncio.sleep(1)     
    await bot.say('QQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    await asyncio.sleep(1)
    await bot.say('QQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    await asyncio.sleep(1)
    await bot.say('QQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    await asyncio.sleep(1)
    await bot.say('QQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQ QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')		       
@bot.command(pass_context = True)
async def stupid(ctx, userName: discord.User): 
    await bot.say("**{0}** is stupid lmaooooo ".format(userName)) 		       
bot.run(os.environ['BOT_TOKEN'])
