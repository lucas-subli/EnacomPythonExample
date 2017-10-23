from source import vehicle


class Motorcycle(vehicle):
    """A motorcycle for sale."""

    base_sale_price = 4000
    wheels = 2

    @staticmethod
    def vehicle_type():
        """
        Returns: string representing the type of vehicle this is.

        """
        return 'motorcycle'
