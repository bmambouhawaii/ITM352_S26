url = input ("Enter a full URL (including http:// or https://):   ")

cleaned_url= url.replace("https://", "")

print("Cleaned URL:", cleaned_url)

parts = cleaned_url.split(".")  

domain = parts[1]   
print("Domain:", domain)    

TLD = parts[2]  
#TLD_clean= TLD.strip("/")
TLD_clean = TLD.replace("/", "")
print("Top-Level Domain (TLD):", TLD_clean)       