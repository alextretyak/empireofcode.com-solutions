from battle import commander, ROLE
unit_client = commander.Client()

def search_target(data=None, **kwargs):
    towers = unit_client.ask_towers()
    #print([t["id"] for t in towers])
    if towers:
        tower_id = None
        for t in towers:
            if t['type'] == "rocketGun":
                #tower_id = t['id']
                break
        if not tower_id:
            for t in towers:
                if t['type'] == "machineGun":
                    #tower_id = t['id']
                    break
        if not tower_id:
            tower_id = unit_client.ask_nearest_enemy([ROLE.TOWER])["id"]
        #print(tower_id)
        unit_client.do_attack(tower_id)
        unit_client.when_item_destroyed(tower_id, search_target)
    else:
        attack_center()
    enemy = unit_client.ask_nearest_enemy()

def attack_center(data=None, **kwargs):
    center = unit_client.ask_center()
    unit_client.do_attack(center['id'])
search_target()

my_info = unit_client.ask_my_info()
print(my_info['coordinates'])

# 6666_Fro
# D3 - 26
# D2 - 15,16
# D2 first rocketGun - 23,22,18
# D2 first rocketGun, then machineGun - 28
