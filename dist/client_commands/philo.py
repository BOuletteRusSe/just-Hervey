import random


async def Philo(ctx):

    if random.randint(1, 2) == 1:
        await ctx.reply(
            f"Si {random.choice([word.strip() for word in open('assets/texts/words_list.txt')])} alors {random.choice([word.strip() for word in open('assets/texts/words_list.txt')])}")
    else:
        await ctx.reply(
            f"Qui {random.choice([word.strip() for word in open('assets/texts/words_list.txt')])} se {random.choice([word.strip() for word in open('assets/texts/words_list.txt')])}")
