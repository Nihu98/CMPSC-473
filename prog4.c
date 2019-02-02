#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/resource.h>
#include "check.h"

int x[5] = {1,2,3,4,5};
//double c = 10.0;

void allocate()
{
    int i;
    int *p;
    for(i =1 ; i<1000000 ; i++)
    {
      p = malloc(500 * sizeof(int));
      //if(func(i)) { free (p);}
	  free (p);
    }
}

void allocate1()
{
  int i;
  int *p;
  for (i=1 ; i<10000 ; i++)
  {
    p = malloc(1000 * sizeof(int));
    if(i & 1)
      free (p);
  }
}

void allocate2()
{
  int i;
  int *p;
  for (i=1 ; i<300000 ; i++)
  {
    p = malloc(10000 * sizeof(int));
    free (p);
  }
}


int main(int argc, char const *argv[]) {
  int i;
  int *p;
  struct timeval start_u, end_u;
  struct timeval start_s, end_s;
  long maxrss, nsignals, nvcsw, nivcsw;
  struct rusage ru;
  printf("Executing the code ......\n");
  allocate();

  for (i=0 ; i<10000 ; i++)
  {
    p = malloc(1000 * sizeof(int));
    free (p);
  }
  getrusage(RUSAGE_SELF, &ru);
  end_s = ru.ru_stime;
  end_u = ru.ru_utime;
  maxrss = ru.ru_maxrss;
  nsignals = ru.ru_nsignals;
  nvcsw = ru.ru_nvcsw;
  nivcsw = ru.ru_nivcsw;
  
  printf("System Start: %ld.%ld s\n", start_s.tv_sec, start_s.tv_usec);
  printf("System End: %ld.%ld s\n", end_s.tv_sec, end_s.tv_usec);
  printf("User Start: %ld.%ld s\n", start_u.tv_sec, start_u.tv_usec);
  printf("User End: %ld.%ld s\n", end_u.tv_sec, end_u.tv_usec);
  printf("%ld, %ld, %ld, %ld", maxrss, nsignals, nvcsw, nivcsw);
  printf("Program execution successfull\n");
  return 0;
}
