from source import vehicle


class Car(vehicle):
    """A car for sale."""

    base_sale_price = 8000
    wheels = 4

    @staticmethod
    def vehicle_type():
        """
        Returns: string representing the type of vehicle this is.

        """
        return 'car'
