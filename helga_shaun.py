import random

from helga.plugins import command


@command('shaun', aliases=['x'], help='SHAAAAAAAAUUUUN')
def shaun(client, channel, nick, message, cmd, args):
    """
    SHAAAAAAAAUUN
    """
    if random.randint(1, 8) == 5:
        return "snes9x"
    return 'SH{a}{u}N'.format(a='A' * random.randint(1, 10),
                              u='U' * random.randint(1, 3))
