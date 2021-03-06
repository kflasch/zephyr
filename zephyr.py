#!/usr/bin/env python3

import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:
    screen_width = 80
    screen_height = 60
    map_width = 80
    map_height = 45
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    tileset = tcod.tileset.load_tilesheet(
        "arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width/2), int(screen_height/2), '@', tcod.white)
    npc = Entity(int(screen_width/2 - 5), int(screen_height/2), '@', tcod.yellow)
    entities = {npc, player}

    game_map = generate_dungeon(max_rooms=max_rooms, room_min_size=room_min_size,
                                room_max_size=room_max_size, map_width=map_width,
                                map_height=map_height, player=player)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(screen_width, screen_height,
                                   tileset=tileset, title='zephyr',
                                   vsync=True) as context:
        # order='F' changes numpy's 2d array ordering to be x,y instead of y,x
        root_console = tcod.Console(screen_width, screen_height, order='F')
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            
            engine.handle_events(events)


if __name__ == '__main__':
    main()
