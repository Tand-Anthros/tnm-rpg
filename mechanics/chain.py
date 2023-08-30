if 'environment':
    import discord


class MeClient(discord.Client):
    async def on_ready(self):
        print('log:', self.user)


    async def on_messege(self, message):
        print('message:', '{0.author}, {0.content}'.format(message))


def chain():
    client = MeClient(intents=discord.Intents.default())
    client.run('ODgyNjY2ODQ2NTM1NDQ2NTI5.Gj_fOR.K8PiZJIGgl5ZfbIqRAbsUcZc4f8DaiBmV1SQPM')