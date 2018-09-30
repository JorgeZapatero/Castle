// f(x) = 96*cos((x+12)*PI/12) + 96
// aka
// f(x) = r * cos( (x + n) * PI/n ) + r


#include <math.h>
#include <stdio.h>
#include <stdlib.h>

//out arr should be of lenght n+1
void calc_pts(double r, int n, double * out);


int main(){
    double radius;
    int n;
    printf("Enter a radius : ");
    scanf("%lf", &radius);

    printf("Enter number of \"bricks\": ");
    scanf("%d", &n);

    double out[n+1];
    calc_pts(radius, n, out);
}


void calc_pts(double r, int n, double * out){
    puts(" X,  f(X)");
    
    int x;
    for ( x = 0; x <= n; x++ ){
        out[x] = r * cos ( (x + n) * M_PI / n ) + r;
        printf("%2d, %3.2lf\n",x, out[x]);
    }
    printf("%2d, %3.2lf\n",x, out[x]);
    
}

