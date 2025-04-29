🔐 Proof-of-Work SHA-256 Hashing Script
This Python script demonstrates a Proof-of-Work (PoW) algorithm using the SHA-256 hash function.
It incrementally modifies an input message until it produces a hash with a specified suffix (e.g., '1111'). This simulates the kind of computational difficulty used in blockchain mining and cryptographic verification.

🧠 Features
Modular and readable structure

Uses SHA-256 from Python’s hashlib

Configurable difficulty by changing the target suffix

Shows real-time progress every 100,000 attempts

Displays total time taken and attempts made

⚙️ How It Works
Starts with a base string:

arduino
Copy code
"My name is Soheil and 9812101100 is my student number. {i}"
Converts the string to a SHA-256 hash.

Checks if the hash ends with the target suffix (default '1111').

Repeats until the condition is met.

Prints the message, hash, total attempts, and duration.

🚀 How to Run
Ensure Python 3 is installed.

Save the script as proof_of_work.py.

Run the script:

bash
Copy code
python proof_of_work.py
🔧 Configuration
You can change the difficulty by modifying the target_suffix variable inside the script:

python
Copy code
target_suffix = '0000'  # More zeroes = higher difficulty
🧪 Example Output
python
Copy code
⛏️  Starting proof-of-work to find SHA-256 hash ending with '1111'...

Checked 100,000 hashes...
Checked 200,000 hashes...

✅ Success!
🔢 Attempts: 472,000
⏱️  Time Taken: 6.82 seconds
📩 Message: My name is Soheil and 9812101100 is my student number. 472000
🔐 Hash: f90ab2...c7e1111
📦 Requirements
Python 3.x

No third-party libraries required

👨‍💻 Author
Soheil Mehrizi
📧 mehrizisoheil@gmail.com

