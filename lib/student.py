#!/usr/bin/env python

from user import User

class Student(User):

    knowledge = []
    
    def learn(self, subject):
        self.knowledge.append(subject)