"""
Number of Customers Who Could Not Get a Computer

PROBLEM DESCRIPTION:
A computer shop has 'n' computers. Customers come and go, represented by a sequence
where each customer appears exactly twice (once when arriving, once when leaving).
If a customer arrives and no computer is available, they are ignored (cannot get service).
Find how many customers were ignored.

Example: computers = 3, seq = "GACCBDDBAGEE"
- G arrives, gets computer #1
- A arrives, gets computer #2
- C arrives, gets computer #3
- C leaves, frees computer #3
- B arrives, gets computer #3
- D arrives, all occupied, IGNORED (count = 1)
- D tries again, IGNORED again (count = 2)
- B leaves, frees computer
- A leaves, frees computer
- G leaves, frees computer
- E arrives, gets computer
- E leaves
Output: 2 (customer D was ignored twice)

Wait, that's wrong interpretation. Let me re-read...

Actually: Each letter represents a unique customer. They appear exactly twice.
First appearance = arrival, second appearance = leaving.

Corrected Example: computers = 2, seq = "ABBAJJKZKZ"
- A arrives (1st time), occupies computer (occupied = 1)
- B arrives (1st time), occupies computer (occupied = 2)
- B leaves (2nd time), frees computer (occupied = 1)
- A leaves (2nd time), frees computer (occupied = 0)
- J arrives (1st time), occupies computer (occupied = 1)
- J leaves (2nd time), frees computer (occupied = 0)
- K arrives (1st time), occupies computer (occupied = 1)
- Z arrives (1st time), occupies computer (occupied = 2)
- K leaves (2nd time), frees computer (occupied = 1)
- Z leaves (2nd time), frees computer (occupied = 0)
Output: 0 (no one ignored)

Another Example: computers = 1, seq = "ABCBCA"
- A arrives, occupies (occupied = 1)
- B arrives, no space, IGNORED (ignored = 1)
- C arrives, no space, IGNORED (ignored = 2)
- B appears again, but was ignored first time, so ignored again
- C appears again, but was ignored first time, so ignored again
- A leaves, frees (occupied = 0)
Output: 2 (B and C were ignored)

WHY THIS APPROACH (State Machine with Hash Map):
We use a STATE MACHINE tracked in a hash map because:
1. Each customer has 3 possible states:
   - 0 (or not in map): Never seen before
   - 1: Arrived but didn't get computer (ignored)
   - 2: Arrived and got computer (occupying)
2. Hash map provides O(1) lookup to check customer state
3. We need to track which customers are occupying computers (occupied counter)
4. When customer appears 2nd time, their state tells us what to do:
   - State 2: They were occupying, now leaving -> free computer
   - State 1: They were ignored first time, now leaving -> no action
   - State 0: Never seen -> first arrival
5. This single-pass solution is optimal O(n)

ALGORITHM:
Step 1: Initialize Tracking Variables
   - seen = defaultdict(int) to track customer states
   - occupied = number of computers currently in use (starts at 0)
   - ignored = number of customers who couldn't get service (starts at 0)

Step 2: Process Each Customer in Sequence
   For each customer C in the sequence:

   Case A: First Appearance (seen[C] == 0)
     - Mark as arrived: seen[C] = 1
     - If computers available (occupied < total):
       - Give them a computer: occupied += 1
       - Mark as occupying: seen[C] = 2
     - Else (no computers available):
       - Cannot serve them: ignored += 1
       - State remains 1 (ignored)

   Case B: Second Appearance (seen[C] == 1 or 2)
     - If seen[C] == 2 (they were occupying):
       - They're leaving: occupied -= 1
     - Reset their state: seen[C] = 0

Step 3: Return Result
   - Return ignored count

EDGE CASES:
1. More computers than customers -> ignored = 0
2. Only 1 computer, many customers -> many ignored
3. All customers can be served -> ignored = 0
4. Customer sequence not valid (appears 1 or 3 times) -> undefined behavior
5. Empty sequence -> ignored = 0

TIME COMPLEXITY: O(n)
- n = length of sequence
- Process each character once: O(n)
- Hash map operations (lookup, update): O(1)
- Overall: O(n)

SPACE COMPLEXITY: O(k)
- k = number of unique customers
- Hash map stores at most k customers
- In worst case, k = n/2 (each customer appears twice)
- Overall: O(k) = O(n)

EXAMPLE WALKTHROUGH:
Input: computers = 2, seq = "GACCBGB"

Process:
1. 'G' (1st): seen[G]=0 -> arrive, occupy -> occupied=1, seen[G]=2
2. 'A' (1st): seen[A]=0 -> arrive, occupy -> occupied=2, seen[A]=2
3. 'C' (1st): seen[C]=0 -> arrive, no space -> ignored=1, seen[C]=1
4. 'C' (2nd): seen[C]=1 -> was ignored, leave -> seen[C]=0
5. 'B' (1st): seen[B]=0 -> arrive, no space -> ignored=2, seen[B]=1
6. 'G' (2nd): seen[G]=2 -> was occupying, leave -> occupied=1, seen[G]=0
7. 'B' (2nd): seen[B]=1 -> was ignored, leave -> seen[B]=0

Output: ignored = 2 (C and B were ignored)
"""

# Function to find Number of customers who could not get a computer


from collections import defaultdict

def runCustomerSimulation(computers, seq):
    """
    Simulate computer shop and count how many customers couldn't get service.

    Args:
        computers: Total number of computers available
        seq: String where each character represents a customer
             (appears exactly twice: arrival then departure)

    Returns:
        Number of customers who were ignored (couldn't get a computer)
    """
    # Step 1: Initialize tracking structures
    seen = defaultdict(int)  # Track customer state: 0=new, 1=ignored, 2=occupying
    ignored = 0  # Count of customers who couldn't get service
    occupied = 0  # Number of computers currently in use

    # Step 2: Process each customer in the sequence
    for customer in seq:
        # Case A: First time seeing this customer (arrival)
        # defaultdict returns 0 for keys not yet in dictionary
        if seen[customer] == 0:
            seen[customer] = 1  # Mark as arrived

            # Check if computers are available
            if occupied < computers:
                # Computer available: give them service
                occupied += 1  # One more computer is now occupied
                seen[customer] = 2  # Update state: they're occupying a computer
            else:
                # No computer available: must ignore this customer
                ignored += 1
                # State remains 1 (arrived but ignored)

        # Case B: Second time seeing this customer (departure)
        else:
            # Check if they were actually using a computer
            if seen[customer] == 2:  # They were occupying a computer
                occupied -= 1  # Free up the computer they were using

            # Reset their state (they've left)
            seen[customer] = 0

    return ignored

print(runCustomerSimulation(3, "GACCBDDBAGEE"))