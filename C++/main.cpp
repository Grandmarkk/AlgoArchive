#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include "sort.cpp"
#include "tree.cpp"
#include "heap.cpp"

using namespace std;

int main()
{
    vector<int> testArr = {2, 3, 1, 5, 64, 2, 8};
    MaxHeap *myHeap = new MaxHeap(testArr);
    myHeap->push(100);
    myHeap->push(2);
    cout << myHeap->size() << endl;
    while (!myHeap->empty())
    {
        cout << myHeap->top() << ' ';
        myHeap->pop();
    }

    cout << endl;
    return 0;
}
