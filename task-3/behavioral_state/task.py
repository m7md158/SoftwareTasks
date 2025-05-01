from abc import ABC, abstractmethod
# Abstract State
class ComputerState(ABC):
    @abstractmethod
    def press_button(self):
        pass

# Concrete States
class SleepState(ComputerState):
    def press_button(self):
        print("Waking up the computer from sleep.")

class ActiveState(ComputerState):
    def press_button(self):
        print("Shutting down the computer.")

class ShutdownState(ComputerState):
    def press_button(self):
        print("Cannot press button. Computer is already shut down.")

# Context: Computer
class Computer:
    def __init__(self):
        self.state = SleepState()  # Initial state

    def set_state(self, state: ComputerState):
        self.state = state

    def press_button(self):
        self.state.press_button()



# Client code
computer = Computer()

# Pressing the button when the computer is in Sleep state
computer.press_button()  # Transition to ActiveState
computer.set_state(ActiveState())

# Pressing the button when the computer is in Active state
computer.press_button()  # Transition to ShutdownState
computer.set_state(ShutdownState())

# Pressing the button when the computer is shut down
computer.press_button()
