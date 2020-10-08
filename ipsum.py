"""
Cras  sit  amet  lorem  fermentum,  ornare  enim  placerat,  fermentum  turpis.
Suspendisse  efficitur,  metus  at  faucibus  pretium,  risus erat tempus quam,
imperdiet  maximus justo mi at augue. Curabitur ac ullamcorper dolor. Phasellus
in ligula finibus, mollis augue eget, venenatis justo. Donec eget mauris lacus.

Lorem  ipsum  dolor sit amet, consectetur adipiscing elit. Donec et condimentum
tortor,  vel  cursus  mi.  Morbi  vel  arcu  auctor,  sodales  libero sit amet,
convallis  magna.  Integer libero odio, molestie eget elementum nec, rhoncus id
mi. Donec pulvinar blandit ex, non tempor risus volutpat a. Nullam sollicitudin
cursus  sem  eget posuere. Nulla gravida vel nunc at ultricies. Fusce quis quam
pulvinar, suscipit nibh a, consectetur velit.
"""

from lorem import function_1

class Class_1:
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

    Attributes
    ----------

    a1 : str
        Aenean ac enim enim. Curabitur et auctor lorem.
    a2 : Float
        Nullam in cursus orci, eget sodales nunc
    """

    def __init__(self, a1, a2):
        """
        Aliquam  vel  leo  id  nunc elementum euismod. Suspendisse lorem neque,
        bibendum  non  nisl  vulputate,  imperdiet  pharetra dui. Donec varius,
        nulla  in malesuada tincidunt, ex libero sodales ex, euismod porta odio
        lacus  non  diam.  Fusce  urna  elit,  viverra  commodo  elementum sed,
        vehicula dictum odio.

        Parameters
        ----------

        a1 : str
            Aenean ac enim enim. Curabitur et auctor lorem.
        a2 : Float
            Nullam in cursus orci, eget sodales nunc

        Returns
        -------

        None.
        """
        self.a1 = a1
        self.a2 = a2
    
    def method_1(self):
        """
        Aliquam  vel  leo  id  nunc elementum euismod. Suspendisse lorem neque,
        bibendum  non  nisl  vulputate,  imperdiet  pharetra dui. Donec varius,
        nulla  in malesuada tincidunt, ex libero sodales ex, euismod porta odio
        lacus  non  diam.  Fusce  urna  elit,  viverra  commodo  elementum sed,
        vehicula dictum odio.
        """
        function_1(self.a1, self.a2)