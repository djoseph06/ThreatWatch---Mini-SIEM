from datetime import datetime
failed_attempts = {}

with open("login_logs.txt", "r") as file:
    for line in file:
        timestamp_text, username, ip, status = line.strip().split(',')

        timestamp = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")
        print(timestamp)

        if status == "failed":
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

            failed_attempts[ip].append(timestamp)




for ip, attempts in failed_attempts.items():
    if attempts >= 5:
        print("SECURITY ALERT")
        print("Possible brute-force attack")
        print(f"IP: {ip}")
        print(f"Failed attempts: {attempts}")
        print("Risk: HIGH")
    elif attempts >= 3:
        print("Risk: MEDIUM")






