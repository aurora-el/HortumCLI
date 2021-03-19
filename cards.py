from display import *

def display_card(card,cycle,pack_name):
    if card['type_code'] == 'identity':
        display_identity(cycle,pack_name,**card)
    elif card['type_code'] == 'event':
        display_event(cycle,pack_name,**card)
    elif card['type_code'] == 'operation':
        display_operation(cycle,pack_name,**card)
    elif card['type_code'] == 'agenda':
        display_agenda(cycle,pack_name,**card)
    elif card['type_code'] == 'hardware':
        display_hardware(cycle,pack_name,**card)
    elif card['type_code'] == 'program':
        display_program(cycle,pack_name,**card)
    elif card['type_code'] == 'resource':
        display_resource(cycle,pack_name,**card)
    elif card['type_code'] == 'asset':
        display_asset(cycle,pack_name,**card)
    elif card['type_code'] == 'upgrade':
        display_asset(cycle,pack_name,**card)
    elif card['type_code'] == 'ice':
        display_ice(cycle,pack_name,**card)



def display_identity(cycle, name, title, faction_code, type_code, minimum_deck_size, influence_limit, side_code, keywords='', text='', base_link=None, flavor = "", **args):
    print(f"""{display_info(title,faction_code,name,cycle)}
{display_type(type_code)} {keywords}
Deck {minimum_deck_size} • Influence {influence_limit}{f' •  {base_link}' if side_code == 'runner' else ''}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))



def display_event(cycle,name,  title, faction_code, type_code, cost, faction_cost, text, flavor='', keywords='', **args):
    print(f"""{display_info(title,faction_code,name,cycle)}
{display_type(type_code)} {keywords}
Cost {cost if cost != None else 'X'} • Influence {faction_cost}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))

def display_operation(cycle,name, title, faction_code, type_code, cost, faction_cost, text, flavor='', keywords='', **args):
    print(f"""{display_info(title,faction_code,name,cycle)}
{display_types(type_code,keywords)}
Cost {cost if cost != None else 'X'} • Influence {faction_cost}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))


def display_agenda(cycle, name, title, faction_code, type_code, advancement_cost, agenda_points, faction_cost, text, flavor='', keywords='', **args):
    print(f"""{display_info(title,faction_code,name,cycle)}
{display_types(type_code,keywords)}
Cost {advancement_cost if advancement_cost != None else 'X'} • Points {agenda_points} • Influence {faction_cost}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))


def display_hardware(cycle,name, title, uniqueness, faction_code, type_code, cost, faction_cost, text, flavor='', keywords='', **args):
    print(f"""{display_info(title,faction_code,name,cycle, uniqueness=uniqueness)}
{display_types(type_code,keywords)}
Cost {cost if cost != None else 'X'} • Influence {faction_cost}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))



def display_program(cycle,name, title, uniqueness, faction_code, type_code, cost, memory_cost, faction_cost, text, flavor='', keywords='', **args):
    print(f"""{display_info(title,faction_code,name, cycle, uniqueness=uniqueness)}
{display_types(type_code,keywords)}
Cost {cost if cost != None else 'X'} • Memory {memory_cost}  • Influence {faction_cost}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))



def display_resource(cycle, name, title, uniqueness, faction_code, type_code, cost, faction_cost, text, flavor='', keywords='', **args):
    print(f"""{display_info(title,faction_code,name,cycle, uniqueness=uniqueness)}
{display_types(type_code,keywords)}
Cost {cost if cost != None else 'X'} • Influence {faction_cost}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))
    
def display_asset(cycle, name, title, uniqueness, faction_code, type_code, cost, trash_cost, faction_cost, text, flavor='', keywords='', **args):
    print(f"""{display_info(title,faction_code,name,cycle, uniqueness=uniqueness)}
{display_types(type_code,keywords)}
Rez {cost if cost != None else 'X'} • Trash {trash_cost}  • Influence {faction_cost}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))

def display_upgrade(cycle,name, title, uniqueness, faction_code, type_code, cost, trash_cost, faction_cost, text, flavor='', keywords='', **args):
    print(f"""{display_info(title,faction_code,name,cycle, uniqueness=uniqueness)}
{display_types(type_code,keywords)}
Rez {cost if cost != None else 'X'} • Trash {trash_cost}  • Influence {faction_cost}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))

def display_ice(cycle,name, title, uniqueness, faction_code, type_code, cost, strength, faction_cost, text, flavor='', keywords='', **args):
    print(f"""{display_info(title,faction_code,name,cycle, uniqueness=uniqueness)}
{display_types(type_code,keywords)}
Rez {cost if cost != None else 'X'} • Strength {strength} • Influence {faction_cost}

{display_text(text)}
{display_flavor(flavor)}""".replace('\n','\n  '))

