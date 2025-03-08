import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # Habilitar permisos de mensajes

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')

@bot.command()
async def adivina(ctx, numero: int):
    numero_secreto = random.randint(1, 10)
    if numero == numero_secreto:
        await ctx.send(f'🎉 ¡Felicidades {ctx.author.mention}! Adivinaste el número ({numero_secreto}) correctamente. 🎉')
    else:
        await ctx.send(f'❌ Lo siento {ctx.author.mention}, el número era {numero_secreto}. ¡Inténtalo de nuevo!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Suma dos números."""
    await ctx.send(left + right)

@bot.command()
async def sumar(ctx, num1: float, num2: float):
    resultado = num1 + num2
    await ctx.send(f'El resultado de sumar {num1} y {num2} es {resultado}.')

# Reemplaza 'TU_TOKEN_AQUI' con tu token real
bot.run('TU_TOKEN_AQUI')
