class TestLenght:
    def test_input_length(self):
        phrase = input("Set a phrase: ")
        allowed_lenght = 15
        assert len(phrase) < allowed_lenght, f"Phrase length is longer than {allowed_lenght}" 