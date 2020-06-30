#pragma once

#include <algorithm>
#include <functional>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

namespace Coding2Challenge
{
template <class type1, class type2> class Sorter
{
  public:
    Sorter() = default;
    Sorter(std::vector<type1>& container1, const std::vector<type2>& container2,
           std::function<bool(type2, type2)> comparator);

    Sorter(std::vector<type1>& container1, const std::vector<type2>& container2);

  private:
    struct Containers
    {
      public:
        Containers(type1 cont1, type2 cont2) : container1_{cont1}, container2_{cont2}
        {
        }
        type1 container1_;
        type2 container2_;
    };

    void UpdateContainer1(std::vector<type1>& output);
    void ExecuteSorting();

    void ExecuteSorting(std::function<bool(type2, type2)> comparator);

    std::vector<Containers> containers_;
};

} // namespace Coding2Challenge
