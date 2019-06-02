from itertools import combinations
import logging


def calculate(usb_size, memes):
    """
    Returns the most valuable memes from given data and usb size
    :param int usb_size: Given in GiB. Size of USB stick
    :param List[Tuple[str, int, int]] memes: Database of memes to optimize costs
    :return Tuple[int, Set[str]: Returns tuple with int - optimized, maximum price and set of meme names
    (int, {name1, name2,...})
    """
    if not memes:
        logging.error('No memes were given')
        return None
    elif usb_size <= 0:
        logging.error('Wrong size of USB stick')
        return None
    usb_size *= 1024
    memes = list(set(memes))
    memes.sort(key=lambda item: item[2]/item[1], reverse=True)
    filtered_memes = []

    for index, meme in enumerate(memes):
        filtered_memes.append([list(combination) for combination in combinations(memes, len(memes)-index) if
                              sum([meme[1] for meme in list(combination)]) <= usb_size])
    sorted_memes = []
    for memes in filter(lambda list_of_memes: list_of_memes, filtered_memes):
        [sorted_memes.append(meme) for meme in memes]
    sorted_memes.sort(key=lambda item: sum([i[2] for i in item]), reverse=True)
    return sum([i[2] for i in sorted_memes[0]]), {i[0] for i in sorted_memes[0]}
