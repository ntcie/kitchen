def isFloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False