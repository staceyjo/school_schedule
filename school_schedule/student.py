class Student:
    """
    attributes:
        - name- string
        - grade- string
        - classes- list
    methods: 
        - add_class, param: string
        - get_num_classes, no args
        - summary, no args
        - pretty print each class- helper function
    """
    
    #  make the constructor, with the attributes:
    def __init__(self, name, grade, classes):
        self.name = name 
        self.grade = grade
        self.classes = classes
        
    # def greeting(self):
    #     print("hi")
    #     self.compliment()
    
    def add_class(self, class_name):
        self.classes.append(class_name)
        return self.classes
    
    def get_num_classes(self):
        pass
    
    def summary(self):
        pass
    
    def display_each_class(self):
        pass
        
    def __str__(self):
        return f"Student {self.name}, grade {self.grade}, classes {self.classes}"
    
    # def compliment(self):
    #     print("Mikelle, your nails look SO good")
        
    # make the instance methods