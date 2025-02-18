# smart_device.py

class SmartDevice:
    # Class attribute to count the total number of devices created.
    # Note: This counter increases cumulatively, so tests should run in isolation
    # (or the module should be re-imported) so that earlier tests don't affect the count.
    device_count = 0

    def __init__(self, device_name, model_number, is_online=False):
        """
        Initializes a new SmartDevice instance.
        
        Parameters:
            device_name (str): The name of the device.
            model_number (str): The model number of the device.
            is_online (bool): The online status of the device (default is False).
        """
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        # The status dictionary will hold various device features (like battery, temperature, etc.)
        self.status = {}
        # Increase the class-level device count on each new instance.
        SmartDevice.device_count += 1

    def update_status(self, attribute, value):
        """
        Adds or updates a status attribute in the device's status dictionary.
        
        Parameters:
            attribute (str): The status attribute (e.g., 'battery', 'temperature').
            value: The value for the attribute.
        """
        self.status[attribute] = value

    def get_status(self, attribute):
        """
        Retrieves the value of a specific status attribute.
        
        Parameters:
            attribute (str): The status attribute to retrieve.
            
        Returns:
            The value of the attribute if it exists, otherwise 'Attribute not found'.
        """
        return self.status.get(attribute, 'Attribute not found')

    def toggle_online(self):
        """
        Toggles the online status of the device.
        
        If the device is online, it will become offline and vice versa.
        """
        self.is_online = not self.is_online

    def reset(self):
        """
        Resets the device's status by clearing the status dictionary.
        """
        self.status.clear()

    def __call__(self):
        """
        Makes the instance callable.
        
        When called (e.g., device()), returns a formatted string containing
        the device name and model number.
        
        Returns:
            A string formatted as "<device_name> (Model: <model_number>)".
        """
        return f"{self.device_name} (Model: {self.model_number})"

    def device_info(self):
        """
        Returns a dictionary representing the current state of the device.
        
        This method is callable and can be replaced at run-time if needed.
        
        Returns:
            dict: Contains the device's name, model number, online status, and a copy of its status.
        """
        return {
            "device_name": self.device_name,
            "model_number": self.model_number,
            "is_online": self.is_online,
            "status": self.status.copy()  # Return a copy to avoid unintended external modifications.
        }
