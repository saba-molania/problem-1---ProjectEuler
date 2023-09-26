
from bubble_sort import bubble_sort
def test_bubble_sort():
    _list = [21, 87, 76, 65, 54, 43, 32, 21, 90, 89, 102, 45, 13]
    assert bubble_sort(_list) == sorted(_list) , "list is not sorted"

if __name__ == "__main__":
    test_bubble_sort()
    print("--- Everything passed ---")