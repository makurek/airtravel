
class Flight:
    def __init__(self, number, aircraft):
        """
        Class invariants - general sanity checks
        https://stackoverflow.com/questions/112064/what-is-an-invariant
        Flight number should always be XY1234
        """
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{n}'".format(n=number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{n}'".format(n=number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{n}'".format(n=number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number



class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
    """ 
    What is the proper way of implementing getters/setters in python?
    Python property feature
    """
    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])