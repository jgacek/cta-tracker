import weather
import bus_tracker
import train_tracker

def main():
    weather.get_weather("Chicago")
    train_tracker.get_train_arrivals("40670")
    bus_tracker.get_bus_arrivals(route="56", stop_id="18358")

if __name__ == "__main__":
    main()
