class student:
    

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum =0 
        for val in self.marks:
            sum += val
            
        print("Hey, ", self.name,", Your Average Score is: ", sum/3 )
       






s1 =student("Siraj", [80,90,70])



s1.get_average()