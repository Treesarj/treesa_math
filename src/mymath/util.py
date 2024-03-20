import math
from pint import UnitRegistry

# Initialize a unit registry
ureg = UnitRegistry()

def with_pint_units(return_unit=None):
    """
    A decorator factory that accepts an optional return_unit argument
    and returns a new decorator. 
    """
    def decorator(func):
        """
        The decorator as a closure. very cool :)
        """
        def wrapper(*args, **kwargs):
            # Extract magnitudes from the arguments
            magnitudes = [arg.magnitude if hasattr(arg, 'magnitude') else arg for arg in args]
            
            # Call the original function with the magnitudes
            result = func(*magnitudes, **kwargs)
            
            # Apply the specified unit back to the result if provided
            if return_unit is not None:
                result_unit = ureg.parse_expression(return_unit)
                return result * result_unit
            else:
                # If no return unit specified, attempt to use the unit of the first argument
                if hasattr(args[0], 'units'):
                    return result * args[0].units
                else:
                    return result
            
        return wrapper
    return decorator

@with_pint_units
def square_root(v):
    return math.sqrt(v)
