import pytest

from main import calculate


@pytest.mark.parametrize(
    'usb_size, memes, expected',
    [
        (1, [('rollsafe.jpg', 205, 6), ('sad_pepe_compilation.gif', 410, 10), ('yodeling_kid.avi', 605, 12)], (22, {'sad_pepe_compilation.gif', 'yodeling_kid.avi'})),
        (1, [('rollsafe.jpg', 205, 6), ('yodeling_kid.avi', 605, 12),('yodeling_kid.avi', 605, 12), ('sad_pepe_compilation.gif', 410, 10), ('rollsafe.jpg', 205, 6),('yodeling_kid.avi', 605, 12)], (22, {'sad_pepe_compilation.gif', 'yodeling_kid.avi'})),
        (1, [('dolan.png', 126, 5), ('expanding_brain.jpeg', 421, 10)], (15, {'dolan.png', 'expanding_brain.jpeg'})),
        (1, [('rollsafe.jpg', 205, 6),('sad_pepe_compilation.gif', 410, 10),('yodeling_kid.avi', 126, 11),('I_got_an_arrow.jpg', 584, 20),('sad_adventurer.gif', 320, 25),('be_like_bill.avi', 175, 16),('But_Thats_None_of_My_Business.jpg', 105, 10),
             ('grumpy_cat.gif', 210, 19),('old_spice_guy.avi', 105, 14),('rickroll.jpg', 265, 9),('doge_the_dog.gif', 320, 15),('leekspin.avi', 635, 11),('doggo.avi', 1000, 100)], (100, {'doggo.avi'})),
        (-1, [('rollsafe.jpg', 205, 6),('sad_pepe_compilation.gif', 410, 10)], None)
    ]
)
def test_calculate(usb_size, memes, expected):
    assert calculate(usb_size, memes) == expected
