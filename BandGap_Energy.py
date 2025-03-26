import PySimpleGUI as sg
import math as math
from typing import ClassVar

class Homework:
    x: ClassVar[int] = 450
    y: ClassVar[int] = 220
    def __init__(self):
        pass
    def main_loop(self):
        self.window = self.create_main_window()
        while True: 

            event, values = self.window.read()
            if event == "SUBMIT_5.1":
                if self.Input_Validation("PEAK_SUN_HOURS", "ENERGY_REQUIREMENT", "SYSTEM_EFFICIENCY", "OVER_SIZING_FACTOR", values = values): continue
                self.Chapter_5_Problem_1()

            elif event == "SUBMIT_5.2":
                if self.Input_Validation("ENERGY_REQUIREMENT_2", "STORAGE_REQUIREMENT", "INVERTER_EFFICIENCY", "DISCHARGE_RATE", "BATTERY_RATING", values = values): continue
                self.Chapter_5_Problem_2()
                
            elif event == "SUBMIT_5.3":
                if self.Input_Validation("REFRIGERATOR", "MICROWAVE_POWER", "MICROWAVE_TIME", "TV_POWER", "TV_TIME", "LAMP_POWER", "LAMP_TIME", "WELL_POWER",
                                        "WELL_TIME", "EFFICIENCY", "AVERAGE_SOLAR_IRRADIATION", "DERATED_FACTOR", values = values): continue
                self.Chapter_5_Problem_3()

            elif event == "SUBMIT_5.5":
                # print(values])
                if self.Input_Validation("STORAGE_REQUIREMENT_5.5", "VOLTAGE", "AMP_HOURS", "DISCHARGE_RATE_5.5", "ENERGY_DEMAND_5.5", values = values): continue
                self.Chapter_5_Problem_5()
            elif event == "SUBMIT_QUIZ_2.1":
                # print(values])
                if self.Input_Validation("MODULE_EFFICIENCY_QUIZ_2_P1", "SOLAR_IRRADIATION_QUIZ_2_P1", "MODULE_AREA_QUIZ_2_P1", "SYSTEM_LOSS_QUIZ_2_P1", values = values): continue
                self.Quiz_2_Problem_1()
            elif event == "SUBMIT_QUIZ_2.2":
                # print(values])
                if self.Input_Validation("SOLAR_IRRADIATION_QUIZ_2_P2", "INVERTER_EFFICIENCY_QUIZ_2_P2", "DESIRED_ENERGY_PRODUCTION_QUIZ_2_P2", values = values): continue
                self.Quiz_2_Problem_2()
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
                        [sg.Text("What is the Average Solar Irradiation (kWh)?"), sg.Input("", key = "AVERAGE_SOLAR_IRRADIATION"), sg.Text("What is the PV-Module Efficiency (%)?"), sg.Input("", key = "EFFICIENCY"), sg.Text("What is your performance ratio (derated factor?"), sg.Input("", key = "DERATED_FACTOR")],
                        [sg.Button("Submit", key = "SUBMIT_5.3")],
                        [sg.Text("Power Rating (output):"), sg.Input("", key = "OUTPUT_5.3_A"), sg.Text("Total Area needed (output):"), sg.Input("", key = "OUTPUT_5.3_B")],
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

        QUIZ_2_Problem_1 = sg.Frame("Quiz 2 Problem 1", [
            [sg.Text("What is your PV module's efficiency? (%): "), sg.Input("", key = "MODULE_EFFICIENCY_QUIZ_2_P1")],
            [sg.Text("What is your solar irradiation?: "), sg.Input("", key = "SOLAR_IRRADIATION_QUIZ_2_P1")],
            [sg.Text("What is your module area? (m^2): "), sg.Input("", key = "MODULE_AREA_QUIZ_2_P1")],
            [sg.Text("What is your total loss? (%): "), sg.Input("", key = "SYSTEM_LOSS_QUIZ_2_P1")],
            [sg.Button("Submit", key = "SUBMIT_QUIZ_2.1")],
            [sg.Text("Output:"), sg.Input("", key = "OUTPUT_QUIZ_2.1")]
        ], size = (Homework.x, Homework.y), key = "Quiz_2_Problem_1")
        
        QUIZ_2_Problem_2 = sg.Frame("Quiz 2 Problem 2" , [
            [sg.Text("What is inverter_Efficiency (%): "), sg.Input("", key = "INVERTER_EFFICIENCY_QUIZ_2_P2")],
            [sg.Text("What is your solar irradiation? (kWh / m^2 / yr): "), sg.Input("", key = "SOLAR_IRRADIATION_QUIZ_2_P2")],
            [sg.Text("What is your desired energy production? (kWh): "), sg.Input("", key = "DESIRED_ENERGY_PRODUCTION_QUIZ_2_P2")],
            [sg.Button("Submit", key = "SUBMIT_QUIZ_2.2")],
            [sg.Text("Output (kWh):"), sg.Input("", key = "OUTPUT_QUIZ_2.2")]
        ], size = (Homework.x, Homework.y), key = "Quiz_2_Problem_2")

        HW_5 = [
            [Chapter_5_Problem_1, Chapter_5_Problem_2],
            [Chapter_5_Problem_3],
            [Chapter_5_Problem_5]
        ]

        QUIZ_2 = [
            [QUIZ_2_Problem_1, QUIZ_2_Problem_2],
        ]
        
        layout = [[sg.TabGroup([[sg.Tab("Homework_5", HW_5), sg.Tab("Quiz_2", QUIZ_2)]])]]
        return sg.Window("Homework_Analysis", layout, resizable = True)
    
    def Chapter_5_Problem_1(self, values):

        self.window["OUTPUT_5.1"].update(round((self.frame_values["ENERGY_REQUIREMENT"]*(1+self.frame_values["OVER_SIZING_FACTOR"])/(self.frame_values["PEAK_SUN_HOURS"]*self.frame_values["SYSTEM_EFFICIENCY"])),2))
    
    def Chapter_5_Problem_2(self, values):

        total_Energy = self.frame_values["ENERGY_REQUIREMENT_2"] * self.frame_values["STORAGE_REQUIREMENT"]
        total_Stored_Energy_Need = total_Energy / self.frame_values["INVERTER_EFFICIENCY"]
        Output = round(total_Stored_Energy_Need / (self.frame_values["DISCHARGE_RATE"]*self.frame_values["BATTERY_RATING"]), 2)
        self.window["OUTPUT_5.2"].update(math.ceil(Output))

    def Chapter_5_Problem_3(self, values):
    
        Energy_Refrigerator = self.frame_values['REFRIGERATOR']
        Energy_Microwave = (self.frame_values["MICROWAVE_POWER"] * self.frame_values["MICROWAVE_TIME"] * 60 / 3600000) # (1000 J / s * 300 s) / 3600
        Energy_TV = (self.frame_values["TV_POWER"] * self.frame_values["TV_TIME"] * 60 / 3600000) # Joules to kWh ->>> Joules / 3600\
        Energy_Lamp = (self.frame_values["LAMP_POWER"] * self.frame_values["LAMP_TIME"] * 60) / 3600000 * self.frame_values["LAMP_NUMBER"] # Joules to kWh ->>> Joules / 3600
        Energy_Well = (self.frame_values["WELL_POWER"] * self.frame_values["WELL_TIME"] * 60) / 3600000 # Joules to kWh ->>> Joules / 3600
        Total_Energy = Energy_Refrigerator + Energy_Microwave + Energy_TV + Energy_Lamp + Energy_Well
        PV_Module_Output = (self.frame_values["EFFICIENCY"])/100*(self.frame_values["AVERAGE_SOLAR_IRRADIATION"])*(self.frame_values["DERATED_FACTOR"])# how much energy I can produce with a single module
        self.window["OUTPUT_5.3_A"].update(f"{round(Total_Energy / PV_Module_Output, 2)} kWh")
        self.window["OUTPUT_5.3_B"].update(f"{round(Total_Energy / PV_Module_Output, 2)} m^2")

    def Chapter_5_Problem_5(self):

        print(self.frame_values)
        Power_Rating = (self.frame_values["VOLTAGE"]*self.frame_values["AMP_HOURS"]) / 1000 # Get kWh of battery
        Energy_Demand = self.frame_values["ENERGY_DEMAND_5.5"] # Energy Demand (day)
        Battery_Number = math.ceil((Energy_Demand*self.frame_values["STORAGE_REQUIREMENT_5.5"]) / (Power_Rating*(self.frame_values["DISCHARGE_RATE_5.5"])/100)) # (total energy need) / (power_rating times discharge_rate)
        self.window["OUTPUT_5.5"].update(f"{Battery_Number}") # output answer to window

    def Quiz_2_Problem_1(self):  

        module_Efficiency = self.frame_values["MODULE_EFFICIENCY_QUIZ_2_P1"] / 100
        solar_Irradiation = self.frame_values["SOLAR_IRRADIATION_QUIZ_2_P1"]
        module_Area = self.frame_values["MODULE_AREA_QUIZ_2_P1"]
        system_Loss = (100 - self.frame_values["SYSTEM_LOSS_QUIZ_2_P1"]) / 100
        specific_Yield = module_Efficiency * solar_Irradiation
        annual_Energy_Production = specific_Yield * module_Area
        net_Energy_Production = annual_Energy_Production * system_Loss
        self.window["OUTPUT_QUIZ_2.1"].update(f"{net_Energy_Production}") # output answer to window
    
    def Quiz_2_Problem_2(self):  

        desired_Energy = self.frame_values["DESIRED_ENERGY_PRODUCTION_QUIZ_2_P2"]
        solar_Irradiation = self.frame_values["SOLAR_IRRADIATION_QUIZ_2_P2"]
        inverter_Efficiency = self.frame_values["INVERTER_EFFICIENCY_QUIZ_2_P2"] / 100
        self.window["OUTPUT_QUIZ_2.2"].update(round(desired_Energy/(solar_Irradiation*inverter_Efficiency), 2))

    def Input_Validation(self, *argv, values):

        for value in argv:
            if values[value] == '':
                sg.popup("Input cannot be blank!", keep_on_top = True)
                return True
            try:
                float(values[value])
            except:
                print(value)
                sg.popup("Input must a numerical value")
                return True
        self.frame_values = {value : float(values[value]) for value in argv} # dictionary comprehension
        print(self.frame_values)
        return False      

if __name__ == "__main__":
     Home_Work_Solutions = Homework() # class instantiation
     Home_Work_Solutions.main_loop()