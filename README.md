📦 Shipping Manager
  A Python-based console application for managing shipping operations using dictionaries, sets, and lists. This project provides a menu-driven interface for
  adding, updating, removing, and filtering shipments across multiple regions.

📘 Overview
  The Shipping Manager is a lightweight logistics management tool designed to demonstrate:
  Efficient use of Python data structures
  Modular function design
  Interactive console menus
  Region-based shipment categorization
  Dynamic tracking of cities and shipment statuses
  It is ideal for beginners learning Python or anyone exploring data structure manipulation in a practical scenario.

🧱 Features
  ✔️ Shipment Management
    Add new shipments
    Update shipment status
    Remove shipments safely (with region/city cleanup)

  ✔️ Filtering & Display
    Filter by ID, status, destination, or region
    Display shipment keys, values, or full items
    Show all cities involved
    Region summary (count of unique cities per region)

  ✔️ Interactive Menu
    A loop-based menu system allows users to perform all operations through simple numeric choices.

🗂️ Project Structure
  Code
  shipping_manager.py
  Main Components
  Global Data Structures
  shipment (dict)
  cities (set)
  Region sets: north_region, south_region, east_region, west_region, middle_region
  Core Functions
  add_shipment()
  update_shipment_status()
  remove_shipment()
  Filtering functions (shipment_by_id, shipment_by_status, etc.)
  Display functions (show_shipments_keys, show_region_summary, etc.)
  show_menus() — main interactive loop
  Initial Test Data  
  Ten shipments are preloaded for demonstration and testing.

🚀 Getting Started
  Prerequisites
  Python 3.8+
  Run the Program
  bash
  python shipping_manager.py
  The interactive menu will appear, allowing you to manage shipments.

🧪 Sample Output
  Region Summary Example
  Code
  Region Summary:
   - North Region: 1 cities
   - South Region: 1 cities
   - East Region: 2 cities
   - West Region: 2 cities
   - Middle Region: 2 cities
  Shipment Example
  Code
  Shipment ID: SHP1001
   - Destination: MIAMI
   - Region: NORTH
   - Status: IN TRANSIT

🛠️ Technologies Used
  Python 3
  Dictionaries
  Sets
  Lists
  Console I/O

📌 Roadmap / Future Enhancements
  Add JSON or database persistence
  Implement logging instead of print statements
  Add unit tests (pytest)
  Create a GUI version (Tkinter or PyQt)
  Add colorized terminal output
  Add import/export of shipment data

🤝 Contributing
  Contributions are welcome!
  If you’d like to contribute:
  Fork the repository
  Create a new branch
  bash
  git checkout -b feature-name
  Commit your changes
  bash
  git commit -m "Add new feature"
  Push the branch
  bash
  git push origin feature-name
  Open a Pull Request
  Please ensure your code follows Python best practices and includes clear documentation.

🐛 Reporting Issues
  If you encounter bugs or have feature requests, open an issue in the GitHub repository with:
  A clear description
  Steps to reproduce
  Expected vs actual behavior

📄 License
  This project is licensed under the MIT License.
  You are free to:
  Use
  Modify
  Distribute
  Sell
  …as long as the original license notice is included.

👤 Author
  Lenin Torrealba  
  Certified AI Engineer • Property Senior Maintenance Technician • Prompt Engineer
  Bilingual (EN/ES) • Technical Project Manager
