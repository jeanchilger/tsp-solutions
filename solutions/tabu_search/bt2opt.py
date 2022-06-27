import functools
import numpy as np
import time
from ..solution import Solution

class BT2opt(Solution):
    def __init__(self):
        super(BT2opt, self).__init__()
    
    def solve(self, adjacency_matrix: np.ndarray, **kwargs: dict) -> np.ndarray:
        assert 'timelimit' in kwargs

        timelimit = kwargs.pop('timelimit')
        tenure = kwargs.pop('tenure')

        initial_path = np.arange(len(adjacency_matrix))

        np.random.shuffle(initial_path)

        return self._solve(
                initial_path, adjacency_matrix,
                time.time(), timelimit, tenure)
    
    def _solve(
            self, initial_path: np.ndarray,
            adjacency_matrix: np.ndarray,
            start_time:int, timelimit: int, tenure: int) -> np.ndarray:
        current_path = initial_path.copy()
        current_cost = self.evaluate(adjacency_matrix, initial_path)

        generated_path = initial_path.copy()
        generated_cost = None

        best_path = initial_path.copy()
        best_cost = current_cost      

        tabu_list = {}

        while True:
            if time.time() - start_time > timelimit:
                print('stopping due to time')
                break

            generated_path = self._get_valid_neighbor(
                    tabu_list, adjacency_matrix,
                    current_path, best_cost)

            generated_cost = self.evaluate(
                    adjacency_matrix, generated_path)

            # Stores the best solution to be returned in the end
            if generated_cost < best_cost:
                best_path = generated_path.copy()
                best_cost = generated_cost

            current_path = generated_path.copy()
            current_cost = generated_cost

            # Updates tabu list
            tabu_list[self._get_path_str(generated_path)] = 0

            for key in list(tabu_list.keys()):
                tabu_list[key] += 1

                if tabu_list[key] > tenure:
                    del tabu_list[key]

        return best_path

    def _get_valid_neighbor(
            self, tabu_list: dict, adjacency_matrix: np.ndarray,
            current_path: np.ndarray, best_cost: float) -> np.ndarray:
        """
        Returns the neighbor of current_path with the lowest cost.
        Considers only neighbors that don't appear in tabu_list or
        that are best than best_cost.

        Args:
            tabu_list (dict): List with already explored paths.
            adjacency_matrix (np.ndarray): Adjacency matrix.
            current_path (np.ndarray): Path being evaluated.
            best_cost (float): Best cost so far.

        Returns:
            np.ndarray: The generated path
        """

        current_cost = self.evaluate(adjacency_matrix, current_path)

        best_path = None

        neighbor_path = None
        neighbor_cost = None

        for i in range(1, len(adjacency_matrix) - 1):
            for j in range(i + 1, len(adjacency_matrix)):

                # Path generation
                neighbor_path = np.concatenate([
                    current_path[:i],
                    np.flip(current_path[i:j + 1]),
                    current_path[j + 1:],
                ])

                neighbor_cost = self.evaluate(
                        adjacency_matrix, neighbor_path)

                # Aspiration rule: ignore tabu list for best performing paths
                if neighbor_cost < best_cost:
                    best_path = neighbor_path.copy()
                    best_cost = neighbor_cost
                    continue

                if (neighbor_cost < current_cost and 
                        self._is_path_valid(neighbor_path, tabu_list)):
                    current_path = neighbor_path.copy()
                    current_cost = neighbor_cost

        return neighbor_path if best_path is None else best_path

    def _is_path_valid(self, path: np.ndarray, tabu_list: dict) -> bool:
        """
        Returns whether the path is valid to be visited or not, 
        based of the tabu list.

        Args:
            path (np.ndarray): Path to be checked.
            tabu_list (dict): Tabu list

        Returns:
            bool: True if the path is valid, False otherwise.
        """
        
        return self._get_path_str(path) not in tabu_list

    def _get_path_str(self, path: np.ndarray) -> str:
        """
        Returns a string with every element of path concatenated
        without any whitespace.

        Args:
            path (np.ndarray): Path to get the string representation.

        Returns:
            str: String representation of the path.
        """

        return functools.reduce(lambda x, y: f'{x}{y:04d}', path, '')

