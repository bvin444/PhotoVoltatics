import PySimpleGUI as sg
import math as math

class Homework:
    def __init__(self):
        pass
    def main_loop(self):
        self.window = self.create_main_window()
        while True:
                event, values = self.window.read()
                if event == "SUBMIT_5.1":
                    if self.Input_Validation(values["PEAK_SUN_HOURS"], values["ENERGY_REQUIREMENT"], values["SYSTEM_EFFICIENCY"], values["OVER_SIZING_FACTOR"]): break
                    self.window["OUTPUT_5.1"].update(round((float(values["ENERGY_REQUIREMENT"])*(1+float(values["OVER_SIZING_FACTOR"]))/(float(values["PEAK_SUN_HOURS"])*float(values["SYSTEM_EFFICIENCY"]))),2))
                elif event == "SUBMIT_5.2":
                    if self.Input_Validation(values["ENERGY_REQUIREMENT_2"], values["STORAGE_REQUIREMENT"], values["INVERTER_EFFICIENCY"], values["DISCHARGE_RATE"], values["BATTERY_RATING"]): break
                    total_Energy = float(float(values["ENERGY_REQUIREMENT_2"]) * float(values["STORAGE_REQUIREMENT"]))
                    total_Stored_Energy_Need = float(total_Energy / float(values["INVERTER_EFFICIENCY"]))
                    Output = float(round(total_Stored_Energy_Need / (float(values["DISCHARGE_RATE"])*float(values["BATTERY_RATING"])), 2))
                    self.window["OUTPUT_5.2"].update(math.ceil(Output))
                elif event == sg.WIN_CLOSED: break
        self.window.close()
    def create_main_window(self):
        Chapter_5_Problem_2 = sg.Frame("5.2", [
                        [sg.Text("What is your Daily Energy Requirement? (kWh)"), sg.Input("", key = "ENERGY_REQUIREMENT_2")],
                        [sg.Text("How many days of storage do you need? (Days)"), sg.Input("", key = "STORAGE_REQUIREMENT")],
                        [sg.Text("What is your discharge rate? "), sg.Input("", key = "DISCHARGE_RATE")],
                        [sg.Text("What is your Inverter Efficiency?"), sg.Input("", key = "INVERTER_EFFICIENCY")],
                        [sg.Text("What is the rating of the desired batteries? (kWh)"), sg.Input("", key = "BATTERY_RATING")],
                        [sg.Button("Submit", key = "SUBMIT_5.2")],
                        [sg.Text("Number of batteries needed (rounded_up):"), sg.Input("", key = "OUTPUT_5.2")]
                            ],
                        size = (320, 180), key = "5.1")
        Chapter_5_Problem_1 = sg.Frame("5.1", [
                        [sg.Text("What is your Energy Requirement?"), sg.Input("", key = "ENERGY_REQUIREMENT")],
                        [sg.Text("What are your Peak Sun Hours?"), sg.Input("", key = "PEAK_SUN_HOURS")],
                        [sg.Text("What is your System-Efficiency?"), sg.Input("", key = "SYSTEM_EFFICIENCY")],
                        [sg.Text("What is your Oversizing Factor?"), sg.Input("", key = "OVER_SIZING_FACTOR")],
                        [sg.Button("Submit", key = "SUBMIT_5.1")],
                        [sg.Text("Output (kWh):"), sg.Input("", key = "OUTPUT_5.1")]
                            ],
                        size = (320, 180), key = "5.1")
        layout = [
            [Chapter_5_Problem_1, Chapter_5_Problem_2],
        ]

        return sg.Window("BandGap Energy calculation", layout, resizable = True)
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