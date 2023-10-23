#include <iostream>
#include <vector>

using namespace std;

int main() {
    string input;
    cout << "Введите строку: ";
    cin >> input;

    vector<char> charVector;
    
    for (int i = input.length() - 1; i >= 0; --i) {
        charVector.push_back(input[i]);
    }

    cout << "Строка в обратной последовательности: ";
    for (char c : charVector) {
        cout << c;
    }
    cout << endl;

    return 0;
}
