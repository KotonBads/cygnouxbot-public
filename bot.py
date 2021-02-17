import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = 'cyg.')

#sens calc

#Made by Cygnoux (https://www.youtube.com/cygnoux)
#Buy me a coffee maybe?: https://www.buymeacoffee.com/cygnoux
#Special thanks to Mrroey & Patchy <3
# - - - - - - - - - -
val1 = [52,51.08333333,50.16666667,49.25,48.33333333,47.41666667,46.5,45.58333333,44.66666667,43.75,42.83333333,41.91666667,41,40.08333333,39.16666667,38.25,37.33333333,36.41666667,35.5,34.58333333,33.66666667,32.75,31.83333333,30.91666667,30]

def sens(argf, base):
    argf = val1[argf]
    s1 = (base*3)/(80/argf)
    s2 = (base*3)/(101/argf)
    s3 = (base*3)/(136/argf)
    s4 = (base*3)/(195/argf)
    s5 = (base*5)/(344/argf)
    s6 = (base*5)/(393/argf)
    return round(s1, 0), round(s2, 0), round(s3, 0), round(s4, 0), round(s5, 0), round(s6, 0)

#bot stuff
#---------
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Cygnoux CODM Sens Calculator open source edition'))

@bot.command(aliases=['sens'])
async def sensitivity(ctx, *, args):
    
    args1 = args.split(' ')
    if int(args1[0]) <= 75:
        s1 = sens(int(args1[0]) - 51, int(args1[1]))[0]
        s2 = sens(int(args1[0]) - 51, int(args1[1]))[1]
        s3 = sens(int(args1[0]) - 51, int(args1[1]))[2]
        s4 = sens(int(args1[0]) - 51, int(args1[1]))[3]
        s5 = sens(int(args1[0]) - 51, int(args1[1]))[4]
        s6 = sens(int(args1[0]) - 51, int(args1[1]))[5]
        
    #embeds to make it pretty
    #------------------------
    embed = discord.Embed(
            colour = discord.Colour.blue()
        )
    embed.set_author(name = 'Sensitivity Values:')
    embed.add_field(name = 'ADS:', value = s1, inline = False)
    embed.add_field(name = 'Tac:', value = s2, inline = False)
    embed.add_field(name = '3x:', value = s3, inline = False)
    embed.add_field(name = '4x:', value = s4, inline = False)
    embed.add_field(name = 'Sniper:', value = s5, inline = False)
    embed.add_field(name = 'Sniper (for quickscope):', value = '{0} or {1}'.format(s5 + (s5/3), round(s5 + (s5/2))), inline = False)
    embed.add_field(name = '6x:', value = s6, inline = False)
    embed.add_field(name = '8x', value = s6, inline = False)
    embed.set_footer(text = 'https://discord.gg/ywKfbpnACs')
    await ctx.send(embed = embed)
    
    #Koton Bads has been here owo

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')

bot.run('BOT TOKEN HERE!!')
