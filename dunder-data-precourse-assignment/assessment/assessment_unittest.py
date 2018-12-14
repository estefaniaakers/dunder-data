import assessment
 
class TestAdd:

    def test_mult_dummy(self):
        result = assessment.mult_dummy(4, 10)
        assert result == 40

    def test_add_divide_product(self):
        result = assessment.add_divide_product(12, 6)
        assert result == .25
 
    def test_count_letters(self):
        result = assessment.count_letters('test count letters', 't')
        assert result == 5

    def test_largest_smallest(self):
        result = assessment.largest_smallest([8, 10, 12, -7, 4])
        assert result == (12, -7)

    def test_greatest_divisble_7(self):
        result = assessment.greatest_divisble_7([8, 98, 10000])
        assert result == 98

    def test_greatest_common_factor(self):
        result = assessment.greatest_common_factor(36, 40)
        assert result == 4

    def test_count_words(self):
        result = assessment.count_words('some   words to   test!')
        assert result == 4

    def test_count_substring_words(self):
        result = assessment.count_substring_words('the man thought about that', 'th')
        assert result == 3

    def test_longest_word(self):
        result = assessment.longest_word('longest word what is it?')
        assert result == 'longest'

    def test_double_letter_words(self):
        result = assessment.double_letter_words('The ladders that fell on the roof popped the balloons')
        assert result == ['ladders', 'fell', 'roof', 'popped', 'balloons']

    def test_dict_of_powers(self):
        result = assessment.dict_of_powers(3)
        assert result == {1:[1, 1, 1], 2:[4, 8, 16], 3:[9, 27, 81]}

    def test_last_2_list(self):
        result = assessment.last_2_list([0, 8, 10, -99, 43, 102])
        assert result == [10, 43]

    def test_reorder_list(self):
        result = assessment.reorder_list(['a', 'b', 'c', 'd', 'e'], [3, 1, 4, 2, 0])
        assert result == ['d', 'b', 'e', 'c', 'a']

    def test_prob_3_dice(self):
        result = assessment.prob_3_dice(3, [1, 2, 3, 4, 5, 6], 14)
        assert result is not None
        assert abs(result - .07) < .01
