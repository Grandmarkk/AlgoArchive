#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include "sort.cpp"

using namespace std;

int main()
{
    vector<int> testArr = {1, 0, 4, 2, 5, 3, 7, 9, 6};
    vector<int> sorted = selectionSort(testArr);
    for (int i : sorted)
    {
        cout << i << " ";
    }
    return 0;
}
