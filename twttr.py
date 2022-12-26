def main():
    string = input('Input: ')
    print(shorten(string))

def shorten(string):
    shortened = []
    for s in string:
        if s not in ['a', 'e', 'i' ,'o' ,'u' , 'A', 'E', 'I', 'O', 'U']:
            shortened.insert(len(shortened), s)
    return(''.join(shortened))

if __name__ == "__main__":
    main()