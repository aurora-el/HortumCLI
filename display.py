from style import style, styleDict

def display_info(title, faction_code, name, cycle, uniqueness=False):
    return f"{style('♦',['bold','underline']) if uniqueness else ''}{display_title(title)} {display_faction(faction_code)}  {display_pack(name,cycle)}"


def display_types(type_code, keywords):
    return f"{display_type(type_code)} {keywords}"

def display_title(title):
    return style(title, ['bold','underline'])

def display_faction(faction):
    if faction == 'anarch':
        return style('',['anarch'])
    elif faction == 'criminal':
        return style('', ['criminal'])
    elif faction == 'shaper':
        return style('', ['shaper'])
    elif faction == 'haas-bioroid':
        return style('', ['haas-bioroid'])
    elif faction == 'jinteki':
        return style('', ['jinteki'])
    elif faction == 'nbn':
        return style('', ['nbn'])
    elif faction == 'weyland-consortium':
        return style('', ['weyland-consortium'])
    elif faction == 'adam':
        return style('',['adam'])
    elif faction == 'sunny-lebeau':
        return style('',['sunny-lebeau'])
    elif faction == 'apex':
        return style('',['apex'])
    elif faction.startswith('neutral'):
        return ' '
    else:
        return '?'



def display_pack(name,cycle):
    cycle_symbol = '?'
    if cycle == 'core':
        cycle_symbol = ''
    if cycle == 'genesis':
        cycle_symbol = ''
    if cycle == 'creation-and-control':
        cycle_symbol = ''
    if cycle == 'spin':
        cycle_symbol = ''
    if cycle == 'honor-and-profit':
        cycle_symbol = ''
    if cycle == 'lunar':
        cycle_symbol = ''
    if cycle == 'order-and-chaos':
        cycle_symbol = ''
    if cycle == 'sansan':
        cycle_symbol = ''
    if cycle == 'data-and-destiny':
        cycle_symbol = ''
    if cycle == 'mumbad':
        cycle_symbol = ''
    if cycle == 'flashpoint':
        cycle_symbol = ''
    if cycle == 'red-sand':
        cycle_symbol = ''
    if cycle == 'terminal-directive':
        cycle_symbol = ''
    if cycle == 'core2':
        cycle_symbol = ''
    if cycle == 'kitara':
        cycle_symbol = ''
    if cycle == 'reign-and-reverie':
        cycle_symbol = ''
    if cycle == 'magnum-opus':
        cycle_symbol = ''
    if cycle == 'sc19':
        cycle_symbol = ''
    if cycle == 'ashes':
        cycle_symbol = ''
    if cycle == 'magnum-opus-reprint':
        cycle_symbol = ''
    if cycle == 'salvaged-memories':
        cycle_symbol = ''
    if cycle == 'system-gateway':
        cycle_symbol = ''
    if cycle == 'system-update-2021':
        cycle_symbol = ''
    return f"   [ {name} {cycle_symbol} ]"


def display_type(card_type):
    return style(card_type.capitalize(),['italic','bold'])

def display_text(text):
    return text \
        .replace('<strong>', styleDict['bold']) \
        .replace('</strong>', styleDict['clear']) \
        .replace('<trace>', styleDict['bold']) \
        .replace('</trace>', '-'+styleDict['clear']) \
        .replace('<em>', styleDict['italic']) \
        .replace('</em>', styleDict['clear']) \
        .replace('<errata>', styleDict['dim']) \
        .replace('</errata>', styleDict['clear']) \
        .replace('<ul>', '\n') \
        .replace('</ul>', '') \
        .replace('<li>', '• ') \
        .replace('</li>', '\n') \
        .replace('his or her', 'their') \
        .replace('[credit]', '') \
        .replace('[click]',' ') \
        .replace('[recurring-credit]','') \
        .replace('[trash]',' ') \
        .replace('[mu]',' ') \
        .replace('[link]','') \
        .replace('[interrupt]','') \
        .replace('[anarch]','') \
        .replace('[criminal]','') \
        .replace('[shaper]','') \
        .replace('[haas-bioroid]','') \
        .replace('[jinteki]','') \
        .replace('[nbn]','') \
        .replace('[weyland-consortium]','') \
        .replace('[subroutine]', '⮡')

def display_flavor(flavor):
    return style(flavor.replace('<champion>', styleDict['dim']).replace('</champion>', styleDict['clear']), ['dim','italic'])
