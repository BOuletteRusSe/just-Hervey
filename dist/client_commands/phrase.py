
from essential_generators import DocumentGenerator
from deep_translator import GoogleTranslator

async def Phrase(ctx):
    
    gen = DocumentGenerator()
    
    translated = GoogleTranslator(source='en', target="fr").translate(gen.sentence())
    await ctx.reply(translated)
