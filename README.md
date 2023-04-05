# Customizable Unit Converter
This is a simple unit converter component featuring the ability to create and use your own custom conversions.
## Installation
The component is installed using:
``` Python
>>> pip install UnitConverter
```
The component is uninstalled using:
``` Python
>>> pip uninstall UnitConverter
```
## Usage
The component is imported using:
``` Python
>>> from UnitConverter import UnitConverter
```
### Built In Unit Conversions
This component supports the following unit conversions:
- Weight: kilograms (kg), grams (g), miligrams (mg), tonnes (t), pounds (lbs), ounces (oz), carats (car);

- Length: meters (m), kilometers (kg), centimeters (cm), millimeters (mm), miles (mi), yards (yd), feet (ft), inches (in);

- Area: square meters (m^2), square kilometers (km^2), square centimeters (cm^2), hectares (ha), acres (ac), square miles (mi^2), square yards (yd^2), square feet (ft^2), square inches (in^2);

- Volume: cubic meters (m^3), cubic centimeters (cm^3), cubic millimeters (mm^3), liters (L), milliliters (mL), cubic yards (yd^3), cubic feet (ft^3), cubic inches (in^3);

- Time: seconds (s), milliseconds (ms), minutes (min), hours (h), days (d) , weeks (week), months (month), years (year).

To use these conversions:

&emsp;&emsp;UnitConverter.BaseUnitConverter.<i>Type</i>(<i>Amount</i>, "<i>Abbreviation</i>", "<i>Abbreviation</i>")

Example:
``` Python
>>> UnitConverter.BaseUnitConverter.Weight(5, "kg", "lbs")
11.023113109
```
### Customizable Unit Converter
First you need to have an array of supported units. Let's say you have three different measurement units you need to convert between, called "Aaa", "Bbb" and "Ccc":
``` Python
>>> Units = ["Aaa", "Bbb", "Ccc"]
```
Next step is to define the conversion coeffients. Let's say that `1 Aaa = 2 Bbb` and `1 Bbb = 2.5 Ccc`. Then the whole matrix would look like:

|         | Aaa | Bbb | Ccc |
|---------|-----|-----|-----|
| **Aaa** | 1   | 2   | 5   |
| **Bbb** | 0.5 | 1   | 2.5 |
| **Ccc** | 0.2 | 0.4 | 1   |

``` Python
>>> Matrix = [[1, 2, 5],
              [0.5, 1, 2.5],
              [0.2, 0.4, 1]]
```
Creating our custom converter object with these parameters:
``` Python
>>> MyCustomConverter = UnitConverter.CustomConverter(Units, Matrix)
```
The conversions are done the same way as before:
``` Python
>>> MyCustomConverter.Convert(2, "Aaa", "Bbb")
4
```
#### Additional Customizable Unit Converter Features
##### Editing the parameter values
While the parameters can be accesed directly, it is recommended to use the `Change()` methods to edit them. It accepts optional `Units` unit array and `Matrix` conversion matrix arguments
```
>>> MyCustomConverter.Units
['Aaa', 'Bbb', 'Ccc']
>>> NewUnits = ["Ddd", "Eee", "Fff"]
>>> MyCustomConverter.Change(Units=NewUnits)
>>> MyCustomConverter.Units
['Ddd', 'Eee', 'Fff']
```
It is also possible to edit a single conversion coefficient with the `ChangeSingle()` method:
``` Python
>>> MyCustomConverter.Matrix
[[1, 2, 5], [0.5, 1, 2.5], [0.2, 0.4, 1]]
>>> MyCustomConverter.ChangeSingle("Ddd","Eee",5)
>>> MyCustomConverter.Matrix
[[1, 5, 5], [0.2, 1, 2.5], [0.2, 0.4, 1]]
```
##### Printing the parameters
Printing the unit converter parameters can also be done using the `Print()` method:
``` Python
>>> MyCustomConverter.Print()
['Ddd', 'Eee', 'Fff']
[[1, 5, 5], [0.2, 1, 2.5], [0.2, 0.4, 1]]
```
This method also accepts optional `Units` and `Matrix` bool values in case you want to see only the relevant info: 
``` Python
>>> MyCustomConverter.Print(Units=True)
['Ddd', 'Eee', 'Fff']
```