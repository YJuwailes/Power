from tkinter import *
import TurboJet
import math

#Setting up the window
root = Tk()
root.title('Jet Engine Claculator')
root.resizable(width=False, height=False)

#Setting up the checkbox
var1 = IntVar()
diameterCheckBox = Checkbutton(root, text='Diameter', variable=var1).grid(row=0, column=4)

#Positioning the cells
thrust_str = StringVar()
power_str = StringVar()
eff_str = StringVar()
thrust_str.set('Thrust =')
power_str.set('Propulsion power =')
eff_str.set('Propulsive efficiency =')

label_1 = Label(root, text="Velocity of the Plane: ")
label_2 = Label(root, text="Mass flowrate/Diameter: ")
label_5 = Label(root, text="Pressure ratio of the compressor: ")
label_6 = Label(root, text="Isentropic efficiency of the compressor: ")
label_7 = Label(root, text="Isentropic efficiency of the turbine: ")
label_8 = Label(root, text="Temperature of the turbine Inlet: ")
label_9 = Label(root, text='Altitude: ')
label_10 = Label(root, textvariable=thrust_str, fg='red')
label_11 = Label(root, textvariable=power_str, fg='blue')
label_12 = Label(root, textvariable=eff_str, fg='black')

entry_1 = Entry(root)
entry_2 = Entry(root)
entry_5 = Entry(root)
entry_6 = Entry(root)
entry_7 = Entry(root)
entry_8 = Entry(root)
entry_9 = Entry(root)

label_1.grid(row=0, sticky=W)
entry_1.grid(row=0, column=1)
label_2.grid(row=0, column=2, sticky=W)
entry_2.grid(row=0, column=3)
label_5.grid(row=1, sticky=W)
entry_5.grid(row=1, column=1)
label_6.grid(row=1, column=2, sticky=W)
entry_6.grid(row=1, column=3)
label_7.grid(row=2, sticky=W)
entry_7.grid(row=2, column=1)
label_8.grid(row=2, column=2, sticky=W)
entry_8.grid(row=2, column=3)
label_9.grid(row=3, sticky=W)
entry_9.grid(row=3, column=1)
label_10.grid(row=5, sticky=W)
label_11.grid(row=6, sticky=W)
label_12.grid(row=7, sticky=W)


def turboCalculate():
    tj = TurboJet.TurboJet()

#Taking the inputs and assigning them to variables
    tj.plane_velocity = float(entry_1.get())
    tj.rp = float(entry_5.get())
    tj.comp_eff = float(entry_6.get()) / 100
    tj.tur_eff = float(entry_7.get()) / 100
    tj.t_turbine = float(entry_8.get())
    tj.altitude = float(entry_9.get())


#An array of different heights with densities, pressure and temperature
    altitude_2 = [
        [0, 1.225, 101.3, 288.15],
        [250, 1.19587, 98.357, 286.525],
        [500, 1.16727, 95.460, 284.900],
        [750, 1.13920, 92.633, 283.275],
        [1000, 1.11164, 89.874, 281.65],
        [1250, 1.08460, 87.182, 280.02],
        [1500, 1.05807, 84.556, 278.40],
        [1750, 1.03202, 81.994, 276.77],
        [2000, 1.00649, 79.495, 275.15],
        [2250, 0.981435, 77.058, 273.525],
        [2500, 0.956859, 74.682, 271.900],
        [2750, 0.932757, 72.366, 270.275],
        [3000, 0.909122, 70.108, 268.65],
        [3250, 0.885948, 67.908, 267.025],
        [3500, 0.863229, 65.764, 265.400],
        [3750, 0.840958, 63.675, 263.775],
        [4000, 0.819129, 61.6402, 262.15],
        [4250, 0.797737, 59.658, 260.525],
        [4500, 0.776775, 57.728, 258.900],
        [4750, 0.756236, 55.849, 257.275],
        [5000, 0.736116, 54.0199, 255.65],
        [5250, 0.716408, 52.239, 254.025],
        [5500, 0.697106, 50.506, 252.400],
        [5750, 0.678204, 48.821, 250.775],
        [6000, 0.659697, 47.181, 249.15],
        [6250, 0.641579, 45.586, 247.525],
        [6500, 0.623844, 44.034, 245.900],
        [6750, 0.606487, 42.526, 244.275],
        [7000, 0.589501, 41.060, 242.65],
        [7250, 0.572882, 39.635, 241.025],
        [7500, 0.556624, 38.251, 239.400],
        [7750, 0.540721, 36.906, 237.775],
        [8000, 0.525168, 35.5998, 236.15],
        [8250, 0.509959, 34.331, 234.525],
        [8500, 0.495090, 33.099, 232.90],
        [8750, 0.480555, 31.903, 231.27],
        [9000, 0.466348, 30.742, 229.65],
        [9250, 0.452465, 29.616, 226.40],
        [9500, 0.438901, 28.523, 226.40],
        [9750, 0.425649, 27.463, 224.77],
        [10000, 0.412707, 26.436, 223.15]
        ]

    for x in altitude_2:
        for y in x:
            if y == tj.altitude:
                tj.density = x[1]
                tj.pressure = x[2]
                tj.temperature = x[3]


# Diameter or Mass flowrate
    if var1.get() == 1:
        tj.jet_diameter = float(entry_2.get())
        tj.m_flowrate = 0
    else:
        tj.m_flowrate = float(entry_2.get())
        tj.jet_diameter = 0


# mass flowrate calculation:
    if tj.jet_diameter == 0:
        mass_flowrate = tj.m_flowrate
    else:
        mass_flowrate = (0.25 * math.pi * tj.plane_velocity * tj.density * tj.jet_diameter ** 2)

    x = mass_flowrate - math.floor(mass_flowrate)
    if x > 0.5:
        mass_flowrate = math.ceil(mass_flowrate)
    else:
        mass_flowrate = math.floor(mass_flowrate)


    tj.mass_flowrate = mass_flowrate
    res = tj.calculate()

#Showing the results on the active window
    thrust_str.set('Thurst = ' + str(res[0]) + ' kN')
    power_str.set('Propulsive power = ' + str(res[1]) + ' kW')
    eff_str.set('Propulsive efficiency = ' + str(res[2]) + ' %')



button1 = Button(root, text='Calculate', fg='black', command=turboCalculate)
button1.grid(row=3, column=2)

root.mainloop()


