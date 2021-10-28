import time
from currency import getEtherium




def main():
    print("Ethereum analysis.....\n")
    first_state = True

    while True:
        getEtherium(first_state)
        first_state = False
        time_to_wait = 5
        print(f'Waiting {time_to_wait} minutes...')
        time.sleep(time_to_wait * 60)


if __name__ == '__main__':
    main()