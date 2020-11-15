#! python3
import handlers

def main():
    # add txn
    handlers.new_transaction("Betto", "DNCCCCCCCC")

    print(handlers.get_chain())


if __name__== "__main__":
    main()