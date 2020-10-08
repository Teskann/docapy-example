"""
Lorem  ipsum  dolor sit amet, consectetur adipiscing elit. Donec et condimentum
tortor,  vel  cursus  mi.  Morbi  vel  arcu  auctor,  sodales  libero sit amet,
convallis  magna.  Integer libero odio, molestie eget elementum nec, rhoncus id
mi. Donec pulvinar blandit ex, non tempor risus volutpat a. Nullam sollicitudin
cursus  sem  eget posuere. Nulla gravida vel nunc at ultricies. Fusce quis quam
pulvinar, suscipit nibh a, consectetur velit.

>>> print("Hello World")
Hello World
>>> 1+1
2

"""

from numpy import cos

def function_1(param1, param2):
    """
    Description
    -----------

    Vivamus tristique, enim ut dapibus rutrum, enim sapien convallis metus, sed
    porta  nulla  felis  id  dui.  Nam  dignissim  felis  odio, in tempus massa
    sagittis  quis.  Aenean  id  tempor  mauris.  Nam  pretium ipsum risus, nec
    tristique  mauris  scelerisque  non.  Duis maximus, urna consequat placerat
    blandit,  ipsum  sem  vehicula  ex,  non  pulvinar ligula lacus sed libero.
    Aliquam  id  nisl  eu  ipsum ultrices varius eget id urna. Integer suscipit
    nisl lacus,  id congue libero finibus vestibulum. Proin luctus vitae sem at
    iaculis. Aliquam erat volutpat.

    Parameters
    ----------

    param1 : str
        Aenean ac enim enim. Curabitur et auctor lorem.
    param2: int
        Nullam in cursus orci, eget sodales nunc :
            - Ut mollis, est non viverra consequat
            - metus turpis varius est
            - id tincidunt lorem eros sit amet turpis
    
    Returns
    -------

    None.

    Example
    -------

    >>> function1("Hey", 10)
    Hello World ! Hey 10

    """
    print("Hello World !", param1, param2)

def function_2(param1, param2):
    """
    Description
    -----------

    Vivamus tristique, enim ut dapibus rutrum, enim sapien convallis metus, sed
    porta  nulla  felis  id  dui.  Nam  dignissim  felis  odio, in tempus massa
    sagittis  quis.  Aenean  id  tempor  mauris.  Nam  pretium ipsum risus, nec
    tristique  mauris  scelerisque  non.  Duis maximus, urna consequat placerat
    blandit,  ipsum  sem  vehicula  ex,  non  pulvinar ligula lacus sed libero.
    Aliquam  id  nisl  eu  ipsum ultrices varius eget id urna. Integer suscipit
    nisl lacus,  id congue libero finibus vestibulum. Proin luctus vitae sem at
    iaculis. Aliquam erat volutpat.

    Parameters
    ----------

    param1 : str
        Aenean ac enim enim. Curabitur et auctor lorem.
    param2 : Float
        Nullam in cursus orci, eget sodales nunc :
            - Ut mollis, est non viverra consequat
            - metus turpis varius est
            - id tincidunt lorem eros sit amet turpis
    
    Returns
    -------

    None.

    Example
    -------

    >>> function2("Hey", 10)
    Hello World !
    Hey 10

    """

    def nested_function():
        """
        Aliquam  vel  leo  id  nunc elementum euismod. Suspendisse lorem neque,
        bibendum  non  nisl  vulputate,  imperdiet  pharetra dui. Donec varius,
        nulla  in malesuada tincidunt, ex libero sodales ex, euismod porta odio
        lacus  non  diam.  Fusce  urna  elit,  viverra  commodo  elementum sed,
        vehicula dictum odio.

        Returns
        -------

        None.
        """
        print("Hello World !")
    
    nested_function()
    print(param1, cos(param2))

    