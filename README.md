In this project Im creating Quantum Random Number Generator and were writing code to prove that the code is truly original.
3 blocks:
1) NIST Frequency block test
2) Bit-by-bit frequency test
3) Test for sequences of identical bits

   The First block converts 0 to -1, 1 to +1, and adds up all the resulting numbers.
   This allows you to calculate the balance relative to zeros and ones.
   
   Frequency-based block analysis divides a sequence into a set of blocks, in each of which the proportion of 1s is calculated.
   This defines and identifies segmental unevenness.

   The third block counts the number of value changes for each type.
   That is, the number of times 0 changed to 1 and 1 changed to 0.
   Next, their ratio is calculated, which, in the optimal case, should be approximately 0.5.

