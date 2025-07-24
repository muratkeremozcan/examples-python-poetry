from typing import List, Dict, Tuple, Set

roster: Dict[str, int] = {
  "Chuck": 37,
  "Devin": 2,
  "Steven": 4
}

agents: List[str] = [
	f"Agent {agent}, {missions} missions" \
  for agent, missions in roster.items()
]

print(agents)