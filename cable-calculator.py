class InstallationCalculator:
    def __init__(self):
        self.lengths = []
        self.roll_sizes = []
        self.camera_quantities = {}

    def set_camera_lengths(self):
        print("Enter possible camera lengths (comma separated):")
        lengths_str = input().strip()
        self.lengths = [int(length.strip())
                        for length in lengths_str.split(",")]
        print(f"Camera lengths set: {self.lengths}\n")

    def set_roll_sizes(self):
        print("Enter possible roll sizes (comma separated):")
        sizes_str = input().strip()
        self.roll_sizes = [int(size.strip()) for size in sizes_str.split(",")]
        print(f"Roll sizes set: {self.roll_sizes}\n")

    def set_camera_quantities(self):
        print("Enter camera quantities for each length:")
        for length in self.lengths:
            quantity = int(input(f"{length} meters: "))
            self.camera_quantities[length] = quantity
        print(f"Camera quantities set: {self.camera_quantities}\n")

    def get_information(self):
        return {
            "lengths": self.lengths,
            "roll_sizes": self.roll_sizes,
            "camera_quantities": self.camera_quantities
        }


calc = InstallationCalculator()
calc.set_camera_lengths()
calc.set_roll_sizes()
calc.set_camera_quantities()
info = calc.get_information()
