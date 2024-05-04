# PassiveComp
This script aims to make the life as an electrical engineer faster by doing tedious calculations and E-Series matching.

# Functionality
At the moment, this tool can match a given resistance to a given E-Series.
Possible resistor combinations are single, series and parallel.
It selects for all three combinations the best match and calculates a match miss to give the user a better understanding what the combination has achieved.

# Functionality
The script uses for now brute force to calculate all possible combinations in the E-Series. Then it calculates the offset for all combinations and selects the smallest offset as the right solution.

# Disclaimer
This repository is currently under development and in no means ready to be fully trusted. Use at OWN RISK.

# Install
To be able to use this script, python3 needs to be installed

```
git clone https://www.github.com/NXZAS8CA/PassiveComp
cd PassiveComp
python3 main.py
```

# Contribution
Fell free to open an PR, for major changes please open an issue first so we can discuss the changes.
