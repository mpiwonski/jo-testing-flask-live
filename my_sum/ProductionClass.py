class ProductionClass:

    a = None
    b = None

    def intermediate_function(self, a, b):
        return self.a * self.b

    def complex_function(self):
        return 2 * self.intermediate_function()