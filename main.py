import requests
import requests_cache
import sys
import json
from art import tprint
from functools import reduce
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter, DeduplicateCompleter, NestedCompleter, merge_completers
from fuzzyfinder import fuzzyfinder
from style import style, styleDict
from cards import display_card

requests_cache.install_cache(expire_after=36000)

def main():
    print(styleDict['bold'])
    tprint("Hortum-CLI",font="cyberlarge")
    print(styleDict['clear'])
    print('''Developed by Aurora Long
2021
https://github.com/GooseLong/HortumCLI
PRs Welcome!
''')
    while True:
        try:
            sess = PromptSession()
            print(style('loading'+style('...',['blinking']),['bold','italic']))
            cards_r = requests.get('https://netrunnerdb.com/api/2.0/public/cards')
            packs_r = requests.get('https://netrunnerdb.com/api/2.0/public/packs')
            delete_last_line()
            cards = json.loads(cards_r.text)['data']
            packs = json.loads(packs_r.text)['data']
            card_names = list(map(lambda x: x['stripped_title'], cards))
            #autocomplete = reduce(lambda a,b: {**a,**b}, list(map(lambda x: reduce(lambda a,b: {b:a}, (x.split()+[None])[::-1]), card_names)))
            p = sess.prompt('> ', completer=DeduplicateCompleter(FuzzyWordCompleter(card_names))) 
            #p = sess.prompt('> ', completer=DeduplicateCompleter(merge_completers([NestedCompleter.from_nested_dict(autocomplete),FuzzyWordCompleter(card_names)])), complete_while_typing=True)
            suggestions = list(fuzzyfinder(p.strip(), card_names))
            card = list(filter(lambda x: x['stripped_title'] == suggestions[0], cards))[0]
            pack = list(filter(lambda x: x['code'] == card['pack_code'], packs))[0]
            display_card(card, pack['cycle_code'], pack['name'])
        except KeyboardInterrupt:
            break

def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


if __name__ == '__main__':
    main()