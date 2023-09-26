
from bubble_sort import bubble_sort
def test_bubble_sort():
    assert bubble_sort([21, 87, 76, 65, 54, 43, 32, 21, 90, 89, 102, 45, 13]) == [13, 21, 21, 32, 43, 45, 54, 65, 76, 87, 89, 90, 102] , "Sould be [13, 21, 21, 32, 43, 45, 54, 65, 76, 87, 89, 90, 102]"

if __name__ == "__main__":
    test_bubble_sort()
    print("--- Everything passed ---")