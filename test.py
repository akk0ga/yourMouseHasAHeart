from pynput import mouse

with mouse.Events() as events:
    for event in events:
        if hasattr(event, 'button'):
            print(type(event.button))
            if event.button == mouse.Button.left:
                print('left click')
            else:
                print('not left click')
        else:
            print('no')
