# include"stdafx.h"
# include <iostream>

using
namespace
std;

void
main()
{
    setlocale(LC_ALL, "Russian");

int
a, b, c;

cout << "Введите уровень продаж для трех менеджеров =\n";
cin >> a >> b >> c;

if (a < 500)
a = 0.03 * a + 200;
else
if (a > 500 & & a < 1000)
a = 0.05 * a + 200;
else
if (a > 1000)
a = 0.08 * a + 200;

if (b < 500)
b = 0.03 * b + 200;
else
if (b > 500 & & b < 1000)
b = 0.05 * b + 200;
else
if (b > 1000)
b = 0.08 * b + 200;

if (c < 500)
c = 0.03 * c + 200;
else
if (c > 500 & & c < 1000)
c = 0.05 * c + 200;
else
if (c > 1000)
c = 0.08 * c + 200;
if (a > b & & a > c)
a = a + 200;
else
if (b > c)
b = b + 200;
else
c = c + 200;

cout << "ЗП 1 менеджера:" << a << "$" << endl;
cout << "ЗП 2 менеджера:" << b << "$" << endl;
cout << "ЗП 3 менеджера:" << c << "$" << endl;

cin.get();
cin.get();
}