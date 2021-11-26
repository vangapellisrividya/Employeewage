''''
    Created on Nov 24, 2021

    @author:srividya
    @Date:  24/11/2021
    @Title: Employeewage

    '''
import random

class Employeewage:

    def display(self):
        """
            Description:
                It wii display the welcome part in employeewage
                program
            Prameters:
                self
            Return:
                None
        """
        print("*****************************************")
        print(" Welcome to Employeewage Program on master")
        print("******************************************")

    def attendance(self):
        """
            Description:
                It wii employee is present or not in employeewage
                program
            Prameters:
                self
            Return:
                None
        """
        self.ispresent  =   1
        self.isabsent   =   0
        attend = random.randint(0,1) 
        while random.randint:
            if attend == 1:
                print(" Employee is Present ")
            else:
                print(" Employee is Absent")
            break
            


    
if __name__=='__main__':
    emp=Employeewage()
    emp.display()
    emp.attendance()
    
    
    