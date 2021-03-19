
styleDict = { 
    'clear': f'\033[0m',
    'bold': f'\033[1m',
    'dim': f'\033[2m',
    'italic': f'\033[3m',
    'underline': f'\033[4m',
    'blinking': f'\033[5m',
    'anarch': f'\033[38;2;255;106;51m',
    'criminal': f'\033[38;2;65;105;255m',
    'shaper': f'\033[38;2;50;205;50m',
    'haas-bioroid': f'\033[38;2;138;43;226m',
    'jinteki': f'\033[38;2;220;20;60m',
    'nbn': f'\033[38;2;255;140;0m',
    'weyland-consortium': f'\033[38;2;0;100;0m',
    'adam': f'\033[38;2;173;167;73m',
    'sunny-lebeau': f'\033[38;2;196;196;196m',
    'apex': f'\033[38;2;231;57;56m',
    'neutral-runner': '',
    'neutral-corp': ''
}

def style(string, styles):
    return ''.join(map(lambda x: styleDict[x],styles)) + string + styleDict['clear']

