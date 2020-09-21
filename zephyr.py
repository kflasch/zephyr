#!/usr/bin/env python3

import tcod

from render import clear_all, render_all
from entity import Entity
from map_objects.game_map import GameMap

# def main_alt():
#     WIDTH, HEIGHT = 720, 480
#     FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED

#     tileset = tcod.tileset.load_tilesheet(
#         "arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
#     )
    
#     with tcod.context.new_window(
#         WIDTH, HEIGHT, sdl_window_flags = FLAGS, tileset=tileset,
#     ) as context:
#         console = tcod.Console(*context.recommended_console_size())
#         while True:
#             console.clear()
#             console.print(0, 0, "hi")
#             context.present(console, integer_scaling=True)

#             for event in tcod.event.wait():
#                 context.convert_event(event) # sets tile coordinates for mouse events
#                 print(event)
#                 if event.type == "QUIT":
#                     raise SystemExit()
#                 if event.type == "WINDOWRESIZED":
#                     # replace console with one that fits new resolution
#                     console = tcod.Console(*context.recommended_console_size())
            
def handle_keys(key):
    if key.vk == tcod.KEY_UP:
        return {'move': (0, -1)}
    if key.vk == tcod.KEY_DOWN:
        return {'move': (0, 1)}
    if key.vk == tcod.KEY_LEFT:
        return {'move': (-1, 0)}
    if key.vk == tcod.KEY_RIGHT:
        return {'move': (1, 0)}

    # alt+enter
    if key.vk == tcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    
    if key.vk == tcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def main():
    screen_width = 80
    screen_height = 60
    map_width = 80
    map_height = 45
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    colors = {
        'dark_wall': tcod.Color(0, 0, 100),
        'dark_ground': tcod.Color(50, 50, 150)
    }

    player = Entity(int(screen_width/2), int(screen_height/2), '@', tcod.white)
    npc = Entity(int(screen_width/2 - 5), int(screen_height/2), '@', tcod.yellow)
    entities = [npc, player]

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(screen_width, screen_height, 'zephyr', False, tcod.RENDERER_SDL2)

    con = tcod.console_new(screen_width, screen_height)
    key = tcod.Key()
    mouse = tcod.Mouse()

    game_map = GameMap(map_width, map_height)
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)
    
    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)
        
        # tcod.console_set_default_foreground(con, tcod.white)
        # tcod.console_put_char(con, player.x, player.y, player.char, tcod.BKGND_NONE)
        # tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        render_all(con, entities, game_map, screen_width, screen_height, colors)
        tcod.console_flush()

        # tcod.console_put_char(con, player.x, player.y, ' ', tcod.BKGND_NONE)
        clear_all(con, entities)

        action = handle_keys(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
        if exit:
            return True
        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
