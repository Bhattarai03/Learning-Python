class student():
    def __init__(self,mark):
        self.mark=mark
        self._mark=None
    

    @property
    def mark(self):
        return self._mark
    @mark.setter
    def mark(self,value):
        if value<0:
            print("The Exam score is invalid")
        else:
            self._mark=value
            print(f"The Exam score is {self._mark}")


p=student(78)


