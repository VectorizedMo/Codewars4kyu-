#include <string>
#include <sstream>

std::string sum_strings(const std::string& a, const std::string& b) {
    bool Carry1 = false;
    std::string Ohio = a;
    std::string Florida = b;
    std::string ans = "";
    int numtoadd;

    if (Ohio.size() > Florida.size()){
        while (Ohio.size() > Florida.size()){
            Florida.insert(0, "0");
        }
    }

    if (Florida.size() > Ohio.size()){
        while (Florida.size() > Ohio.size()){
            Ohio.insert(0, "0");
        }
    }

    for (int i = Ohio.size()-1; i >= 0; --i){
        numtoadd = Ohio[i] + Florida[i] - '0' - '0';

        if (Carry1){
            numtoadd++;
            Carry1 = false;
        }
        if (numtoadd > 9){
            Carry1 = true;
            ans += std::to_string(numtoadd-10);
        }
        else {
            ans += std::to_string(numtoadd);
        }
    }
    if (Carry1){
        ans += '1';
    }
    std::string answer = std::string(ans.rbegin(), ans.rend());
    return answer;
}
