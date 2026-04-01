#Write a lambda function to return "Pass" or "Fail" based on marks (>= 40 pass).
result=lambda marks:"pass" if marks>=40 else "fail"
print(result(99))
print(result(34))
