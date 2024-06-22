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

    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self.people)
    
    def sort_age(self):
        self.people.sort(key= lambda person: person.yob)
    
    def compute_teachers_yob_avg(self):

        teachers = [person for person in self.people if isinstance(person, Teacher)]
        
        if teachers:
            return sum(teacher.yob for teacher in teachers) / len(teachers)
        
        else: 
            return f"None teacher(s) found on the {self.ward_name}"


class Stack:
    '''
    • initialization method nhận một input "capacity": dùng để khởi tạo stack với capacity là số lượng element mà stack có thể chứa
    • .is_empty(): kiểm tra stack có đang rỗng
    • .is_full(): kiểm tra stack đã full chưa
    • .pop(): loại bỏ top element và trả về giá trị đó
    • .push(value) add thêm value vào trong stack
    • .top() lấy giá trị top element hiện tại của stack, nhưng không loại bỏ giá trị đó
    '''

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return True if len(self.stack) == 0 else False
    
    def is_full(self):
        return True if len(self.stack) >= self.capacity else False 
    
    def pop(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            return self.stack.pop()
        
    def push(self,value):
        if self.is_full():
            print("The stack is full.")
        else:
            return self.stack.append(value)
    
    def top(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            return self.stack[-1]

    def describe(self):
        print(self.stack)



class Queue:
    '''
    Thực hiện xây dựng class Queue với các chức năng (method) sau đây
    • initialization method nhận một input "capacity": dùng để khởi tạo queue với capacity là số lượng element mà queue có thể chứa
    • .is_empty(): kiểm tra queue có đang rỗng
    • .is_full(): kiểm tra queue đã full chưa
    • .dequeue(): loại bỏ first element và trả về giá trị đó
    • .enqueue(value) add thêm value vào trong queue
    • .front() lấy giá trị first element hiện tại của queue, nhưng không loại bỏ giá trị đó
    '''

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return True if len(self.queue) == 0 else False
    
    def is_full(self):
        return True if len(self.queue) >= self.capacity else False 
    
    def dequeue(self, idx=0):
        if self.is_empty():
            print("The queue is empty.") 
        else:
            element = self.queue.pop(idx)  
            print(element)
    
    def enqueue(self, value):
        if self.is_full():
            print("The queue is full.")
        else:
            return self.queue.append(value) 
            
    
    def front(self):
        return self.queue[0]
    
    def describe(self):
        print(self.queue)