

#include <stdlib.h>
#include <stdio.h>
#include <float.h>
#include <math.h>
#include <float.h> /* for max_float */
#include "cdtw.h"


double min3(const double x, const double y, const double z){  
  if (x < y)
    if (x < z) return x;
  if (y < z) return y;
  return z;
}

/*
 Returns the  minimum-distance warp path 
 between multivariate time series x and y. 
*/
double dtw(double* x, double* y, int size_x, int size_y){
  int i, j;
  double* temp;
  double *costP =  malloc(size_x*sizeof(double));
  if (! costP) return -1;
  double *costC = malloc(size_x*sizeof(double));
  if (! costC){
    free(costP);
    return -1; /* TODO:  better handling of the error */
  }
  
  costP[0] =  fabs(x[0] - y[0]);
  for (i=1; i < size_x; i++){
    costP[i] = fabs(x[i] - y[0]) + costP[i-1];
  }
  for (j=1; j< size_y; j++){
    costC[0] = costP[0] + fabs(x[0] - y[j]);
    for (i=1; i < size_x; i++){
      costC[i] = min3(costC[i-1], costP[i-1], costP[i]) + fabs(x[i] - y[j]);
    }
    temp = costP;
    costP = costC;
    costC = temp;
    
  }
  /* result is read in costP because switching between costP and costC is done */
  double ret = costP[size_x-1];
  free(costP);
  free(costC);
  return ret;
}

double cort(double *x, double *y, int size){
  int t;
  double slopex, slopey;
  double num;
  double sumSquareXslope, sumSquareYslope;

  num = sumSquareXslope = sumSquareYslope = 0.0;
  for (t = 0; t < size-1; t++){    
    slopex = x[t+1] -  x[t]; 
    slopey = y[t+1] -  y[t];
    num += slopex * slopey;
    sumSquareXslope += slopex * slopex;
    sumSquareYslope += slopey * slopey;      
  }
  return num/sqrt(sumSquareXslope*sumSquareYslope);  
}
