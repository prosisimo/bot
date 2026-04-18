import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
@bot.command()
async def calentamiento(ctx):
    await ctx.send("hola soy el bot que te va a enseñar sobre el calentamiento global")
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    with open('images/mem1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def pregunta(ctx, *, texto_pregunta: str):
    # Convertimos la pregunta a minúsculas para evitar problemas con mayúsculas/minúsculas
    pregunta_minusculas = texto_pregunta.lower()

    # Evaluamos qué palabras clave están dentro de la pregunta del usuario
    if "qué es" in pregunta_minusculas or "que es" in pregunta_minusculas:
        respuesta = "🌍 **El calentamiento global** es el aumento a largo plazo de la temperatura media del sistema climático de la Tierra, debido principalmente a la actividad humana."
        
    elif "causas" in pregunta_minusculas or "por qué" in pregunta_minusculas or "por que" in pregunta_minusculas:
        respuesta = "🏭 **Las principales causas** incluyen la quema de combustibles fósiles (carbón, petróleo y gas), la deforestación de los bosques y la agricultura industrial, que emiten grandes cantidades de gases de efecto invernadero."
        
    elif "consecuencias" in pregunta_minusculas or "efectos" in pregunta_minusculas:
        respuesta = "🌊 **Las consecuencias** son severas: derretimiento de los glaciares, aumento del nivel del mar, eventos climáticos extremos (como sequías y huracanes más fuertes) y la pérdida de biodiversidad."
        
    elif "solución" in pregunta_minusculas or "evitar" in pregunta_minusculas or "qué hacer" in pregunta_minusculas:
        respuesta = "🌱 **Para ayudar a mitigarlo** podemos reducir nuestra huella de carbono: usar transporte público o bicicleta, ahorrar energía en casa, reciclar, reducir el consumo de carne y apoyar las energías renovables."
        
    else:
        # Si no detecta ninguna palabra clave de las anteriores
        respuesta = "Lo siento, no estoy seguro de cómo responder a eso. Intenta preguntarme sobre las **causas**, **consecuencias**, o **qué es** el calentamiento global."

    # Enviamos la respuesta calculada
    await ctx.send(respuesta)

bot.run("TU_TOKEN_AQUI")