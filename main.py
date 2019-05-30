from itertools import combinations


def calculate(usb_size, memes):
    """
    Returns the most valuable memes from given data and usb size
    :param int usb_size: Given in GiB. Size of USB stick
    :param List[Tuple[str, int, int]] memes: Database of memes to optimize costs
    :return Tuple[int, Set[str]: Returns tuple with int - optimized, maximum price and set of meme names(
    int, {name1, name2,...})
    """
    usb_size = usb_size*(1024)
    memes = list(set(memes))
    memes.sort(key=lambda item: item[2]/item[1], reverse=True)
    filtred_memes = []

    for i, meme in enumerate(memes):
        filtred_memes.append([list(i) for i in combinations(memes, len(memes) - i) if
                              sum([k[1] for k in list(i)]) < usb_size])
    sorted_memes = []

    for i in filtred_memes:
        if i is not None:
            [sorted_memes.append(j) for j in i]
    sorted_memes.sort(key=lambda item: sum([i[2] for i in item]), reverse=True)

    return sum([i[2] for i in sorted_memes[0]]), {i[0] for i in sorted_memes[0]}
