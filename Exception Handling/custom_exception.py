
class InvalidMarksError(Exception):
    pass

marks = int(input("Enter Marks :"))

if marks > 100:
    raise InvalidMarksError("Marks can not be exceed 100")