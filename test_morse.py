from  morse import Morse, InsufficientAmount
import pytest

@pytest.fixture
def translate():
    return Morse()
@pytest.mark.decode
@pytest.mark.parametrize("codes, decodes",
                            [
                                (["--",".-","--",".-","-----","--..--"], 'мама0,'),
                                (["-----",".-","--",".-","-----","--..--"], '0ама0,'),
                                ([".-",".-","--",".-","-----","--..--"], 'аама0,')
                            ]
                         )
def test_encoding(translate, codes, decodes):
    translate.morse_string = decodes
    assert translate.morse_string == (codes, decodes), "Incorrect data"
@pytest.mark.code
@pytest.mark.parametrize("codes, decodes",
                            [
                                (["--",".-","--",".-","-----","--..--"], 'мама0,'),
                                (["-----",".-","--",".-","-----","--..--"], '0ама0,'),
                                ([".-",".-","--",".-","-----","--..--"], 'аама0,')
                            ]
                         )
def test_decoding(translate, codes, decodes):
    translate.morse_string = ' '.join(codes)
    assert translate.morse_string == (codes, decodes), "Incorrect data"

def  test_set_insuficient(translate):
    with pytest.raises(InsufficientAmount):
        translate.morse_string="мамаf"
        print(translate.morse_string)
def main():
    pass

if __name__ == "__main__":
    main()