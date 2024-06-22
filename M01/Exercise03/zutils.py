import sys 
import os
import torch 
import torch.nn as nn
import torch.nn.functional as F 
from dataclasses import dataclass
from typing import List, Union

class Softmax(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super(Softmax,self).__init__(*args, **kwargs)

    def forward(self,x):
        exp_x = torch.exp(x)
        exp_sum = torch.sum(exp_x)
        softmax = exp_x / exp_sum 
        return softmax
    

class Softmax_stable(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super(Softmax_stable, self).__init__()

    def forward(self,x):
        c = torch.max(x)
        exp_x = torch.exp(x-c)
        exp_sum = torch.sum(exp_x)
        softmax_stable = exp_x / exp_sum
        return softmax_stable


@dataclass
class Person:
    name: str
    yob: int

    def myname(self):
        return self.name

    def myyob(self):
        return self.yob
    
    def describe(self):
        return f"Name: {self.name} - YoB: {self.yob}"


@dataclass
class Student(Person):
    grade: str

    def mygrade(self):
        return self.grade
    
    def describe(self):
        return f"{self.__class__.__name__} - {super().describe()} - Grade: {self.grade}"
    

@dataclass
class Teacher(Person):
    subject: str 

    def mysubject(self):
        return self.subject
    
    def describe(self):
        return f"{self.__class__.__name__} - {super().describe()} - Subject: {self.subject}"


@dataclass
class Doctor(Person):
    specialist: str

    def myspecialist(self):
        return self.specialist

    def describe(self):
        return f"{self.__class__.__name__} - {super().describe()} - Specialist: {self.specialist}"
    

class Ward:
    def __init__(self, ward_name) -> None:
        self.ward_name= ward_name 
        self.people: List[Union[Student, Teacher, Doctor]] = []

    def add_people(self, person: Union[Student, Teacher, Doctor]):
        self.people.append(person)

    def describe(self):
        print(f"Ward Namw: {self.ward_name}")
        for p in self.people:
            print(p.describe())

    def count_docter(self):
        return sum(isinstance(person, Doctor) for person in self.people)
    
    def sort_age(self):
        self.people.sort(key= lambda person: person.yob)
    
    def compute_teachers_yob_avg(self):

        teachers = [person for person in self.people if isinstance(person, Teacher)]
        
        if teachers:
            return sum(teacher.yob for teacher in teachers) / len(teachers)
        
        else: 
            return f"None teacher(s) found on the {self.ward_name}"
