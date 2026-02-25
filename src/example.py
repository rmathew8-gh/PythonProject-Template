from lib.compute import AddRequest, add

if __name__ == "__main__":
    req = AddRequest(a=2, b=3)
    print(f"2 + 3 = {add(req)}")
