# import
from school_schedule.student import Student

#first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

# print(quinn)
# # vars function returns student object as dictionary
# # vars prints the repr
# print(vars(quinn))
# quinn.greeting()

# print(quinn.add_class("Painting"))
# print(quinn.get_num_classes())
print(quinn.summary())

# second instance
claire = Student(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
            )

# claire.get_num_classes()
# claire.summary()

# Extra:
# - create a function that will return the student with more classes
# - create a test for that function

ghameerah = Student(
    "Ghameerah", 
    "junior"
)

mikelle = Student(
    "Mikelle", 
    "junior"
)

# print(mikelle)
# print(ghameerah)

# mikelle.add_class("jazzercise")

# print(mikelle)
# print(ghameerah)

# print(id(mikelle.classes))
# print(id(ghameerah.classes))
