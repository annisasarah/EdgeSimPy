""" Contains a user privacy model definition."""


class UserLocationPrivacyModel:
    """
    Lorem ipsum
    """

    @classmethod
    def get_power_consumption(cls, device: object) -> float:
        """Gets the power consumption of a server.

        Args:
            device (object): Server whose power consumption will be computed.

        Returns:
            power_consumption (float): Server's power consumption.
        """
        if device.active:
            static_power = (
                device.power_model_parameters["static_power_percentage"] * device.power_model_parameters["max_power_consumption"]
            )
            constant = (device.power_model_parameters["max_power_consumption"] - static_power) / 100

            demand = device.cpu_demand
            capacity = device.cpu
            utilization = demand / capacity

            power_consumption = static_power + constant * utilization * 100
        else:
            power_consumption = 0

        return power_consumption