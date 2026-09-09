import sys
import json
from client import LloydSwarmCoverage

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "optimize_coverage":
        cov = LloydSwarmCoverage(params.get("bounds", (0, 100, 0, 100)))
        for r in params.get("robots", []):
            cov.add_robot(r.get("id"), r.get("pos"))
        return {"centroids": cov.iterate_lloyd(params.get("res", 10))}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
