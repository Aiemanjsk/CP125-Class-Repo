def count_bright_spots(pixels):
    bright_spots = 0
    for count in range (1, len(pixels) - 1): 
        if pixels[count] > pixels[count - 1] and pixels[count] > pixels[count + 1]:
            bright_spots += 1

    return bright_spots

pixels = [100, 120, 200, 150, 180, 160, 140]
pass
