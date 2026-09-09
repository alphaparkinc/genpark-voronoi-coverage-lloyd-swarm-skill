from client import LloydSwarmCoverage

def main():
    print("=== Testing Lloyd's Swarm Coverage ===")
    cov = LloydSwarmCoverage(region_bounds=(0, 50, 0, 50))
    cov.add_robot("agent_1", [5, 5])
    cov.add_robot("agent_2", [45, 45])

    pos = cov.iterate_lloyd(grid_res=5)
    print("Agent positions after Lloyd centroid iteration:", pos)
    assert pos['agent_1'][0] < pos['agent_2'][0]

    print("Lloyd Swarm Coverage verified successfully!")

if __name__ == '__main__':
    main()
