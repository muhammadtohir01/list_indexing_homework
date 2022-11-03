def main(list1):
    """
    A list of several elements is given. Return the last item.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    s=list1[len(list1)-1:len(list1)]
    return s
print(main([1,2,3,4,5]))