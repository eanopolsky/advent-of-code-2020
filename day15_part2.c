#include <stdio.h>
#include <stdlib.h>

/*  A just-for-fun rewrite of day 15 part 2 in C. On my machine, the python
 *  solution takes ~8000ms, while this solution takes ~600ms with default gcc
 *  options and ~430ms with -O3.
 */

int main() {
  int numberList[] = {1,0,15,2,10,13}; // problem input
  int *numberHistory;
  int lastSaidNumberIndex = 5;
  int lastSaidNumber = numberList[5];
  
  numberHistory = (int *) malloc(30000000*sizeof(int));

  for (int i = 0; i <= 29999999; i++) {
    numberHistory[i] = -1;
  }

  for (int i = 0; i <= 5; i++) {
    numberHistory[numberList[i]] = i;
  }

  while(1) {
    int previousLastSaidNumberIndex = numberHistory[lastSaidNumber];
    int newNumber;
    
    if (previousLastSaidNumberIndex == -1) {
      newNumber = 0;
    } else {
      newNumber = lastSaidNumberIndex - previousLastSaidNumberIndex;
    }
    numberHistory[lastSaidNumber] = lastSaidNumberIndex;
    lastSaidNumber = newNumber;
    lastSaidNumberIndex++;
    if (lastSaidNumberIndex == (30000000-1)) {
      printf("Solution: %d",lastSaidNumber);
      break;
    }
  }
  return 0;
}
