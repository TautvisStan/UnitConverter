'''
This module will let you convert one measurement unit to another.
'''
class BaseUnitConverter:
    '''
    The base class. It has the five main conversion types
    '''
    def Convert(amount:float, unitFrom:str, unitTo:str, Units:str, Matrix:float):
        ''' This method does the conversion from the current unit to the new unit. You can use it if you want to define your own custom conversions.

        Args:
           | amount (float) - amount of current units 
           | unitFrom (string) - current unit 
           | unitTo (string) - new unit
           | Units (string array) - array of all supported units that can be converted to each other
           | Matrix (float matrix) - conversion matrix at the size of [Units][Units]
        Returns:
           | float - conversion result
        '''
        try:
            unitFromIndex = Units.index(unitFrom)
        except:
            unitFromIndex = -1
        try:
            unitToIndex = Units.index(unitTo)
        except:
            unitToIndex = -1
        if(unitFromIndex == -1):
            raise Exception("Current unit not found: " + unitFrom)
        if(unitToIndex == -1):
            raise Exception("New unit not found: " + unitTo)
        if(unitFromIndex != -1 and unitToIndex != -1):
            return amount * Matrix[unitFromIndex][unitToIndex]
        
    def Weight(amount:float, unitFrom:str, unitTo:str):
        ''' Weight conversion method

        Args:
            | amount (float) - amount of current units
            | unitFrom (string) - current unit
            | unitTo (string) - new unit
        Returns:
            | float - conversion result
        '''
        Units = ["kg", "g", "mg", "t", "lbs", "oz", "car"]
        Matrix = [[1, 1000, 1000000, 0.001, 2.2046226218 , 35.27396195 , 5000 ],
                 [0.001 ,1,1000 ,0.000001,0.0022046226,0.0352739619,5 ],
                 [0.000001, 0.001,1,1e-9,0.0000022046,0.000035274,0.005],
                 [1000,1000000,1000000000,1,2204.6226218,35273.96195,5000000],
                 [0.45359237,453.59237,453592.37,0.0004535924,1,16,2267.96185],
                 [0.0283495231,28.349523125,28349.523125,0.0000283495,0.0625,1,141.74761563],
                 [0.0002,0.2,200,2e-7,0.0004409245,0.0070547924,1]]
        return UnitConverter.Convert(amount, unitFrom, unitTo, Units, Matrix)
    
    def Length(amount:float, unitFrom:str, unitTo:str):
        ''' Length conversion method

        Args:
            | amount (float) - amount of current units
            | unitFrom (string) - current unit
            | unitTo (string) - new unit
        Returns:
            | float - conversion result
        '''
        Units = ["m", "km", "cm", "mm", "mi", "yd", "ft", "in"]
        Matrix = [[1,0.001,100,1000,0.0006213689,1.0936132983,3.280839895,39.37007874],
                  [1000,1,100000,1000000,0.6213688756,1093.6132983,3280.839895,39370.07874],
                  [0.01,0.00001,1,10,0.0000062137,0.010936133,0.032808399,0.3937007874],
                  [0.001,0.000001,0.1,1,6.213688756e-7,0.0010936133,0.0032808399,0.0393700787],
                  [1609.35,1.60935,160935,1609350,1,1760.0065617,5280.019685,63360.23622],
                  [0.9144,0.0009144,91.44,914.4,0.0005681797,1,3,36],
                  [0.3048,0.0003048,30.48,304.8,0.0001893932,0.3333333333,1,12],
                  [0.0254,0.0000254,2.54,25.4,0.0000157828,0.0277777778,0.0833333333,1]]

        return UnitConverter.Convert(amount, unitFrom, unitTo, Units, Matrix)
    
    def Area(amount:float, unitFrom:str, unitTo:str):
        ''' Area conversion method

        Args:
            | amount (float) - amount of current units
            | unitFrom (string) - current unit
            | unitTo (string) - new unit
        Returns:
            | float - conversion result
        '''
        Units = ["m^2", "km^2", "cm^2", "ha", "ac", "mi^2", "yd^2", "ft^2", "in^2"]
        Matrix = [[1,0.000001,10000,0.0001,0.0002471054,3.861021585e-7,1.1959900463,10.763910417,1550.0031],
                  [1000000,1,10000000000,100,247.10538147,0.3861021585,1195990.0463,10763910.417,1550003100],
                  [0.0001,1e-10,1,1e-8,2.471053814e-8,3.861021585e-11,0.000119599,0.001076391,0.15500031],
                  [10000,0.01,100000000,1,2.4710538147,0.0038610216,11959.900463,107639.10417,15500031],
                  [4046.8564224,0.0040468564,40468564.224,0.4046856422,1,0.0015625,4840,43560,6272640],
                  [2589988.1103,2.5899881103,25899881103,258.99881103,640,1,3097600,27878400,4014489600],
                  [0.83612736,8.361273599e-7,8361.2736,0.0000836127,0.0002066116,3.228305785e-7,1,9,1296],
                  [0.09290304,9.290303999e-8,929.0304,0.0000092903,0.0000229568,3.587006427e-8,0.1111111111,1,144],
                  [0.00064516,6.4516e-10,6.4516,6.4516e-8,1.594225079e-7,2.490976686e-10,0.0007716049,0.0069444444,1]]


        return UnitConverter.Convert(amount, unitFrom, unitTo, Units, Matrix)
    
    def Volume(amount:float, unitFrom:str, unitTo:str):
        ''' Volume conversion method

        Args:
            | amount (float) - amount of current units
            | unitFrom (string) - current unit
            | unitTo (string) - new unit
        Returns:
            | float - conversion result
        '''
        Units = ["m^3", "cm^3", "mm^3", "L", "mL", "yd^3", "ft^3", "in^3"]
        Matrix = [[1,1000000,1000000000,1000,1000000,1.3079506193,35.314666721,61023.744095],
                  [0.000001,1,1000,0.001,1,0.000001308,0.0000353147,0.0610237441],
                  [1e-9,0.001,1,0.000001,0.001,1.307950619e-9,3.531466672e-8,0.0000610237],
                  [0.001,1000,1000000,1,1000,0.0013079506,0.0353146667,61.023744095],
                  [0.000001,1,1000,0.001,1,0.000001308,0.0000353147,0.0610237441],
                  [0.764554858,764554.85798,764554857.98,764.55485798,764554.85798,1,27,46656],
                  [0.0283168466,28316.846592,28316846.592,28.316846592,28316.846592,0.037037037,1,1728],
                  [0.0000163871,16.387064,16387.064,0.016387064,16.387064,0.0000214335,0.0005787037,1]]

        return UnitConverter.Convert(amount, unitFrom, unitTo, Units, Matrix)
    
    def Time(amount:float, unitFrom:str, unitTo:str):
        ''' Time conversion method

        Args:
            | amount (float) - amount of current units
            | unitFrom (string) - current unit
            | unitTo (string) - new unit
        Returns:
            | float - conversion result
        '''
        Units = ["s", "ms", "min", "h", "d", "week", "month", "year"]
        Matrix = [[1,1000,0.0166666667,0.0002777778,0.0000115741,0.0000016534,3.802570537e-7,3.168808781e-8],
                  [0.001,1,0.0000166667,2.777777777e-7,1.157407407e-8,1.653439153e-9,3.802570537e-10,3.168808781e-11],
                  [60,60000,1,0.0166666667,0.0006944444,0.0000992063,0.0000228154,0.0000019013],
                  [3600,3600000,60,1,0.0416666667,0.005952381,0.0013689254,0.0001140771],
                  [86400,86400000,1440,24,1,0.1428571429,0.0328542094,0.0027378508],
                  [604800,604800000,10080,168,7,1,0.2299794661,0.0191649555],
                  [2629800,2629800000,43830,730.5,30.4375,4.3482142857,1,0.0833333333],
                  [31557600,31557600000,525960,8766,365.25,52.178571429,12,1]]

        return UnitConverter.Convert(amount, unitFrom, unitTo, Units, Matrix)

class CustomConverter:
    '''
    The customizable unit converter class
    '''
    def __init__(self, Units:str, Matrix:float):
        '''
        Args:
            | Units (string array) - array of all supported units that can be converted to each other
            | Matrix (float matrix) - conversion matrix at the size of [Units][Units]
        '''
        ArrayLength = len(Units)
        if (len(Units) != len(set(Units))):
            raise Exception("Unit array contains duplicates!")
        if(len(Matrix) == ArrayLength and len(Matrix[0]) == ArrayLength):
            self.Units = Units
            self.Matrix = Matrix
        else:
            raise Exception("Unit array and conversion matrix sizes does not match!")
        
    def Print(self, Units:bool=False, Matrix:bool=False):
        ''' Converter parameter print method

        Args:
            | Units (bool) - Should it print the units?
            | Matrix (bool) - Should it print the matrix?
        '''
        if(Units == True):
            print(self.Units)
        if(Matrix == True):
            print(self.Matrix)
        if(Units == False and Matrix == False):
            print(self.Units)
            print(self.Matrix)
    def ChangeSingle(self, UnitFrom:str, UnitTo:str, Conversion:float):
        ''' Single conversion change method

        Args:
            | unitFrom (string) - current unit
            | unitTo (string) - new unit
            | Conversion (float) - conversion coefficient
        '''
        try:
            unitFromIndex = self.Units.index(UnitFrom)
        except:
            unitFromIndex = -1
        try:
            unitToIndex = self.Units.index(UnitTo)
        except:
            unitToIndex = -1
        if(unitFromIndex == -1):
            raise Exception("Current unit not found: " + UnitFrom)
        if(unitToIndex == -1):
            raise Exception("New unit not found: " + UnitTo)
        if(unitFromIndex != -1 and unitToIndex != -1):
            self.Matrix[unitFromIndex][unitToIndex] = Conversion
            self.Matrix[unitToIndex][unitFromIndex] = 1/Conversion
    def Change(self, Units:str=None, Matrix:float=None):
        ''' Converter parameter change method. Both arguments are optional.

        Args:
            | Units (string array) - array of all supported units that can be converted to each other
            | Matrix (float matrix) - conversion matrix at the size of [Units][Units]
        '''
        if(Units != None and Matrix != None):
            if (len(Units) != len(set(Units))):
                raise Exception("Unit array contains duplicates!")
            if(len(Units) == len(Matrix) and len(Units) == len(Matrix[0])):
                self.Units = Units
                self.Matrix = Matrix
            else:
                raise Exception("Unit array and conversion matrix sizes does not match!")
        else:
            if(Units != None):
                if(len(Units) == len(self.Units)):
                    self.Units = Units
                else:
                    raise Exception("Unit array length does not match!")
            if(Matrix != None):
                if(len(Matrix) == len(self.Matrix)):
                    self.Matrix = Matrix
                else:
                    raise Exception("Conversion matrix size does not match!")
                
    def Convert(self, amount:float, unitFrom:str, unitTo:str):
        ''' Unit conversion method.

        Args:
            | amount (float) - amount of current units
            | unitFrom (string) - current unit
            | unitTo (string) - new unit
        Returns:
            | float - conversion result
        '''
        return UnitConverter.Convert(amount, unitFrom, unitTo, self.Units, self.Matrix)
