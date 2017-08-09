from battle import commander, ROLE
unit_client = commander.Client()

def search_target(data=None, **kwargs):
    unit_client.do_move([25, 35])
    unit_client.when_idle(attack_center)

def attack_center(data=None, **kwargs):
    center = unit_client.ask_center()
    unit_client.do_attack(center['id'])
#search_target()

my_info = unit_client.ask_my_info()
#print(my_info['coordinates'])
#print(my_info['id'])

def check_all(data):
    #print(data)
    #print(unit_client.ask_my_info())
    for u in unit_client.ask_my_items():
        if u['state']['action'] != 'idle':
            return
    unit_client.do_message_to_team('attack')
    search_target()

def on_message(a):
    if a['message'] == 'attack':
        search_target()
unit_client.when_message(on_message, False)

def after_landing(data):
    myi = unit_client.ask_my_items()
    unit_client.do_move([40, 35]) # sum(u["coordinates"][1] for u in myi)/len(myi)])
    #unit_client.when_time(16, search_target)
    unit_client.when_idle(check_all)

#after_landing(None)
unit_client.when_time(2, after_landing)