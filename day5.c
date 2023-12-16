#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int words[8][10];

int digit(int thing) {
  int count = 0;
  while (thing/10 >=1) {
    count ++;
  }
  return count;
}

void printseeds(int * in) {
  printf("\n");
  for (int i = 0; i < 10; i++) {
    printf("(%d)", in[i]);
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
    if (strncmp(line,"\n" , 1) != 0) {
      int curr = -1;
      for (int i = 0; i < len; i++){
        if (line[i] == '\n') {
            break;
        }
        if ( '0' <=line[i] && '9' >=line[i]){
          words[curritem][count] =  scanf("%d", curr, line[i]);
          i += digit(words[curritem][count]);
        }
      }
    } else {
      //printf("\n->skip\n");
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
  parse("input2.txt");
  for (int i = 0; i < 8; i++) {
    printseeds(words[i]);
  }
  for (int i= 1; i < 8; i++) {
    for (int j = 0; j < 4; j++) {
      for (int k = 1; k < 10; k+=3) {
         if (words[0][j] >= words[i][k] && words[0][j] <= words[i][k] + words[i][k +1]) {
          words[0][j] = words[0][j]-  words[i][k] + words[i][k-1];
          if (j == 0) {
            printf(" -> %u @ %u, (%u, %u, %u)b",words[0][j], i, words[i][k-1],words[i][k] ,words[i][k+1]);
          }
          break;
         }
      }
    }
  }
  
  return 0;
}