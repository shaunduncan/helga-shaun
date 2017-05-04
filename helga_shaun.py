import random

from helga.plugins import command


@command('shaun', aliases=['x'], help='SHAAAAAAAAUUUUN')
def shaun(client, channel, nick, message, cmd, args):
    """
    SHAAAAAAAAUUN
    """
    if random.randint(1, 8) == 5:
        return "snes9x"
    if random.randint(1, 16) == 15:
        return "https://twitter.com/ABCPolitics/status/859474856596783104"
    return 'SH{a}{u}N'.format(a='A' * random.randint(1, 10),
                              u='U' * random.randint(1, 3))
