numbers = input().split()
answers = input().split()

# numbers_cleaned = set(numbers)
# answers_cleaned = set(answers)
#
#
# def check_num():
#     for numbers_ in answers_cleaned:
#         if numbers_ not in numbers_cleaned:
#             return False
#         elif numbers_ in numbers_cleaned:
#             numbers_cleaned.remove(numbers_)
#     if len(numbers_cleaned) > 0:
#         return False
#     return True
#
#
# print(check_num())

print(set(numbers) == set(answers))
