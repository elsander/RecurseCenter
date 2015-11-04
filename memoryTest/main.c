#include <stdio.h>

int main (int argc, char *argv[]){
	char * FileName = argv[1];
	FILE * F;
	F = fopen(FileName, "w");
	fprintf(F, "C was here\n");
	fflush(F);
	char c;
	printf("Waiting for you to mess things up: ");
	c = getchar();
	fprintf(F, "C was here again\n");
	fclose(F);
	return 0;
}
