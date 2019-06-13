def flag(N):
    if type(N) is not int:
        raise Exception(AttributeError)
    elif N % 2 != 0:
        raise Exception(AttributeError)
    if N == 0:
        return ''
    N = abs(N)
    result = ''
    height = 2 * N + 2  # +2 is top and bottom border
    wight = 3 * N + 2  # +2 is left and right border
    f_top = N / 2  # top flag border
    f_bot = height - N / 2  # bottom flag border
    f_left = N  # left flag border
    f_right = wight - N  # right flag border
    for i in range(height):  # height cycle
        for j in range(wight):  # wight cycle
            if i == 0 or i == height - 1:  # draw top and bot borders
                result += '#'
            elif j == 0 or j == wight - 1:  # draw left and right border
                result += '#'
            elif f_top < i < f_bot - 1 and f_left < j < f_right - 1:  # find flag drawing area
                if j == f_left - (i - height/2) or \
                        j == f_right + (i - height/2 - 1) or\
                        j == f_left + (i - height/2 + 1) or \
                        j == f_right - (i - height/2 + 2):  # drawing flag border (l_top, l_bot, r_top, r_bot)
                    result += '*'
                else:
                    if j < f_left - (i - height / 2) or \
                            j > f_right + (i - height / 2 - 1) or \
                            j < f_left + (i - height / 2 + 1) or \
                            j > f_right - (i - height / 2 + 2):  # drawing inner part of flag
                        result += ' '
                    else:
                        result += 'o'
            else:
                result += ' '
        result += '\n'
    return result


if __name__ == "__main__":
    print(flag(0))
    print(flag(2))
    print(flag(4))
    print(flag(6))
