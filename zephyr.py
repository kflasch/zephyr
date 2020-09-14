#!/usr/bin/env python3

import tcod

from entity import Entity

def main_alt():
    WIDTH, HEIGHT = 720, 480
    FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED

    tileset = tcod.tileset.load_tilesheet(
        "arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
    )
    
    with tcod.context.new_window(
        WIDTH, HEIGHT, sdl_window_flags = FLAGS, tileset=tileset,
    ) as context:
        console = tcod.Console(*context.recommended_console_size())
        while True:
            console.clear()
            console.print(0, 0, "hi")
            context.present(console, integer_scaling=True)

            for event in tcod.event.wait():
                context.convert_event(event) # sets tile coordinates for mouse events
                print(event)
                if event.type == "QUIT":
                    raise SystemExit()
                if event.type == "WINDOWRESIZED":
                    # replace console with one that fits new resolution
                    console = tcod.Console(*context.recommended_console_size())
            

def main():
    screen_width = 80
    screen_height = 60    

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(screen_width, screen_height, 'zephyr', False, tcod.RENDERER_SDL2)

    while not tcod.console_is_window_closed():
        tcod.console_set_default_foreground(0, tcod.white)
        tcod.console_put_char(0, 1, 1, '@', tcod.BKGND_NONE)
        tcod.console_flush()

        key = tcod.console_check_for_keypress()

        if key.vk == tcod.KEY_ESCAPE:
            return True
        

if __name__ == '__main__':
    main()
