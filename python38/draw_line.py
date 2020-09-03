# continuation of precise type topic

def draw_line(direction: str) -> None:
    if direction == 'horizontal':
        # draw a horizontal line
        print('drawing horizontal line')
    elif direction == 'vertical':
        # draw a vertical line
        print('drawing a vertical line')
    else:
        raise ValueError(f'invalid direction {direction!r}')

if __name__ == '__main__':
    draw_line('up')
