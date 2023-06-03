from abc import abstractmethod, ABC


# O(n+k)
# we have 2 types of sorting algorithms
# 1. they are based on comparison so the time complexity is not lower than O(nlogn)
# 2. they are based on some restrictions like the numbers

class SortAlgorithm(ABC):
    """base class for CountingSort algorithm class or any new algorithm

    """

    def __init__(self, data: list) -> None:
        """Initialize algorithm with a list of numbers
        :param data: the initial data for doing sort
        :type data: list
        """
        self.data = data

    @abstractmethod
    def sort(self) -> list:
        """ Sort the list, then return the sorted list

        :return: list of sorted numbers
        :rtype: list
        """
        pass


class CountingSort(SortAlgorithm):
    """CounteringSort will sort your algoritm by O(n+k)


        >>> sort_algorithm = CountingSort([1,0,0,0,5])
        >>> sort_algorithm.sort()
        [0, 0, 0, 1, 5]
    """

    def __init__(self, data: list) -> None:
        """
        :param list data: a list to be sorted
        :type data: list
        """
        super().__init__(data)
        self.index_array = [0] * 10
        self.output = [0] * len(self.data)

    def sort(self) -> list:
        """Sort the array

        :return: return the sorted array
        :rtype: list
        """
        # O(n)
        for number in self.data:
            self.index_array[number] += 1

        # O(k)
        for index in range(len(self.index_array) - 1):
            self.index_array[index + 1] += self.index_array[index]

        # O(n)
        for number in self.data:
            self.output[self.index_array[number] - 1] = number
            self.index_array[number] -= 1

        # O(n) + O(n) + O(k) = O(2*n) + O(k) = O(n) + o(k)

        return self.output

    def __str__(self) -> str:
        """get a string of sorted result

        :return: a string representation of sorted list
        :rtype: str
        """
        return f"{self.output}"

    def __repr__(self) -> str:
        """Create a programmer representation of the object
        :return: a string of state of the object
        :rtype: str
        """
        return f'''CountingSort(
                    {self.data},
                    {self.index_array},
                    {self.output},
               )'''


def main():
    # test counting algorithm with a test data
    counting_sort_algorithm = CountingSort([2, 3, 1, 1, 7, 5, 4])
    # call sort
    counting_sort_algorithm.sort()
    print(counting_sort_algorithm)


if __name__ == '__main__':
    main()
