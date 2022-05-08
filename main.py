import discord 
from discord.ext import commands
from discord.utils import get
from discord_components import Button, ButtonStyle, Interaction
from discord_components import DiscordComponents


bot = commands.Bot(command_prefix = "$")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Ich bin jetzt online")
    DiscordComponents(bot)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('$help'))





@bot.event
async def on_member_join(member):
    channel_willkommen = bot.get_channel(972744719367020565)
    guild = member.guild
    RegelwerkC = guild.get_channel(967174494261215244)
    VerifyC = guild.get_channel(972874707609202688)
    embed_willkommen = discord.Embed(title=f"Willkommmen auf {member.guild.name}", description=f"Willkommen {member.mention}.", colour=discord.Color.random())
    embed_willkommen.add_field(name="📖- Lies die Regeln hier", value=f"{RegelwerkC.mention}", inline=False)
    embed_willkommen.add_field(name="✅- Verifiziere dich bitte hier mit !verify", value=f"{VerifyC.mention}", inline=False)
    embed_willkommen.set_image(url="https://cdn.discordapp.com/attachments/972806429574590544/972875573619744838/IMG_2009.png")
    await channel_willkommen.send(embed=embed_willkommen)


@bot.command()
async def verify(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(
        "Hast du die Regeln gelesen, und möchtest dich verifizieren?",
        components = [
            Button(style=ButtonStyle.blue, label="Ja ✔"),Button(style=ButtonStyle.blue, label="Nein ❌"),
        ]
    )
    res = await bot.wait_for("button_click")
    if res.component.label == "Ja ✔":
        if res.channel == ctx.channel:
            role = discord.utils.get(ctx.guild.roles, id = 967840561639854150)
            await res.author.add_roles(role)
            await res.respond(
                type=4,
                content="Du wurdest vertifiziert"
                )
            await ctx.channel.purge(limit=10)

    if res.component.label == "Nein ❌":
        if res.channel == ctx.channel:
            await res.respond(
                type=4,
                content="Du wurdest nicht vertifiziert"
                )
            await ctx.channel.purge(limit=10)





bot.run('OTcyODA0OTU2ODQxMTgxMjA0.YneZNw.WDsARUOGgAjcikj9EiR2b0qL1Eg')
