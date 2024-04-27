def insertion_sort(array):
    
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1

        while j >= 0 and current < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        array[j+1] = current

    return array


print(insertion_sort([5, 2, 4, 1, 6, 3]))