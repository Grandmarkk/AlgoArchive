#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include "sort.cpp"

using namespace std;

int main()
{
    vector<int> testArr = {0, -10, 0, 4, 2, 5, 23, 7, 9, 6, 6};
    testArr = radixSort(testArr, 5);
    for (int i : testArr)
    {
        cout << i << " ";
    }

    cout << endl;
    return 0;
}
