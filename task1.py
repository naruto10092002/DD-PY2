class Forest:
    """This model describes a forest."""
    def __init__(self, location: str, area: float):
        """
        Initializes an instance.
        :param location: String with description of forest location
        :param area: The area occupied by forest in square kilometers
        """
        self.location = location
        self.area = area

    def __str__(self) -> str:
        return f"{self.__class__.__name__} located in {self.location} and occupying area of {self.area} square kilometers."

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(location={self.location!r}, area={self.area})'

    def cut_down(self, area_decrement: float):
        """
        Decreases the area occupied by forest by area_decrement
        :param area_decrement: Should be float-typed
        :return: No return
        """
        self.area -= area_decrement

    def restore(self, area_increment: float):
        """
        Increases the area occupied by forest by area_increment
        :param area_increment: Should be float-typed
        :return: No return
        """
        self.area += area_increment


class Taiga(Forest):
    def __init__(self, location: str, area: float, species: tuple):
        """
        Initializes an instance
        Overloaded to add 'species' attribute
        :param location: String with description of forest location
        :param area: The area occupied by forest in square kilometers
        :param species: The tuple of tree species in the forest. The species should be string-typed
        """
        super().__init__(location, area)
        self.species = species

    def __repr__(self):
        """
        Needs to be overloaded because of new attribute "species"
        :return: String with python representation of the object
        """
        return f'{self.__class__.__name__}(location={self.location!r}, area={self.area}, species={self.species})'

    def restore(self, area_increment: float, species_restoration: tuple):
        """
        Needs to be overloaded because of specification of species used in restoration
        :param area_increment:
        :param species_restoration:
        :return: No return
        """
        super().restore(area_increment)
        self.species += species_restoration
        self.species = set(self.species)
        self.species = tuple(self.species)


if __name__ == "__main__":
    # Write your solution here
    pass
