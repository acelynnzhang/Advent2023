#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int seeds[50];

void printseeds() {
  char* info;
  for (int i = 0; i < 50; i++) {
    sprintf(info, " %i ", seeds[i]);
  }
}

void parse(char* input) {
  FILE* fp = fopen(input, "r");

  char* line = NULL;
  size_t len = 0;
  int count = 0;
  while ((getline(&line, &len, fp)) != -1) {
    line[] = '\0';
    printf("%s", "back we r yes \n");
    printf("%s", line);
    printf("%s", "back we r yes \n");
    if (strncmp(line, "seeds", 5) == 0) {
      
      char* curr;
      int strlen = 0;
      for (int i = 6; i < len; i++){
        printf("%c", seeds[i]);
        if (seeds[i] == '\n') {
          break;
        }
        if (seeds[i] != ' ') {
          curr[i] = seeds[i];
          strlen++;
        } else {
          char* temp;
          strncat(temp, curr, strlen);
          seeds[count] = atoi(temp);
          count++;
          strlen = 0;
          curr += strlen;
        }
      }
      break;
    }
  }
  fclose(fp);
  if (line) {
    free(line);
  }
}

void main() {
  parse("input2.txt");
}