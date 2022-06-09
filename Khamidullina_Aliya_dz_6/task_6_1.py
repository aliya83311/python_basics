import re

parsed_data = []

with open ("nginx_logs.txt", "r",encoding="utf-8") as f:
  for line in f:
    remote_addr = re.search("^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", line)
    request_type = re.search("GET", line)
    requested_resource = re.search(r"/downloads/product_\d", line)
    parsed_data.append((remote_addr.group(), request_type.group(), requested_resource.group()))

print(parsed_data)
