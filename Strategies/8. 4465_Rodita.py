from battle import commander, ROLE
unit_client = commander.Client()

def attack(data=None, **kwargs):
    towers = unit_client.ask_towers()
    #print([t["id"] for t in towers])
    #towers = None
    if towers:
        tower_id = None
        for t in towers:
            if t['type'] == "rocketGun":
                #tower_id = t['id']
                break
        if not tower_id:
            tower_id = unit_client.ask_nearest_enemy([ROLE.TOWER])["id"]
        #print(tower_id)
        unit_client.do_attack(tower_id)
        unit_client.when_item_destroyed(tower_id, attack)
    else:
        attack_center()
        
def search_target(data=None, **kwargs):
    unit_client.do_move([20, 3])

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

units_idle = 1

def on_message(a):
    if a['message'] == 'attack':
        search_target()
unit_client.when_message(on_message, False)

#coords=[[40-8.5,21.5],[40-9,19],[40-12,23],[40-11.5,18.5],[40-8.5,24.5],[40-9,27],[40-11.5,27.5]]
coords=[[40-9,19],[40-9,27],[40-12,23],[40-8.5,21.5],[40-8.5,24.5],[40-11.5,18.5],[40-11.5,27.5]]

def after_landing_(data):
    myi = unit_client.ask_my_items()
    unit_client.do_move([40, 3]) # sum(u["coordinates"][1] for u in myi)/len(myi)])
    #unit_client.when_time(16, search_target)
    unit_client.when_idle(search_target)#check_all)
    unit_client.when_time(14, attack)

def after_landing(data):
    print('-----------------------')
    for t in unit_client.ask_towers():
        print(t['coordinates'], end='')
    print('')
    tid = None
    while coords and not tid:
        for t in unit_client.ask_towers():
            if t['coordinates'] == coords[0]:
                tid = t['id']
                break
        coords.pop(0)
    if tid:
        unit_client.do_attack(tid)
        unit_client.when_item_destroyed(tid, after_landing)
    else:
        attack_center()
#after_landing(None)
unit_client.when_time(2, after_landing)
#unit_client.when_time(12, attack)#after_landing)
