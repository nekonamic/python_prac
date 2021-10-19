# ```python
# import random
# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3
# ```
#
# -   *What did you see on line 1?*
#     What was the smallest number you could have seen, what was the
#     largest?
#     answer: 5, 18, 19
#
# -   *What did you see on line 2?*
#     What was the smallest number you could have seen, what was the
#     largest?
#     answer: 3. 7, 9
#     *Could line 2 have produced a 4?*
#     can't
#
# -   *What did you see on line 3?*
#     What was the smallest number you could have seen, what was the
#     largest?
#     answer: 3.693333938743381, 4.50572733222155, 5.468690602670762
#
# -   Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
print(random.uniform(2.5, 5.5))
