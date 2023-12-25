import numpy as np
import random
import string
import pandas as pd
from typing import Union

letters = string.ascii_lowercase

class Doctor():

    def __init__(self, specialty):
        self.name: str = ''.join(random.choice(letters) for i in range(7)).title()
        self.surname: str = ''.join(random.choice(letters) for i in range(10)).title()
        self.specialty: str = specialty
        self.queue: int = 0

    def __str__(self):
        return f'{self.surname} {self.name}'


class Surgeon(Doctor):

    def __init__(self, limbs, specialty):
        Doctor.__init__(self, specialty)
        self.specialty: str = 'surgeon'
        self.limbs: int = limbs

    def cutting_legs(self, legs, legs_to_cut):
        if legs < 4 or legs - legs_to_cut < 4:
            raise BaseException('Ног не может быть меньше 4.')
        if legs < legs_to_cut:
            raise BaseException('Нельзя ампутировать больше ног, чем есть у пациента.')
        else:
            return legs - legs_to_cut


class Oculist(Doctor):

    def __init__(self, eyes, specialty):
        Doctor.__init__(self, specialty)
        self.specialty: str = 'oculist'
        self.eyes: int = eyes

    def adding_eyes(self, eyes, eyes_to_add):
        if eyes > 8 or eyes + eyes_to_add > 8:
            raise BaseException('Глаз не может быть больше 8.')
        else:
            return eyes_to_add


class Customer():

    def __init__(self, eyes, limbs):
        self.name: str = ''.join(random.choice(letters) for i in range(7)).title()
        self.surname: str = ''.join(random.choice(letters) for i in range(10)).title()
        self.eyes: int = eyes
        self.limbs: int = limbs

    def __str__(self):
        return f'{self.surname} {self.name}'


class Appointment():

    def __init__(self, doctor, customer, queue):
        self.doctor: Union[Surgeon, Oculist] = doctor 
        self.customer: Customer = customer
        self.queue: int = queue

    def __str__(self):
        return f'{self.doctor}: {self.customer}, {self.queue}'


class Journal():

    def __init__(self):
        self.history: list = []
        self.common_queue: int = 0
        self.eyes_stats: list = []
        self.__eyes_mean: int = 0
        self.limbs_stats: list = []
        self.__limbs_mean: int = 0

    def check_queue(self, doctor):
        if doctor.queue == 10:
            raise BaseException('На сегодня приём у врача закончен, приползайте завтра.')
        elif self.common_queue == 20:
            raise BaseException('Посетителям вход ограничен по ковидным мерам.')
        return True

    def add_appointment(self, customer, doctor):
        if self.check_queue(doctor):
            if type(doctor) is Oculist:
                self.eyes_stats.append(customer.eyes)
            if type(doctor) is Surgeon:
                self.limbs_stats.append(customer.limbs)
            self.history.append(Appointment(doctor, customer, doctor.queue))
            doctor.queue += 1
            self.common_queue += 1
        else:
            raise BaseException('Запись не удалось осуществить.')
        
    def get_all_appointments(self):
        for appointment in self.history:
            print(appointment)

    def plot_eyes(self):
        eyes_stats = pd.Series(self.eyes_stats)
        return eyes_stats
    
    @property
    def eyes_mean(self):
        self.__eyes_mean = np.mean(self.eyes_stats)
        return self.__eyes_mean
    
    @eyes_mean.setter
    def eyes_mean(self, eyes_mean):
        self.__eyes_mean = eyes_mean

    @property
    def limbs_mean(self):
        self.__limbs_mean = np.mean(self.limbs_stats)
        return self.__limbs_mean
    
    @limbs_mean.setter
    def limbs_mean(self, limbs_mean):
        self.__limbs_mean = limbs_mean
        

oculist = Oculist(eyes=12, specialty='oculist')
print(oculist.queue)
surgeon = Surgeon(limbs=12, specialty='surgeon')
print(surgeon.queue)

customer = Customer(eyes=5, limbs=10)

jour = Journal()
jour.add_appointment(customer, oculist)
jour.add_appointment(customer, oculist)
jour.add_appointment(customer, oculist)
jour.add_appointment(customer, oculist)
jour.add_appointment(customer, oculist)
jour.add_appointment(customer, oculist)
jour.add_appointment(customer, oculist)
jour.add_appointment(customer, oculist)
jour.add_appointment(customer, oculist)
jour.add_appointment(customer, surgeon)
jour.add_appointment(customer, oculist)
print(oculist.queue)
print(jour.common_queue)
print(jour.limbs_mean)