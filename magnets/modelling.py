class Material:
    def __init__(self, name) -> None:
        """
        * @param: name - name of matierial
        """
        self.name = name

class Rod:
    def __init__(self, material, length, diameter, pos=(0,0,0), shape="cylinder") -> None:
        """
        * @param: material - another class that has the materials properties
        * @param: length (float - m)
        * @param: diameter (float - m)
        * @param: pos - vector position of centre of mass - assumes uniform

        """
        self.material = material
        self.length = length
        self.diameter = diameter
        self.pos = pos
        self.shape = shape

class Transformer:
    def __init__(self, material, num_coils, dimensions, pos=(0,0,0), voltage = 0, current = 0) -> None:
        """
        * @param: material - class object
        * @param: num_coils - int
        * @param: dimensions - {"outer": m, "inner",: m}
        * @param: voltage - V (float)
        * @param: current - Amps (float)
        """
        self.material = material
        self.num_coils = num_coils
        self.dimensions = dimensions
        self.pos = pos
        self.voltage = voltage
        self.current = current





