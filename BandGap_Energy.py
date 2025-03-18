import PySimpleGUI as sg
import math as math
from typing import ClassVar

class Homework:
    # TODO: figure out how to more seemlessly configure inputs as floats.
    x: ClassVar[int] = 450
    y: ClassVar[int] = 290
    def __init__(self):
        pass
    def main_loop(self):
        self.window = self.create_main_window()
        while True: 
                event, values = self.window.read()
                if event == "SUBMIT_5.1":
                    if self.Input_Validation(values["PEAK_SUN_HOURS"], values["ENERGY_REQUIREMENT"], values["SYSTEM_EFFICIENCY"], values["OVER_SIZING_FACTOR"]): continue
                    self.window["OUTPUT_5.1"].update(round((float(values["ENERGY_REQUIREMENT"])*(1+float(values["OVER_SIZING_FACTOR"]))/(float(values["PEAK_SUN_HOURS"])*float(values["SYSTEM_EFFICIENCY"]))),2))
                elif event == "SUBMIT_5.2":
                    if self.Input_Validation(values["ENERGY_REQUIREMENT_2"], values["STORAGE_REQUIREMENT"], values["INVERTER_EFFICIENCY"], values["DISCHARGE_RATE"], values["BATTERY_RATING"]): continue
                    total_Energy = float(float(values["ENERGY_REQUIREMENT_2"]) * float(values["STORAGE_REQUIREMENT"]))
                    total_Stored_Energy_Need = float(total_Energy / float(values["INVERTER_EFFICIENCY"]))
                    Output = float(round(total_Stored_Energy_Need / (float(values["DISCHARGE_RATE"])*float(values["BATTERY_RATING"])), 2))
                    self.window["OUTPUT_5.2"].update(math.ceil(Output))
                elif event == "SUBMIT_5.3":
                    if self.Input_Validation(values["REFRIGERATOR"], values["MICROWAVE_POWER"], values["MICROWAVE_TIME"], values["TV_POWER"], values["TV_TIME"], values["LAMP_POWER"], values["LAMP_TIME"], values["WELL_POWER"],
                    values["WELL_TIME"], values["EFFICIENCY"], values["AVERAGE_SOLAR_IRRADIATION"], values["DERATED_FACTOR"]): continue
                    Energy_Refrigerator = float(values['REFRIGERATOR']) 
                    Energy_Microwave = float((float(values["MICROWAVE_POWER"]) * float(values["MICROWAVE_TIME"]) * 60) / 3600000) # (1000 J / s * 300 s) / 3600
                    Energy_TV = float((float(values["TV_POWER"]) * float(values["TV_TIME"]) * 60) / 3600000) # Joules to kWh ->>> Joules / 3600\
                    Energy_Lamp = float((float(values["LAMP_POWER"]) * float(values["LAMP_TIME"]) * 60) / 3600000) * float(values["LAMP_NUMBER"]) # Joules to kWh ->>> Joules / 3600
                    Energy_Well = float((float(values["WELL_POWER"]) * float(values["WELL_TIME"]) * 60) / 3600000) # Joules to kWh ->>> Joules / 3600
                    Total_Energy = Energy_Refrigerator + Energy_Microwave + Energy_TV + Energy_Lamp + Energy_Well
                    PV_Module_Output = float((float(values["EFFICIENCY"])/100)*(float(values["AVERAGE_SOLAR_IRRADIATION"]))*(float(values["DERATED_FACTOR"]))) # how much energy I can produce with a single module
                    self.window["OUTPUT_5.3_A"].update(f"{round(float(Total_Energy / PV_Module_Output), 2)} kWh")
                    self.window["OUTPUT_5.3_B"].update(f"{round(float(Total_Energy / PV_Module_Output), 2)} m^2")
                elif event == "SUBMIT_5.5":
                    Power_Rating = float(values["VOLTAGE"])*float(values["AMP_HOURS"]) / 1000
                    Energy_Demand = float(values["ENERGY_DEMAND_5.5"])
                    Battery_Number = math.ceil((Energy_Demand**float(values["STORAGE_REQUIREMENT_5.5"])) / (Power_Rating*((float(values["DISCHARGE_RATE_5.5"])/100))))
                    self.window["OUTPUT_5.5"].update(f"{Battery_Number}")
                elif event == sg.WIN_CLOSED: break
        self.window.close()
    def create_main_window(self):
        Chapter_5_Problem_5 = sg.Frame("5.5", [
                        [sg.Text("How many days of storage do you need?"), sg.Input("", key = "STORAGE_REQUIREMENT_5.5")],
                        [sg.Text("Battery specification (Voltage)?"), sg.Input("", key = "VOLTAGE")],
                        [sg.Text("Battery specification (amp-hours)?"), sg.Input("", key = "AMP_HOURS")],
                        [sg.Text("What is the Discharge-Rate (%) ?"), sg.Input("", key = "DISCHARGE_RATE_5.5")],
                        [sg.Text("Energy demand (kWh)?"), sg.Input("", key = "ENERGY_DEMAND_5.5")],
                        [sg.Button("Submit", key = "SUBMIT_5.5")],
                        [sg.Text("Number of batteries needed (rounded_up):"), sg.Input("", key = "OUTPUT_5.5")]
                            ],
                        size = (Homework.x, Homework.y), key = "5.5")
        Chapter_5_Problem_3 = sg.Frame("5.3", [ # First put everything into kWh. # Email the professor about this problem.
                        [sg.Text("How much energy does the refrigerator use per day (kWh)?"), sg.Input("", key = "REFRIGERATOR")],
                        [sg.Text("How much Power does the Microwave use (W)?"), sg.Input("", key = "MICROWAVE_POWER"), sg.Text("Length of use (min)?"), sg.Input("", key = "MICROWAVE_TIME")],
                        [sg.Text("How much power does the TV use (min)?"), sg.Input("", key = "TV_POWER"), sg.Text("Length of use (min)?"), sg.Input("", key = "TV_TIME")],
                        [sg.Text("How much power do the lamps use (W)?"), sg.Input("", key = "LAMP_POWER"), sg.Text("Length of use (min)?"), sg.Input("", key = "LAMP_TIME")],
                        [sg.Text("How many lamps do you have?"), sg.Input("", key = "LAMP_NUMBER")],
                        [sg.Text("How much power does the well use (W)?"), sg.Input("", key = "WELL_POWER"), sg.Text("Length of use (min)?"), sg.Input("", key = "WELL_TIME")],
                        [sg.Text("What is the Average Solar Irradiation (kWh)?"), sg.Input("", key = "AVERAGE_SOLAR_IRRADIATION")],
                        [sg.Text("What is the PV-Module Efficiency (%)?"), sg.Input("", key = "EFFICIENCY")],
                        [sg.Text("What is your performance ratio (derated factor?"), sg.Input("", key = "DERATED_FACTOR")],
                        [sg.Text("Power Rating:"), sg.Input("", key = "OUTPUT_5.3_A")],
                        [sg.Text("Total Area needed:"), sg.Input("", key = "OUTPUT_5.3_B")],
                        [sg.Button("Submit", key = "SUBMIT_5.3")],
                            ],
                        size = (1000, Homework.y), key = "5.3")
        Chapter_5_Problem_2 = sg.Frame("5.2", [
                        [sg.Text("What is your Daily Energy Requirement? (kWh)"), sg.Input("", key = "ENERGY_REQUIREMENT_2")],
                        [sg.Text("How many days of storage do you need? (Days)"), sg.Input("", key = "STORAGE_REQUIREMENT")],
                        [sg.Text("What is your discharge rate? "), sg.Input("", key = "DISCHARGE_RATE")],
                        [sg.Text("What is your Inverter Efficiency?"), sg.Input("", key = "INVERTER_EFFICIENCY")],
                        [sg.Text("What is the rating of the desired batteries? (kWh)"), sg.Input("", key = "BATTERY_RATING")],
                        [sg.Button("Submit", key = "SUBMIT_5.2")],
                        [sg.Text("Number of batteries needed (rounded_up):"), sg.Input("", key = "OUTPUT_5.2")]
                            ],
                        size = (Homework.x, Homework.y), key = "5.2")
        Chapter_5_Problem_1 = sg.Frame("5.1", [
                        [sg.Text("What is your Energy Requirement?"), sg.Input("", key = "ENERGY_REQUIREMENT")],
                        [sg.Text("What are your Peak Sun Hours?"), sg.Input("", key = "PEAK_SUN_HOURS")],
                        [sg.Text("What is your System-Efficiency?"), sg.Input("", key = "SYSTEM_EFFICIENCY")],
                        [sg.Text("What is your Oversizing Factor?"), sg.Input("", key = "OVER_SIZING_FACTOR")],
                        [sg.Button("Submit", key = "SUBMIT_5.1")],
                        [sg.Text("Output (kWh):"), sg.Input("", key = "OUTPUT_5.1")]
                            ],
                        size = (Homework.x, Homework.y), key = "5.1")
        HW_5 = [
            [Chapter_5_Problem_1, Chapter_5_Problem_2],
            [Chapter_5_Problem_3],
            [Chapter_5_Problem_5]
        ]
        HW_4 = [
            [sg.Button("HW_4_Solutiions", key = "NONE")]
        ]
        layout = [[sg.TabGroup([[sg.Tab("Homework_5", HW_5), sg.Tab("Homework_4", HW_4)]])]]
       

        return sg.Window("Homework_Analysis", layout, resizable = True)
    def Input_Validation(self, *argv):
        for value in argv:
            if value == '':
                sg.popup("Input cannot be blank!", keep_on_top = True)
                return True
        return False      

if __name__ == "__main__":
     Home_Work_Solutions = Homework() # class instantiation
     Home_Work_Solutions.main_loop()
# For work, let us code up solutions to homework problems 5.1, 5.2, 5.3, 5.4