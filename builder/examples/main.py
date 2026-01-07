from adapter_example.adaptee import Adaptee
from adapter_example.adapter import Adapter


def main() -> None:
    
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    print("Client: I can work with objects that follow the Target interface:")
    print(adapter.request())


if __name__ == "__main__":
    main()
