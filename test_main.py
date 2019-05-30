import pytest

from main import calculate


@pytest.mark.parametrize(
    'usb_size, memes, expected',
    [
        (1, [('rollsafe.jpg', 205, 6), ('sad_pepe_compilation.gif', 410, 10), ('yodeling_kid.avi', 605, 12)], (22, {'sad_pepe_compilation.gif', 'yodeling_kid.avi'})),
        (1, [('rollsafe.jpg', 205, 6), ('yodeling_kid.avi', 605, 12),('yodeling_kid.avi', 605, 12), ('sad_pepe_compilation.gif', 410, 10), ('rollsafe.jpg', 205, 6),('yodeling_kid.avi', 605, 12)], (22, {'sad_pepe_compilation.gif', 'yodeling_kid.avi'})),
        (1, [('dolan.png', 126, 5), ('expanding_brain.jpeg', 421, 10)], (15, {'dolan.png', 'expanding_brain.jpeg'})),
    ]
)
def test_calculate(usb_size, memes, expected):
    assert calculate(usb_size, memes) == expected
