import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import random
import wikipedia
from mcstatus import MinecraftServer
from datetime import datetime
import glob

defaultserver = "sevenbitsci.mooo.com"

partBwords = ["EASY", "SIMPLE", "GENIUS", "BRILIANT", "DELICIOUS", "STUNNING", "EPIC", "CRAZY", "COOL", "WONDERFUL", "USEFUL", "SIMPLE AND FUN", "SIMPLE YED BRILLIANT", "AMAZING", "UNEXPECTED", "CLEANING", "CREATIVE", "CREATIVE YET SIMPLE", "SMART", "HANDY", "FANTASTIC"]
partCwords = ["HACKS", "COOKING IDEAS", "DIYS", "ART IDEAS", "SECRETS", "INSTAGRAM TRICKS", "SCHOOL PRANKS", "CRAFTS", "RECIPES", "SOAP IDEAS", "IDEAS", "LIFE HACKS", "INVENTIONS", "GADGET IDEAS", "IDEAS", "TRICKS", "DIY DECOR IDEAS", "RECIPES", "CLOTHES HACKS", "SCIENCE TRICKS", "NAIL ART"]
partDwords = ["TO HELP YOU SURVIVE", "YOU WISH YOU KNEW SOONER", "TO IMPRESS YOUR FRIENDS", "THAT ARE TOTALlY EASY TO DO", "BEAUTY IDEAS", "TO MAKE YOU SAY WOW", "WITH STUFF YOU HAVE AT HOME", "FROM PRESSIONALS", "YOU SHOULD TRY", "YOU HAVE TO TRY RIGHT NOW", "FOR ANY OCCASION", "THAT LOOK COOL", "YOU NEED TO KNOW", "TO MAKE YOU LOOK COOL", "TO MAKE WHEN YOU ARE BORED", "TO TRY RIGHT NOW", "YOU HAD NO IDEA ABOUT", "YOU SHOULD TRY", "FOR YOUR GADGETS", "THAT WILL SUPRISE YOU", "UNDER $5"]

jokes = ['Whats the best thing about switzerland? ||I dont know, but its a big plus||', 'I invented a new word!\n ||Plagiarism!||', 'Did you hear about the mathematician who’s afraid of negative numbers?\n||He’ll stop at nothing to avoid them.||', 'Why do we tell actors to “break a leg?”\n||Because every play has a cast.||', 'Helvetica and Times New Roman walk into a bar.\n||“Get out of here!” shouts the bartender. “We don’t serve your type.”||', 'Yesterday I saw a guy spill all his Scrabble letters on the road.\n||I asked him, “What’s the word on the street?”||', 'Hear about the new restaurant called Karma?\n||There’s no menu: You get what you deserve.||', 'A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”\n||“Don’t worry,” said the doc. “Those are just contractions.”||', 'A bear walks into a bar and says, “Give me a whiskey and … cola.”\n||“Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”||', 'Did you hear about the actor who fell through the floorboards?\n||He was just going through a stage.||', 'Did you hear about the claustrophobic astronaut?\n||He just needed a little space.||', 'Why don’t scientists trust atoms?\n||Because they make up everything.||', 'Why did the chicken go to the séance?\n||To get to the other side.||', 'Where are average things manufactured?\n||The satisfactory||']

bot = commands.Bot(command_prefix='$')

dice_list = ['side','side','side','heads','heads','tails']

print ('Bot started at ' + str(datetime.now()))

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot) + ' at ' + str(datetime.now()))
	game = discord.Game('with my bot friends!')
	await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def roll(ctx, brief='Voice chat rickroll'):
	channel = ctx.author.voice.channel
	vc = await channel.connect()
	vc.play(discord.FFmpegPCMAudio('rickroll.mp3'), after=lambda e: ctx.voice_client.disconnect())
	print('command sent:roll:' + datetime.now())

@bot.command()
async def ping(ctx, hidden=True):
	await ctx.send('pong')
	print('command sent:ping:' + str(datetime.now()))

@bot.command()
async def null(ctx, hidden=True):
	await ctx.send('sevenbitscience.github.io/Video.mp4')
	print('command sent: :' + str(datetime.now()))

@bot.command()
async def shrek(ctx, brief='Need i say more'):
	await ctx.channel.send('somebody once told me the world is gonna roll me \n i aint the sharpest tool in the shed\n She was looking kind of dumb with her finger and her thumb \n In the shape of an L on her forehead', tts=True)
	print('command sent:shrek:' + str(datetime.now()))

@bot.command()
async def rickroll(ctx, brief='Text chat rickroll'):
	await ctx.channel.send('Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you', tts=True)
	print('command sent:rickroll:' + str(datetime.now()))

@bot.command()
async def coinflip(ctx, brief='Flips a coin'):
	await ctx.channel.send(random.choice(dice_list))
	print('command sent:coinflip:' + str(datetime.now()))

@bot.command()
async def dice(ctx, brief='Rolls a dice'):
	await ctx.channel.send('the dice landed on ||ur mum||')
	print('command sent:dice:' + str(datetime.now()))

@bot.command()
async def craft(ctx, brief='Gives a randomly generated 5 minute craft title'):
	partA = random.randrange(20, 41)
	partB = random.randrange(len(partBwords))
	partC = random.randrange(len(partCwords))
	partD = random.randrange(len(partDwords))
	await ctx.channel.send(str(partA) + ' ' + partBwords[partB] + ' ' + partCwords[partC] + ' ' + partDwords[partD])
	print('command sent:craft:' + str(datetime.now()))

@bot.command()
async def meme(ctx, brief='Randomly selects a meme from our expansive library of memes'):
	await ctx.channel.send(file=discord.File('meme.jpg'))
	print('command sent:meme:' + str(datetime.now()))

@bot.command()
async def stockphoto(ctx, brief='random stock photo'):
	await ctx.channel.send(file=discord.File("stockphotos/" + (str(random.randint(0,len(glob.glob('*.png'))))+'.png')))
	print('command sent:stockphoto:' + str(datetime.now()))

@bot.command()
async def joke(ctx, brief='Tells a joke'):
	await ctx.channel.send(jokes[random.randrange(len(jokes))])
	print('command sent:joke:' + str(datetime.now()))

@bot.command()
async def wiki(ctx, brief='Gives a summary from wikipedia. format:$wiki (search goes here)', *, arg):
    await ctx.channel.send(wikipedia.summary(arg, sentences=1))
    print('command sent:wiki ' + arg + ':' + str(datetime.now()))

@bot.command()
async def status(ctx, *, arg, hidden=True):
	game = discord.Game(arg)
	await bot.change_presence(status=discord.Status.online, activity=game)
	print('command sent:status ' + arg + ':' + str(datetime.now()))

@bot.command()
async def helltaker(ctx, brief='random demon girl'):
	await ctx.channel.send(file=discord.File("helltaker/" + (str(random.randint(0,len(glob.glob('*.png'))))+'.png')))
	print('command sent:helltaker:' + str(datetime.now()))

@bot.command()
async def mc(ctx, *, arg=defaultserver):
    server = MinecraftServer.lookup(arg)
    status = server.status()
    await ctx.channel.send("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

@bot.command()
async def setmc(ctx, *, arg=defaultserver):
    await ctx.channel.send("Set default server to " + defaultserver)
    
@bot.command()
async def addhell(ctx):
    await ctx.channel.message.save('helltaker/' + len(glob.glob('*.png'))+1 + '.png')

# Get key from file
keyFile = open('../Key.txt', 'r')
key = keyFile.read()
keyFile.close()

bot.run(key)
