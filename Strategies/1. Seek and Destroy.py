from battle import commander
unit_client = commander.Client()


def search_and_destroy(data=None, *args, **kwargs):
    enemy = unit_client.ask_nearest_enemy()
    unit_client.do_attack(enemy['id'])
    unit_client.when_item_destroyed(enemy['id'], search_and_destroy)

search_and_destroy()
