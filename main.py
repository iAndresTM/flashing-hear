def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
    basic.pause(100)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.clear_screen()
    basic.pause(100)
basic.forever(on_forever)