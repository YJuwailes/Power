import math

class TurboJet:
    def __init__(self):
        pass
        self.plane_velocity = 0.0
        self.pressure = 0.0
        self.temperature = 0.0
        self.rp = 0.0
        self.comp_eff = 0.0
        self.tur_eff = 0.0
        self.t_turbine = 0.0
        self.mass_flowrate = 0.0
        self.altitude = 0.0


    def readFile(self, fn):
        inFile = open(fn, "r");
        self.plane_velocity = float(inFile.readline())
        self.pressure = float(inFile.readline())
        self.temperature = float(inFile.readline())
        self.rp = float(inFile.readline())
        self.comp_eff = float(inFile.readline())
        self.tur_eff = float(inFile.readline())
        self.t_turbine = float(inFile.readline())
        self.mass_flowrate = float(inFile.readline())
        self.altitude = float(inFile.readline())
        inFile.close();


    def calculate(self):

        plane_velocity = self.plane_velocity
        pressure = self.pressure
        temperature = self.temperature
        rp = self.rp
        comp_eff = self.comp_eff
        tur_eff = self.tur_eff
        t_turbine = self.t_turbine
        mass_flowrate = self.mass_flowrate
        altitude = self.altitude



    #the diffuser calculations
        t1 = temperature
        t2 = t1 + ((plane_velocity ** 2) / (2000 * 1.005))
        p1 = pressure
        p2 = ((t2 / t1) ** (1.4 / 0.4)) * p1


    #calculations of the compressor
        p3 = rp * p2
        t3s = t2 * ((rp) ** (0.4 / 1.4))
        if comp_eff != 1:
            t3a = t2 + ((t3s - t2) / comp_eff)
        else:
            t3a = t3s

    #turbine calculations
        t5a = t_turbine - t3a + t2
        p4 = p3
        if tur_eff != 1:
            t5s = t_turbine - ((t_turbine - t5a) / tur_eff)
        else:
            t5s = t5a
        p5 = p4 * ((t5s / t_turbine) ** (1.4/0.4))



    #the calculations of the nozzle
        p6 = p1
        t6 = t5a * ((p6 / p5) ** (0.4 / 1.4))
        velocity_out = math.sqrt(2000 * 1.005 * (t5a - t6))

    #calculations of the thurst, power and the propulsive efficiency
        f_thrust = mass_flowrate * (velocity_out - plane_velocity)
        power = f_thrust * plane_velocity
        propulsive_eff = power / (mass_flowrate * 1.005 * (t_turbine - t3a))



    #Neater numbers
        x2 = f_thrust - math.floor(f_thrust)
        if x2 > 0.5:
            f_thrust = math.ceil(f_thrust)
        else:
            f_thrust = math.floor(f_thrust)

        x3 = power - math.floor(power)
        if x3 > 0.5:
            power = math.ceil(power)
        else:
            power = math.floor(power)

        x4 = propulsive_eff - math.floor(propulsive_eff)
        if x4 > 0.5:
            propulsive_eff = math.ceil(propulsive_eff)
        else:
            propulsive_eff = math.floor(propulsive_eff)


        return (f_thrust/1000, power/1000, propulsive_eff/10);