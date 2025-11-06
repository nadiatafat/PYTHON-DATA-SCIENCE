from datetime import datetime

epoch = datetime(1970, 1, 1, 0, 0, 0, 0)
now = datetime.now()
delta = now - epoch
seconds = delta.total_seconds()

print("Seconds since January 1, 1970:")
print(f"{seconds:,.2f}", "or", f"{seconds:.2e} in scientific notation")

now = datetime.now()
print(now.strftime("%b %d %Y"))
