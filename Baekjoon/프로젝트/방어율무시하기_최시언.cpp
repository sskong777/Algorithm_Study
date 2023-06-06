#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;

  double defenseIgRate = 0;
  for (int i = 0; i < n; i++) {
    int effPotion; cin >> effPotion;
    defenseIgRate = (effPotion + defenseIgRate) - ((defenseIgRate * effPotion) / 100);

    cout.setf(ios::fixed); cout.precision(6);
    cout << defenseIgRate << "\n";
  }

  return 0;
}
