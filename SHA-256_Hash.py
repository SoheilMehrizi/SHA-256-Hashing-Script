import hashlib
import time

def proof_of_work(suffix_target='1111'):
    """
    Continuously hashes incremented data until the SHA-256 hash ends with a target suffix.
    
    Parameters:
    - suffix_target (str): The required ending string for the hexadecimal hash (e.g., '1111')
    
    Returns:
    - Tuple[str, str, int, float]: (final message, resulting hash, iterations, elapsed_time)
    """
    i = 0
    start_time = time.time()

    while True:
        i += 1
        data = f"My name is Soheil and 9812101100 is my student number. {i}"
        hash_hex = hashlib.sha256(data.encode('utf-8')).hexdigest()

        if hash_hex.endswith(suffix_target):
            elapsed_time = time.time() - start_time
            return data, hash_hex, i, elapsed_time

        if i % 100000 == 0:
            print(f"Checked {i:,} hashes...")

if __name__ == "__main__":
    target_suffix = '1111'
    print(f"⛏️  Starting proof-of-work to find SHA-256 hash ending with '{target_suffix}'...\n")

    message, final_hash, iterations, duration = proof_of_work(target_suffix)

    print("\n✅ Success!")
    print(f"🔢 Attempts: {iterations:,}")
    print(f"⏱️  Time Taken: {duration:.2f} seconds")
    print(f"📩 Message: {message}")
    print(f"🔐 Hash: {final_hash}")
