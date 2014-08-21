import random

from helga.plugins import command


@command('shaun', help='SHAAAAAAAAUUUUN')
def shaun(client, channel, nick, message, cmd, args):
    """
    SHAAAAAAAAUUN
    """
    return 'SH{a}{u}N'.format(a='A' * random.randint(1, 10),
                              u='U' * random.randint(1, 3))
