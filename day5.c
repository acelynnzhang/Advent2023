#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long long words[8][141];
//int lenn[8] = {20, 99, 72, 66, 57, 33, 27, 123};

void printseeds(unsigned long long* in) {
  unsigned long long smallest = in[0];
  printf("\n");
  for (int i = 0; i < 105; i++) {
    if (in[i] < smallest) {
      smallest = in[i];
    }
    printf("(%llu)", in[i]);
  }

  printf("\n");
}

void parse(char* input) {
  FILE* fp = fopen(input, "r");
  char* line = NULL;
  size_t len = 0;
  int curritem = 0;
  int count = 0;
  while ((getline(&line, &len, fp)) != -1) {
    if (strncmp(line, "\n", 1) != 0) {
      char* curr = calloc(50, 1);
      int strleng = 0;
      for (int i = 0; i < len; i++) {
        if ((line[i] == ' ' || line[i] == '\n') && strlen(curr) != 0) {
          char* temp = calloc(15, 1);
          strncat(temp, curr, strleng);
          // printf(" ok:[%s]", temp);
          words[curritem][count] = atoll(temp);
          free(temp);
          count++;
          strleng = 0;
          curr += strleng;
        }
        if (line[i] == '\n') {
          break;
        } else if ('0' <= line[i] && '9' >= line[i]) {
          // printf("curr : %s\n",curr);
          curr[strleng] = line[i];
          strleng++;
        }
      }
      free(curr);
    } else {
      // printf("\n->skip\n");
      curritem++;
      count = 0;
    }
  }
  fclose(fp);
  if (line) {
    free(line);
  }
}

int main() {
  parse("input.txt");
  // for (int i = 0; i < 8; i++) {
  //   for (int j = 0; j < lenn[i]; j++) {
  //     printf("(%llu)", words[i][j]);
  //   }
  //   printf("\n");
  // }

  unsigned  long long smallest = SIZE_MAX;

  for (int k = 0; k < 20; k += 2) {
    for (unsigned  long long h = words[0][k];
         h < words[0][k] + words[0][k + 1]; h++) {
        unsigned  long long curr = h;
      for (int i = 1; i < 8; i++) {
        for (int k = 1; k < 141; k += 3) {
          if (curr >= words[i][k] &&
              curr < words[i][k] + words[i][k + 1]) {
            curr = curr - words[i][k] + words[i][k - 1];
            // if (j == 0) {
            //   printf(" -> %u @ %u, (%u, %u, %u)",words[0][j], i,
            //   words[i][k-1],words[i][k] ,words[i][k+1]);
            // }
            break;
          }
        }
      }
      if (curr < smallest) {
        smallest = curr;
      }
    }
  }

  printf("%llu\n", smallest);
  return 0;
}