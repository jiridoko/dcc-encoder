#!/usr/bin/env python3
import controller
from dcc_signals import *

class loco_function(object):
    def __init__(self, name, toggle=False, value=None, ident=None):
        self.toggle = toggle
        self.name = name
        self.value = value
        self.ident = ident
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_ident(self):
        return self.ident
    def is_toggle(self):
        return self.toggle

class locomotive(object):
    def __init__(self, name, ident, control):
        self.name = name
        self.ident = ident
        self.control = control
        self.functions = dict()
        self.speed = 0
        self.forward = True
        self.emergency_stop = False
    def add_function(self, name, toggle, value, ident):
        new_func = loco_function(name, toggle=toggle, value=value, ident=ident)
        self.functions[ident] = new_func
    def get_function(self, ident):
        return self.functions[ident]
    def get_function_value(self, ident):
        if ident in self.functions.keys():
            return self.functions[ident].get_value()
        else:
            return False
    def emergency(self, stop=True):
        self.speed = 0
        self.emergency_stop = stop
        self.update_speed()
    def update_speed(self):
        lights = self.get_function_value(0)
        data = loco_speed(address=self.ident, speed=self.speed, emergency_stop=self.emergency_stop, forward=self.forward, lights=lights)
        self.control.send(data)
    def set_direction(self, forward=True):
        if forward != self.forward:
            self.forward = forward
            self.update_speed()
    def set_speed(self, speed=0):
        if speed != self.speed and speed >= 0 and speed <= 14:
            self.speed = speed
            self.update_speed()
    def get_speed(self):
        return self.speed
    def is_forward(self):
        return self.forward
    def call_function(self, ident, value=False):
        if not ident in self.functions.keys():
            return None

        f = self.functions[ident]
        f.set_value(value)

        if ident >= 0 and ident <= 4:
            v = []
            for i in range(0,5):
                v.append(self.get_function_value(i))
            if f.is_toggle():
                data = loco_functions_1(address=self.ident, lights=v[0], f1=v[1], f2=v[2], f3=v[3], f4=v[4])
                self.control.send(data)
            else:
                v[ident] = True
                data1 = loco_functions_1(address=self.ident, lights=v[0], f1=v[1], f2=v[2], f3=v[3], f4=v[4])
                v[ident] = False
                data2 = loco_functions_1(address=self.ident, lights=v[0], f1=v[1], f2=v[2], f3=v[3], f4=v[4])
                self.control.send(data1)
                self.control.send(data2)
        elif ident >= 5 and ident <= 8:
            v = []
            for i in range(0,4):
                v.append(self.get_function_value(i+5))
            if f.is_toggle():
                data = loco_functions_2(address=self.ident, f5=v[0], f6=v[1], f7=v[2], f8=v[3])
                self.control.send(data)
            else:
                v[ident-5] = True
                data1 = loco_functions_2(address=self.ident, f5=v[0], f6=v[1], f7=v[2], f8=v[3])
                v[ident-5] = False
                data2 = loco_functions_2(address=self.ident, f5=v[0], f6=v[1], f7=v[2], f8=v[3])
                self.control.send(data1)
                self.control.send(data2)
        elif ident >= 9 and ident <= 12:
            v = []
            for i in range(0,4):
                v.append(self.get_function_value(i+9))
            if f.is_toggle():
                data = loco_functions_3(address=self.ident, f9=v[0], f10=v[1], f11=v[2], f12=v[3])
                self.control.send(data)
            else:
                v[ident-9] = True
                data1 = loco_functions_3(address=self.ident, f9=v[0], f10=v[1], f11=v[2], f12=v[3])
                v[ident-9] = False
                data2 = loco_functions_3(address=self.ident, f9=v[0], f10=v[1], f11=v[2], f12=v[3])
                self.control.send(data1)
                self.control.send(data2)
        elif ident >= 13 and ident <= 20:
            v = []
            for i in range(0,8):
                v.append(self.get_function_value(i+13))
            if f.is_toggle():
                data = loco_functions_4(address=self.ident, f13=v[0], f14=v[1], f15=v[2], f16=v[3], f17=v[4], f18=v[5], f19=v[6], f20=v[7])
                self.control.send(data)
            else:
                v[ident-13] = True
                data1 = loco_functions_4(address=self.ident, f13=v[0], f14=v[1], f15=v[2], f16=v[3], f17=v[4], f18=v[5], f19=v[6], f20=v[7])
                v[ident-13] = False
                data2 = loco_functions_4(address=self.ident, f13=v[0], f14=v[1], f15=v[2], f16=v[3], f17=v[4], f18=v[5], f19=v[6], f20=v[7])
                self.control.send(data1)
                self.control.send(data2)
        elif ident >= 21 and ident <= 28:
            v = []
            for i in range(0,8):
                v.append(self.get_function_value(i+21))
            if f.is_toggle():
                data = loco_functions_5(address=self.ident, f21=v[0], f22=v[1], f23=v[2], f24=v[3], f25=v[4], f26=v[5], f27=v[6], f28=v[7])
                self.control.send(data)
            else:
                v[ident-21] = True
                data1 = loco_functions_5(address=self.ident, f21=v[0], f22=v[1], f23=v[2], f24=v[3], f25=v[4], f26=v[5], f27=v[6], f28=v[7])
                v[ident-21] = False
                data2 = loco_functions_5(address=self.ident, f21=v[0], f22=v[1], f23=v[2], f24=v[3], f25=v[4], f26=v[5], f27=v[6], f28=v[7])
                self.control.send(data1)
                self.control.send(data2)

if __name__=="__main__":
    import time
    c = controller.controller()
    loco1 = locomotive("brejlovec", 47, c)
    loco1.add_function("light",         True,  False, 0)
    loco1.add_function("sound",         True,  False, 1)
    loco1.add_function("horn",          False, False, 2)
    loco1.add_function("whistle",       False, False, 3)
    loco1.add_function("coupling",      False, False, 4)
    loco1.add_function("conductor",     False, False, 5)
    loco1.add_function("shunting",      True,  False, 6)
    loco1.add_function("curve",         True,  False, 7)
    loco1.add_function("sanding",       True,  False, 8)
    loco1.add_function("announcement",  False, False, 10)
    loco1.add_function("short horn",    False, False, 12)
    loco1.add_function("short whistle", False, False, 13)
    loco1.add_function("mute",          True,  False, 14)

    loco1.call_function(0, value=True)
    loco1.set_speed(14)
    time.sleep(6)
    loco1.emergency(stop=True)
    time.sleep(6)
    loco1.emergency(stop=False)
    loco1.set_direction(forward=True)
    time.sleep(2)
    loco1.set_speed(speed=3)
    time.sleep(5)
    loco1.set_speed(speed=0)
    time.sleep(2)
    loco1.set_direction(forward=False)
    time.sleep(2)
    loco1.set_speed(speed=3)
    time.sleep(5)
    loco1.set_speed(speed=0)
    time.sleep(2)
    loco1.call_function(7, value=True)
    time.sleep(2)
    loco1.call_function(13)
    time.sleep(2)
    loco1.call_function(7, value=False)
    time.sleep(4)
    loco1.call_function(0, value=False)
