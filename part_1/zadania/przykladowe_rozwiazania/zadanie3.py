import operator
from collections import defaultdict

result = {}

METHODS = [
    "GET",
    "HEAD",
    "POST",
    "PUT",
    "DELETE",
    "CONNECT",
    "OPTIONS",
    "TRACE",
    "PATCH"
]


def get_domain_or_ip(line):
    return line.split(" ")[0]


def find_method(line):
    for method_name in METHODS:
        if method_name in line:
            return method_name


with open("access_log_Jul95", "r") as f:
    for i, line in enumerate(f):
        domain_or_ip = get_domain_or_ip(line)
        parts = domain_or_ip.split(".")

        method = find_method(line)

        if domain_or_ip not in result:
            result[domain_or_ip] = defaultdict(int)

        result[domain_or_ip][method] += 1

top_10 = [ (key, sum(value.values())) for key, value in result.iteritems() ]
print(sorted(top_10, key=operator.itemgetter(1), reverse=True)[:10])
