#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>

long parse_int(std::string number) {
    std::map<std::string, std::string> map;
    std::vector<std::string> num10 = {"zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    std::vector<std::string> twentytohundred = {"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
    std::vector<std::string> unit10 = {"hundred", "thousand", "million"};
    std::vector<std::string> unit10nums = {"100", "1000", "1000000"};
    std::vector<std::string> nums = {"0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11","12","13","14","15","16","17","18","19"};
    std::vector<std::string> twentytohundrednums = {"20", "30", "40", "50", "60", "70", "80", "90"};
    std::vector<std::string> items;
    std::stringstream numstr(number);
    std::string num = "";
    int index = 0;
    int ans = 0;
    int ans2 = 0;
    while (numstr >> num){
        if (std::find(num.begin(), num.end(), '-') != num.end()){
            std::string Part1(num.begin(), std::find(num.begin(), num.end(), '-'));
            std::string Part2(std::find(num.begin(), num.end(), '-')+1, num.end());
            std::string number = "";
            number += twentytohundrednums[std::distance(twentytohundred.begin(),std::find(twentytohundred.begin(), twentytohundred.end(), Part1))];
            number[1] = nums[std::distance(num10.begin(),std::find(num10.begin(), num10.end(), Part2))][0];
            items.push_back(number);
        }
        else if (num != "and") {
            if (std::find(unit10.begin(), unit10.end(), num) != unit10.end()){
                items.push_back(unit10nums[std::distance(unit10.begin(),std::find(unit10.begin(), unit10.end(), num))]);
            }
            else {
                if (std::find(num10.begin(), num10.end(), num) != num10.end()){
                    items.push_back(nums[std::distance(num10.begin(),std::find(num10.begin(), num10.end(), num))]);
                }
                else {
                    items.push_back(twentytohundrednums[std::distance(twentytohundred.begin(),std::find(twentytohundred.begin(), twentytohundred.end(), num))]);
                }
            }
        }
    }

    if (std::find(items.begin(), items.end(), "1000") != items.end()){
        index = std::distance(items.begin(),std::find(items.begin(), items.end(), "1000"));
        for (int i = 0; i <= index; ++i){
            if (std::find(unit10nums.begin(),unit10nums.end(),items[i]) != unit10nums.end()){
                ans *= std::stoi(items[i]);
            }
            else {
                ans += std::stoi(items[i]);
            }
        }
    }
    for (int i = index; i < items.size(); ++i){
        if (std::find(unit10nums.begin(),unit10nums.end(),items[i]) != unit10nums.end()){
            ans2 *= std::stoi(items[i]);
        }
        else {
            ans2 += std::stoi(items[i]);
        }
    }
    return ans+ans2;
}
