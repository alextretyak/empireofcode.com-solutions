from battle import commander
unit_client = commander.Client()

def attack_center(*args, **kawargs):
    center = unit_client.ask_center()
    unit_client.do_attack(center['id'])
attack_center()
