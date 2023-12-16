#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int seeds[50];
int seedto[50];
int soil[50];
int fertilizer[50];
int water[50];
int light[50];
int temperature[50];
int humidity[50];
char* words[8] = {"seeds\0", "seedto\0", "soil", "fertilizer", "water", "light", "temperature", "humidity"};

void printseeds(char * in) {
  printf("\n");
  for (int i = 0; i < 50; i++) {
    if (in[i] == '0'){
      break;
    }
    printf("(%d)", in[i]);
  }
  printf("\n");
}

void parse(char* input) {
  FILE* fp = fopen(input, "r");
  char* line = NULL;
  size_t len = 0;
  int curritem = 0;
  char* currstring = calloc(15,1);
  int count = 0;
  while ((getline(&line, &len, fp)) != -1) {
    if (strncmp(line, words[curritem], strlen(words[curritem])) == 0) {
      free(currstring);
      currstring = calloc(15,1);
      strncat(currstring, words[curritem], strlen(words[curritem]));
    }
    // if () {
    //   currstring[0] = '\0';
    //   printf("->skip\n");
    //   count = 0;
    // }
    if (strncmp(line,"\n" , 1) != 0) {
      printf("[%s]:%s\n", words[curritem], line);
      char* curr = calloc(100, 1);
      int strleng = 0;
      for (int i = strlen(words[curritem]); i < len; i++){
        if ((line[i] == ' ' || line[i] == '\n') && strlen(curr) != 0) {
          char* temp = calloc(10, 1);
          strncat(temp, curr, strlen(curr));
          words[curritem][count] = atoi(temp);
          //printf(" ok:[%s]", temp);
          free(temp);
          count++;
          strleng = 0;
          curr += strleng;
        }
        if (line[i] == '\n') {
            curritem++;
            break;
        } else if (line[i] != ' '){
          curr[strleng] = line[i];
          strleng++;
        }
      }
    }
  }
  fclose(fp);
  if (line) {
    free(line);
  }
}

int main() {
  parse("input2.txt");
  //printseeds("seeds");
  return 0;
}