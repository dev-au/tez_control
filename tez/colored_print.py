from termcolor import colored


def colored_print(msg, color):
    msg = msg.lstrip().strip()
    data = msg.split('\n')
    print(colored('_' * len(data[0]), 'yellow',  attrs=['bold']))
    print(colored(msg, color, attrs=['bold']))
    print('🏎\n\n')