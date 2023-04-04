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

print(quinn.add_class("Painting"))
# quinn.get_num_classes()
# quinn.summary()

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