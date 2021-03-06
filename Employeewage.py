''''
    Created on Nov 24, 2021

    @author:srividya
    @Date:  24/11/2021
    @Title: Employeewage

    '''
import random

class Employeewage:
    #static variable
    total_workinghours  =   100
    wageperhour     =   20
    daysof_month    =   20
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
    
    def parttime(self):
        """
            Description:
                It wii decide employee present or not in employeewage
                program
            Prameters:
                self
            Return:
                None
        """
        empCheck = random.randint(0,2) 
        #print("Employee is present",empCheck)
    
        if empCheck == 1:
            self.workinghours = 8
            print(" Employee working fulltime ")
        elif empCheck == 2 :
            self.workinghours = 4
            print(" Employee working parttime ")
        else:
            self.workinghours = 0
            print(" Employee is absent ")

    def calculate_wage(self):
        """
            Description:
                This function calculates the employee wages
                in given condition
                program
            Prameters:
                self
            Return:
                None
        """
        self.ispresent  =   1
        self.isabsent   =   0
        empCheck = random.randint(0,1) 
       
        if empCheck== 1:
            self.workinghours = 8
        else:
            self.workinghours = 0
        employeewage = self.workinghours * self.wageperhour
        print(" Employee wage is: ",employeewage)   

    def switcher(self):
        """
            Description:
                This function calculates the employee working
                fulltime or parttime
                in given condition
                program
            Prameters:
                self
            Return:
                None
        """
        switcher={
            0: Employeewage.calculate_wage(self),

            1: Employeewage.parttime(self),
            }
          
    
    def month_wage(self):
        """
            Description:
                This function calculates the employee wages
                in given condition
                program
            Prameters:
                self
            Return:
                None
        """
        empCheck = random.randint(0,2)
        daysof_month = 20
       
        if empCheck == 1:
            self.workinghours = 8
            print(" Employee working fulltime ")
        elif empCheck == 2 :
            self.workinghours = 4
            print(" Employee working parttime ")
        else:
            self.workinghours = 0
            print(" Employee is absent ")
        employeewage = self.workinghours * Employeewage.wageperhour
        total_empwage = employeewage * daysof_month
        print(" Employee month wage is: ",total_empwage)

    def _calculate_wage_tillcondition(self):
        """
            Description:
                This function calculates the employee wages
                in given condition
                program
            Prameters:
                self
            Return:
                None
        """
        empCheck = random.randint(0,2)
        daysof_month = 20
        # conditionis applied here daysof_month is 20 days and working hours should be 100
        while(Employeewage.total_workinghours ==100 and daysof_month==20):
            try:
                    daysof_month +=1
                    if empCheck == 1:
                        self.workinghours = 8
                        print(" Employee working fulltime ")
                    elif empCheck == 2 :
                        self.workinghours = 4
                        print(" Employee working parttime ")
                    else:
                        self.workinghours = 0
                        print(" Employee is absent ")
                    employeewage = self.workinghours * Employeewage.wageperhour
                    total_empwage = employeewage * daysof_month
                    print(" Employee wage by given condition: ",total_empwage)
            except Exception as e:
                print("Error...",e)



    
if __name__=='__main__':
    emp=Employeewage()
    emp.display()
    emp.attendance()
    emp.parttime()
    emp.calculate_wage()
    emp.switcher()
    emp.month_wage()
    emp._calculate_wage_tillcondition()

    
    
    