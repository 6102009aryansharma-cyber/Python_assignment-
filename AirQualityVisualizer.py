import csv
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None
    print("matplotlib not installed. Install with:\n  python -m pip install matplotlib")


class AirQualityVisualizer:
    def __init__(self):
        self.data = []

    def load_data(self, file_name):
        try:
            with open(file_name, "r") as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
            print("✅ Data loaded successfully!")
        except FileNotFoundError:
            print("❌ Error: CSV file not found!")
        except Exception as e:
            print("❌ Unexpected Error:", e)

    def preview(self, count=5):
        if not self.data:
            print("⚠ Load data first!")
            return
        print(f"\nShowing first {count} records:")
        for row in self.data[:count]:
            print(row)

    def filter_by_city(self, city):
        result = [row for row in self.data if row["City"].lower() == city.lower()]
        if result:
            print(f"\n✅ Records for {city}:")
            for r in result[:5]:
                print(r)
        else:
            print("❌ City not found in data!")

    def show_summary(self):
        if not self.data:
            print("⚠ Load data first!")
            return
        
        try:
            aqis = [int(row["AQI"]) for row in self.data]
            print("\n📊 AQI Summary:")
            print(f"Max AQI: {max(aqis)}")
            print(f"Min AQI: {min(aqis)}")
            print(f"Avg AQI: {sum(aqis)/len(aqis):.2f}")
        except:
            print("❌ Error calculating statistics")

    def plot_city(self, city):
     def plot_city(self, city):
        if plt is None:
            print("❌ matplotlib not available. Install with:\n  python -m pip install matplotlib")
            return

        filtered = [row for row in self.data if row["City"].lower() == city.lower()]
        if not filtered:
            print("❌ City not found!")
            return
        
        days = [row["Date"] for row in filtered]
        values = [int(row["AQI"]) for row in filtered]

        plt.figure()
        plt.plot(days, values, marker='o')
        plt.title(f"AQI Trend for {city}")
        plt.xlabel("Date")
        plt.ylabel("AQI")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def menu():
    tool = AirQualityVisualizer()

    while True:
        print("\n=== Air Quality Data Visualizer ===")
        print("1. Load CSV File")
        print("2. Preview Data")
        print("3. Filter by City")
        print("4. Show AQI Summary")
        print("5. Plot AQI Trend")
        print("0. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            tool.load_data(input("Enter CSV file name: "))
        elif ch == "2":
            tool.preview()
        elif ch == "3":
            tool.filter_by_city(input("Enter city name: "))
        elif ch == "4":
            tool.show_summary()
        elif ch == "5":
            tool.plot_city(input("Enter city name: "))
        elif ch == "0":
            print("✅ Program closed.")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    menu()
