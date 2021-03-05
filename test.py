from pynput import mouse

with mouse.Events() as events:
    for event in events:
        if event == mouse.Button.right:
            print('yes')
        else:
            print('Received event {}'.format(event))
