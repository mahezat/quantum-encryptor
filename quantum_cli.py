import os
import time
import random
import sys
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# No need for API key since we're using Python's random module

# ASCII art banner
BANNER = f"""
{Fore.GREEN}
 ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗██╗   ██╗███╗   ███╗      ██████╗ ████████╗██████╗ 
██╔═══██╗██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██║   ██║████╗ ████║      ██╔══██╗╚══██╔══╝██╔══██╗
██║   ██║██████╔╝███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║█████╗██║  ██║   ██║   ██████╔╝
██║▄▄ ██║██╔══██╗██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║╚════╝██║  ██║   ██║   ██╔═══╝ 
╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║      ██████╔╝   ██║   ██║     
 ╚══▀▀═╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝      ╚═════╝    ╚═╝   ╚═╝     
                                                                                                 
{Fore.CYAN}[ QUANTUM ENCRYPTION MODULE V1.0 ]{Style.RESET_ALL}
"""

def fake_typing(text, speed=0.03):
    """Simulate typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed * random.random())
    print()

def hacker_print(text, color=Fore.GREEN, speed=0.01):
    """Print text with a hacker-style effect"""
    print(color, end="")
    fake_typing(text, speed)
    print(Style.RESET_ALL, end="")

def progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    """Display a progress bar"""
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{Fore.GREEN}{bar}{Style.RESET_ALL}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total: 
        print()

def matrix_effect(seconds=1.5):
    """Create a brief matrix-like effect"""
    chars = "10"
    for _ in range(int(seconds * 10)):
        line = ''.join(random.choice(chars) for _ in range(70))
        colored_line = ""
        for char in line:
            if random.random() > 0.8:
                colored_line += Fore.WHITE + char
            else:
                colored_line += Fore.GREEN + char
        print(colored_line)
        time.sleep(0.05)
    print("\033[H\033[J", end="")  # Clear screen

def encrypt_otp(key, plaintext):
    """Encrypt using XOR (One-Time Pad)"""
    hacker_print(f"\n[*] DEBUG: ENCRYPTION PROCESS", Fore.YELLOW)
    hacker_print(f"[+] Plaintext length: {len(plaintext)} bytes", Fore.CYAN)
    hacker_print(f"[+] Key length: {len(key)} bytes", Fore.CYAN)
    
    # Simulate encryption process
    print()
    for i in range(10):
        progress_bar(i+1, 10, prefix=f'{Fore.YELLOW}[*] Applying quantum key...{Style.RESET_ALL}', length=30)
        time.sleep(0.1)
    print()
    
    return bytes([x ^ y for x, y in zip(key, plaintext)])

def decrypt_otp(key, ciphertext):
    """Decrypt using XOR (One-Time Pad)"""
    hacker_print(f"\n[*] DEBUG: DECRYPTION PROCESS", Fore.YELLOW)
    hacker_print(f"[+] Ciphertext length: {len(ciphertext)} bytes", Fore.CYAN)
    hacker_print(f"[+] Key length: {len(key)} bytes", Fore.CYAN)
    
    # Simulate decryption process
    print()
    for i in range(10):
        progress_bar(i+1, 10, prefix=f'{Fore.YELLOW}[*] Reversing quantum encryption...{Style.RESET_ALL}', length=30)
        time.sleep(0.1)
    print()
    
    return bytes([x ^ y for x, y in zip(key, ciphertext)])

def display_hex(data, prefix="", chunk_size=2):
    """Display data in a cool hex format"""
    hex_str = data.hex()
    chunks = [hex_str[i:i+chunk_size] for i in range(0, len(hex_str), chunk_size)]
    
    result = ""
    for i, chunk in enumerate(chunks):
        if i % 16 == 0:
            result += f"\n{Fore.YELLOW}{prefix}{Style.RESET_ALL} {Fore.GREEN}{i:04x}{Style.RESET_ALL}  "
        if i % 8 == 0 and i % 16 != 0:
            result += " "
        result += f"{Fore.CYAN}{chunk}{Style.RESET_ALL} "
    
    print(result)

def display_binary_animation(data, duration=2):
    """Display a cool binary representation animation"""
    start_time = time.time()
    while time.time() - start_time < duration:
        line = ""
        for b in data[:16]:  # Take just first 16 bytes
            if random.random() > 0.7:  # Sometimes show actual bits
                bits = format(b, '08b')
                line += f"{Fore.WHITE}{bits}{Style.RESET_ALL} "
            else:  # Sometimes show random bits
                fake_bits = ''.join(random.choice('01') for _ in range(8))
                line += f"{Fore.GREEN}{fake_bits}{Style.RESET_ALL} "
        print(f"\r{line}", end="")
        time.sleep(0.1)
    print()

def main():
    """Main program function"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    
    hacker_print("[*] Initializing quantum random number generator...", Fore.YELLOW)
    time.sleep(1)
    hacker_print("[+] Connected to quantum source", Fore.GREEN)
    
    print()
    hacker_print("[?] Enter your message:", Fore.CYAN)
    message = input(f"{Fore.WHITE}> {Style.RESET_ALL}").encode()
    
    # Generate quantum random numbers
    hacker_print("\n[*] Simulating quantum entropy...", Fore.YELLOW)
    
    for i in range(10):
        progress_bar(i+1, 10, prefix=f'{Fore.YELLOW}[*] Collecting quantum randomness...{Style.RESET_ALL}', length=30)
        time.sleep(0.2)
    
    key_length = len(message)
    hacker_print(f"\n[+] Generating {key_length} quantum random bytes...", Fore.GREEN)
    
    random_integers = [random.randint(0, 255) for _ in range(key_length)]
    encryption_key = bytes(random_integers)
    
    hacker_print("[+] Quantum key generated successfully", Fore.GREEN)
    hacker_print("\n[*] Quantum key signature:", Fore.YELLOW)
    display_binary_animation(encryption_key)
    display_hex(encryption_key, "KEY ")
    
    # Encrypt
    hacker_print("\n[*] Initiating quantum encryption algorithm...", Fore.YELLOW)
    time.sleep(0.5)
    encrypted_message = encrypt_otp(encryption_key, message)
    
    hacker_print("\n[+] Message encrypted with quantum one-time pad", Fore.GREEN)
    hacker_print("[*] Encrypted message hex dump:", Fore.YELLOW)
    display_hex(encrypted_message, "ENC ")
    
    # Short matrix effect for visual coolness
    hacker_print("\n[*] Performing security verification...", Fore.YELLOW)
    matrix_effect(1.0)
    
    # Decrypt
    hacker_print("\n[*] Initiating quantum decryption protocol...", Fore.YELLOW)
    time.sleep(0.5)
    decrypted_message = decrypt_otp(encryption_key, encrypted_message)
    
    hacker_print("\n[+] Message successfully decrypted", Fore.GREEN)
    hacker_print("[*] Decrypted message hex dump:", Fore.YELLOW)
    display_hex(decrypted_message, "DEC ")
    
    print(f"\n{Fore.GREEN}[+] Decrypted message: {Fore.CYAN}{decrypted_message.decode()}{Style.RESET_ALL}")
    
    hacker_print("\n[*] Quantum random number sequence:", Fore.YELLOW)
    
    # Display random numbers in a more hacker-like way
    for i in range(0, len(random_integers), 8):
        chunk = random_integers[i:i+8]
        formatted = ' '.join([f"{Fore.CYAN}{num:03d}{Style.RESET_ALL}" for num in chunk])
        print(f"{Fore.GREEN}[{i:02d}]{Style.RESET_ALL} {formatted}")
    
    # Final summary display
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[***] OPERATION SUMMARY [***]{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}[+] ORIGINAL MESSAGE:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{message.decode()}{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}[+] ENCRYPTION KEY (HEX):{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{encryption_key.hex()}{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}[+] ENCRYPTED PAYLOAD (HEX):{Style.RESET_ALL}")
    print(f"{Fore.RED}{encrypted_message.hex()}{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}[+] DECRYPTED MESSAGE:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{decrypted_message.decode()}{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}[+] RANDOM NUMBER SEQUENCE:{Style.RESET_ALL}")
    for i in range(0, len(random_integers), 8):
        chunk = random_integers[i:i+8]
        formatted = ' '.join([f"{Fore.CYAN}{num:03d}{Style.RESET_ALL}" for num in chunk])
        print(f"{Fore.GREEN}[{i:02d}]{Style.RESET_ALL} {formatted}")
    
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] Quantum encryption operation completed successfully{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Connection to quantum source terminated{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Operation aborted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
        sys.exit(1)